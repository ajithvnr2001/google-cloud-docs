---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Affiliation.LineageOrBuilder
title: Interface Affiliation.LineageOrBuilder (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:59.982387+00:00
---

# Interface Affiliation.LineageOrBuilder (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Affiliation.LineageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Affiliation.LineageOrBuilder (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface Affiliation.LineageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getProcessFqn()
    
    
    public abstract String getProcessFqn()

Optional. FQN of process which created the lineage i.e. dataplex, datastream etc.

`string process_fqn = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The processFqn.  
  
### getProcessFqnBytes()
    
    
    public abstract ByteString getProcessFqnBytes()

Optional. FQN of process which created the lineage i.e. dataplex, datastream etc.

`string process_fqn = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for processFqn.  
  
### getProcessType()
    
    
    public abstract Affiliation.ProcessType getProcessType()

Optional. Type of process which created the lineage.

` .google.cloud.databasecenter.v1beta.Affiliation.ProcessType process_type = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Affiliation.ProcessType](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Affiliation.ProcessType)` | The processType.  
  
### getProcessTypeValue()
    
    
    public abstract int getProcessTypeValue()

Optional. Type of process which created the lineage.

` .google.cloud.databasecenter.v1beta.Affiliation.ProcessType process_type = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for processType.  
  
### getSourceFqn()
    
    
    public abstract String getSourceFqn()

Optional. FQN of source table / column

`string source_fqn = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceFqn.  
  
### getSourceFqnBytes()
    
    
    public abstract ByteString getSourceFqnBytes()

Optional. FQN of source table / column

`string source_fqn = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceFqn.  
  
### getTargetFqn()
    
    
    public abstract String getTargetFqn()

Optional. FQN of target table / column

`string target_fqn = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetFqn.  
  
### getTargetFqnBytes()
    
    
    public abstract ByteString getTargetFqnBytes()

Optional. FQN of target table / column

`string target_fqn = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetFqn.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
