---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RaySpecOrBuilder
title: Interface RaySpecOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:46.997436+00:00
---

# Interface RaySpecOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RaySpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RaySpecOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface RaySpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsResourcePoolImages(String key)
    
    
    public abstract boolean containsResourcePoolImages(String key)

Optional. Required if image_uri isn't set. A map of resource_pool_id to prebuild Ray image if user need to use different images for different head/worker pools. This map needs to cover all the resource pool ids. Example: { "ray_head_node_pool": "head image" "ray_worker_node_pool1": "worker image" "ray_worker_node_pool2": "another worker image" }

` map<string, string> resource_pool_images = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeadNodeResourcePoolId()
    
    
    public abstract String getHeadNodeResourcePoolId()

Optional. This will be used to indicate which resource pool will serve as the Ray head node(the first node within that pool). Will use the machine from the first workerpool as the head node by default if this field isn't set.

`string head_node_resource_pool_id = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The headNodeResourcePoolId.  
  
### getHeadNodeResourcePoolIdBytes()
    
    
    public abstract ByteString getHeadNodeResourcePoolIdBytes()

Optional. This will be used to indicate which resource pool will serve as the Ray head node(the first node within that pool). Will use the machine from the first workerpool as the head node by default if this field isn't set.

`string head_node_resource_pool_id = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for headNodeResourcePoolId.  
  
### getImageUri()
    
    
    public abstract String getImageUri()

Optional. Default image for user to choose a preferred ML framework (for example, TensorFlow or Pytorch) by choosing from [Vertex prebuilt images](https://cloud.google.com/vertex-ai/docs/training/pre-built-containers). Either this or the resource_pool_images is required. Use this field if you need all the resource pools to have the same Ray image. Otherwise, use the {@code resource_pool_images} field.

`string image_uri = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imageUri.  
  
### getImageUriBytes()
    
    
    public abstract ByteString getImageUriBytes()

Optional. Default image for user to choose a preferred ML framework (for example, TensorFlow or Pytorch) by choosing from [Vertex prebuilt images](https://cloud.google.com/vertex-ai/docs/training/pre-built-containers). Either this or the resource_pool_images is required. Use this field if you need all the resource pools to have the same Ray image. Otherwise, use the {@code resource_pool_images} field.

`string image_uri = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imageUri.  
  
### getNfsMounts(int index)
    
    
    public abstract NfsMount getNfsMounts(int index)

Optional. Use if you want to mount to any NFS storages.

` repeated .google.cloud.aiplatform.v1beta1.NfsMount nfs_mounts = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NfsMount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NfsMount)` |   
  
### getNfsMountsCount()
    
    
    public abstract int getNfsMountsCount()

Optional. Use if you want to mount to any NFS storages.

` repeated .google.cloud.aiplatform.v1beta1.NfsMount nfs_mounts = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNfsMountsList()
    
    
    public abstract List<NfsMount> getNfsMountsList()

Optional. Use if you want to mount to any NFS storages.

` repeated .google.cloud.aiplatform.v1beta1.NfsMount nfs_mounts = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NfsMount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NfsMount)>` |   
  
### getNfsMountsOrBuilder(int index)
    
    
    public abstract NfsMountOrBuilder getNfsMountsOrBuilder(int index)

Optional. Use if you want to mount to any NFS storages.

` repeated .google.cloud.aiplatform.v1beta1.NfsMount nfs_mounts = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NfsMountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NfsMountOrBuilder)` |   
  
### getNfsMountsOrBuilderList()
    
    
    public abstract List<? extends NfsMountOrBuilder> getNfsMountsOrBuilderList()

Optional. Use if you want to mount to any NFS storages.

` repeated .google.cloud.aiplatform.v1beta1.NfsMount nfs_mounts = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.NfsMountOrBuilder>` |   
  
### getRayLogsSpec()
    
    
    public abstract RayLogsSpec getRayLogsSpec()

Optional. OSS Ray logging configurations.

