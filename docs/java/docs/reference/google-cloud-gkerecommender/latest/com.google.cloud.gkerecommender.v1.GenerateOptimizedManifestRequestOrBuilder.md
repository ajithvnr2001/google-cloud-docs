---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequestOrBuilder
title: Interface GenerateOptimizedManifestRequestOrBuilder (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:59.754654+00:00
---

# Interface GenerateOptimizedManifestRequestOrBuilder (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GenerateOptimizedManifestRequestOrBuilder (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GenerateOptimizedManifestRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAcceleratorType()
    
    
    public abstract String getAcceleratorType()

Required. The accelerator type. Use GkeInferenceQuickstart.FetchProfiles to find valid accelerators for a given `model_server_info`.

`string accelerator_type = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The acceleratorType.  
  
### getAcceleratorTypeBytes()
    
    
    public abstract ByteString getAcceleratorTypeBytes()

Required. The accelerator type. Use GkeInferenceQuickstart.FetchProfiles to find valid accelerators for a given `model_server_info`.

`string accelerator_type = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for acceleratorType.  
  
### getKubernetesNamespace()
    
    
    public abstract String getKubernetesNamespace()

Optional. The kubernetes namespace to deploy the manifests in.

`string kubernetes_namespace = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kubernetesNamespace.  
  
### getKubernetesNamespaceBytes()
    
    
    public abstract ByteString getKubernetesNamespaceBytes()

Optional. The kubernetes namespace to deploy the manifests in.

`string kubernetes_namespace = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kubernetesNamespace.  
  
### getModelServerInfo()
    
    
    public abstract ModelServerInfo getModelServerInfo()

Required. The model server configuration to generate the manifest for. Use GkeInferenceQuickstart.FetchProfiles to find valid configurations.

` .google.cloud.gkerecommender.v1.ModelServerInfo model_server_info = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelServerInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.ModelServerInfo)` | The modelServerInfo.  
  
### getModelServerInfoOrBuilder()
    
    
    public abstract ModelServerInfoOrBuilder getModelServerInfoOrBuilder()

Required. The model server configuration to generate the manifest for. Use GkeInferenceQuickstart.FetchProfiles to find valid configurations.

` .google.cloud.gkerecommender.v1.ModelServerInfo model_server_info = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelServerInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.ModelServerInfoOrBuilder)` |   
  
### getPerformanceRequirements()
    
    
    public abstract PerformanceRequirements getPerformanceRequirements()

Optional. The performance requirements to use for generating Horizontal Pod Autoscaler (HPA) resources. If provided, the manifest includes HPA resources to adjust the model server replica count to maintain the specified targets (e.g., NTPOT, TTFT) at a P50 latency. Cost targets are not currently supported for HPA generation. If the specified targets are not achievable, the HPA manifest will not be generated.

` .google.cloud.gkerecommender.v1.PerformanceRequirements performance_requirements = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PerformanceRequirements](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.PerformanceRequirements)` | The performanceRequirements.  
  
### getPerformanceRequirementsOrBuilder()
    
    
    public abstract PerformanceRequirementsOrBuilder getPerformanceRequirementsOrBuilder()

Optional. The performance requirements to use for generating Horizontal Pod Autoscaler (HPA) resources. If provided, the manifest includes HPA resources to adjust the model server replica count to maintain the specified targets (e.g., NTPOT, TTFT) at a P50 latency. Cost targets are not currently supported for HPA generation. If the specified targets are not achievable, the HPA manifest will not be generated.

` .google.cloud.gkerecommender.v1.PerformanceRequirements performance_requirements = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PerformanceRequirementsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.PerformanceRequirementsOrBuilder)` |   
  
### getStorageConfig()
    
    
    public abstract StorageConfig getStorageConfig()

Optional. The storage configuration for the model. If not provided, the model is loaded from Huggingface.

` .google.cloud.gkerecommender.v1.StorageConfig storage_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.StorageConfig)` | The storageConfig.  
  
### getStorageConfigOrBuilder()
    
    
    public abstract StorageConfigOrBuilder getStorageConfigOrBuilder()

Optional. The storage configuration for the model. If not provided, the model is loaded from Huggingface.

` .google.cloud.gkerecommender.v1.StorageConfig storage_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StorageConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.StorageConfigOrBuilder)` |   
  
### hasModelServerInfo()
    
    
    public abstract boolean hasModelServerInfo()

Required. The model server configuration to generate the manifest for. Use GkeInferenceQuickstart.FetchProfiles to find valid configurations.

` .google.cloud.gkerecommender.v1.ModelServerInfo model_server_info = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modelServerInfo field is set.  
  
### hasPerformanceRequirements()
    
    
    public abstract boolean hasPerformanceRequirements()

Optional. The performance requirements to use for generating Horizontal Pod Autoscaler (HPA) resources. If provided, the manifest includes HPA resources to adjust the model server replica count to maintain the specified targets (e.g., NTPOT, TTFT) at a P50 latency. Cost targets are not currently supported for HPA generation. If the specified targets are not achievable, the HPA manifest will not be generated.

` .google.cloud.gkerecommender.v1.PerformanceRequirements performance_requirements = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the performanceRequirements field is set.  
  
### hasStorageConfig()
    
    
    public abstract boolean hasStorageConfig()

Optional. The storage configuration for the model. If not provided, the model is loaded from Huggingface.

` .google.cloud.gkerecommender.v1.StorageConfig storage_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the storageConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
