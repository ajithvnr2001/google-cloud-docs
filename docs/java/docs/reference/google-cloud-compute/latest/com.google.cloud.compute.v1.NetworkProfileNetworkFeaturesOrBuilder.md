---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkProfileNetworkFeaturesOrBuilder
title: Interface NetworkProfileNetworkFeaturesOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:05.960010+00:00
---

# Interface NetworkProfileNetworkFeaturesOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkProfileNetworkFeaturesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NetworkProfileNetworkFeaturesOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface NetworkProfileNetworkFeaturesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAddressPurposes(int index)
    
    
    public abstract String getAddressPurposes(int index)

Specifies what address purposes are supported. If empty, all address purposes are supported. Check the AddressPurposes enum for the list of possible values.

`repeated string address_purposes = 433024768;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The addressPurposes at the given index.  
  
### getAddressPurposesBytes(int index)
    
    
    public abstract ByteString getAddressPurposesBytes(int index)

Specifies what address purposes are supported. If empty, all address purposes are supported. Check the AddressPurposes enum for the list of possible values.

`repeated string address_purposes = 433024768;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the addressPurposes at the given index.  
  
### getAddressPurposesCount()
    
    
    public abstract int getAddressPurposesCount()

Specifies what address purposes are supported. If empty, all address purposes are supported. Check the AddressPurposes enum for the list of possible values.

`repeated string address_purposes = 433024768;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of addressPurposes.  
  
### getAddressPurposesList()
    
    
    public abstract List<String> getAddressPurposesList()

Specifies what address purposes are supported. If empty, all address purposes are supported. Check the AddressPurposes enum for the list of possible values.

`repeated string address_purposes = 433024768;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the addressPurposes.  
  
### getAllowAddressCreation()
    
    
    public abstract String getAllowAddressCreation()

Specifies whether address creation is allowed. Check the AllowAddressCreation enum for the list of possible values.

`optional string allow_address_creation = 450941184;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowAddressCreation.  
  
### getAllowAddressCreationBytes()
    
    
    public abstract ByteString getAllowAddressCreationBytes()

Specifies whether address creation is allowed. Check the AllowAddressCreation enum for the list of possible values.

`optional string allow_address_creation = 450941184;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowAddressCreation.  
  
### getAllowAliasIpRanges()
    
    
    public abstract String getAllowAliasIpRanges()

Specifies whether alias IP ranges (and secondary address ranges) are allowed. Check the AllowAliasIpRanges enum for the list of possible values.

`optional string allow_alias_ip_ranges = 457984201;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowAliasIpRanges.  
  
### getAllowAliasIpRangesBytes()
    
    
    public abstract ByteString getAllowAliasIpRangesBytes()

Specifies whether alias IP ranges (and secondary address ranges) are allowed. Check the AllowAliasIpRanges enum for the list of possible values.

`optional string allow_alias_ip_ranges = 457984201;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowAliasIpRanges.  
  
### getAllowAutoModeSubnet()
    
    
    public abstract String getAllowAutoModeSubnet()

Specifies whether auto mode subnet creation is allowed. Check the AllowAutoModeSubnet enum for the list of possible values.

`optional string allow_auto_mode_subnet = 152191263;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowAutoModeSubnet.  
  
### getAllowAutoModeSubnetBytes()
    
    
    public abstract ByteString getAllowAutoModeSubnetBytes()

Specifies whether auto mode subnet creation is allowed. Check the AllowAutoModeSubnet enum for the list of possible values.

`optional string allow_auto_mode_subnet = 152191263;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowAutoModeSubnet.  
  
### getAllowClassDFirewalls()
    
    
    public abstract String getAllowClassDFirewalls()

Specifies whether firewalls for Class D address ranges are supported. Check the AllowClassDFirewalls enum for the list of possible values.

`optional string allow_class_d_firewalls = 131608987;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowClassDFirewalls.  
  
### getAllowClassDFirewallsBytes()
    
    
    public abstract ByteString getAllowClassDFirewallsBytes()

Specifies whether firewalls for Class D address ranges are supported. Check the AllowClassDFirewalls enum for the list of possible values.

`optional string allow_class_d_firewalls = 131608987;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowClassDFirewalls.  
  
### getAllowCloudNat()
    
    
    public abstract String getAllowCloudNat()

Specifies whether cloud NAT creation is allowed. Check the AllowCloudNat enum for the list of possible values.

`optional string allow_cloud_nat = 254831265;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowCloudNat.  
  
### getAllowCloudNatBytes()
    
    
    public abstract ByteString getAllowCloudNatBytes()

Specifies whether cloud NAT creation is allowed. Check the AllowCloudNat enum for the list of possible values.

`optional string allow_cloud_nat = 254831265;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowCloudNat.  
  
