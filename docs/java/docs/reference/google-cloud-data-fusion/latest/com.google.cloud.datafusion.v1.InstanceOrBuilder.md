---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.InstanceOrBuilder
title: Interface InstanceOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:36.295979+00:00
---

# Interface InstanceOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.InstanceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InstanceOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.1.1 
    
    
    public interface InstanceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.

`map<string, string> labels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsOptions(String key)
    
    
    public abstract boolean containsOptions(String key)

Map of additional options used to configure the behavior of Data Fusion instance.

`map<string, string> options = 9;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccelerators(int index)
    
    
    public abstract Accelerator getAccelerators(int index)

List of accelerators enabled for this CDF instance.

`repeated .google.cloud.datafusion.v1.Accelerator accelerators = 22;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Accelerator)` |   
  
### getAcceleratorsCount()
    
    
    public abstract int getAcceleratorsCount()

List of accelerators enabled for this CDF instance.

`repeated .google.cloud.datafusion.v1.Accelerator accelerators = 22;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAcceleratorsList()
    
    
    public abstract List<Accelerator> getAcceleratorsList()

List of accelerators enabled for this CDF instance.

`repeated .google.cloud.datafusion.v1.Accelerator accelerators = 22;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Accelerator)>` |   
  
### getAcceleratorsOrBuilder(int index)
    
    
    public abstract AcceleratorOrBuilder getAcceleratorsOrBuilder(int index)

List of accelerators enabled for this CDF instance.

`repeated .google.cloud.datafusion.v1.Accelerator accelerators = 22;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.AcceleratorOrBuilder)` |   
  
### getAcceleratorsOrBuilderList()
    
    
    public abstract List<? extends AcceleratorOrBuilder> getAcceleratorsOrBuilderList()

List of accelerators enabled for this CDF instance.

`repeated .google.cloud.datafusion.v1.Accelerator accelerators = 22;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.datafusion.v1.AcceleratorOrBuilder>` |   
  
### getApiEndpoint()
    
    
    public abstract String getApiEndpoint()

Output only. Endpoint on which the REST APIs is accessible.

`string api_endpoint = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The apiEndpoint.  
  
### getApiEndpointBytes()
    
    
    public abstract ByteString getApiEndpointBytes()

Output only. Endpoint on which the REST APIs is accessible.

`string api_endpoint = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for apiEndpoint.  
  
### getAvailableVersion(int index)
    
    
    public abstract Version getAvailableVersion(int index)

Available versions that the instance can be upgraded to using UpdateInstanceRequest.

`repeated .google.cloud.datafusion.v1.Version available_version = 19;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Version)` |   
  
### getAvailableVersionCount()
    
    
    public abstract int getAvailableVersionCount()

Available versions that the instance can be upgraded to using UpdateInstanceRequest.

`repeated .google.cloud.datafusion.v1.Version available_version = 19;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAvailableVersionList()
    
    
    public abstract List<Version> getAvailableVersionList()

Available versions that the instance can be upgraded to using UpdateInstanceRequest.

`repeated .google.cloud.datafusion.v1.Version available_version = 19;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Version](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Version)>` |   
  
### getAvailableVersionOrBuilder(int index)
    
    
    public abstract VersionOrBuilder getAvailableVersionOrBuilder(int index)

Available versions that the instance can be upgraded to using UpdateInstanceRequest.

`repeated .google.cloud.datafusion.v1.Version available_version = 19;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VersionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.VersionOrBuilder)` |   
  
### getAvailableVersionOrBuilderList()
    
    
    public abstract List<? extends VersionOrBuilder> getAvailableVersionOrBuilderList()

Available versions that the instance can be upgraded to using UpdateInstanceRequest.

`repeated .google.cloud.datafusion.v1.Version available_version = 19;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.datafusion.v1.VersionOrBuilder>` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time the instance was created.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time the instance was created.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCryptoKeyConfig()
    
    
    public abstract CryptoKeyConfig getCryptoKeyConfig()

The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.

`.google.cloud.datafusion.v1.CryptoKeyConfig crypto_key_config = 28;`

**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.CryptoKeyConfig)` | The cryptoKeyConfig.  
  
### getCryptoKeyConfigOrBuilder()
    
    
    public abstract CryptoKeyConfigOrBuilder getCryptoKeyConfigOrBuilder()

The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.

`.google.cloud.datafusion.v1.CryptoKeyConfig crypto_key_config = 28;`

**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.CryptoKeyConfigOrBuilder)` |   
  
### getDataprocServiceAccount()
    
    
    public abstract String getDataprocServiceAccount()

