---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.BillingInfoOrBuilder
title: Interface BillingInfoOrBuilder (0.32.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:53.280573+00:00
---

# Interface BillingInfoOrBuilder (0.32.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.BillingInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BillingInfoOrBuilder (0.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.32.0 (latest)  0.28.0  0.27.0  0.26.0  0.24.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface BillingInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCurrentBillingInfoCase()
    
    
    public abstract BillingInfo.CurrentBillingInfoCase getCurrentBillingInfoCase()

**Returns**  
---  
**Type** | **Description**  
`[BillingInfo.CurrentBillingInfoCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.BillingInfo.CurrentBillingInfoCase)` |   
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

Output only. When the billing ends.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

Output only. When the billing ends.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. When the billing starts.

`.google.protobuf.Timestamp start_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. When the billing starts.

`.google.protobuf.Timestamp start_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getUserCountBilling()
    
    
    public abstract UserCountBillingInfo getUserCountBilling()

Required. This type of billing uses user count for computing total charge.

` .google.cloud.licensemanager.v1.UserCountBillingInfo user_count_billing = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCountBillingInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.UserCountBillingInfo)` | The userCountBilling.  
  
### getUserCountBillingOrBuilder()
    
    
    public abstract UserCountBillingInfoOrBuilder getUserCountBillingOrBuilder()

Required. This type of billing uses user count for computing total charge.

` .google.cloud.licensemanager.v1.UserCountBillingInfo user_count_billing = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCountBillingInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.UserCountBillingInfoOrBuilder)` |   
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

Output only. When the billing ends.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. When the billing starts.

`.google.protobuf.Timestamp start_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
### hasUserCountBilling()
    
    
    public abstract boolean hasUserCountBilling()

Required. This type of billing uses user count for computing total charge.

` .google.cloud.licensemanager.v1.UserCountBillingInfo user_count_billing = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userCountBilling field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
