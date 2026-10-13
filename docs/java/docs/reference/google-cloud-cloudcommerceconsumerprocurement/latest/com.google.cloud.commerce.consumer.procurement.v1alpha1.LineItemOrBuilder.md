---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemOrBuilder
title: Interface LineItemOrBuilder (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:19.723502+00:00
---

# Interface LineItemOrBuilder (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LineItemOrBuilder (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 
    
    
    public interface LineItemOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChangeHistory(int index)
    
    
    public abstract LineItemChange getChangeHistory(int index)

Output only. Changes made on the item that are not pending anymore which might be because they already took effect, were reverted by the customer, or were rejected by the partner. No more operations are allowed on these changes.

` repeated .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange change_history = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineItemChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange)` |   
  
### getChangeHistoryCount()
    
    
    public abstract int getChangeHistoryCount()

Output only. Changes made on the item that are not pending anymore which might be because they already took effect, were reverted by the customer, or were rejected by the partner. No more operations are allowed on these changes.

` repeated .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange change_history = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getChangeHistoryList()
    
    
    public abstract List<LineItemChange> getChangeHistoryList()

Output only. Changes made on the item that are not pending anymore which might be because they already took effect, were reverted by the customer, or were rejected by the partner. No more operations are allowed on these changes.

` repeated .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange change_history = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LineItemChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange)>` |   
  
### getChangeHistoryOrBuilder(int index)
    
    
    public abstract LineItemChangeOrBuilder getChangeHistoryOrBuilder(int index)

Output only. Changes made on the item that are not pending anymore which might be because they already took effect, were reverted by the customer, or were rejected by the partner. No more operations are allowed on these changes.

` repeated .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange change_history = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineItemChangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChangeOrBuilder)` |   
  
### getChangeHistoryOrBuilderList()
    
    
    public abstract List<? extends LineItemChangeOrBuilder> getChangeHistoryOrBuilderList()

Output only. Changes made on the item that are not pending anymore which might be because they already took effect, were reverted by the customer, or were rejected by the partner. No more operations are allowed on these changes.

` repeated .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange change_history = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChangeOrBuilder>` |   
  
### getLineItemId()
    
    
    public abstract String getLineItemId()

Output only. Line item ID.

`string line_item_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The lineItemId.  
  
### getLineItemIdBytes()
    
    
    public abstract ByteString getLineItemIdBytes()

Output only. Line item ID.

`string line_item_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for lineItemId.  
  
### getLineItemInfo()
    
    
    public abstract LineItemInfo getLineItemInfo()

Output only. Current state and information of this item. It tells what, e.g. which offer, is currently effective.

` .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemInfo line_item_info = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemInfo)` | The lineItemInfo.  
  
### getLineItemInfoOrBuilder()
    
    
    public abstract LineItemInfoOrBuilder getLineItemInfoOrBuilder()

Output only. Current state and information of this item. It tells what, e.g. which offer, is currently effective.

` .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemInfo line_item_info = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemInfoOrBuilder)` |   
  
### getPendingChange()
    
    
    public abstract LineItemChange getPendingChange()

Output only. A change made on the item which is pending and not yet effective. Absence of this field indicates the line item is not undergoing a change.

` .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange pending_change = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange)` | The pendingChange.  
  
### getPendingChangeOrBuilder()
    
    
    public abstract LineItemChangeOrBuilder getPendingChangeOrBuilder()

Output only. A change made on the item which is pending and not yet effective. Absence of this field indicates the line item is not undergoing a change.

` .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange pending_change = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemChangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChangeOrBuilder)` |   
  
### hasLineItemInfo()
    
    
    public abstract boolean hasLineItemInfo()

Output only. Current state and information of this item. It tells what, e.g. which offer, is currently effective.

` .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemInfo line_item_info = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lineItemInfo field is set.  
  
### hasPendingChange()
    
    
    public abstract boolean hasPendingChange()

Output only. A change made on the item which is pending and not yet effective. Absence of this field indicates the line item is not undergoing a change.

` .google.cloud.commerce.consumer.procurement.v1alpha1.LineItemChange pending_change = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pendingChange field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
