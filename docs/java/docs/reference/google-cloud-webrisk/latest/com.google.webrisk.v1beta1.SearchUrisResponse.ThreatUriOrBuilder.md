---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1beta1.SearchUrisResponse.ThreatUriOrBuilder
title: Interface SearchUrisResponse.ThreatUriOrBuilder (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:45.753703+00:00
---

# Interface SearchUrisResponse.ThreatUriOrBuilder (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1beta1.SearchUrisResponse.ThreatUriOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchUrisResponse.ThreatUriOrBuilder (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.6  2.0.12 
    
    
    public static interface SearchUrisResponse.ThreatUriOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExpireTime()
    
    
    public abstract Timestamp getExpireTime()

The cache lifetime for the returned match. Clients must not cache this response past this timestamp to avoid false positives.

`.google.protobuf.Timestamp expire_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expireTime.  
  
### getExpireTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getExpireTimeOrBuilder()

The cache lifetime for the returned match. Clients must not cache this response past this timestamp to avoid false positives.

`.google.protobuf.Timestamp expire_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getThreatTypes(int index)
    
    
    public abstract ThreatType getThreatTypes(int index)

The ThreatList this threat belongs to.

`repeated .google.cloud.webrisk.v1beta1.ThreatType threat_types = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1beta1.ThreatType)` | The threatTypes at the given index.  
  
### getThreatTypesCount()
    
    
    public abstract int getThreatTypesCount()

The ThreatList this threat belongs to.

`repeated .google.cloud.webrisk.v1beta1.ThreatType threat_types = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of threatTypes.  
  
### getThreatTypesList()
    
    
    public abstract List<ThreatType> getThreatTypesList()

The ThreatList this threat belongs to.

`repeated .google.cloud.webrisk.v1beta1.ThreatType threat_types = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1beta1.ThreatType)>` | A list containing the threatTypes.  
  
### getThreatTypesValue(int index)
    
    
    public abstract int getThreatTypesValue(int index)

The ThreatList this threat belongs to.

`repeated .google.cloud.webrisk.v1beta1.ThreatType threat_types = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of threatTypes at the given index.  
  
### getThreatTypesValueList()
    
    
    public abstract List<Integer> getThreatTypesValueList()

The ThreatList this threat belongs to.

`repeated .google.cloud.webrisk.v1beta1.ThreatType threat_types = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for threatTypes.  
  
### hasExpireTime()
    
    
    public abstract boolean hasExpireTime()

The cache lifetime for the returned match. Clients must not cache this response past this timestamp to avoid false positives.

`.google.protobuf.Timestamp expire_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expireTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
