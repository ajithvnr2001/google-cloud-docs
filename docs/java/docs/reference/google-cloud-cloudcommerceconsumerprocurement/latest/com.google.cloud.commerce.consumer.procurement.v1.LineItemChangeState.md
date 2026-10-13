---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeState
title: Enum LineItemChangeState (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:39.408578+00:00
---

# Enum LineItemChangeState (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum LineItemChangeState (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 
    
    
    public enum LineItemChangeState extends Enum<LineItemChangeState> implements ProtocolMessageEnum

State of a change.

Protobuf enum `google.cloud.commerce.consumer.procurement.v1.LineItemChangeState`

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
`LINE_ITEM_CHANGE_STATE_ABANDONED` |  Change is in this state if it was abandoned by the user. This state is only applicable for change in history. `LINE_ITEM_CHANGE_STATE_ABANDONED = 5;`  
`LINE_ITEM_CHANGE_STATE_ABANDONED_VALUE` |  Change is in this state if it was abandoned by the user. This state is only applicable for change in history. `LINE_ITEM_CHANGE_STATE_ABANDONED = 5;`  
`LINE_ITEM_CHANGE_STATE_ACTIVATING` |  Change is in this state if it's currently being provisioned downstream. The change can't be overwritten or cancelled when it's in this state. This state is only applicable for pending change. `LINE_ITEM_CHANGE_STATE_ACTIVATING = 6;`  
`LINE_ITEM_CHANGE_STATE_ACTIVATING_VALUE` |  Change is in this state if it's currently being provisioned downstream. The change can't be overwritten or cancelled when it's in this state. This state is only applicable for pending change. `LINE_ITEM_CHANGE_STATE_ACTIVATING = 6;`  
`LINE_ITEM_CHANGE_STATE_APPROVED` |  Change is in this state after it's approved by the partner or auto-approved but before it takes effect. The change can be overwritten or cancelled depending on the new line item info property (pending Private Offer change cannot be cancelled and can only be overwritten by another Private Offer). This state is only applicable for pending change. `LINE_ITEM_CHANGE_STATE_APPROVED = 2;`  
`LINE_ITEM_CHANGE_STATE_APPROVED_VALUE` |  Change is in this state after it's approved by the partner or auto-approved but before it takes effect. The change can be overwritten or cancelled depending on the new line item info property (pending Private Offer change cannot be cancelled and can only be overwritten by another Private Offer). This state is only applicable for pending change. `LINE_ITEM_CHANGE_STATE_APPROVED = 2;`  
`LINE_ITEM_CHANGE_STATE_COMPLETED` |  Change is in this state after it's been activated. This state is only applicable for change in history. `LINE_ITEM_CHANGE_STATE_COMPLETED = 3;`  
`LINE_ITEM_CHANGE_STATE_COMPLETED_VALUE` |  Change is in this state after it's been activated. This state is only applicable for change in history. `LINE_ITEM_CHANGE_STATE_COMPLETED = 3;`  
`LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL` |  Change is in this state when a change is initiated and waiting for partner approval. This state is only applicable for pending change. `LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL = 1;`  
`LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL_VALUE` |  Change is in this state when a change is initiated and waiting for partner approval. This state is only applicable for pending change. `LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL = 1;`  
`LINE_ITEM_CHANGE_STATE_REJECTED` |  Change is in this state if it was rejected by the partner. This state is only applicable for change in history. `LINE_ITEM_CHANGE_STATE_REJECTED = 4;`  
`LINE_ITEM_CHANGE_STATE_REJECTED_VALUE` |  Change is in this state if it was rejected by the partner. This state is only applicable for change in history. `LINE_ITEM_CHANGE_STATE_REJECTED = 4;`  
`LINE_ITEM_CHANGE_STATE_UNSPECIFIED` |  Sentinel value. Do not use. `LINE_ITEM_CHANGE_STATE_UNSPECIFIED = 0;`  
`LINE_ITEM_CHANGE_STATE_UNSPECIFIED_VALUE` |  Sentinel value. Do not use. `LINE_ITEM_CHANGE_STATE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeState#com_google_cloud_commerce_consumer_procurement_v1_LineItemChangeState_forNumber_int_) instead._  
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

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