User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines.

This allows users to have fine-grained access control on Dataproc's accesses to cloud resources.

`string dataproc_service_account = 25;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataprocServiceAccount.  
  
### getDataprocServiceAccountBytes()
    
    
    public abstract ByteString getDataprocServiceAccountBytes()

User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines.

This allows users to have fine-grained access control on Dataproc's accesses to cloud resources.

`string dataproc_service_account = 25;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataprocServiceAccount.  
  
### getDescription()
    
    
    public abstract String getDescription()

A description of this instance.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

A description of this instance.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisabledReason(int index)
    
    
    public abstract Instance.DisabledReason getDisabledReason(int index)

Output only. If the instance state is DISABLED, the reason for disabling the instance.

` repeated .google.cloud.datafusion.v1.Instance.DisabledReason disabled_reason = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Instance.DisabledReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Instance.DisabledReason)` | The disabledReason at the given index.  
  
### getDisabledReasonCount()
    
    
    public abstract int getDisabledReasonCount()

Output only. If the instance state is DISABLED, the reason for disabling the instance.

` repeated .google.cloud.datafusion.v1.Instance.DisabledReason disabled_reason = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of disabledReason.  
  
### getDisabledReasonList()
    
    
    public abstract List<Instance.DisabledReason> getDisabledReasonList()

Output only. If the instance state is DISABLED, the reason for disabling the instance.

` repeated .google.cloud.datafusion.v1.Instance.DisabledReason disabled_reason = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DisabledReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Instance.DisabledReason)>` | A list containing the disabledReason.  
  
### getDisabledReasonValue(int index)
    
    
    public abstract int getDisabledReasonValue(int index)

Output only. If the instance state is DISABLED, the reason for disabling the instance.

` repeated .google.cloud.datafusion.v1.Instance.DisabledReason disabled_reason = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of disabledReason at the given index.  
  
### getDisabledReasonValueList()
    
    
    public abstract List<Integer> getDisabledReasonValueList()

Output only. If the instance state is DISABLED, the reason for disabling the instance.

` repeated .google.cloud.datafusion.v1.Instance.DisabledReason disabled_reason = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for disabledReason.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Display name for an instance.

`string display_name = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Display name for an instance.

`string display_name = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnableRbac()
    
    
    public abstract boolean getEnableRbac()

Option to enable granular role-based access control.

`bool enable_rbac = 27;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableRbac.  
  
### getEnableStackdriverLogging()
    
    
    public abstract boolean getEnableStackdriverLogging()

Option to enable Stackdriver Logging.

`bool enable_stackdriver_logging = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableStackdriverLogging.  
  
### getEnableStackdriverMonitoring()
    
    
    public abstract boolean getEnableStackdriverMonitoring()

Option to enable Stackdriver Monitoring.

`bool enable_stackdriver_monitoring = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableStackdriverMonitoring.  
  
### getGcsBucket()
    
    
    public abstract String getGcsBucket()

Output only. Cloud Storage bucket generated by Data Fusion in the customer project.

`string gcs_bucket = 21 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcsBucket.  
  
### getGcsBucketBytes()
    
    
    public abstract ByteString getGcsBucketBytes()

Output only. Cloud Storage bucket generated by Data Fusion in the customer project.

`string gcs_bucket = 21 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcsBucket.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.InstanceOrBuilder#com_google_cloud_datafusion_v1_InstanceOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.

`map<string, string> labels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.

`map<string, string> labels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.

`map<string, string> labels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.

`map<string, string> labels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}.

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}.

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetworkConfig()
    
    
    public abstract NetworkConfig getNetworkConfig()

Network configuration options. These are required when a private Data Fusion instance is to be created.

`.google.cloud.datafusion.v1.NetworkConfig network_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.NetworkConfig)` | The networkConfig.  
  
### getNetworkConfigOrBuilder()
    
    
    public abstract NetworkConfigOrBuilder getNetworkConfigOrBuilder()

Network configuration options. These are required when a private Data Fusion instance is to be created.

`.google.cloud.datafusion.v1.NetworkConfig network_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.NetworkConfigOrBuilder)` |   
  
### getOptions() (deprecated)
    
    
    public abstract Map<String,String> getOptions()

