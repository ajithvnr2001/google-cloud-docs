---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsageOrBuilder
title: Interface ReportPropertyUsageResponse.PropertyUsageOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:24.416940+00:00
---

# Interface ReportPropertyUsageResponse.PropertyUsageOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse.PropertyUsageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportPropertyUsageResponse.PropertyUsageOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ReportPropertyUsageResponse.PropertyUsageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccountId()
    
    
    public abstract long getAccountId()

The ID of the property's parent account.

`int64 account_id = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The accountId.  
  
### getBillableEventCount()
    
    
    public abstract long getBillableEventCount()

The number of events for which the property is billed in the requested month.

`int64 billable_event_count = 7;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The billableEventCount.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

The display name of the property.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

The display name of the property.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getProperty()
    
    
    public abstract String getProperty()

The name of the Google Analytics Admin API property resource.

Format: analyticsadmin.googleapis.com/properties/{property_id}

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The property.  
  
### getPropertyBytes()
    
    
    public abstract ByteString getPropertyBytes()

The name of the Google Analytics Admin API property resource.

Format: analyticsadmin.googleapis.com/properties/{property_id}

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for property.  
  
### getPropertyType()
    
    
    public abstract AnalyticsPropertyType getPropertyType()

The subtype of the analytics property. This affects the billable event count.

`.google.marketingplatform.admin.v1alpha.AnalyticsPropertyType property_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsPropertyType](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsPropertyType)` | The propertyType.  
  
### getPropertyTypeValue()
    
    
    public abstract int getPropertyTypeValue()

The subtype of the analytics property. This affects the billable event count.

`.google.marketingplatform.admin.v1alpha.AnalyticsPropertyType property_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for propertyType.  
  
### getServiceLevel()
    
    
    public abstract AnalyticsServiceLevel getServiceLevel()

The service level of the property.

`.google.marketingplatform.admin.v1alpha.AnalyticsServiceLevel service_level = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsServiceLevel](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsServiceLevel)` | The serviceLevel.  
  
### getServiceLevelValue()
    
    
    public abstract int getServiceLevelValue()

The service level of the property.

`.google.marketingplatform.admin.v1alpha.AnalyticsServiceLevel service_level = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for serviceLevel.  
  
### getTotalEventCount()
    
    
    public abstract long getTotalEventCount()

Total event count that the property received during the requested month.

`int64 total_event_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalEventCount.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