### getAllowCloudRouter()
    
    
    public abstract String getAllowCloudRouter()

Specifies whether cloud router creation is allowed. Check the AllowCloudRouter enum for the list of possible values.

`optional string allow_cloud_router = 451110345;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowCloudRouter.  
  
### getAllowCloudRouterBytes()
    
    
    public abstract ByteString getAllowCloudRouterBytes()

Specifies whether cloud router creation is allowed. Check the AllowCloudRouter enum for the list of possible values.

`optional string allow_cloud_router = 451110345;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowCloudRouter.  
  
### getAllowDefaultNicAttachment()
    
    
    public abstract String getAllowDefaultNicAttachment()

Specifies whether default NIC attachment is allowed. Check the AllowDefaultNicAttachment enum for the list of possible values.

`optional string allow_default_nic_attachment = 53917486;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowDefaultNicAttachment.  
  
### getAllowDefaultNicAttachmentBytes()
    
    
    public abstract ByteString getAllowDefaultNicAttachmentBytes()

Specifies whether default NIC attachment is allowed. Check the AllowDefaultNicAttachment enum for the list of possible values.

`optional string allow_default_nic_attachment = 53917486;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowDefaultNicAttachment.  
  
### getAllowExternalIpAccess()
    
    
    public abstract String getAllowExternalIpAccess()

Specifies whether VMs are allowed to have external IP access on network interfaces connected to this VPC. Check the AllowExternalIpAccess enum for the list of possible values.

`optional string allow_external_ip_access = 131538110;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowExternalIpAccess.  
  
### getAllowExternalIpAccessBytes()
    
    
    public abstract ByteString getAllowExternalIpAccessBytes()

Specifies whether VMs are allowed to have external IP access on network interfaces connected to this VPC. Check the AllowExternalIpAccess enum for the list of possible values.

`optional string allow_external_ip_access = 131538110;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowExternalIpAccess.  
  
### getAllowFirewallPolicy()
    
    
    public abstract String getAllowFirewallPolicy()

Specifies whether firewall policy can be attached to the network. Check the AllowFirewallPolicy enum for the list of possible values.

`optional string allow_firewall_policy = 254200923;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowFirewallPolicy.  
  
### getAllowFirewallPolicyBytes()
    
    
    public abstract ByteString getAllowFirewallPolicyBytes()

Specifies whether firewall policy can be attached to the network. Check the AllowFirewallPolicy enum for the list of possible values.

`optional string allow_firewall_policy = 254200923;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowFirewallPolicy.  
  
### getAllowInterconnect()
    
    
    public abstract String getAllowInterconnect()

Specifies whether Cloud Interconnect creation is allowed. Check the AllowInterconnect enum for the list of possible values.

`optional string allow_interconnect = 280512964;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowInterconnect.  
  
### getAllowInterconnectBytes()
    
    
    public abstract ByteString getAllowInterconnectBytes()

Specifies whether Cloud Interconnect creation is allowed. Check the AllowInterconnect enum for the list of possible values.

`optional string allow_interconnect = 280512964;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowInterconnect.  
  
### getAllowIpForwarding()
    
    
    public abstract String getAllowIpForwarding()

Specifies whether IP forwarding is allowed. Check the AllowIpForwarding enum for the list of possible values.

`optional string allow_ip_forwarding = 500838047;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowIpForwarding.  
  
### getAllowIpForwardingBytes()
    
    
    public abstract ByteString getAllowIpForwardingBytes()

Specifies whether IP forwarding is allowed. Check the AllowIpForwarding enum for the list of possible values.

`optional string allow_ip_forwarding = 500838047;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowIpForwarding.  
  
### getAllowLoadBalancing()
    
    
    public abstract String getAllowLoadBalancing()

Specifies whether cloud load balancing is allowed. Check the AllowLoadBalancing enum for the list of possible values.

`optional string allow_load_balancing = 223366198;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowLoadBalancing.  
  
### getAllowLoadBalancingBytes()
    
    
    public abstract ByteString getAllowLoadBalancingBytes()

Specifies whether cloud load balancing is allowed. Check the AllowLoadBalancing enum for the list of possible values.

`optional string allow_load_balancing = 223366198;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowLoadBalancing.  
  
### getAllowMultiNicInSameNetwork()
    
    
    public abstract String getAllowMultiNicInSameNetwork()

Specifies whether multi-nic in the same network is allowed. Check the AllowMultiNicInSameNetwork enum for the list of possible values.

