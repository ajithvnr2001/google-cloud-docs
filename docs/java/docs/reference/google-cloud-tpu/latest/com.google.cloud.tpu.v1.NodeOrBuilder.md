---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.NodeOrBuilder
title: Interface NodeOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:43.328632+00:00
---

# Interface NodeOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.NodeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NodeOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.2.6 
    
    
    public interface NodeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Resource labels to represent user-provided metadata.

`map<string, string> labels = 24;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAcceleratorType()
    
    
    public abstract String getAcceleratorType()

Required. The type of hardware accelerators associated with this node.

`string accelerator_type = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The acceleratorType.  
  
### getAcceleratorTypeBytes()
    
    
    public abstract ByteString getAcceleratorTypeBytes()

Required. The type of hardware accelerators associated with this node.

`string accelerator_type = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for acceleratorType.  
  
### getApiVersion()
    
    
    public abstract Node.ApiVersion getApiVersion()

Output only. The API version that created this Node.

` .google.cloud.tpu.v1.Node.ApiVersion api_version = 38 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Node.ApiVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.Node.ApiVersion)` | The apiVersion.  
  
### getApiVersionValue()
    
    
    public abstract int getApiVersionValue()

Output only. The API version that created this Node.

` .google.cloud.tpu.v1.Node.ApiVersion api_version = 38 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for apiVersion.  
  
### getCidrBlock()
    
    
    public abstract String getCidrBlock()

The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block.

`string cidr_block = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cidrBlock.  
  
### getCidrBlockBytes()
    
    
    public abstract ByteString getCidrBlockBytes()

The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block.

`string cidr_block = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cidrBlock.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the node was created.

`.google.protobuf.Timestamp create_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the node was created.

`.google.protobuf.Timestamp create_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

The user-supplied description of the TPU. Maximum of 512 characters.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

The user-supplied description of the TPU. Maximum of 512 characters.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getHealth()
    
    
    public abstract Node.Health getHealth()

The health status of the TPU node.

`.google.cloud.tpu.v1.Node.Health health = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Node.Health](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.Node.Health)` | The health.  
  
### getHealthDescription()
    
    
    public abstract String getHealthDescription()

Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy.

`string health_description = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The healthDescription.  
  
### getHealthDescriptionBytes()
    
    
    public abstract ByteString getHealthDescriptionBytes()

Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy.

`string health_description = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for healthDescription.  
  
### getHealthValue()
    
    
    public abstract int getHealthValue()

The health status of the TPU node.

`.google.cloud.tpu.v1.Node.Health health = 22;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for health.  
  
### getIpAddress() (deprecated)
    
    
    public abstract String getIpAddress()

**Deprecated.** _google.cloud.tpu.v1.Node.ip_address is deprecated. See google/cloud/tpu/v1/cloud_tpu.proto;l=282_

Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances.

`string ip_address = 8 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ipAddress.  
  
### getIpAddressBytes() (deprecated)
    
    
    public abstract ByteString getIpAddressBytes()

**Deprecated.** _google.cloud.tpu.v1.Node.ip_address is deprecated. See google/cloud/tpu/v1/cloud_tpu.proto;l=282_

Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances.

`string ip_address = 8 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ipAddress.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.NodeOrBuilder#com_google_cloud_tpu_v1_NodeOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Resource labels to represent user-provided metadata.

`map<string, string> labels = 24;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Resource labels to represent user-provided metadata.

`map<string, string> labels = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Resource labels to represent user-provided metadata.

`map<string, string> labels = 24;`

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

Resource labels to represent user-provided metadata.

`map<string, string> labels = 24;`

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

Output only. Immutable. The name of the TPU

` string name = 1 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Immutable. The name of the TPU

` string name = 1 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, "default" will be used.

`string network = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, "default" will be used.

`string network = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNetworkEndpoints(int index)
    
    
    public abstract NetworkEndpoint getNetworkEndpoints(int index)

Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first.

` repeated .google.cloud.tpu.v1.NetworkEndpoint network_endpoints = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.NetworkEndpoint)` |   
  
### getNetworkEndpointsCount()
    
    
    public abstract int getNetworkEndpointsCount()

Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first.

` repeated .google.cloud.tpu.v1.NetworkEndpoint network_endpoints = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNetworkEndpointsList()
    
    
    public abstract List<NetworkEndpoint> getNetworkEndpointsList()

Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first.

` repeated .google.cloud.tpu.v1.NetworkEndpoint network_endpoints = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NetworkEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.NetworkEndpoint)>` |   
  
### getNetworkEndpointsOrBuilder(int index)
    
    
    public abstract NetworkEndpointOrBuilder getNetworkEndpointsOrBuilder(int index)

Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first.

