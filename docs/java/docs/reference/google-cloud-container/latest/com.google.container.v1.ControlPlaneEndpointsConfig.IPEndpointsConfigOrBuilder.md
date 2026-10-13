---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEndpointsConfig.IPEndpointsConfigOrBuilder
title: Interface ControlPlaneEndpointsConfig.IPEndpointsConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:12.778923+00:00
---

# Interface ControlPlaneEndpointsConfig.IPEndpointsConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEndpointsConfig.IPEndpointsConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ControlPlaneEndpointsConfig.IPEndpointsConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public static interface ControlPlaneEndpointsConfig.IPEndpointsConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthorizedNetworksConfig()
    
    
    public abstract MasterAuthorizedNetworksConfig getAuthorizedNetworksConfig()

Configuration of authorized networks. If enabled, restricts access to the control plane based on source IP. It is invalid to specify both [Cluster.masterAuthorizedNetworksConfig][] and this field at the same time.

`.google.container.v1.MasterAuthorizedNetworksConfig authorized_networks_config = 4; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthorizedNetworksConfig)` | The authorizedNetworksConfig.  
  
### getAuthorizedNetworksConfigOrBuilder()
    
    
    public abstract MasterAuthorizedNetworksConfigOrBuilder getAuthorizedNetworksConfigOrBuilder()

Configuration of authorized networks. If enabled, restricts access to the control plane based on source IP. It is invalid to specify both [Cluster.masterAuthorizedNetworksConfig][] and this field at the same time.

`.google.container.v1.MasterAuthorizedNetworksConfig authorized_networks_config = 4; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthorizedNetworksConfigOrBuilder)` |   
  
### getEnablePublicEndpoint()
    
    
    public abstract boolean getEnablePublicEndpoint()

Controls whether the control plane allows access through a public IP. It is invalid to specify both [PrivateClusterConfig.enablePrivateEndpoint][] and this field at the same time.

`optional bool enable_public_endpoint = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enablePublicEndpoint.  
  
### getEnabled()
    
    
    public abstract boolean getEnabled()

Controls whether to allow direct IP access.

`optional bool enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enabled.  
  
### getGlobalAccess()
    
    
    public abstract boolean getGlobalAccess()

Controls whether the control plane's private endpoint is accessible from sources in other regions. It is invalid to specify both PrivateClusterMasterGlobalAccessConfig.enabled and this field at the same time.

`optional bool global_access = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The globalAccess.  
  
### getPrivateEndpoint()
    
    
    public abstract String getPrivateEndpoint()

Output only. The internal IP address of this cluster's control plane. Only populated if enabled.

`string private_endpoint = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The privateEndpoint.  
  
### getPrivateEndpointBytes()
    
    
    public abstract ByteString getPrivateEndpointBytes()

Output only. The internal IP address of this cluster's control plane. Only populated if enabled.

`string private_endpoint = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for privateEndpoint.  
  
### getPrivateEndpointSubnetwork()
    
    
    public abstract String getPrivateEndpointSubnetwork()

Subnet to provision the master's private endpoint during cluster creation. Specified in projects/*/regions/*/subnetworks/* format. It is invalid to specify both [PrivateClusterConfig.privateEndpointSubnetwork][] and this field at the same time.

`string private_endpoint_subnetwork = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The privateEndpointSubnetwork.  
  
### getPrivateEndpointSubnetworkBytes()
    
    
    public abstract ByteString getPrivateEndpointSubnetworkBytes()

Subnet to provision the master's private endpoint during cluster creation. Specified in projects/*/regions/*/subnetworks/* format. It is invalid to specify both [PrivateClusterConfig.privateEndpointSubnetwork][] and this field at the same time.

`string private_endpoint_subnetwork = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for privateEndpointSubnetwork.  
  
### getPublicEndpoint()
    
    
    public abstract String getPublicEndpoint()

Output only. The external IP address of this cluster's control plane. Only populated if enabled.

`string public_endpoint = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The publicEndpoint.  
  
### getPublicEndpointBytes()
    
    
    public abstract ByteString getPublicEndpointBytes()

Output only. The external IP address of this cluster's control plane. Only populated if enabled.

`string public_endpoint = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for publicEndpoint.  
  
### hasAuthorizedNetworksConfig()
    
    
    public abstract boolean hasAuthorizedNetworksConfig()

Configuration of authorized networks. If enabled, restricts access to the control plane based on source IP. It is invalid to specify both [Cluster.masterAuthorizedNetworksConfig][] and this field at the same time.

`.google.container.v1.MasterAuthorizedNetworksConfig authorized_networks_config = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the authorizedNetworksConfig field is set.  
  
### hasEnablePublicEndpoint()
    
    
    public abstract boolean hasEnablePublicEndpoint()

Controls whether the control plane allows access through a public IP. It is invalid to specify both [PrivateClusterConfig.enablePrivateEndpoint][] and this field at the same time.

`optional bool enable_public_endpoint = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enablePublicEndpoint field is set.  
  
### hasEnabled()
    
    
    public abstract boolean hasEnabled()

Controls whether to allow direct IP access.

`optional bool enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enabled field is set.  
  
### hasGlobalAccess()
    
    
    public abstract boolean hasGlobalAccess()

Controls whether the control plane's private endpoint is accessible from sources in other regions. It is invalid to specify both PrivateClusterMasterGlobalAccessConfig.enabled and this field at the same time.

`optional bool global_access = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the globalAccess field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