`optional string allow_multi_nic_in_same_network = 88251004;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowMultiNicInSameNetwork.  
  
### getAllowMultiNicInSameNetworkBytes()
    
    
    public abstract ByteString getAllowMultiNicInSameNetworkBytes()

Specifies whether multi-nic in the same network is allowed. Check the AllowMultiNicInSameNetwork enum for the list of possible values.

`optional string allow_multi_nic_in_same_network = 88251004;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowMultiNicInSameNetwork.  
  
### getAllowMultiNicInSameSubnetwork()
    
    
    public abstract String getAllowMultiNicInSameSubnetwork()

Specifies whether multi-nic in the same subnetwork is allowed. Check the AllowMultiNicInSameSubnetwork enum for the list of possible values.

`optional string allow_multi_nic_in_same_subnetwork = 278087904;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowMultiNicInSameSubnetwork.  
  
### getAllowMultiNicInSameSubnetworkBytes()
    
    
    public abstract ByteString getAllowMultiNicInSameSubnetworkBytes()

Specifies whether multi-nic in the same subnetwork is allowed. Check the AllowMultiNicInSameSubnetwork enum for the list of possible values.

`optional string allow_multi_nic_in_same_subnetwork = 278087904;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowMultiNicInSameSubnetwork.  
  
### getAllowMulticast()
    
    
    public abstract String getAllowMulticast()

Specifies whether multicast is allowed. Check the AllowMulticast enum for the list of possible values.

`optional string allow_multicast = 11002498;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowMulticast.  
  
### getAllowMulticastBytes()
    
    
    public abstract ByteString getAllowMulticastBytes()

Specifies whether multicast is allowed. Check the AllowMulticast enum for the list of possible values.

`optional string allow_multicast = 11002498;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowMulticast.  
  
### getAllowNcc()
    
    
    public abstract String getAllowNcc()

Specifies whether NCC is allowed. Check the AllowNcc enum for the list of possible values.

`optional string allow_ncc = 372354904;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowNcc.  
  
### getAllowNccBytes()
    
    
    public abstract ByteString getAllowNccBytes()

Specifies whether NCC is allowed. Check the AllowNcc enum for the list of possible values.

`optional string allow_ncc = 372354904;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowNcc.  
  
### getAllowNetworkMigration()
    
    
    public abstract String getAllowNetworkMigration()

Specifies whether VM network migration is allowed. Check the AllowNetworkMigration enum for the list of possible values.

`optional string allow_network_migration = 239588231;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowNetworkMigration.  
  
### getAllowNetworkMigrationBytes()
    
    
    public abstract ByteString getAllowNetworkMigrationBytes()

Specifies whether VM network migration is allowed. Check the AllowNetworkMigration enum for the list of possible values.

`optional string allow_network_migration = 239588231;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowNetworkMigration.  
  
### getAllowPacketMirroring()
    
    
    public abstract String getAllowPacketMirroring()

Specifies whether Packet Mirroring 1.0 is supported. Check the AllowPacketMirroring enum for the list of possible values.

`optional string allow_packet_mirroring = 512227074;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowPacketMirroring.  
  
### getAllowPacketMirroringBytes()
    
    
    public abstract ByteString getAllowPacketMirroringBytes()

Specifies whether Packet Mirroring 1.0 is supported. Check the AllowPacketMirroring enum for the list of possible values.

`optional string allow_packet_mirroring = 512227074;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowPacketMirroring.  
  
### getAllowPrivateGoogleAccess()
    
    
    public abstract String getAllowPrivateGoogleAccess()

Specifies whether private Google access is allowed. Check the AllowPrivateGoogleAccess enum for the list of possible values.

`optional string allow_private_google_access = 374702072;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowPrivateGoogleAccess.  
  
### getAllowPrivateGoogleAccessBytes()
    
    
    public abstract ByteString getAllowPrivateGoogleAccessBytes()

Specifies whether private Google access is allowed. Check the AllowPrivateGoogleAccess enum for the list of possible values.

`optional string allow_private_google_access = 374702072;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowPrivateGoogleAccess.  
  
### getAllowPsc()
    
    
    public abstract String getAllowPsc()

Specifies whether PSC creation is allowed. Check the AllowPsc enum for the list of possible values.

`optional string allow_psc = 372357322;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowPsc.  
  
### getAllowPscBytes()
    
    
    public abstract ByteString getAllowPscBytes()

Specifies whether PSC creation is allowed. Check the AllowPsc enum for the list of possible values.

`optional string allow_psc = 372357322;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowPsc.  
  
### getAllowSameNetworkUnicast()
    
    
    public abstract String getAllowSameNetworkUnicast()

Specifies whether unicast within the same network is allowed. Check the AllowSameNetworkUnicast enum for the list of possible values.

