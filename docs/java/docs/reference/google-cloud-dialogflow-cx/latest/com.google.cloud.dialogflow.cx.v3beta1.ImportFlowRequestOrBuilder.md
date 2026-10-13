---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequestOrBuilder
title: Interface ImportFlowRequestOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:42.639679+00:00
---

# Interface ImportFlowRequestOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportFlowRequestOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public interface ImportFlowRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFlowCase()
    
    
    public abstract ImportFlowRequest.FlowCase getFlowCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportFlowRequest.FlowCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequest.FlowCase)` |   
  
### getFlowContent()
    
    
    public abstract ByteString getFlowContent()

Uncompressed raw byte content for flow.

`bytes flow_content = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The flowContent.  
  
### getFlowImportStrategy()
    
    
    public abstract FlowImportStrategy getFlowImportStrategy()

Optional. Specifies the import strategy used when resolving resource conflicts.

` .google.cloud.dialogflow.cx.v3beta1.FlowImportStrategy flow_import_strategy = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FlowImportStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowImportStrategy)` | The flowImportStrategy.  
  
### getFlowImportStrategyOrBuilder()
    
    
    public abstract FlowImportStrategyOrBuilder getFlowImportStrategyOrBuilder()

Optional. Specifies the import strategy used when resolving resource conflicts.

` .google.cloud.dialogflow.cx.v3beta1.FlowImportStrategy flow_import_strategy = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FlowImportStrategyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowImportStrategyOrBuilder)` |   
  
### getFlowUri()
    
    
    public abstract String getFlowUri()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import flow from. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

`string flow_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The flowUri.  
  
### getFlowUriBytes()
    
    
    public abstract ByteString getFlowUriBytes()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import flow from. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

`string flow_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for flowUri.  
  
### getImportOption()
    
    
    public abstract ImportFlowRequest.ImportOption getImportOption()

Flow import mode. If not specified, `KEEP` is assumed.

`.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequest.ImportOption import_option = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ImportFlowRequest.ImportOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequest.ImportOption)` | The importOption.  
  
### getImportOptionValue()
    
    
    public abstract int getImportOptionValue()

Flow import mode. If not specified, `KEEP` is assumed.

`.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequest.ImportOption import_option = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for importOption.  
  
### getParent()
    
    
    public abstract String getParent()

Required. The agent to import the flow into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The agent to import the flow into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasFlowContent()
    
    
    public abstract boolean hasFlowContent()

Uncompressed raw byte content for flow.

`bytes flow_content = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the flowContent field is set.  
  
### hasFlowImportStrategy()
    
    
    public abstract boolean hasFlowImportStrategy()

Optional. Specifies the import strategy used when resolving resource conflicts.

` .google.cloud.dialogflow.cx.v3beta1.FlowImportStrategy flow_import_strategy = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the flowImportStrategy field is set.  
  
### hasFlowUri()
    
    
    public abstract boolean hasFlowUri()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import flow from. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

`string flow_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the flowUri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
