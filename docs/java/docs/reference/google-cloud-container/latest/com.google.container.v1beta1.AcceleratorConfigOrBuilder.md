---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AcceleratorConfigOrBuilder
title: Interface AcceleratorConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:51.822246+00:00
---

# Interface AcceleratorConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AcceleratorConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AcceleratorConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface AcceleratorConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAcceleratorCount()
    
    
    public abstract long getAcceleratorCount()

The number of the accelerator cards exposed to an instance.

`int64 accelerator_count = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The acceleratorCount.  
  
### getAcceleratorType()
    
    
    public abstract String getAcceleratorType()

The accelerator type resource name. List of supported accelerators [here](https://cloud.google.com/compute/docs/gpus)

`string accelerator_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The acceleratorType.  
  
### getAcceleratorTypeBytes()
    
    
    public abstract ByteString getAcceleratorTypeBytes()

The accelerator type resource name. List of supported accelerators [here](https://cloud.google.com/compute/docs/gpus)

`string accelerator_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for acceleratorType.  
  
### getGpuDriverInstallationConfig()
    
    
    public abstract GPUDriverInstallationConfig getGpuDriverInstallationConfig()

The configuration for auto installation of GPU driver.

` optional .google.container.v1beta1.GPUDriverInstallationConfig gpu_driver_installation_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[GPUDriverInstallationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GPUDriverInstallationConfig)` | The gpuDriverInstallationConfig.  
  
### getGpuDriverInstallationConfigOrBuilder()
    
    
    public abstract GPUDriverInstallationConfigOrBuilder getGpuDriverInstallationConfigOrBuilder()

The configuration for auto installation of GPU driver.

` optional .google.container.v1beta1.GPUDriverInstallationConfig gpu_driver_installation_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[GPUDriverInstallationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GPUDriverInstallationConfigOrBuilder)` |   
  
### getGpuPartitionSize()
    
    
    public abstract String getGpuPartitionSize()

Size of partitions to create on the GPU. Valid values are described in the NVIDIA [mig user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#partitioning).

`string gpu_partition_size = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gpuPartitionSize.  
  
### getGpuPartitionSizeBytes()
    
    
    public abstract ByteString getGpuPartitionSizeBytes()

Size of partitions to create on the GPU. Valid values are described in the NVIDIA [mig user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#partitioning).

`string gpu_partition_size = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gpuPartitionSize.  
  
### getGpuSharingConfig()
    
    
    public abstract GPUSharingConfig getGpuSharingConfig()

The configuration for GPU sharing options.

`optional .google.container.v1beta1.GPUSharingConfig gpu_sharing_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[GPUSharingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GPUSharingConfig)` | The gpuSharingConfig.  
  
### getGpuSharingConfigOrBuilder()
    
    
    public abstract GPUSharingConfigOrBuilder getGpuSharingConfigOrBuilder()

The configuration for GPU sharing options.

`optional .google.container.v1beta1.GPUSharingConfig gpu_sharing_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[GPUSharingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GPUSharingConfigOrBuilder)` |   
  
### getMaxTimeSharedClientsPerGpu() (deprecated)
    
    
    public abstract long getMaxTimeSharedClientsPerGpu()

**Deprecated.** _google.container.v1beta1.AcceleratorConfig.max_time_shared_clients_per_gpu is deprecated. See google/container/v1beta1/cluster_service.proto;l=6555_

The number of time-shared GPU resources to expose for each physical GPU.

`int64 max_time_shared_clients_per_gpu = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxTimeSharedClientsPerGpu.  
  
### hasGpuDriverInstallationConfig()
    
    
    public abstract boolean hasGpuDriverInstallationConfig()

The configuration for auto installation of GPU driver.

` optional .google.container.v1beta1.GPUDriverInstallationConfig gpu_driver_installation_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gpuDriverInstallationConfig field is set.  
  
### hasGpuSharingConfig()
    
    
    public abstract boolean hasGpuSharingConfig()

The configuration for GPU sharing options.

`optional .google.container.v1beta1.GPUSharingConfig gpu_sharing_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gpuSharingConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