`optional string allow_same_network_unicast = 167531643;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowSameNetworkUnicast.  
  
### getAllowSameNetworkUnicastBytes()
    
    
    public abstract ByteString getAllowSameNetworkUnicastBytes()

Specifies whether unicast within the same network is allowed. Check the AllowSameNetworkUnicast enum for the list of possible values.

`optional string allow_same_network_unicast = 167531643;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowSameNetworkUnicast.  
  
### getAllowStaticRoutes()
    
    
    public abstract String getAllowStaticRoutes()

Specifies whether static route creation is allowed. Check the AllowStaticRoutes enum for the list of possible values.

`optional string allow_static_routes = 185257925;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowStaticRoutes.  
  
### getAllowStaticRoutesBytes()
    
    
    public abstract ByteString getAllowStaticRoutesBytes()

Specifies whether static route creation is allowed. Check the AllowStaticRoutes enum for the list of possible values.

`optional string allow_static_routes = 185257925;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowStaticRoutes.  
  
### getAllowSubInterfaces()
    
    
    public abstract String getAllowSubInterfaces()

Specifies whether sub interfaces are allowed. Check the AllowSubInterfaces enum for the list of possible values.

`optional string allow_sub_interfaces = 247208303;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowSubInterfaces.  
  
### getAllowSubInterfacesBytes()
    
    
    public abstract ByteString getAllowSubInterfacesBytes()

Specifies whether sub interfaces are allowed. Check the AllowSubInterfaces enum for the list of possible values.

`optional string allow_sub_interfaces = 247208303;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowSubInterfaces.  
  
### getAllowSubnetworkCreation()
    
    
    public abstract String getAllowSubnetworkCreation()

Specifies whether subnetwork creation is allowed. Check the AllowSubnetworkCreation enum for the list of possible values.

`optional string allow_subnetwork_creation = 459328026;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowSubnetworkCreation.  
  
### getAllowSubnetworkCreationBytes()
    
    
    public abstract ByteString getAllowSubnetworkCreationBytes()

Specifies whether subnetwork creation is allowed. Check the AllowSubnetworkCreation enum for the list of possible values.

`optional string allow_subnetwork_creation = 459328026;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowSubnetworkCreation.  
  
### getAllowVpcFirewallRules()
    
    
    public abstract String getAllowVpcFirewallRules()

Specifies whether VPC firewall rules can be created under the network. Check the AllowVpcFirewallRules enum for the list of possible values.

`optional string allow_vpc_firewall_rules = 509076420;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowVpcFirewallRules.  
  
### getAllowVpcFirewallRulesBytes()
    
    
    public abstract ByteString getAllowVpcFirewallRulesBytes()

Specifies whether VPC firewall rules can be created under the network. Check the AllowVpcFirewallRules enum for the list of possible values.

`optional string allow_vpc_firewall_rules = 509076420;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowVpcFirewallRules.  
  
### getAllowVpcPeering()
    
    
    public abstract String getAllowVpcPeering()

Specifies whether VPC peering is allowed. Check the AllowVpcPeering enum for the list of possible values.

`optional string allow_vpc_peering = 115402228;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowVpcPeering.  
  
### getAllowVpcPeeringBytes()
    
    
    public abstract ByteString getAllowVpcPeeringBytes()

Specifies whether VPC peering is allowed. Check the AllowVpcPeering enum for the list of possible values.

`optional string allow_vpc_peering = 115402228;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowVpcPeering.  
  
### getAllowVpn()
    
    
    public abstract String getAllowVpn()

Specifies whether VPN creation is allowed. Check the AllowVpn enum for the list of possible values.

`optional string allow_vpn = 372363006;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowVpn.  
  
### getAllowVpnBytes()
    
    
    public abstract ByteString getAllowVpnBytes()

Specifies whether VPN creation is allowed. Check the AllowVpn enum for the list of possible values.

`optional string allow_vpn = 372363006;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for allowVpn.  
  
### getFirewallPolicyTypes(int index)
    
    
    public abstract String getFirewallPolicyTypes(int index)

Check the FirewallPolicyTypes enum for the list of possible values.

`repeated string firewall_policy_types = 390742027;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The firewallPolicyTypes at the given index.  
  
### getFirewallPolicyTypesBytes(int index)
    
    
    public abstract ByteString getFirewallPolicyTypesBytes(int index)

Check the FirewallPolicyTypes enum for the list of possible values.

`repeated string firewall_policy_types = 390742027;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the firewallPolicyTypes at the given index.  
  
### getFirewallPolicyTypesCount()
    
    
    public abstract int getFirewallPolicyTypesCount()

Check the FirewallPolicyTypes enum for the list of possible values.