` repeated .google.cloud.tpu.v1.NetworkEndpoint network_endpoints = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.NetworkEndpointOrBuilder)` |   
  
### getNetworkEndpointsOrBuilderList()
    
    
    public abstract List<? extends NetworkEndpointOrBuilder> getNetworkEndpointsOrBuilderList()

Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first.

` repeated .google.cloud.tpu.v1.NetworkEndpoint network_endpoints = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.tpu.v1.NetworkEndpointOrBuilder>` |   
  
### getPort() (deprecated)
    
    
    public abstract String getPort()

**Deprecated.** _google.cloud.tpu.v1.Node.port is deprecated. See google/cloud/tpu/v1/cloud_tpu.proto;l=286_

Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances.

`string port = 14 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The port.  
  
### getPortBytes() (deprecated)
    
    
    public abstract ByteString getPortBytes()

**Deprecated.** _google.cloud.tpu.v1.Node.port is deprecated. See google/cloud/tpu/v1/cloud_tpu.proto;l=286_

Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances.

`string port = 14 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for port.  
  
### getSchedulingConfig()
    
    
    public abstract SchedulingConfig getSchedulingConfig()

The scheduling options for this node.

`.google.cloud.tpu.v1.SchedulingConfig scheduling_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[SchedulingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.SchedulingConfig)` | The schedulingConfig.  
  
### getSchedulingConfigOrBuilder()
    
    
    public abstract SchedulingConfigOrBuilder getSchedulingConfigOrBuilder()

The scheduling options for this node.

`.google.cloud.tpu.v1.SchedulingConfig scheduling_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[SchedulingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.SchedulingConfigOrBuilder)` |   
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

Output only. The service account used to run the tensor flow services within the node. To share resources, including Google Cloud Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.

`string service_account = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

Output only. The service account used to run the tensor flow services within the node. To share resources, including Google Cloud Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.

`string service_account = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getState()
    
    
    public abstract Node.State getState()

Output only. The current state for the TPU Node.

`.google.cloud.tpu.v1.Node.State state = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Node.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.Node.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state for the TPU Node.

`.google.cloud.tpu.v1.Node.State state = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getSymptoms(int index)
    
    
    public abstract Symptom getSymptoms(int index)

Output only. The Symptoms that have occurred to the TPU Node.

` repeated .google.cloud.tpu.v1.Symptom symptoms = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Symptom](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.Symptom)` |   
  
### getSymptomsCount()
    
    
    public abstract int getSymptomsCount()

Output only. The Symptoms that have occurred to the TPU Node.

` repeated .google.cloud.tpu.v1.Symptom symptoms = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSymptomsList()
    
    
    public abstract List<Symptom> getSymptomsList()

Output only. The Symptoms that have occurred to the TPU Node.

` repeated .google.cloud.tpu.v1.Symptom symptoms = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Symptom](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.Symptom)>` |   
  
### getSymptomsOrBuilder(int index)
    
    
    public abstract SymptomOrBuilder getSymptomsOrBuilder(int index)

Output only. The Symptoms that have occurred to the TPU Node.

` repeated .google.cloud.tpu.v1.Symptom symptoms = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SymptomOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v1.SymptomOrBuilder)` |   
  
### getSymptomsOrBuilderList()
    
    
    public abstract List<? extends SymptomOrBuilder> getSymptomsOrBuilderList()

Output only. The Symptoms that have occurred to the TPU Node.

` repeated .google.cloud.tpu.v1.Symptom symptoms = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.tpu.v1.SymptomOrBuilder>` |   
  
### getTensorflowVersion()
    
    
    public abstract String getTensorflowVersion()

Required. The version of Tensorflow running in the Node.

`string tensorflow_version = 11 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tensorflowVersion.  
  
### getTensorflowVersionBytes()
    
    
    public abstract ByteString getTensorflowVersionBytes()

Required. The version of Tensorflow running in the Node.

`string tensorflow_version = 11 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tensorflowVersion.  
  
### getUseServiceNetworking()
    
    
    public abstract boolean getUseServiceNetworking()

Whether the VPC peering for the node is set up through Service Networking API. The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network, that you want to peer the TPU Node to, is Shared VPC networks, the node must be created with this this field enabled.

`bool use_service_networking = 27;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The useServiceNetworking.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the node was created.

`.google.protobuf.Timestamp create_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasSchedulingConfig()
    
    
    public abstract boolean hasSchedulingConfig()

The scheduling options for this node.

`.google.cloud.tpu.v1.SchedulingConfig scheduling_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the schedulingConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
