---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.stages.PipelineExecuteOptions
title: Class PipelineExecuteOptions (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:48.267314+00:00
---

# Class PipelineExecuteOptions (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.stages.PipelineExecuteOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PipelineExecuteOptions (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public final class PipelineExecuteOptions extends AbstractOptions<PipelineExecuteOptions>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.firestore.pipeline.stages.AbstractOptions > PipelineExecuteOptions

## Inherited Members

com.google.cloud.firestore.pipeline.stages.AbstractOptions.adding(com.google.cloud.firestore.pipeline.stages.AbstractOptions<?>)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,boolean)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,com.google.cloud.firestore.pipeline.expressions.Field)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,com.google.cloud.firestore.pipeline.stages.AbstractOptions<?>)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,com.google.firestore.v1.Value)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,double)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,java.lang.String)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,java.lang.String[])

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,java.util.List<? extends com.google.cloud.firestore.pipeline.expressions.Expression>)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.with(java.lang.String,long)

com.google.cloud.firestore.pipeline.stages.AbstractOptions.withSection(java.lang.String,com.google.cloud.firestore.pipeline.stages.RawOptions)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### PipelineExecuteOptions()
    
    
    public PipelineExecuteOptions()

## Methods 

### withExplainOptions(ExplainOptions options)
    
    
    public PipelineExecuteOptions withExplainOptions(ExplainOptions options)

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ExplainOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.stages.ExplainOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PipelineExecuteOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.stages.PipelineExecuteOptions)` |   
  
### withIndexMode(String indexMode)
    
    
    public PipelineExecuteOptions withIndexMode(String indexMode)

**Parameter**  
---  
**Name** | **Description**  
`indexMode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PipelineExecuteOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.stages.PipelineExecuteOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