`repeated string firewall_policy_types = 390742027;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of firewallPolicyTypes.  
  
### getFirewallPolicyTypesList()
    
    
    public abstract List<String> getFirewallPolicyTypesList()

Check the FirewallPolicyTypes enum for the list of possible values.

`repeated string firewall_policy_types = 390742027;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the firewallPolicyTypes.  
  
### getInterfaceTypes(int index)
    
    
    public abstract String getInterfaceTypes(int index)

If set, limits the interface types that the network supports. If empty, all interface types are supported. Check the InterfaceTypes enum for the list of possible values.

`repeated string interface_types = 157981171;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The interfaceTypes at the given index.  
  
### getInterfaceTypesBytes(int index)
    
    
    public abstract ByteString getInterfaceTypesBytes(int index)

If set, limits the interface types that the network supports. If empty, all interface types are supported. Check the InterfaceTypes enum for the list of possible values.

`repeated string interface_types = 157981171;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the interfaceTypes at the given index.  
  
### getInterfaceTypesCount()
    
    
    public abstract int getInterfaceTypesCount()

If set, limits the interface types that the network supports. If empty, all interface types are supported. Check the InterfaceTypes enum for the list of possible values.

`repeated string interface_types = 157981171;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of interfaceTypes.  
  
### getInterfaceTypesList()
    
    
    public abstract List<String> getInterfaceTypesList()

If set, limits the interface types that the network supports. If empty, all interface types are supported. Check the InterfaceTypes enum for the list of possible values.

`repeated string interface_types = 157981171;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the interfaceTypes.  
  
### getMulticast()
    
    
    public abstract String getMulticast()

Specifies which type of multicast is supported. Check the Multicast enum for the list of possible values.

`optional string multicast = 404098040;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The multicast.  
  
### getMulticastBytes()
    
    
    public abstract ByteString getMulticastBytes()

Specifies which type of multicast is supported. Check the Multicast enum for the list of possible values.

`optional string multicast = 404098040;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for multicast.  
  
### getPredefinedNetworkInternalIpv6Range()
    
    
    public abstract String getPredefinedNetworkInternalIpv6Range()

Specifies a predefined internal IPv6 range for the network.

`optional string predefined_network_internal_ipv6_range = 527810909;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The predefinedNetworkInternalIpv6Range.  
  
### getPredefinedNetworkInternalIpv6RangeBytes()
    
    
    public abstract ByteString getPredefinedNetworkInternalIpv6RangeBytes()

Specifies a predefined internal IPv6 range for the network.

`optional string predefined_network_internal_ipv6_range = 527810909;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for predefinedNetworkInternalIpv6Range.  
  
### getPredefinedSubnetworkRanges(int index)
    
    
    public abstract NetworkProfileNetworkFeaturesPredefinedSubnetworkRange getPredefinedSubnetworkRanges(int index)

Predefined subnetwork ranges for the network.

` repeated .google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange predefined_subnetwork_ranges = 408740430; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkProfileNetworkFeaturesPredefinedSubnetworkRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange)` |   
  
### getPredefinedSubnetworkRangesCount()
    
    
    public abstract int getPredefinedSubnetworkRangesCount()

Predefined subnetwork ranges for the network.

` repeated .google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange predefined_subnetwork_ranges = 408740430; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPredefinedSubnetworkRangesList()
    
    
    public abstract List<NetworkProfileNetworkFeaturesPredefinedSubnetworkRange> getPredefinedSubnetworkRangesList()

Predefined subnetwork ranges for the network.

` repeated .google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange predefined_subnetwork_ranges = 408740430; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NetworkProfileNetworkFeaturesPredefinedSubnetworkRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange)>` |   
  
### getPredefinedSubnetworkRangesOrBuilder(int index)
    
    
    public abstract NetworkProfileNetworkFeaturesPredefinedSubnetworkRangeOrBuilder getPredefinedSubnetworkRangesOrBuilder(int index)

Predefined subnetwork ranges for the network.

` repeated .google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange predefined_subnetwork_ranges = 408740430; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkProfileNetworkFeaturesPredefinedSubnetworkRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRangeOrBuilder)` |   
  
### getPredefinedSubnetworkRangesOrBuilderList()
    
    
    public abstract List<? extends NetworkProfileNetworkFeaturesPredefinedSubnetworkRangeOrBuilder> getPredefinedSubnetworkRangesOrBuilderList()

Predefined subnetwork ranges for the network.

` repeated .google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRange predefined_subnetwork_ranges = 408740430; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.NetworkProfileNetworkFeaturesPredefinedSubnetworkRangeOrBuilder>` |   
  
### getSubnetPurposes(int index)
    
    
    public abstract String getSubnetPurposes(int index)

Specifies which subnetwork purposes are supported. Check the SubnetPurposes enum for the list of possible values.

`repeated string subnet_purposes = 301338039;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetPurposes at the given index.  
  
