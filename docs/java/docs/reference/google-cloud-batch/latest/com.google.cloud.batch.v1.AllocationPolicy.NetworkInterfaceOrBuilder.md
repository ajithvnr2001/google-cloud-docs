---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterfaceOrBuilder
title: Interface AllocationPolicy.NetworkInterfaceOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:09.839830+00:00
---

# Interface AllocationPolicy.NetworkInterfaceOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterfaceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AllocationPolicy.NetworkInterfaceOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static interface AllocationPolicy.NetworkInterfaceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNetwork()
    
    
    public abstract String getNetwork()

The URL of an existing network resource. You can specify the network as a full or partial URL.

For example, the following are all valid URLs:

  * https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
  * projects/{project}/global/networks/{network}
  * global/networks/{network}



`string network = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

The URL of an existing network resource. You can specify the network as a full or partial URL.

For example, the following are all valid URLs:

  * https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
  * projects/{project}/global/networks/{network}
  * global/networks/{network}



`string network = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNicType()
    
    
    public abstract AllocationPolicy.NetworkInterface.NicType getNicType()

Optional. The NIC type of the network interface.

` optional .google.cloud.batch.v1.AllocationPolicy.NetworkInterface.NicType nic_type = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.NetworkInterface.NicType](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.NicType)` | The nicType.  
  
### getNicTypeValue()
    
    
    public abstract int getNicTypeValue()

Optional. The NIC type of the network interface.

` optional .google.cloud.batch.v1.AllocationPolicy.NetworkInterface.NicType nic_type = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for nicType.  
  
### getNoExternalIpAddress()
    
    
    public abstract boolean getNoExternalIpAddress()

Default is false (with an external IP address). Required if no external public IP address is attached to the VM. If no external public IP address, additional configuration is required to allow the VM to access Google Services. See <https://cloud.google.com/vpc/docs/configure-private-google-access> and <https://cloud.google.com/nat/docs/gce-example#create-nat> for more information.

`bool no_external_ip_address = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The noExternalIpAddress.  
  
### getSubnetwork()
    
    
    public abstract String getSubnetwork()

The URL of an existing subnetwork resource in the network. You can specify the subnetwork as a full or partial URL.

For example, the following are all valid URLs:

  * https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
  * projects/{project}/regions/{region}/subnetworks/{subnetwork}
  * regions/{region}/subnetworks/{subnetwork}



`string subnetwork = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetwork.  
  
### getSubnetworkBytes()
    
    
    public abstract ByteString getSubnetworkBytes()

The URL of an existing subnetwork resource in the network. You can specify the subnetwork as a full or partial URL.

For example, the following are all valid URLs:

  * https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
  * projects/{project}/regions/{region}/subnetworks/{subnetwork}
  * regions/{region}/subnetworks/{subnetwork}



`string subnetwork = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetwork.  
  
### hasNicType()
    
    
    public abstract boolean hasNicType()

Optional. The NIC type of the network interface.

` optional .google.cloud.batch.v1.AllocationPolicy.NetworkInterface.NicType nic_type = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nicType field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
