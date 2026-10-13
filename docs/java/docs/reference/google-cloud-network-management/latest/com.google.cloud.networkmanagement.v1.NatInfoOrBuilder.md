---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.NatInfoOrBuilder
title: Interface NatInfoOrBuilder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:58.645976+00:00
---

# Interface NatInfoOrBuilder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.NatInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NatInfoOrBuilder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 
    
    
    public interface NatInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCloudNatGatewayType()
    
    
    public abstract NatInfo.CloudNatGatewayType getCloudNatGatewayType()

Type of Cloud NAT gateway. Only valid when `type` is CLOUD_NAT.

` .google.cloud.networkmanagement.v1.NatInfo.CloudNatGatewayType cloud_nat_gateway_type = 14; `

**Returns**  
---  
**Type** | **Description**  
`[NatInfo.CloudNatGatewayType](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.NatInfo.CloudNatGatewayType)` | The cloudNatGatewayType.  
  
### getCloudNatGatewayTypeValue()
    
    
    public abstract int getCloudNatGatewayTypeValue()

Type of Cloud NAT gateway. Only valid when `type` is CLOUD_NAT.

` .google.cloud.networkmanagement.v1.NatInfo.CloudNatGatewayType cloud_nat_gateway_type = 14; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for cloudNatGatewayType.  
  
### getNatGatewayName()
    
    
    public abstract String getNatGatewayName()

The name of Cloud NAT Gateway. Only valid when type is CLOUD_NAT.

`string nat_gateway_name = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The natGatewayName.  
  
### getNatGatewayNameBytes()
    
    
    public abstract ByteString getNatGatewayNameBytes()

The name of Cloud NAT Gateway. Only valid when type is CLOUD_NAT.

`string nat_gateway_name = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for natGatewayName.  
  
### getNetworkUri()
    
    
    public abstract String getNetworkUri()

URI of the network where NAT translation takes place.

`string network_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The networkUri.  
  
### getNetworkUriBytes()
    
    
    public abstract ByteString getNetworkUriBytes()

URI of the network where NAT translation takes place.

`string network_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for networkUri.  
  
### getNewDestinationIp()
    
    
    public abstract String getNewDestinationIp()

Destination IP address after NAT translation.

`string new_destination_ip = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The newDestinationIp.  
  
### getNewDestinationIpBytes()
    
    
    public abstract ByteString getNewDestinationIpBytes()

Destination IP address after NAT translation.

`string new_destination_ip = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for newDestinationIp.  
  
### getNewDestinationPort()
    
    
    public abstract int getNewDestinationPort()

Destination port after NAT translation. Only valid when protocol is TCP or UDP.

`int32 new_destination_port = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The newDestinationPort.  
  
### getNewSourceIp()
    
    
    public abstract String getNewSourceIp()

Source IP address after NAT translation.

`string new_source_ip = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The newSourceIp.  
  
### getNewSourceIpBytes()
    
    
    public abstract ByteString getNewSourceIpBytes()

Source IP address after NAT translation.

`string new_source_ip = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for newSourceIp.  
  
### getNewSourcePort()
    
    
    public abstract int getNewSourcePort()

Source port after NAT translation. Only valid when protocol is TCP or UDP.

`int32 new_source_port = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The newSourcePort.  
  
### getOldDestinationIp()
    
    
    public abstract String getOldDestinationIp()

Destination IP address before NAT translation.

`string old_destination_ip = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The oldDestinationIp.  
  
### getOldDestinationIpBytes()
    
    
    public abstract ByteString getOldDestinationIpBytes()

Destination IP address before NAT translation.

`string old_destination_ip = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for oldDestinationIp.  
  
### getOldDestinationPort()
    
    
    public abstract int getOldDestinationPort()

Destination port before NAT translation. Only valid when protocol is TCP or UDP.

`int32 old_destination_port = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The oldDestinationPort.  
  
### getOldSourceIp()
    
    
    public abstract String getOldSourceIp()

Source IP address before NAT translation.

`string old_source_ip = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The oldSourceIp.  
  
### getOldSourceIpBytes()
    
    
    public abstract ByteString getOldSourceIpBytes()

Source IP address before NAT translation.

`string old_source_ip = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for oldSourceIp.  
  
### getOldSourcePort()
    
    
    public abstract int getOldSourcePort()

Source port before NAT translation. Only valid when protocol is TCP or UDP.

`int32 old_source_port = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The oldSourcePort.  
  
### getProtocol()
    
    
    public abstract String getProtocol()

IP protocol in string format, for example: "TCP", "UDP", "ICMP".

`string protocol = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The protocol.  
  
### getProtocolBytes()
    
    
    public abstract ByteString getProtocolBytes()

IP protocol in string format, for example: "TCP", "UDP", "ICMP".

`string protocol = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for protocol.  
  
### getRouterUri()
    
    
    public abstract String getRouterUri()

Uri of the Cloud Router. Only valid when type is CLOUD_NAT.

`string router_uri = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The routerUri.  
  
### getRouterUriBytes()
    
    
    public abstract ByteString getRouterUriBytes()

Uri of the Cloud Router. Only valid when type is CLOUD_NAT.

`string router_uri = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for routerUri.  
  
### getType()
    
    
    public abstract NatInfo.Type getType()

Type of NAT.

`.google.cloud.networkmanagement.v1.NatInfo.Type type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[NatInfo.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.NatInfo.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Type of NAT.

`.google.cloud.networkmanagement.v1.NatInfo.Type type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
