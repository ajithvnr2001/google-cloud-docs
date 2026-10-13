---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupOrBuilder
title: Interface NetworkEndpointGroupOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:48.190210+00:00
---

# Interface NetworkEndpointGroupOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NetworkEndpointGroupOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface NetworkEndpointGroupOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAnnotations(String key)
    
    
    public abstract boolean containsAnnotations(String key)

Optional. Metadata defined as annotations on the network endpoint group.

`map<string, string> annotations = 112032548;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotations() (deprecated)
    
    
    public abstract Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupOrBuilder#com_google_cloud_compute_v1_NetworkEndpointGroupOrBuilder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public abstract int getAnnotationsCount()

Optional. Metadata defined as annotations on the network endpoint group.

`map<string, string> annotations = 112032548;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public abstract Map<String,String> getAnnotationsMap()

Optional. Metadata defined as annotations on the network endpoint group.

`map<string, string> annotations = 112032548;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public abstract String getAnnotationsOrDefault(String key, String defaultValue)

Optional. Metadata defined as annotations on the network endpoint group.

`map<string, string> annotations = 112032548;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public abstract String getAnnotationsOrThrow(String key)

Optional. Metadata defined as annotations on the network endpoint group.

`map<string, string> annotations = 112032548;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAppEngine()
    
    
    public abstract NetworkEndpointGroupAppEngine getAppEngine()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

`optional .google.cloud.compute.v1.NetworkEndpointGroupAppEngine app_engine = 340788768; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupAppEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupAppEngine)` | The appEngine.  
  
### getAppEngineOrBuilder()
    
    
    public abstract NetworkEndpointGroupAppEngineOrBuilder getAppEngineOrBuilder()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

`optional .google.cloud.compute.v1.NetworkEndpointGroupAppEngine app_engine = 340788768; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupAppEngineOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupAppEngineOrBuilder)` |   
  
### getCloudFunction()
    
    
    public abstract NetworkEndpointGroupCloudFunction getCloudFunction()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

` optional .google.cloud.compute.v1.NetworkEndpointGroupCloudFunction cloud_function = 519893666; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupCloudFunction)` | The cloudFunction.  
  
### getCloudFunctionOrBuilder()
    
    
    public abstract NetworkEndpointGroupCloudFunctionOrBuilder getCloudFunctionOrBuilder()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

` optional .google.cloud.compute.v1.NetworkEndpointGroupCloudFunction cloud_function = 519893666; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupCloudFunctionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupCloudFunctionOrBuilder)` |   
  
### getCloudRun()
    
    
    public abstract NetworkEndpointGroupCloudRun getCloudRun()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

`optional .google.cloud.compute.v1.NetworkEndpointGroupCloudRun cloud_run = 111060353; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupCloudRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupCloudRun)` | The cloudRun.  
  
### getCloudRunOrBuilder()
    
    
    public abstract NetworkEndpointGroupCloudRunOrBuilder getCloudRunOrBuilder()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

`optional .google.cloud.compute.v1.NetworkEndpointGroupCloudRun cloud_run = 111060353; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupCloudRunOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupCloudRunOrBuilder)` |   
  
### getCreationTimestamp()
    
    
    public abstract String getCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public abstract ByteString getCreationTimestampBytes()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getDefaultPort()
    
    
    public abstract int getDefaultPort()

The default port used if the port number is not specified in the network endpoint.

Optional. If the network endpoint type is either GCE_VM_IP,SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified.

`optional int32 default_port = 423377855;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The defaultPort.  
  
### getDescription()
    
    
    public abstract String getDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getId()
    
    
    public abstract long getId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getName()
    
    
    public abstract String getName()

Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required.

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required.

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNetworkEndpointType()
    
    
    public abstract String getNetworkEndpointType()

Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values.

`optional string network_endpoint_type = 118301523;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The networkEndpointType.  
  
### getNetworkEndpointTypeBytes()
    
    
    public abstract ByteString getNetworkEndpointTypeBytes()

Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values.

`optional string network_endpoint_type = 118301523;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for networkEndpointType.  
  
### getPscData()
    
    
    public abstract NetworkEndpointGroupPscData getPscData()

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

