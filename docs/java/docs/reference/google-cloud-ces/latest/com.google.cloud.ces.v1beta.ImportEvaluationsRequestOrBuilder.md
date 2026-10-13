---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequestOrBuilder
title: Interface ImportEvaluationsRequestOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:05.072437+00:00
---

# Interface ImportEvaluationsRequestOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportEvaluationsRequestOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ImportEvaluationsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConversationList()
    
    
    public abstract ImportEvaluationsRequest.ConversationList getConversationList()

The conversations to import the evaluations from.

`.google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationList conversation_list = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ImportEvaluationsRequest.ConversationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationList)` | The conversationList.  
  
### getConversationListOrBuilder()
    
    
    public abstract ImportEvaluationsRequest.ConversationListOrBuilder getConversationListOrBuilder()

The conversations to import the evaluations from.

`.google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationList conversation_list = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ImportEvaluationsRequest.ConversationListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationListOrBuilder)` |   
  
### getCsvContent()
    
    
    public abstract ByteString getCsvContent()

Raw bytes representing the csv file with the evaluations structure.

`bytes csv_content = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The csvContent.  
  
### getGcsUri()
    
    
    public abstract String getGcsUri()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import evaluations. The format of this URI must be `gs://<bucket-name>/<object-name>`.

`string gcs_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcsUri.  
  
### getGcsUriBytes()
    
    
    public abstract ByteString getGcsUriBytes()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import evaluations. The format of this URI must be `gs://<bucket-name>/<object-name>`.

`string gcs_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcsUri.  
  
### getImportOptions()
    
    
    public abstract ImportEvaluationsRequest.ImportOptions getImportOptions()

Optional. Options governing the import process for the evaluations.

` .google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions import_options = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportEvaluationsRequest.ImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions)` | The importOptions.  
  
### getImportOptionsOrBuilder()
    
    
    public abstract ImportEvaluationsRequest.ImportOptionsOrBuilder getImportOptionsOrBuilder()

Optional. Options governing the import process for the evaluations.

` .google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions import_options = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportEvaluationsRequest.ImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptionsOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The app to import the evaluations into. Format: `projects/{project}/locations/{location}/apps/{app}`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The app to import the evaluations into. Format: `projects/{project}/locations/{location}/apps/{app}`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getSourceCase()
    
    
    public abstract ImportEvaluationsRequest.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportEvaluationsRequest.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest.SourceCase)` |   
  
### hasConversationList()
    
    
    public abstract boolean hasConversationList()

The conversations to import the evaluations from.

`.google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationList conversation_list = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the conversationList field is set.  
  
### hasCsvContent()
    
    
    public abstract boolean hasCsvContent()

Raw bytes representing the csv file with the evaluations structure.

`bytes csv_content = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the csvContent field is set.  
  
### hasGcsUri()
    
    
    public abstract boolean hasGcsUri()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import evaluations. The format of this URI must be `gs://<bucket-name>/<object-name>`.

`string gcs_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsUri field is set.  
  
### hasImportOptions()
    
    
    public abstract boolean hasImportOptions()

Optional. Options governing the import process for the evaluations.

` .google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions import_options = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the importOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