### getSubnetPurposesBytes(int index)
    
    
    public abstract ByteString getSubnetPurposesBytes(int index)

Specifies which subnetwork purposes are supported. Check the SubnetPurposes enum for the list of possible values.

`repeated string subnet_purposes = 301338039;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the subnetPurposes at the given index.  
  
### getSubnetPurposesCount()
    
    
    public abstract int getSubnetPurposesCount()

Specifies which subnetwork purposes are supported. Check the SubnetPurposes enum for the list of possible values.

`repeated string subnet_purposes = 301338039;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of subnetPurposes.  
  
### getSubnetPurposesList()
    
    
    public abstract List<String> getSubnetPurposesList()

Specifies which subnetwork purposes are supported. Check the SubnetPurposes enum for the list of possible values.

`repeated string subnet_purposes = 301338039;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the subnetPurposes.  
  
### getSubnetStackTypes(int index)
    
    
    public abstract String getSubnetStackTypes(int index)

Specifies which subnetwork stack types are supported. Check the SubnetStackTypes enum for the list of possible values.

`repeated string subnet_stack_types = 521008672;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetStackTypes at the given index.  
  
### getSubnetStackTypesBytes(int index)
    
    
    public abstract ByteString getSubnetStackTypesBytes(int index)

Specifies which subnetwork stack types are supported. Check the SubnetStackTypes enum for the list of possible values.

`repeated string subnet_stack_types = 521008672;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the subnetStackTypes at the given index.  
  
### getSubnetStackTypesCount()
    
    
    public abstract int getSubnetStackTypesCount()

Specifies which subnetwork stack types are supported. Check the SubnetStackTypes enum for the list of possible values.

`repeated string subnet_stack_types = 521008672;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of subnetStackTypes.  
  
### getSubnetStackTypesList()
    
    
    public abstract List<String> getSubnetStackTypesList()

Specifies which subnetwork stack types are supported. Check the SubnetStackTypes enum for the list of possible values.

`repeated string subnet_stack_types = 521008672;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the subnetStackTypes.  
  
### getSubnetworkPurposes(int index)
    
    
    public abstract String getSubnetworkPurposes(int index)

Output only. Specifies which subnetwork purposes are supported. Check the SubnetworkPurposes enum for the list of possible values.

`repeated string subnetwork_purposes = 528240710;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetworkPurposes at the given index.  
  
### getSubnetworkPurposesBytes(int index)
    
    
    public abstract ByteString getSubnetworkPurposesBytes(int index)

Output only. Specifies which subnetwork purposes are supported. Check the SubnetworkPurposes enum for the list of possible values.

`repeated string subnetwork_purposes = 528240710;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the subnetworkPurposes at the given index.  
  
### getSubnetworkPurposesCount()
    
    
    public abstract int getSubnetworkPurposesCount()

Output only. Specifies which subnetwork purposes are supported. Check the SubnetworkPurposes enum for the list of possible values.

`repeated string subnetwork_purposes = 528240710;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of subnetworkPurposes.  
  
### getSubnetworkPurposesList()
    
    
    public abstract List<String> getSubnetworkPurposesList()

Output only. Specifies which subnetwork purposes are supported. Check the SubnetworkPurposes enum for the list of possible values.

`repeated string subnetwork_purposes = 528240710;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the subnetworkPurposes.  
  
### getSubnetworkStackTypes(int index)
    
    
    public abstract String getSubnetworkStackTypes(int index)

Output only. Specifies which subnetwork stack types are supported. Check the SubnetworkStackTypes enum for the list of possible values.

`repeated string subnetwork_stack_types = 436827441;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetworkStackTypes at the given index.  
  
### getSubnetworkStackTypesBytes(int index)
    
    
    public abstract ByteString getSubnetworkStackTypesBytes(int index)

Output only. Specifies which subnetwork stack types are supported. Check the SubnetworkStackTypes enum for the list of possible values.

`repeated string subnetwork_stack_types = 436827441;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the subnetworkStackTypes at the given index.  
  
### getSubnetworkStackTypesCount()
    
    
    public abstract int getSubnetworkStackTypesCount()

Output only. Specifies which subnetwork stack types are supported. Check the SubnetworkStackTypes enum for the list of possible values.

`repeated string subnetwork_stack_types = 436827441;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of subnetworkStackTypes.  
  
### getSubnetworkStackTypesList()
    
    
    public abstract List<String> getSubnetworkStackTypesList()

Output only. Specifies which subnetwork stack types are supported. Check the SubnetworkStackTypes enum for the list of possible values.