`optional .google.cloud.compute.v1.NetworkEndpointGroupPscData psc_data = 71937481;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupPscData](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupPscData)` | The pscData.  
  
### getPscDataOrBuilder()
    
    
    public abstract NetworkEndpointGroupPscDataOrBuilder getPscDataOrBuilder()

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

`optional .google.cloud.compute.v1.NetworkEndpointGroupPscData psc_data = 71937481;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupPscDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupPscDataOrBuilder)` |   
  
### getPscTargetService()
    
    
    public abstract String getPscTargetService()

The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

`optional string psc_target_service = 269132134;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pscTargetService.  
  
### getPscTargetServiceBytes()
    
    
    public abstract ByteString getPscTargetServiceBytes()

The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

`optional string psc_target_service = 269132134;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pscTargetService.  
  
### getRegion()
    
    
    public abstract String getRegion()

Output only. [Output Only] The URL of theregion where the network endpoint group is located.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The region.  
  
### getRegionBytes()
    
    
    public abstract ByteString getRegionBytes()

Output only. [Output Only] The URL of theregion where the network endpoint group is located.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for region.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getSize()
    
    
    public abstract int getSize()

Output only. [Output only] Number of network endpoints in the network endpoint group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The size.  
  
### getSubnetwork()
    
    
    public abstract String getSubnetwork()

Optional URL of the subnetwork to which all network endpoints in the NEG belong.

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetwork.  
  
### getSubnetworkBytes()
    
    
    public abstract ByteString getSubnetworkBytes()

Optional URL of the subnetwork to which all network endpoints in the NEG belong.

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetwork.  
  
### getZone()
    
    
    public abstract String getZone()

Output only. [Output Only] The URL of thezone where the network endpoint group is located.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public abstract ByteString getZoneBytes()

Output only. [Output Only] The URL of thezone where the network endpoint group is located.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasAppEngine()
    
    
    public abstract boolean hasAppEngine()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

`optional .google.cloud.compute.v1.NetworkEndpointGroupAppEngine app_engine = 340788768; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appEngine field is set.  
  
### hasCloudFunction()
    
    
    public abstract boolean hasCloudFunction()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

` optional .google.cloud.compute.v1.NetworkEndpointGroupCloudFunction cloud_function = 519893666; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudFunction field is set.  
  
### hasCloudRun()
    
    
    public abstract boolean hasCloudRun()

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

`optional .google.cloud.compute.v1.NetworkEndpointGroupCloudRun cloud_run = 111060353; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudRun field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasDefaultPort()
    
    
    public abstract boolean hasDefaultPort()

The default port used if the port number is not specified in the network endpoint.

Optional. If the network endpoint type is either GCE_VM_IP,SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified.

`optional int32 default_port = 423377855;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the defaultPort field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasNetwork()
    
    
    public abstract boolean hasNetwork()

The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required.

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the network field is set.  
  
### hasNetworkEndpointType()
    
    
    public abstract boolean hasNetworkEndpointType()

Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values.

`optional string network_endpoint_type = 118301523;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkEndpointType field is set.  
  
### hasPscData()
    
    
    public abstract boolean hasPscData()

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

`optional .google.cloud.compute.v1.NetworkEndpointGroupPscData psc_data = 71937481;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscData field is set.  
  
### hasPscTargetService()
    
    
    public abstract boolean hasPscTargetService()

The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

`optional string psc_target_service = 269132134;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscTargetService field is set.  
  
### hasRegion()
    
    
    public abstract boolean hasRegion()

Output only. [Output Only] The URL of theregion where the network endpoint group is located.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the region field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasSize()
    
    
    public abstract boolean hasSize()

Output only. [Output only] Number of network endpoints in the network endpoint group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the size field is set.  
  
### hasSubnetwork()
    
    
    public abstract boolean hasSubnetwork()

Optional URL of the subnetwork to which all network endpoints in the NEG belong.

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subnetwork field is set.  
  
### hasZone()
    
    
    public abstract boolean hasZone()

Output only. [Output Only] The URL of thezone where the network endpoint group is located.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zone field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
