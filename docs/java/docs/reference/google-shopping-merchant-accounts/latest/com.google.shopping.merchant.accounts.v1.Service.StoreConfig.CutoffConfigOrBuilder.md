---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfigOrBuilder
title: Interface Service.StoreConfig.CutoffConfigOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:55.687844+00:00
---

# Interface Service.StoreConfig.CutoffConfigOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Service.StoreConfig.CutoffConfigOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface Service.StoreConfig.CutoffConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLocalCutoffTime()
    
    
    public abstract Service.StoreConfig.CutoffConfig.LocalCutoffTime getLocalCutoffTime()

Time that local delivery ends for the day.

` optional .google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfig.LocalCutoffTime local_cutoff_time = 1; `

**Returns**  
---  
**Type** | **Description**  
`[Service.StoreConfig.CutoffConfig.LocalCutoffTime](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfig.LocalCutoffTime)` | The localCutoffTime.  
  
### getLocalCutoffTimeOrBuilder()
    
    
    public abstract Service.StoreConfig.CutoffConfig.LocalCutoffTimeOrBuilder getLocalCutoffTimeOrBuilder()

Time that local delivery ends for the day.

` optional .google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfig.LocalCutoffTime local_cutoff_time = 1; `

**Returns**  
---  
**Type** | **Description**  
`[Service.StoreConfig.CutoffConfig.LocalCutoffTimeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfig.LocalCutoffTimeOrBuilder)` |   
  
### getNoDeliveryPostCutoff()
    
    
    public abstract boolean getNoDeliveryPostCutoff()

Businesses can opt-out of showing n+1 day local delivery when they have a shipping service configured to n day local delivery. For example, if the shipping service defines same-day delivery, and it's past the cut-off, setting this field to `true` results in the calculated shipping service rate returning `NO_DELIVERY_POST_CUTOFF`. In the same example, setting this field to `false` results in the calculated shipping time being one day. This is only for local delivery.

`optional bool no_delivery_post_cutoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The noDeliveryPostCutoff.  
  
### getStoreCloseOffsetHours()
    
    
    public abstract long getStoreCloseOffsetHours()

Only valid with local delivery fulfillment. Represents cutoff time as the number of hours before store closing. Mutually exclusive with `local_cutoff_time`.

`optional int64 store_close_offset_hours = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The storeCloseOffsetHours.  
  
### hasLocalCutoffTime()
    
    
    public abstract boolean hasLocalCutoffTime()

Time that local delivery ends for the day.

` optional .google.shopping.merchant.accounts.v1.Service.StoreConfig.CutoffConfig.LocalCutoffTime local_cutoff_time = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the localCutoffTime field is set.  
  
### hasNoDeliveryPostCutoff()
    
    
    public abstract boolean hasNoDeliveryPostCutoff()

Businesses can opt-out of showing n+1 day local delivery when they have a shipping service configured to n day local delivery. For example, if the shipping service defines same-day delivery, and it's past the cut-off, setting this field to `true` results in the calculated shipping service rate returning `NO_DELIVERY_POST_CUTOFF`. In the same example, setting this field to `false` results in the calculated shipping time being one day. This is only for local delivery.

`optional bool no_delivery_post_cutoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the noDeliveryPostCutoff field is set.  
  
### hasStoreCloseOffsetHours()
    
    
    public abstract boolean hasStoreCloseOffsetHours()

Only valid with local delivery fulfillment. Represents cutoff time as the number of hours before store closing. Mutually exclusive with `local_cutoff_time`.

`optional int64 store_close_offset_hours = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the storeCloseOffsetHours field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
