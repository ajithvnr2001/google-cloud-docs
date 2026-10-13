---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerCitationOrBuilder
title: Interface Answer.AnswerCitationOrBuilder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:10.748762+00:00
---

# Interface Answer.AnswerCitationOrBuilder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerCitationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Answer.AnswerCitationOrBuilder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public static interface Answer.AnswerCitationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEndIndex()
    
    
    public abstract int getEndIndex()

Output only. Indicates the end of the segment, measured in bytes (UTF-8 unicode), exclusive. If there are multi-byte characters, such as non-ASCII characters, the index measurement is longer than the string length.

`int32 end_index = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The endIndex.  
  
### getSources(int index)
    
    
    public abstract Answer.CitationSource getSources(int index)

Output only. Contains citation sources for the attributed segment.

` repeated .google.developers.knowledge.v1.Answer.CitationSource sources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Answer.CitationSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.CitationSource)` |   
  
### getSourcesCount()
    
    
    public abstract int getSourcesCount()

Output only. Contains citation sources for the attributed segment.

` repeated .google.developers.knowledge.v1.Answer.CitationSource sources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourcesList()
    
    
    public abstract List<Answer.CitationSource> getSourcesList()

Output only. Contains citation sources for the attributed segment.

` repeated .google.developers.knowledge.v1.Answer.CitationSource sources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CitationSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.CitationSource)>` |   
  
### getSourcesOrBuilder(int index)
    
    
    public abstract Answer.CitationSourceOrBuilder getSourcesOrBuilder(int index)

Output only. Contains citation sources for the attributed segment.

` repeated .google.developers.knowledge.v1.Answer.CitationSource sources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Answer.CitationSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.CitationSourceOrBuilder)` |   
  
### getSourcesOrBuilderList()
    
    
    public abstract List<? extends Answer.CitationSourceOrBuilder> getSourcesOrBuilderList()

Output only. Contains citation sources for the attributed segment.

` repeated .google.developers.knowledge.v1.Answer.CitationSource sources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.developers.knowledge.v1.Answer.CitationSourceOrBuilder>` |   
  
### getStartIndex()
    
    
    public abstract int getStartIndex()

Output only. Indicates the start of the segment, measured in bytes (UTF-8 unicode), inclusive. If there are multi-byte characters, such as non-ASCII characters, the index measurement is longer than the string length.

`int32 start_index = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The startIndex.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
