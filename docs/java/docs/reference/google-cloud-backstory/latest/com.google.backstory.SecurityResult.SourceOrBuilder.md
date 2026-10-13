---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult.SourceOrBuilder
title: Interface SecurityResult.SourceOrBuilder (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:38.641909+00:00
---

# Interface SecurityResult.SourceOrBuilder (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult.SourceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SecurityResult.SourceOrBuilder (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public static interface SecurityResult.SourceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBenignCount()
    
    
    public abstract int getBenignCount()

Count of responses where this IoC was marked benign.

`int32 benign_count = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The benignCount.  
  
### getMaliciousCount()
    
    
    public abstract int getMaliciousCount()

Count of responses where this IoC was marked malicious.

`int32 malicious_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maliciousCount.  
  
### getName()
    
    
    public abstract String getName()

Name of the IoC source.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the IoC source.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getQuality()
    
    
    public abstract SecurityResult.ProductConfidence getQuality()

Quality of the IoC mapping extracted from the source.

`.google.backstory.SecurityResult.ProductConfidence quality = 4;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityResult.ProductConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult.ProductConfidence)` | The quality.  
  
### getQualityValue()
    
    
    public abstract int getQualityValue()

Quality of the IoC mapping extracted from the source.

`.google.backstory.SecurityResult.ProductConfidence quality = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for quality.  
  
### getResponseCount()
    
    
    public abstract int getResponseCount()

Total response count from this source.

`int32 response_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The responseCount.  
  
### getSourceCount()
    
    
    public abstract int getSourceCount()

Number of sources from which intelligence was extracted.

`int32 source_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sourceCount.  
  
### getThreatIntelligenceSources(int index)
    
    
    public abstract SecurityResult.Source getThreatIntelligenceSources(int index)

Different threat intelligence sources from which IoC info was extracted.

`repeated .google.backstory.SecurityResult.Source threat_intelligence_sources = 7; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityResult.Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult.Source)` |   
  
### getThreatIntelligenceSourcesCount()
    
    
    public abstract int getThreatIntelligenceSourcesCount()

Different threat intelligence sources from which IoC info was extracted.

`repeated .google.backstory.SecurityResult.Source threat_intelligence_sources = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getThreatIntelligenceSourcesList()
    
    
    public abstract List<SecurityResult.Source> getThreatIntelligenceSourcesList()

Different threat intelligence sources from which IoC info was extracted.

`repeated .google.backstory.SecurityResult.Source threat_intelligence_sources = 7; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult.Source)>` |   
  
### getThreatIntelligenceSourcesOrBuilder(int index)
    
    
    public abstract SecurityResult.SourceOrBuilder getThreatIntelligenceSourcesOrBuilder(int index)

Different threat intelligence sources from which IoC info was extracted.

`repeated .google.backstory.SecurityResult.Source threat_intelligence_sources = 7; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityResult.SourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult.SourceOrBuilder)` |   
  
### getThreatIntelligenceSourcesOrBuilderList()
    
    
    public abstract List<? extends SecurityResult.SourceOrBuilder> getThreatIntelligenceSourcesOrBuilderList()

Different threat intelligence sources from which IoC info was extracted.

`repeated .google.backstory.SecurityResult.Source threat_intelligence_sources = 7; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.backstory.SecurityResult.SourceOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
