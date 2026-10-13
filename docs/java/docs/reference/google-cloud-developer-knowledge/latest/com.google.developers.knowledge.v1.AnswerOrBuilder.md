---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerOrBuilder
title: Interface AnswerOrBuilder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:11.839723+00:00
---

# Interface AnswerOrBuilder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnswerOrBuilder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public interface AnswerOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnswerText()
    
    
    public abstract String getAnswerText()

Contains the text of the answer.

`string answer_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The answerText.  
  
### getAnswerTextBytes()
    
    
    public abstract ByteString getAnswerTextBytes()

Contains the text of the answer.

`string answer_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for answerText.  
  
### getCitations(int index)
    
    
    public abstract Answer.AnswerCitation getCitations(int index)

Output only. Contains citations for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerCitation citations = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Answer.AnswerCitation](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerCitation)` |   
  
### getCitationsCount()
    
    
    public abstract int getCitationsCount()

Output only. Contains citations for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerCitation citations = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCitationsList()
    
    
    public abstract List<Answer.AnswerCitation> getCitationsList()

Output only. Contains citations for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerCitation citations = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AnswerCitation](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerCitation)>` |   
  
### getCitationsOrBuilder(int index)
    
    
    public abstract Answer.AnswerCitationOrBuilder getCitationsOrBuilder(int index)

Output only. Contains citations for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerCitation citations = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Answer.AnswerCitationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerCitationOrBuilder)` |   
  
### getCitationsOrBuilderList()
    
    
    public abstract List<? extends Answer.AnswerCitationOrBuilder> getCitationsOrBuilderList()

Output only. Contains citations for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerCitation citations = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.developers.knowledge.v1.Answer.AnswerCitationOrBuilder>` |   
  
### getReferences(int index)
    
    
    public abstract Answer.AnswerReference getReferences(int index)

Output only. Contains references for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerReference references = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Answer.AnswerReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerReference)` |   
  
### getReferencesCount()
    
    
    public abstract int getReferencesCount()

Output only. Contains references for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerReference references = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getReferencesList()
    
    
    public abstract List<Answer.AnswerReference> getReferencesList()

Output only. Contains references for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerReference references = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AnswerReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerReference)>` |   
  
### getReferencesOrBuilder(int index)
    
    
    public abstract Answer.AnswerReferenceOrBuilder getReferencesOrBuilder(int index)

Output only. Contains references for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerReference references = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Answer.AnswerReferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Answer.AnswerReferenceOrBuilder)` |   
  
### getReferencesOrBuilderList()
    
    
    public abstract List<? extends Answer.AnswerReferenceOrBuilder> getReferencesOrBuilderList()

Output only. Contains references for the answer.

` repeated .google.developers.knowledge.v1.Answer.AnswerReference references = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.developers.knowledge.v1.Answer.AnswerReferenceOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
