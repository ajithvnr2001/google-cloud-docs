---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.AppProfile.DataBoostIsolationReadOnlyPolicy
title: Class AppProfile.DataBoostIsolationReadOnlyPolicy (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:36.879376+00:00
---

# Class AppProfile.DataBoostIsolationReadOnlyPolicy (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.AppProfile.DataBoostIsolationReadOnlyPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AppProfile.DataBoostIsolationReadOnlyPolicy (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public static class AppProfile.DataBoostIsolationReadOnlyPolicy implements AppProfile.IsolationPolicy

A Data Boost Read Only IsolationPolicy for running high-throughput read traffic on your Bigtable data without affecting application traffic. Data Boost App Profile needs to be created with a ComputeBillingOwner which specifies how usage should be accounted when using Data Boost.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AppProfile.DataBoostIsolationReadOnlyPolicy

## Implements

[AppProfile.IsolationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.AppProfile.IsolationPolicy)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### of(AppProfile.ComputeBillingOwner billingOwner)
    
    
    public static AppProfile.DataBoostIsolationReadOnlyPolicy of(AppProfile.ComputeBillingOwner billingOwner)

Creates a new instance of DataBoostIsolationReadOnlyPolicy with specified ComputeBillingOwner.

**Parameter**  
---  
**Name** | **Description**  
`billingOwner` | `[AppProfile.ComputeBillingOwner](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.AppProfile.ComputeBillingOwner)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppProfile.DataBoostIsolationReadOnlyPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.AppProfile.DataBoostIsolationReadOnlyPolicy)` |   
  
## Methods 

### equals(Object o)
    
    
    public boolean equals(Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getComputeBillingOwner()
    
    
    public AppProfile.ComputeBillingOwner getComputeBillingOwner()

Gets the ComputeBillingOwner on the current DataBoostIsolationReadOnlyPolicy instance.

**Returns**  
---  
**Type** | **Description**  
`[AppProfile.ComputeBillingOwner](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.AppProfile.ComputeBillingOwner)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toProto()
    
    
    public AppProfile.DataBoostIsolationReadOnly toProto()

**Internal Only** : This feature is not stable for application use.

Creates the request protobuf. This method is considered an internal implementation detail and not meant to be used by applications.

**Returns**  
---  
**Type** | **Description**  
`com.google.bigtable.admin.v2.AppProfile.DataBoostIsolationReadOnly` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