`repeated string subnetwork_stack_types = 436827441;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the subnetworkStackTypes.  
  
### getUnicast()
    
    
    public abstract String getUnicast()

Specifies which type of unicast is supported. Check the Unicast enum for the list of possible values.

`optional string unicast = 249841711;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unicast.  
  
### getUnicastBytes()
    
    
    public abstract ByteString getUnicastBytes()

Specifies which type of unicast is supported. Check the Unicast enum for the list of possible values.

`optional string unicast = 249841711;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for unicast.  
  
### hasAllowAddressCreation()
    
    
    public abstract boolean hasAllowAddressCreation()

Specifies whether address creation is allowed. Check the AllowAddressCreation enum for the list of possible values.

`optional string allow_address_creation = 450941184;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowAddressCreation field is set.  
  
### hasAllowAliasIpRanges()
    
    
    public abstract boolean hasAllowAliasIpRanges()

Specifies whether alias IP ranges (and secondary address ranges) are allowed. Check the AllowAliasIpRanges enum for the list of possible values.

`optional string allow_alias_ip_ranges = 457984201;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowAliasIpRanges field is set.  
  
### hasAllowAutoModeSubnet()
    
    
    public abstract boolean hasAllowAutoModeSubnet()

Specifies whether auto mode subnet creation is allowed. Check the AllowAutoModeSubnet enum for the list of possible values.

`optional string allow_auto_mode_subnet = 152191263;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowAutoModeSubnet field is set.  
  
### hasAllowClassDFirewalls()
    
    
    public abstract boolean hasAllowClassDFirewalls()

Specifies whether firewalls for Class D address ranges are supported. Check the AllowClassDFirewalls enum for the list of possible values.

`optional string allow_class_d_firewalls = 131608987;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowClassDFirewalls field is set.  
  
### hasAllowCloudNat()
    
    
    public abstract boolean hasAllowCloudNat()

Specifies whether cloud NAT creation is allowed. Check the AllowCloudNat enum for the list of possible values.

`optional string allow_cloud_nat = 254831265;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowCloudNat field is set.  
  
### hasAllowCloudRouter()
    
    
    public abstract boolean hasAllowCloudRouter()

Specifies whether cloud router creation is allowed. Check the AllowCloudRouter enum for the list of possible values.

`optional string allow_cloud_router = 451110345;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowCloudRouter field is set.  
  
### hasAllowDefaultNicAttachment()
    
    
    public abstract boolean hasAllowDefaultNicAttachment()

Specifies whether default NIC attachment is allowed. Check the AllowDefaultNicAttachment enum for the list of possible values.

`optional string allow_default_nic_attachment = 53917486;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowDefaultNicAttachment field is set.  
  
### hasAllowExternalIpAccess()
    
    
    public abstract boolean hasAllowExternalIpAccess()

Specifies whether VMs are allowed to have external IP access on network interfaces connected to this VPC. Check the AllowExternalIpAccess enum for the list of possible values.

`optional string allow_external_ip_access = 131538110;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowExternalIpAccess field is set.  
  
### hasAllowFirewallPolicy()
    
    
    public abstract boolean hasAllowFirewallPolicy()

Specifies whether firewall policy can be attached to the network. Check the AllowFirewallPolicy enum for the list of possible values.

`optional string allow_firewall_policy = 254200923;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowFirewallPolicy field is set.  
  
### hasAllowInterconnect()
    
    
    public abstract boolean hasAllowInterconnect()

Specifies whether Cloud Interconnect creation is allowed. Check the AllowInterconnect enum for the list of possible values.

`optional string allow_interconnect = 280512964;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowInterconnect field is set.  
  
### hasAllowIpForwarding()
    
    
    public abstract boolean hasAllowIpForwarding()

Specifies whether IP forwarding is allowed. Check the AllowIpForwarding enum for the list of possible values.

`optional string allow_ip_forwarding = 500838047;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowIpForwarding field is set.  
  
### hasAllowLoadBalancing()
    
    
    public abstract boolean hasAllowLoadBalancing()

Specifies whether cloud load balancing is allowed. Check the AllowLoadBalancing enum for the list of possible values.

`optional string allow_load_balancing = 223366198;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowLoadBalancing field is set.  
  
### hasAllowMultiNicInSameNetwork()
    
    
    public abstract boolean hasAllowMultiNicInSameNetwork()

Specifies whether multi-nic in the same network is allowed. Check the AllowMultiNicInSameNetwork enum for the list of possible values.

`optional string allow_multi_nic_in_same_network = 88251004;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowMultiNicInSameNetwork field is set.  
  
### hasAllowMultiNicInSameSubnetwork()
    
    
    public abstract boolean hasAllowMultiNicInSameSubnetwork()

Specifies whether multi-nic in the same subnetwork is allowed. Check the AllowMultiNicInSameSubnetwork enum for the list of possible values.

