---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionLoadConfigOrBuilder
title: Interface WorkflowInvocationAction.DataPreparationAction.ActionLoadConfigOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:41.259892+00:00
---

# Interface WorkflowInvocationAction.DataPreparationAction.ActionLoadConfigOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionLoadConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WorkflowInvocationAction.DataPreparationAction.ActionLoadConfigOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public static interface WorkflowInvocationAction.DataPreparationAction.ActionLoadConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppend()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode getAppend()

Append into destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode append = 2; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode)` | The append.  
  
### getAppendOrBuilder()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadModeOrBuilder getAppendOrBuilder()

Append into destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode append = 2; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadModeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadModeOrBuilder)` |   
  
### getMaximum()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode getMaximum()

Insert records where the value exceeds the previous maximum value for a column in the destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode maximum = 3; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode)` | The maximum.  
  
### getMaximumOrBuilder()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadModeOrBuilder getMaximumOrBuilder()

Insert records where the value exceeds the previous maximum value for a column in the destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode maximum = 3; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadModeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadModeOrBuilder)` |   
  
### getModeCase()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig.ModeCase getModeCase()

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig.ModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig.ModeCase)` |   
  
### getReplace()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode getReplace()

Replace destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode replace = 1; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode)` | The replace.  
  
### getReplaceOrBuilder()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadModeOrBuilder getReplaceOrBuilder()

Replace destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode replace = 1; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadModeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadModeOrBuilder)` |   
  
### getUnique()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode getUnique()

Insert records where the value of a column is not already present in the destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode unique = 4; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode)` | The unique.  
  
### getUniqueOrBuilder()
    
    
    public abstract WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadModeOrBuilder getUniqueOrBuilder()

Insert records where the value of a column is not already present in the destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode unique = 4; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadModeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadModeOrBuilder)` |   
  
### hasAppend()
    
    
    public abstract boolean hasAppend()

Append into destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode append = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the append field is set.  
  
### hasMaximum()
    
    
    public abstract boolean hasMaximum()

Insert records where the value exceeds the previous maximum value for a column in the destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode maximum = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maximum field is set.  
  
### hasReplace()
    
    
    public abstract boolean hasReplace()

Replace destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode replace = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the replace field is set.  
  
### hasUnique()
    
    
    public abstract boolean hasUnique()

Insert records where the value of a column is not already present in the destination table

` .google.cloud.dataform.v1.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode unique = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unique field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
