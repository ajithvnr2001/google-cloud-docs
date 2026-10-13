---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponseOrBuilder
title: Interface ReportPropertyUsageResponseOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:24.612039+00:00
---

# Interface ReportPropertyUsageResponseOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportPropertyUsageResponseOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ReportPropertyUsageResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBillInfo()
    
    
    public abstract ReportPropertyUsageResponse.BillInfo getBillInfo()

Bill amount in the specified organization and month.

Will be empty if user only has access to usage data.

` .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.BillInfo bill_info = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse.BillInfo](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.BillInfo)` | The billInfo.  
  
### getBillInfoOrBuilder()
    
    
    public abstract ReportPropertyUsageResponse.BillInfoOrBuilder getBillInfoOrBuilder()

Bill amount in the specified organization and month.

Will be empty if user only has access to usage data.

` .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.BillInfo bill_info = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse.BillInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.BillInfoOrBuilder)` |   
  
### getPropertyUsages(int index)
    
    
    public abstract ReportPropertyUsageResponse.PropertyUsage getPropertyUsages(int index)

Usage data for all properties in the specified organization and month.

` repeated .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage property_usages = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse.PropertyUsage](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage)` |   
  
### getPropertyUsagesCount()
    
    
    public abstract int getPropertyUsagesCount()

Usage data for all properties in the specified organization and month.

` repeated .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage property_usages = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPropertyUsagesList()
    
    
    public abstract List<ReportPropertyUsageResponse.PropertyUsage> getPropertyUsagesList()

Usage data for all properties in the specified organization and month.

` repeated .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage property_usages = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PropertyUsage](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage)>` |   
  
### getPropertyUsagesOrBuilder(int index)
    
    
    public abstract ReportPropertyUsageResponse.PropertyUsageOrBuilder getPropertyUsagesOrBuilder(int index)

Usage data for all properties in the specified organization and month.

` repeated .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage property_usages = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse.PropertyUsageOrBuilder](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsageOrBuilder)` |   
  
### getPropertyUsagesOrBuilderList()
    
    
    public abstract List<? extends ReportPropertyUsageResponse.PropertyUsageOrBuilder> getPropertyUsagesOrBuilderList()

Usage data for all properties in the specified organization and month.

` repeated .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsage property_usages = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsageOrBuilder>` |   
  
### hasBillInfo()
    
    
    public abstract boolean hasBillInfo()

Bill amount in the specified organization and month.

Will be empty if user only has access to usage data.

` .google.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.BillInfo bill_info = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the billInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