`optional string allow_multi_nic_in_same_subnetwork = 278087904;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowMultiNicInSameSubnetwork field is set.  
  
### hasAllowMulticast()
    
    
    public abstract boolean hasAllowMulticast()

Specifies whether multicast is allowed. Check the AllowMulticast enum for the list of possible values.

`optional string allow_multicast = 11002498;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowMulticast field is set.  
  
### hasAllowNcc()
    
    
    public abstract boolean hasAllowNcc()

Specifies whether NCC is allowed. Check the AllowNcc enum for the list of possible values.

`optional string allow_ncc = 372354904;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowNcc field is set.  
  
### hasAllowNetworkMigration()
    
    
    public abstract boolean hasAllowNetworkMigration()

Specifies whether VM network migration is allowed. Check the AllowNetworkMigration enum for the list of possible values.

`optional string allow_network_migration = 239588231;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowNetworkMigration field is set.  
  
### hasAllowPacketMirroring()
    
    
    public abstract boolean hasAllowPacketMirroring()

Specifies whether Packet Mirroring 1.0 is supported. Check the AllowPacketMirroring enum for the list of possible values.

`optional string allow_packet_mirroring = 512227074;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowPacketMirroring field is set.  
  
### hasAllowPrivateGoogleAccess()
    
    
    public abstract boolean hasAllowPrivateGoogleAccess()

Specifies whether private Google access is allowed. Check the AllowPrivateGoogleAccess enum for the list of possible values.

`optional string allow_private_google_access = 374702072;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowPrivateGoogleAccess field is set.  
  
### hasAllowPsc()
    
    
    public abstract boolean hasAllowPsc()

Specifies whether PSC creation is allowed. Check the AllowPsc enum for the list of possible values.

`optional string allow_psc = 372357322;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowPsc field is set.  
  
### hasAllowSameNetworkUnicast()
    
    
    public abstract boolean hasAllowSameNetworkUnicast()

Specifies whether unicast within the same network is allowed. Check the AllowSameNetworkUnicast enum for the list of possible values.

`optional string allow_same_network_unicast = 167531643;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowSameNetworkUnicast field is set.  
  
### hasAllowStaticRoutes()
    
    
    public abstract boolean hasAllowStaticRoutes()

Specifies whether static route creation is allowed. Check the AllowStaticRoutes enum for the list of possible values.

`optional string allow_static_routes = 185257925;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowStaticRoutes field is set.  
  
### hasAllowSubInterfaces()
    
    
    public abstract boolean hasAllowSubInterfaces()

Specifies whether sub interfaces are allowed. Check the AllowSubInterfaces enum for the list of possible values.

`optional string allow_sub_interfaces = 247208303;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowSubInterfaces field is set.  
  
### hasAllowSubnetworkCreation()
    
    
    public abstract boolean hasAllowSubnetworkCreation()

Specifies whether subnetwork creation is allowed. Check the AllowSubnetworkCreation enum for the list of possible values.

`optional string allow_subnetwork_creation = 459328026;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowSubnetworkCreation field is set.  
  
### hasAllowVpcFirewallRules()
    
    
    public abstract boolean hasAllowVpcFirewallRules()

Specifies whether VPC firewall rules can be created under the network. Check the AllowVpcFirewallRules enum for the list of possible values.

`optional string allow_vpc_firewall_rules = 509076420;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowVpcFirewallRules field is set.  
  
### hasAllowVpcPeering()
    
    
    public abstract boolean hasAllowVpcPeering()

Specifies whether VPC peering is allowed. Check the AllowVpcPeering enum for the list of possible values.

`optional string allow_vpc_peering = 115402228;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowVpcPeering field is set.  
  
### hasAllowVpn()
    
    
    public abstract boolean hasAllowVpn()

Specifies whether VPN creation is allowed. Check the AllowVpn enum for the list of possible values.

`optional string allow_vpn = 372363006;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowVpn field is set.  
  
### hasMulticast()
    
    
    public abstract boolean hasMulticast()

Specifies which type of multicast is supported. Check the Multicast enum for the list of possible values.

`optional string multicast = 404098040;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multicast field is set.  
  
### hasPredefinedNetworkInternalIpv6Range()
    
    
    public abstract boolean hasPredefinedNetworkInternalIpv6Range()

Specifies a predefined internal IPv6 range for the network.

`optional string predefined_network_internal_ipv6_range = 527810909;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the predefinedNetworkInternalIpv6Range field is set.  
  
### hasUnicast()
    
    
    public abstract boolean hasUnicast()

Specifies which type of unicast is supported. Check the Unicast enum for the list of possible values.

`optional string unicast = 249841711;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unicast field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
