---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.SdpContentLocationOrBuilder
title: Interface SdpContentLocationOrBuilder (0.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:37.523130+00:00
---

# Interface SdpContentLocationOrBuilder (0.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.SdpContentLocationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SdpContentLocationOrBuilder (0.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.40.0 (latest)  0.36.0  0.35.0  0.34.0  0.32.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface SdpContentLocationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContainerName()
    
    
    public abstract String getContainerName()

Name of the container where the finding is located. The top level name is the source file name or table name.

Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document).

`string container_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The containerName.  
  
### getContainerNameBytes()
    
    
    public abstract ByteString getContainerNameBytes()

Name of the container where the finding is located. The top level name is the source file name or table name.

Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document).

`string container_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for containerName.  
  
### getImageFindingLocation()
    
    
    public abstract SdpImageFindingLocation getImageFindingLocation()

Location within an image's pixels.

`.google.cloud.modelarmor.v1.SdpImageFindingLocation image_finding_location = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SdpImageFindingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.SdpImageFindingLocation)` | The imageFindingLocation.  
  
### getImageFindingLocationOrBuilder()
    
    
    public abstract SdpImageFindingLocationOrBuilder getImageFindingLocationOrBuilder()

Location within an image's pixels.

`.google.cloud.modelarmor.v1.SdpImageFindingLocation image_finding_location = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SdpImageFindingLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.SdpImageFindingLocationOrBuilder)` |   
  
### getLocationCase()
    
    
    public abstract SdpContentLocation.LocationCase getLocationCase()

**Returns**  
---  
**Type** | **Description**  
`[SdpContentLocation.LocationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.SdpContentLocation.LocationCase)` |   
  
### hasImageFindingLocation()
    
    
    public abstract boolean hasImageFindingLocation()

Location within an image's pixels.

`.google.cloud.modelarmor.v1.SdpImageFindingLocation image_finding_location = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the imageFindingLocation field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