Use [#getOptionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.InstanceOrBuilder#com_google_cloud_datafusion_v1_InstanceOrBuilder_getOptionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getOptionsCount()
    
    
    public abstract int getOptionsCount()

Map of additional options used to configure the behavior of Data Fusion instance.

`map<string, string> options = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOptionsMap()
    
    
    public abstract Map<String,String> getOptionsMap()

Map of additional options used to configure the behavior of Data Fusion instance.

`map<string, string> options = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getOptionsOrDefault(String key, String defaultValue)
    
    
    public abstract String getOptionsOrDefault(String key, String defaultValue)

Map of additional options used to configure the behavior of Data Fusion instance.

`map<string, string> options = 9;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getOptionsOrThrow(String key)
    
    
    public abstract String getOptionsOrThrow(String key)

Map of additional options used to configure the behavior of Data Fusion instance.

`map<string, string> options = 9;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getP4ServiceAccount()
    
    
    public abstract String getP4ServiceAccount()

Output only. P4 service account for the customer project.

`string p4_service_account = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The p4ServiceAccount.  
  
### getP4ServiceAccountBytes()
    
    
    public abstract ByteString getP4ServiceAccountBytes()

Output only. P4 service account for the customer project.

`string p4_service_account = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for p4ServiceAccount.  
  
### getPrivateInstance()
    
    
    public abstract boolean getPrivateInstance()

Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet.

`bool private_instance = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The privateInstance.  
  
### getServiceAccount() (deprecated)
    
    
    public abstract String getServiceAccount()

**Deprecated.** _google.cloud.datafusion.v1.Instance.service_account is deprecated. See google/cloud/datafusion/v1/datafusion.proto;l=361_

Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID.

` string service_account = 17 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes() (deprecated)
    
    
    public abstract ByteString getServiceAccountBytes()

**Deprecated.** _google.cloud.datafusion.v1.Instance.service_account is deprecated. See google/cloud/datafusion/v1/datafusion.proto;l=361_

Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID.

` string service_account = 17 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getServiceEndpoint()
    
    
    public abstract String getServiceEndpoint()

Output only. Endpoint on which the Data Fusion UI is accessible.

`string service_endpoint = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceEndpoint.  
  
### getServiceEndpointBytes()
    
    
    public abstract ByteString getServiceEndpointBytes()

Output only. Endpoint on which the Data Fusion UI is accessible.

`string service_endpoint = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceEndpoint.  
  
### getState()
    
    
    public abstract Instance.State getState()

Output only. The current state of this Data Fusion instance.

` .google.cloud.datafusion.v1.Instance.State state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Instance.State)` | The state.  
  
### getStateMessage()
    
    
    public abstract String getStateMessage()

Output only. Additional information about the current state of this Data Fusion instance if available.

`string state_message = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateMessage.  
  
### getStateMessageBytes()
    
    
    public abstract ByteString getStateMessageBytes()

Output only. Additional information about the current state of this Data Fusion instance if available.

`string state_message = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateMessage.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of this Data Fusion instance.

` .google.cloud.datafusion.v1.Instance.State state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getTenantProjectId()
    
    
    public abstract String getTenantProjectId()

Output only. The name of the tenant project.

`string tenant_project_id = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tenantProjectId.  
  
### getTenantProjectIdBytes()
    
    
    public abstract ByteString getTenantProjectIdBytes()

Output only. The name of the tenant project.

`string tenant_project_id = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tenantProjectId.  
  
### getType()
    
    
    public abstract Instance.Type getType()

Required. Instance type.

` .google.cloud.datafusion.v1.Instance.Type type = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1.Instance.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Required. Instance type.

` .google.cloud.datafusion.v1.Instance.Type type = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time the instance was last updated.

`.google.protobuf.Timestamp update_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time the instance was last updated.

`.google.protobuf.Timestamp update_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getVersion()
    
    
    public abstract String getVersion()

Current version of the Data Fusion. Only specifiable in Update.

`string version = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The version.  
  
### getVersionBytes()
    
    
    public abstract ByteString getVersionBytes()

Current version of the Data Fusion. Only specifiable in Update.

`string version = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for version.  
  
### getZone()
    
    
    public abstract String getZone()

Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field.

`string zone = 15;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public abstract ByteString getZoneBytes()

Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field.

`string zone = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time the instance was created.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasCryptoKeyConfig()
    
    
    public abstract boolean hasCryptoKeyConfig()

The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.

`.google.cloud.datafusion.v1.CryptoKeyConfig crypto_key_config = 28;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cryptoKeyConfig field is set.  
  
### hasNetworkConfig()
    
    
    public abstract boolean hasNetworkConfig()

Network configuration options. These are required when a private Data Fusion instance is to be created.

`.google.cloud.datafusion.v1.NetworkConfig network_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkConfig field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time the instance was last updated.

`.google.protobuf.Timestamp update_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
