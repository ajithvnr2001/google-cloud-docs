---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.ModelServerInfoOrBuilder
title: Interface ModelServerInfoOrBuilder (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:20.113116+00:00
---

# Interface ModelServerInfoOrBuilder (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.ModelServerInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModelServerInfoOrBuilder (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ModelServerInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getModel()
    
    
    public abstract String getModel()

Required. The model. Open-source models follow the Huggingface Hub `owner/model_name` format. Use GkeInferenceQuickstart.FetchModels to find available models.

`string model = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The model.  
  
### getModelBytes()
    
    
    public abstract ByteString getModelBytes()

Required. The model. Open-source models follow the Huggingface Hub `owner/model_name` format. Use GkeInferenceQuickstart.FetchModels to find available models.

`string model = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for model.  
  
### getModelServer()
    
    
    public abstract String getModelServer()

Required. The model server. Open-source model servers use simplified, lowercase names (e.g., `vllm`). Use GkeInferenceQuickstart.FetchModelServers to find available servers.

`string model_server = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modelServer.  
  
### getModelServerBytes()
    
    
    public abstract ByteString getModelServerBytes()

Required. The model server. Open-source model servers use simplified, lowercase names (e.g., `vllm`). Use GkeInferenceQuickstart.FetchModelServers to find available servers.

`string model_server = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modelServer.  
  
### getModelServerVersion()
    
    
    public abstract String getModelServerVersion()

Optional. The model server version. Use GkeInferenceQuickstart.FetchModelServerVersions to find available versions. If not provided, the latest available version is used.

`string model_server_version = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modelServerVersion.  
  
### getModelServerVersionBytes()
    
    
    public abstract ByteString getModelServerVersionBytes()

Optional. The model server version. Use GkeInferenceQuickstart.FetchModelServerVersions to find available versions. If not provided, the latest available version is used.

`string model_server_version = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modelServerVersion.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
