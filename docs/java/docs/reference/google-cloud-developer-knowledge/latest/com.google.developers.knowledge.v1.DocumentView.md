---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentView
title: Enum DocumentView (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:09.601397+00:00
---

# Enum DocumentView (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentView

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum DocumentView (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public enum DocumentView extends Enum<DocumentView> implements ProtocolMessageEnum

Specifies which fields of the Document are included.

Protobuf enum `google.developers.knowledge.v1.DocumentView`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`DOCUMENT_VIEW_BASIC` |  Includes only the basic metadata fields:

  * `name`
  * `uri`
  * `data_source`
  * `title`
  * `description`
  * `update_time`
  * `view`
  * `content_length_bytes` This is the default of view for DeveloperKnowledge.SearchDocumentChunks.

`DOCUMENT_VIEW_BASIC = 1;`  
`DOCUMENT_VIEW_BASIC_VALUE` |  Includes only the basic metadata fields:

  * `name`
  * `uri`
  * `data_source`
  * `title`
  * `description`
  * `update_time`
  * `view`
  * `content_length_bytes` This is the default of view for DeveloperKnowledge.SearchDocumentChunks.

`DOCUMENT_VIEW_BASIC = 1;`  
`DOCUMENT_VIEW_CONTENT` |  Includes the `DOCUMENT_VIEW_BASIC` fields and the `content` field. This is the default of view for DeveloperKnowledge.GetDocument and DeveloperKnowledge.BatchGetDocuments. `DOCUMENT_VIEW_CONTENT = 3;`  
`DOCUMENT_VIEW_CONTENT_VALUE` |  Includes the `DOCUMENT_VIEW_BASIC` fields and the `content` field. This is the default of view for DeveloperKnowledge.GetDocument and DeveloperKnowledge.BatchGetDocuments. `DOCUMENT_VIEW_CONTENT = 3;`  
`DOCUMENT_VIEW_FULL` |  Includes all Document fields. `DOCUMENT_VIEW_FULL = 2;`  
`DOCUMENT_VIEW_FULL_VALUE` |  Includes all Document fields. `DOCUMENT_VIEW_FULL = 2;`  
`DOCUMENT_VIEW_UNSPECIFIED` |  The default / unset value. See each API method for its default value if DocumentView is not specified. `DOCUMENT_VIEW_UNSPECIFIED = 0;`  
`DOCUMENT_VIEW_UNSPECIFIED_VALUE` |  The default / unset value. See each API method for its default value if DocumentView is not specified. `DOCUMENT_VIEW_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentView#com_google_developers_knowledge_v1_DocumentView_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
