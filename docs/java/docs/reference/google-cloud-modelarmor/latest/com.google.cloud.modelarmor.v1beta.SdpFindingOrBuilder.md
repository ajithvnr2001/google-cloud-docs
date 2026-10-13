---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1beta.SdpFindingOrBuilder
title: Interface SdpFindingOrBuilder (0.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:53.886086+00:00
---

# Interface SdpFindingOrBuilder (0.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1beta.SdpFindingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SdpFindingOrBuilder (0.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.40.0 (latest)  0.36.0  0.35.0  0.34.0  0.32.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface SdpFindingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getInfoType()
    
    
    public abstract String getInfoType()

Name of Sensitive Data Protection info type for this finding.

`string info_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The infoType.  
  
### getInfoTypeBytes()
    
    
    public abstract ByteString getInfoTypeBytes()

Name of Sensitive Data Protection info type for this finding.

`string info_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for infoType.  
  
### getLikelihood()
    
    
    public abstract SdpFindingLikelihood getLikelihood()

Identified confidence likelihood for `info_type`.

`.google.cloud.modelarmor.v1beta.SdpFindingLikelihood likelihood = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SdpFindingLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1beta.SdpFindingLikelihood)` | The likelihood.  
  
### getLikelihoodValue()
    
    
    public abstract int getLikelihoodValue()

Identified confidence likelihood for `info_type`.

`.google.cloud.modelarmor.v1beta.SdpFindingLikelihood likelihood = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for likelihood.  
  
### getLocation()
    
    
    public abstract SdpFinding.SdpFindingLocation getLocation()

Location for this finding.

`.google.cloud.modelarmor.v1beta.SdpFinding.SdpFindingLocation location = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SdpFinding.SdpFindingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1beta.SdpFinding.SdpFindingLocation)` | The location.  
  
### getLocationOrBuilder()
    
    
    public abstract SdpFinding.SdpFindingLocationOrBuilder getLocationOrBuilder()

Location for this finding.

`.google.cloud.modelarmor.v1beta.SdpFinding.SdpFindingLocation location = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SdpFinding.SdpFindingLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1beta.SdpFinding.SdpFindingLocationOrBuilder)` |   
  
### hasLocation()
    
    
    public abstract boolean hasLocation()

Location for this finding.

`.google.cloud.modelarmor.v1beta.SdpFinding.SdpFindingLocation location = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the location field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
