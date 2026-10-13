---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationsRequestOrBuilder
title: Interface ExportEvaluationsRequestOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:11.080510+00:00
---

# Interface ExportEvaluationsRequestOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExportEvaluationsRequestOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ExportEvaluationsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExportOptions()
    
    
    public abstract ExportOptions getExportOptions()

Optional. The export options for the evaluations.

` .google.cloud.ces.v1beta.ExportOptions export_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportOptions)` | The exportOptions.  
  
### getExportOptionsOrBuilder()
    
    
    public abstract ExportOptionsOrBuilder getExportOptionsOrBuilder()

Optional. The export options for the evaluations.

` .google.cloud.ces.v1beta.ExportOptions export_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportOptionsOrBuilder)` |   
  
### getIncludeEvaluationResults()
    
    
    public abstract boolean getIncludeEvaluationResults()

Optional. Includes evaluation results in the export. At least one of include_evaluation_results or include_evaluations must be set.

`bool include_evaluation_results = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The includeEvaluationResults.  
  
### getIncludeEvaluations()
    
    
    public abstract boolean getIncludeEvaluations()

Optional. Includes evaluations in the export. At least one of include_evaluation_results or include_evaluations must be set.

`bool include_evaluations = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The includeEvaluations.  
  
### getNames(int index)
    
    
    public abstract String getNames(int index)

Required. The resource names of the evaluations to export.

` repeated string names = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

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

Required. The resource names of the evaluations to export.

` repeated string names = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

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

Required. The resource names of the evaluations to export.

` repeated string names = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of names.  
  
### getNamesList()
    
    
    public abstract List<String> getNamesList()

Required. The resource names of the evaluations to export.

` repeated string names = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the names.  
  
### getParent()
    
    
    public abstract String getParent()

Required. The resource name of the app to export evaluations from. Format: `projects/{project}/locations/{location}/apps/{app}`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The resource name of the app to export evaluations from. Format: `projects/{project}/locations/{location}/apps/{app}`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasExportOptions()
    
    
    public abstract boolean hasExportOptions()

Optional. The export options for the evaluations.

` .google.cloud.ces.v1beta.ExportOptions export_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the exportOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