` .google.cloud.aiplatform.v1beta1.RayLogsSpec ray_logs_spec = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RayLogsSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RayLogsSpec)` | The rayLogsSpec.  
  
### getRayLogsSpecOrBuilder()
    
    
    public abstract RayLogsSpecOrBuilder getRayLogsSpecOrBuilder()

Optional. OSS Ray logging configurations.

` .google.cloud.aiplatform.v1beta1.RayLogsSpec ray_logs_spec = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RayLogsSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RayLogsSpecOrBuilder)` |   
  
### getRayMetricSpec()
    
    
    public abstract RayMetricSpec getRayMetricSpec()

Optional. Ray metrics configurations.

` .google.cloud.aiplatform.v1beta1.RayMetricSpec ray_metric_spec = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RayMetricSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RayMetricSpec)` | The rayMetricSpec.  
  
### getRayMetricSpecOrBuilder()
    
    
    public abstract RayMetricSpecOrBuilder getRayMetricSpecOrBuilder()

Optional. Ray metrics configurations.

` .google.cloud.aiplatform.v1beta1.RayMetricSpec ray_metric_spec = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RayMetricSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RayMetricSpecOrBuilder)` |   
  
### getResourcePoolImages() (deprecated)
    
    
    public abstract Map<String,String> getResourcePoolImages()

Use [#getResourcePoolImagesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RaySpecOrBuilder#com_google_cloud_aiplatform_v1beta1_RaySpecOrBuilder_getResourcePoolImagesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourcePoolImagesCount()
    
    
    public abstract int getResourcePoolImagesCount()

Optional. Required if image_uri isn't set. A map of resource_pool_id to prebuild Ray image if user need to use different images for different head/worker pools. This map needs to cover all the resource pool ids. Example: { "ray_head_node_pool": "head image" "ray_worker_node_pool1": "worker image" "ray_worker_node_pool2": "another worker image" }

` map<string, string> resource_pool_images = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourcePoolImagesMap()
    
    
    public abstract Map<String,String> getResourcePoolImagesMap()

Optional. Required if image_uri isn't set. A map of resource_pool_id to prebuild Ray image if user need to use different images for different head/worker pools. This map needs to cover all the resource pool ids. Example: { "ray_head_node_pool": "head image" "ray_worker_node_pool1": "worker image" "ray_worker_node_pool2": "another worker image" }

` map<string, string> resource_pool_images = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourcePoolImagesOrDefault(String key, String defaultValue)
    
    
    public abstract String getResourcePoolImagesOrDefault(String key, String defaultValue)

Optional. Required if image_uri isn't set. A map of resource_pool_id to prebuild Ray image if user need to use different images for different head/worker pools. This map needs to cover all the resource pool ids. Example: { "ray_head_node_pool": "head image" "ray_worker_node_pool1": "worker image" "ray_worker_node_pool2": "another worker image" }

` map<string, string> resource_pool_images = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourcePoolImagesOrThrow(String key)
    
    
    public abstract String getResourcePoolImagesOrThrow(String key)

Optional. Required if image_uri isn't set. A map of resource_pool_id to prebuild Ray image if user need to use different images for different head/worker pools. This map needs to cover all the resource pool ids. Example: { "ray_head_node_pool": "head image" "ray_worker_node_pool1": "worker image" "ray_worker_node_pool2": "another worker image" }

` map<string, string> resource_pool_images = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasRayLogsSpec()
    
    
    public abstract boolean hasRayLogsSpec()

Optional. OSS Ray logging configurations.

` .google.cloud.aiplatform.v1beta1.RayLogsSpec ray_logs_spec = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rayLogsSpec field is set.  
  
### hasRayMetricSpec()
    
    
    public abstract boolean hasRayMetricSpec()

Optional. Ray metrics configurations.

` .google.cloud.aiplatform.v1beta1.RayMetricSpec ray_metric_spec = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rayMetricSpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
