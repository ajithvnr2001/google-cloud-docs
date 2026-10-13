---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.VirusDetailOrBuilder
title: Interface VirusDetailOrBuilder (0.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:18.643167+00:00
---

# Interface VirusDetailOrBuilder (0.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.VirusDetailOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VirusDetailOrBuilder (0.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.40.0 (latest)  0.36.0  0.35.0  0.34.0  0.32.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface VirusDetailOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNames(int index)
    
    
    public abstract String getNames(int index)

Names of this Virus.

`repeated string names = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The names at the given index.  
  
### getNamesBytes(int index)
    
    
    public abstract ByteString getNamesBytes(int index)

Names of this Virus.

`repeated string names = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the names at the given index.  
  
### getNamesCount()
    
    
    public abstract int getNamesCount()

Names of this Virus.

`repeated string names = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of names.  
  
### getNamesList()
    
    
    public abstract List<String> getNamesList()

Names of this Virus.

`repeated string names = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the names.  
  
### getThreatType()
    
    
    public abstract VirusDetail.ThreatType getThreatType()

Threat type of the identified virus

`.google.cloud.modelarmor.v1.VirusDetail.ThreatType threat_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[VirusDetail.ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.VirusDetail.ThreatType)` | The threatType.  
  
### getThreatTypeValue()
    
    
    public abstract int getThreatTypeValue()

Threat type of the identified virus

`.google.cloud.modelarmor.v1.VirusDetail.ThreatType threat_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for threatType.  
  
### getVendor()
    
    
    public abstract String getVendor()

Name of vendor that produced this virus identification.

`string vendor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vendor.  
  
### getVendorBytes()
    
    
    public abstract ByteString getVendorBytes()

Name of vendor that produced this virus identification.

`string vendor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vendor.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
