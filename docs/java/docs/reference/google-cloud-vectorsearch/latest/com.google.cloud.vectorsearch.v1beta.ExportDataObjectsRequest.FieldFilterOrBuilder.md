---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilterOrBuilder
title: Interface ExportDataObjectsRequest.FieldFilterOrBuilder (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:03.029037+00:00
---

# Interface ExportDataObjectsRequest.FieldFilterOrBuilder (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExportDataObjectsRequest.FieldFilterOrBuilder (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface ExportDataObjectsRequest.FieldFilterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExcludedFields()
    
    
    public abstract ExportDataObjectsRequest.FieldFilter.FieldList getExcludedFields()

Optional. Every top-level field except these will appear in each exported record.

` .google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList excluded_fields = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExportDataObjectsRequest.FieldFilter.FieldList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList)` | The excludedFields.  
  
### getExcludedFieldsOrBuilder()
    
    
    public abstract ExportDataObjectsRequest.FieldFilter.FieldListOrBuilder getExcludedFieldsOrBuilder()

Optional. Every top-level field except these will appear in each exported record.

` .google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList excluded_fields = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExportDataObjectsRequest.FieldFilter.FieldListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldListOrBuilder)` |   
  
### getIncludedFields()
    
    
    public abstract ExportDataObjectsRequest.FieldFilter.FieldList getIncludedFields()

Optional. Only these top-level fields will appear in each exported record.

` .google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList included_fields = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExportDataObjectsRequest.FieldFilter.FieldList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList)` | The includedFields.  
  
### getIncludedFieldsOrBuilder()
    
    
    public abstract ExportDataObjectsRequest.FieldFilter.FieldListOrBuilder getIncludedFieldsOrBuilder()

Optional. Only these top-level fields will appear in each exported record.

` .google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList included_fields = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExportDataObjectsRequest.FieldFilter.FieldListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldListOrBuilder)` |   
  
### getSelectorCase()
    
    
    public abstract ExportDataObjectsRequest.FieldFilter.SelectorCase getSelectorCase()

**Returns**  
---  
**Type** | **Description**  
`[ExportDataObjectsRequest.FieldFilter.SelectorCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.SelectorCase)` |   
  
### hasExcludedFields()
    
    
    public abstract boolean hasExcludedFields()

Optional. Every top-level field except these will appear in each exported record.

` .google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList excluded_fields = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the excludedFields field is set.  
  
### hasIncludedFields()
    
    
    public abstract boolean hasIncludedFields()

Optional. Only these top-level fields will appear in each exported record.

` .google.cloud.vectorsearch.v1beta.ExportDataObjectsRequest.FieldFilter.FieldList included_fields = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the includedFields field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
