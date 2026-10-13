---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentOrBuilder
title: Interface InterconnectAttachmentOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:02.486898+00:00
---

# Interface InterconnectAttachmentOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InterconnectAttachmentOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface InterconnectAttachmentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.

`map<string, string> labels = 500195327;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdminEnabled()
    
    
    public abstract boolean getAdminEnabled()

Determines whether this Attachment will carry packets. Not present for PARTNER_PROVIDER.

`optional bool admin_enabled = 445675089;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The adminEnabled.  
  
### getAttachmentGroup()
    
    
    public abstract String getAttachmentGroup()

Output only. [Output Only] URL of the AttachmentGroup that includes this Attachment.

`optional string attachment_group = 63442019;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The attachmentGroup.  
  
### getAttachmentGroupBytes()
    
    
    public abstract ByteString getAttachmentGroupBytes()

Output only. [Output Only] URL of the AttachmentGroup that includes this Attachment.

`optional string attachment_group = 63442019;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for attachmentGroup.  
  
### getBandwidth()
    
    
    public abstract String getBandwidth()

Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, and can take one of the following values:

  * BPS_50M: 50 Mbit/s
  * BPS_100M: 100 Mbit/s
  * BPS_200M: 200 Mbit/s
  * BPS_300M: 300 Mbit/s
  * BPS_400M: 400 Mbit/s
  * BPS_500M: 500 Mbit/s
  * BPS_1G: 1 Gbit/s
  * BPS_2G: 2 Gbit/s
  * BPS_5G: 5 Gbit/s
  * BPS_10G: 10 Gbit/s
  * BPS_20G: 20 Gbit/s
  * BPS_50G: 50 Gbit/s
  * BPS_100G: 100 Gbit/s
  * BPS_400G: 400 Gbit/s Check the Bandwidth enum for the list of possible values.



`optional string bandwidth = 181715121;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bandwidth.  
  
### getBandwidthBytes()
    
    
    public abstract ByteString getBandwidthBytes()

Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, and can take one of the following values:

  * BPS_50M: 50 Mbit/s
  * BPS_100M: 100 Mbit/s
  * BPS_200M: 200 Mbit/s
  * BPS_300M: 300 Mbit/s
  * BPS_400M: 400 Mbit/s
  * BPS_500M: 500 Mbit/s
  * BPS_1G: 1 Gbit/s
  * BPS_2G: 2 Gbit/s
  * BPS_5G: 5 Gbit/s
  * BPS_10G: 10 Gbit/s
  * BPS_20G: 20 Gbit/s
  * BPS_50G: 50 Gbit/s
  * BPS_100G: 100 Gbit/s
  * BPS_400G: 400 Gbit/s Check the Bandwidth enum for the list of possible values.



`optional string bandwidth = 181715121;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bandwidth.  
  
### getCandidateCloudRouterIpAddress()
    
    
    public abstract String getCandidateCloudRouterIpAddress()

Single IPv4 address + prefix length to be configured on the cloud router interface for this interconnect attachment.

  * Both candidate_cloud_router_ip_address and candidate_customer_router_ip_address fields must be set or both must be unset.
  * Prefix length of both candidate_cloud_router_ip_address and candidate_customer_router_ip_address must be the same.
  * Max prefix length is 31.



`optional string candidate_cloud_router_ip_address = 311379276;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The candidateCloudRouterIpAddress.  
  
### getCandidateCloudRouterIpAddressBytes()
    
    
    public abstract ByteString getCandidateCloudRouterIpAddressBytes()

Single IPv4 address + prefix length to be configured on the cloud router interface for this interconnect attachment.

  * Both candidate_cloud_router_ip_address and candidate_customer_router_ip_address fields must be set or both must be unset.
  * Prefix length of both candidate_cloud_router_ip_address and candidate_customer_router_ip_address must be the same.
  * Max prefix length is 31.



`optional string candidate_cloud_router_ip_address = 311379276;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for candidateCloudRouterIpAddress.  
  
### getCandidateCloudRouterIpv6Address()
    
    
    public abstract String getCandidateCloudRouterIpv6Address()

Single IPv6 address + prefix length to be configured on the cloud router interface for this interconnect attachment.

  * Both candidate_cloud_router_ipv6_address and candidate_customer_router_ipv6_address fields must be set or both must be unset.
  * Prefix length of both candidate_cloud_router_ipv6_address and candidate_customer_router_ipv6_address must be the same.
  * Max prefix length is 126.



`optional string candidate_cloud_router_ipv6_address = 417499660;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The candidateCloudRouterIpv6Address.  
  
### getCandidateCloudRouterIpv6AddressBytes()
    
    
    public abstract ByteString getCandidateCloudRouterIpv6AddressBytes()

Single IPv6 address + prefix length to be configured on the cloud router interface for this interconnect attachment.

  * Both candidate_cloud_router_ipv6_address and candidate_customer_router_ipv6_address fields must be set or both must be unset.
  * Prefix length of both candidate_cloud_router_ipv6_address and candidate_customer_router_ipv6_address must be the same.
  * Max prefix length is 126.



`optional string candidate_cloud_router_ipv6_address = 417499660;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for candidateCloudRouterIpv6Address.  
  
### getCandidateCustomerRouterIpAddress()
    
    
    public abstract String getCandidateCustomerRouterIpAddress()

Single IPv4 address + prefix length to be configured on the customer router interface for this interconnect attachment.

`optional string candidate_customer_router_ip_address = 339113389;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The candidateCustomerRouterIpAddress.  
  
### getCandidateCustomerRouterIpAddressBytes()
    
    
    public abstract ByteString getCandidateCustomerRouterIpAddressBytes()

Single IPv4 address + prefix length to be configured on the customer router interface for this interconnect attachment.

`optional string candidate_customer_router_ip_address = 339113389;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for candidateCustomerRouterIpAddress.  
  
### getCandidateCustomerRouterIpv6Address()
    
    
    public abstract String getCandidateCustomerRouterIpv6Address()

Single IPv6 address + prefix length to be configured on the customer router interface for this interconnect attachment.

`optional string candidate_customer_router_ipv6_address = 226436653;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The candidateCustomerRouterIpv6Address.  
  
### getCandidateCustomerRouterIpv6AddressBytes()
    
    
    public abstract ByteString getCandidateCustomerRouterIpv6AddressBytes()

Single IPv6 address + prefix length to be configured on the customer router interface for this interconnect attachment.

`optional string candidate_customer_router_ipv6_address = 226436653;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for candidateCustomerRouterIpv6Address.  
  
### getCandidateIpv6Subnets(int index)
    
    
    public abstract String getCandidateIpv6Subnets(int index)

This field is not available.

`repeated string candidate_ipv6_subnets = 70682522;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The candidateIpv6Subnets at the given index.  
  
### getCandidateIpv6SubnetsBytes(int index)
    
    
    public abstract ByteString getCandidateIpv6SubnetsBytes(int index)

This field is not available.

`repeated string candidate_ipv6_subnets = 70682522;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the candidateIpv6Subnets at the given index.  
  
### getCandidateIpv6SubnetsCount()
    
    
    public abstract int getCandidateIpv6SubnetsCount()

This field is not available.

`repeated string candidate_ipv6_subnets = 70682522;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of candidateIpv6Subnets.  
  
### getCandidateIpv6SubnetsList()
    
    
    public abstract List<String> getCandidateIpv6SubnetsList()

This field is not available.

`repeated string candidate_ipv6_subnets = 70682522;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the candidateIpv6Subnets.  
  
### getCandidateSubnets(int index)
    
    
    public abstract String getCandidateSubnets(int index)

Input only. Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space.

`repeated string candidate_subnets = 237842938;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The candidateSubnets at the given index.  
  
### getCandidateSubnetsBytes(int index)
    
    
    public abstract ByteString getCandidateSubnetsBytes(int index)

Input only. Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space.

`repeated string candidate_subnets = 237842938;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the candidateSubnets at the given index.  
  
### getCandidateSubnetsCount()
    
    
    public abstract int getCandidateSubnetsCount()

Input only. Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space.

`repeated string candidate_subnets = 237842938;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of candidateSubnets.  
  
### getCandidateSubnetsList()
    
    
    public abstract List<String> getCandidateSubnetsList()

Input only. Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space.

`repeated string candidate_subnets = 237842938;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the candidateSubnets.  
  
### getCloudRouterIpAddress()
    
    
    public abstract String getCloudRouterIpAddress()

Output only. [Output Only] IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.

`optional string cloud_router_ip_address = 287392776;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudRouterIpAddress.  
  
### getCloudRouterIpAddressBytes()
    
    
    public abstract ByteString getCloudRouterIpAddressBytes()

Output only. [Output Only] IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.

`optional string cloud_router_ip_address = 287392776;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudRouterIpAddress.  
  
### getCloudRouterIpv6Address()
    
    
    public abstract String getCloudRouterIpv6Address()

Output only. [Output Only] IPv6 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.

`optional string cloud_router_ipv6_address = 451922376;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudRouterIpv6Address.  
  
### getCloudRouterIpv6AddressBytes()
    
    
    public abstract ByteString getCloudRouterIpv6AddressBytes()

Output only. [Output Only] IPv6 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.

`optional string cloud_router_ipv6_address = 451922376;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudRouterIpv6Address.  
  
### getCloudRouterIpv6InterfaceId()
    
    
    public abstract String getCloudRouterIpv6InterfaceId()

This field is not available.

`optional string cloud_router_ipv6_interface_id = 521282701;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudRouterIpv6InterfaceId.  
  
### getCloudRouterIpv6InterfaceIdBytes()
    
    
    public abstract ByteString getCloudRouterIpv6InterfaceIdBytes()

This field is not available.

`optional string cloud_router_ipv6_interface_id = 521282701;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudRouterIpv6InterfaceId.  
  
### getConfigurationConstraints()
    
    
    public abstract InterconnectAttachmentConfigurationConstraints getConfigurationConstraints()

Output only. [Output Only] Constraints for this attachment, if any. The attachment does not work if these constraints are not met.

` optional .google.cloud.compute.v1.InterconnectAttachmentConfigurationConstraints configuration_constraints = 179681389; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentConfigurationConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentConfigurationConstraints)` | The configurationConstraints.  
  
### getConfigurationConstraintsOrBuilder()
    
    
    public abstract InterconnectAttachmentConfigurationConstraintsOrBuilder getConfigurationConstraintsOrBuilder()

Output only. [Output Only] Constraints for this attachment, if any. The attachment does not work if these constraints are not met.

` optional .google.cloud.compute.v1.InterconnectAttachmentConfigurationConstraints configuration_constraints = 179681389; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentConfigurationConstraintsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentConfigurationConstraintsOrBuilder)` |   
  
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
  
### getCustomerRouterIpAddress()
    
    
    public abstract String getCustomerRouterIpAddress()

Output only. [Output Only] IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.

`optional string customer_router_ip_address = 332475761;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customerRouterIpAddress.  
  
### getCustomerRouterIpAddressBytes()
    
    
    public abstract ByteString getCustomerRouterIpAddressBytes()

Output only. [Output Only] IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.

`optional string customer_router_ip_address = 332475761;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customerRouterIpAddress.  
  
### getCustomerRouterIpv6Address()
    
    
    public abstract String getCustomerRouterIpv6Address()

Output only. [Output Only] IPv6 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.

`optional string customer_router_ipv6_address = 290127089;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customerRouterIpv6Address.  
  
### getCustomerRouterIpv6AddressBytes()
    
    
    public abstract ByteString getCustomerRouterIpv6AddressBytes()

Output only. [Output Only] IPv6 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.

`optional string customer_router_ipv6_address = 290127089;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customerRouterIpv6Address.  
  
### getCustomerRouterIpv6InterfaceId()
    
    
    public abstract String getCustomerRouterIpv6InterfaceId()

This field is not available.

`optional string customer_router_ipv6_interface_id = 380994308;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customerRouterIpv6InterfaceId.  
  
### getCustomerRouterIpv6InterfaceIdBytes()
    
    
    public abstract ByteString getCustomerRouterIpv6InterfaceIdBytes()

This field is not available.

`optional string customer_router_ipv6_interface_id = 380994308;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customerRouterIpv6InterfaceId.  
  
### getDataplaneVersion()
    
    
    public abstract int getDataplaneVersion()

Output only. [Output Only] Dataplane version for this InterconnectAttachment. This field is only present for Dataplane version 2 and higher. Absence of this field in the API output indicates that the Dataplane is version 1.

`optional int32 dataplane_version = 34920075;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dataplaneVersion.  
  
### getDescription()
    
    
    public abstract String getDescription()

An optional description of this resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

An optional description of this resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEdgeAvailabilityDomain()
    
    
    public abstract String getEdgeAvailabilityDomain()

Input only. Desired availability domain for the attachment. Only available for type PARTNER, at creation time, and can take one of the following values:

  * AVAILABILITY_DOMAIN_ANY
  * AVAILABILITY_DOMAIN_1
  * AVAILABILITY_DOMAIN_2



For improved reliability, customers should configure a pair of attachments, one per availability domain. The selected availability domain will be provided to the Partner via the pairing key, so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY. Check the EdgeAvailabilityDomain enum for the list of possible values.

`optional string edge_availability_domain = 71289510;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The edgeAvailabilityDomain.  
  
### getEdgeAvailabilityDomainBytes()
    
    
    public abstract ByteString getEdgeAvailabilityDomainBytes()

Input only. Desired availability domain for the attachment. Only available for type PARTNER, at creation time, and can take one of the following values:

  * AVAILABILITY_DOMAIN_ANY
  * AVAILABILITY_DOMAIN_1
  * AVAILABILITY_DOMAIN_2



For improved reliability, customers should configure a pair of attachments, one per availability domain. The selected availability domain will be provided to the Partner via the pairing key, so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY. Check the EdgeAvailabilityDomain enum for the list of possible values.

`optional string edge_availability_domain = 71289510;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for edgeAvailabilityDomain.  
  
### getEncryption()
    
    
    public abstract String getEncryption()

Indicates the user-supplied encryption option of this VLAN attachment (interconnectAttachment). Can only be specified at attachment creation for PARTNER or DEDICATED attachments. Possible values are:

  * NONE - This is the default value, which means that the VLAN attachment carries unencrypted traffic. VMs are able to send traffic to, or receive traffic from, such a VLAN attachment.
  * IPSEC - The VLAN attachment carries only encrypted traffic that is encrypted by an IPsec device, such as an HA VPN gateway or third-party IPsec VPN. VMs cannot directly send traffic to, or receive traffic from, such a VLAN attachment. To use _HA VPN over Cloud Interconnect_ , the VLAN attachment must be created with this option. Check the Encryption enum for the list of possible values.



`optional string encryption = 97980291;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The encryption.  
  
### getEncryptionBytes()
    
    
    public abstract ByteString getEncryptionBytes()

Indicates the user-supplied encryption option of this VLAN attachment (interconnectAttachment). Can only be specified at attachment creation for PARTNER or DEDICATED attachments. Possible values are:

  * NONE - This is the default value, which means that the VLAN attachment carries unencrypted traffic. VMs are able to send traffic to, or receive traffic from, such a VLAN attachment.
  * IPSEC - The VLAN attachment carries only encrypted traffic that is encrypted by an IPsec device, such as an HA VPN gateway or third-party IPsec VPN. VMs cannot directly send traffic to, or receive traffic from, such a VLAN attachment. To use _HA VPN over Cloud Interconnect_ , the VLAN attachment must be created with this option. Check the Encryption enum for the list of possible values.



`optional string encryption = 97980291;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for encryption.  
  
### getGoogleReferenceId()
    
    
    public abstract String getGoogleReferenceId()

Output only. [Output Only] Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity issues. [Deprecated] This field is not used.

`optional string google_reference_id = 534944469;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The googleReferenceId.  
  
### getGoogleReferenceIdBytes()
    
    
    public abstract ByteString getGoogleReferenceIdBytes()

Output only. [Output Only] Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity issues. [Deprecated] This field is not used.

`optional string google_reference_id = 534944469;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for googleReferenceId.  
  
### getId()
    
    
    public abstract long getId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getInterconnect()
    
    
    public abstract String getInterconnect()

URL of the underlying Interconnect object that this attachment's traffic will traverse through.

`optional string interconnect = 224601230;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The interconnect.  
  
### getInterconnectBytes()
    
    
    public abstract ByteString getInterconnectBytes()

URL of the underlying Interconnect object that this attachment's traffic will traverse through.

`optional string interconnect = 224601230;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for interconnect.  
  
### getIpsecInternalAddresses(int index)
    
    
    public abstract String getIpsecInternalAddresses(int index)

A list of URLs of addresses that have been reserved for the VLAN attachment. Used only for the VLAN attachment that has the encryption option as IPSEC. The addresses must be regional internal IP address ranges. When creating an HA VPN gateway over the VLAN attachment, if the attachment is configured to use a regional internal IP address, then the VPN gateway's IP address is allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this VLAN attachment, then a regional internal IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this VLAN attachment. If this field is not specified when creating the VLAN attachment, then later on when creating an HA VPN gateway on this VLAN attachment, the HA VPN gateway's IP address is allocated from the regional external IP address pool.

`repeated string ipsec_internal_addresses = 407648565;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ipsecInternalAddresses at the given index.  
  
### getIpsecInternalAddressesBytes(int index)
    
    
    public abstract ByteString getIpsecInternalAddressesBytes(int index)

A list of URLs of addresses that have been reserved for the VLAN attachment. Used only for the VLAN attachment that has the encryption option as IPSEC. The addresses must be regional internal IP address ranges. When creating an HA VPN gateway over the VLAN attachment, if the attachment is configured to use a regional internal IP address, then the VPN gateway's IP address is allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this VLAN attachment, then a regional internal IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this VLAN attachment. If this field is not specified when creating the VLAN attachment, then later on when creating an HA VPN gateway on this VLAN attachment, the HA VPN gateway's IP address is allocated from the regional external IP address pool.

`repeated string ipsec_internal_addresses = 407648565;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the ipsecInternalAddresses at the given index.  
  
### getIpsecInternalAddressesCount()
    
    
    public abstract int getIpsecInternalAddressesCount()

A list of URLs of addresses that have been reserved for the VLAN attachment. Used only for the VLAN attachment that has the encryption option as IPSEC. The addresses must be regional internal IP address ranges. When creating an HA VPN gateway over the VLAN attachment, if the attachment is configured to use a regional internal IP address, then the VPN gateway's IP address is allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this VLAN attachment, then a regional internal IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this VLAN attachment. If this field is not specified when creating the VLAN attachment, then later on when creating an HA VPN gateway on this VLAN attachment, the HA VPN gateway's IP address is allocated from the regional external IP address pool.

`repeated string ipsec_internal_addresses = 407648565;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of ipsecInternalAddresses.  
  
### getIpsecInternalAddressesList()
    
    
    public abstract List<String> getIpsecInternalAddressesList()

A list of URLs of addresses that have been reserved for the VLAN attachment. Used only for the VLAN attachment that has the encryption option as IPSEC. The addresses must be regional internal IP address ranges. When creating an HA VPN gateway over the VLAN attachment, if the attachment is configured to use a regional internal IP address, then the VPN gateway's IP address is allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this VLAN attachment, then a regional internal IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this VLAN attachment. If this field is not specified when creating the VLAN attachment, then later on when creating an HA VPN gateway on this VLAN attachment, the HA VPN gateway's IP address is allocated from the regional external IP address pool.

`repeated string ipsec_internal_addresses = 407648565;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the ipsecInternalAddresses.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output Only] Type of the resource. Alwayscompute#interconnectAttachment for interconnect attachments.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output Only] Type of the resource. Alwayscompute#interconnectAttachment for interconnect attachments.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getL2Forwarding()
    
    
    public abstract InterconnectAttachmentL2Forwarding getL2Forwarding()

L2 Interconnect Attachment related config. This field is required if the type is L2_DEDICATED.

The configuration specifies how VLAN tags (like dot1q, qinq, or dot1ad) within L2 packets are mapped to the destination appliances IP addresses. The packet is then encapsulated with the appliance IP address and sent to the edge appliance.

` optional .google.cloud.compute.v1.InterconnectAttachmentL2Forwarding l2_forwarding = 84784022; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentL2Forwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentL2Forwarding)` | The l2Forwarding.  
  
### getL2ForwardingOrBuilder()
    
    
    public abstract InterconnectAttachmentL2ForwardingOrBuilder getL2ForwardingOrBuilder()

L2 Interconnect Attachment related config. This field is required if the type is L2_DEDICATED.

The configuration specifies how VLAN tags (like dot1q, qinq, or dot1ad) within L2 packets are mapped to the destination appliances IP addresses. The packet is then encapsulated with the appliance IP address and sent to the edge appliance.

` optional .google.cloud.compute.v1.InterconnectAttachmentL2Forwarding l2_forwarding = 84784022; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentL2ForwardingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentL2ForwardingOrBuilder)` |   
  
### getLabelFingerprint()
    
    
    public abstract String getLabelFingerprint()

A fingerprint for the labels being applied to this InterconnectAttachment, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve an InterconnectAttachment.

`optional string label_fingerprint = 178124825;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The labelFingerprint.  
  
### getLabelFingerprintBytes()
    
    
    public abstract ByteString getLabelFingerprintBytes()

A fingerprint for the labels being applied to this InterconnectAttachment, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve an InterconnectAttachment.

`optional string label_fingerprint = 178124825;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for labelFingerprint.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentOrBuilder#com_google_cloud_compute_v1_InterconnectAttachmentOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.

`map<string, string> labels = 500195327;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.

`map<string, string> labels = 500195327;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.

`map<string, string> labels = 500195327;`

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

Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.

`map<string, string> labels = 500195327;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMtu()
    
    
    public abstract int getMtu()

Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Valid values are 1440, 1460, 1500, and 8896. If not specified, the value will default to 1440.

`optional int32 mtu = 108462;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The mtu.  
  
### getName()
    
    
    public abstract String getName()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOperationalStatus()
    
    
    public abstract String getOperationalStatus()

Output only. [Output Only] The current status of whether or not this interconnect attachment is functional, which can take one of the following values:

  * OS_ACTIVE: The attachment has been turned up and is ready to use.
  * OS_UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete. Check the OperationalStatus enum for the list of possible values.



`optional string operational_status = 201070847;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The operationalStatus.  
  
### getOperationalStatusBytes()
    
    
    public abstract ByteString getOperationalStatusBytes()

Output only. [Output Only] The current status of whether or not this interconnect attachment is functional, which can take one of the following values:

  * OS_ACTIVE: The attachment has been turned up and is ready to use.
  * OS_UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete. Check the OperationalStatus enum for the list of possible values.



`optional string operational_status = 201070847;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for operationalStatus.  
  
### getPairingKey()
    
    
    public abstract String getPairingKey()

[Output only for type PARTNER. Input only for PARTNER_PROVIDER. Not present for DEDICATED]. The opaque identifier of a PARTNER attachment used to initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"

`optional string pairing_key = 439695464;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pairingKey.  
  
### getPairingKeyBytes()
    
    
    public abstract ByteString getPairingKeyBytes()

[Output only for type PARTNER. Input only for PARTNER_PROVIDER. Not present for DEDICATED]. The opaque identifier of a PARTNER attachment used to initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"

`optional string pairing_key = 439695464;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pairingKey.  
  
### getParams()
    
    
    public abstract InterconnectAttachmentParams getParams()

Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.

`optional .google.cloud.compute.v1.InterconnectAttachmentParams params = 78313862;`

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentParams)` | The params.  
  
### getParamsOrBuilder()
    
    
    public abstract InterconnectAttachmentParamsOrBuilder getParamsOrBuilder()

Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.

`optional .google.cloud.compute.v1.InterconnectAttachmentParams params = 78313862;`

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentParamsOrBuilder)` |   
  
### getPartnerAsn()
    
    
    public abstract long getPartnerAsn()

Optional BGP ASN for the router supplied by a Layer 3 Partner if they configured BGP on behalf of the customer. Output only for PARTNER type, input only for PARTNER_PROVIDER, not available for DEDICATED.

`optional int64 partner_asn = 438166149;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The partnerAsn.  
  
### getPartnerMetadata()
    
    
    public abstract InterconnectAttachmentPartnerMetadata getPartnerMetadata()

Informational metadata about Partner attachments from Partners to display to customers. Output only for PARTNER type, mutable for PARTNER_PROVIDER, not available for DEDICATED.

` optional .google.cloud.compute.v1.InterconnectAttachmentPartnerMetadata partner_metadata = 65908934; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentPartnerMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentPartnerMetadata)` | The partnerMetadata.  
  
### getPartnerMetadataOrBuilder()
    
    
    public abstract InterconnectAttachmentPartnerMetadataOrBuilder getPartnerMetadataOrBuilder()

Informational metadata about Partner attachments from Partners to display to customers. Output only for PARTNER type, mutable for PARTNER_PROVIDER, not available for DEDICATED.

` optional .google.cloud.compute.v1.InterconnectAttachmentPartnerMetadata partner_metadata = 65908934; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentPartnerMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentPartnerMetadataOrBuilder)` |   
  
### getPrivateInterconnectInfo()
    
    
    public abstract InterconnectAttachmentPrivateInfo getPrivateInterconnectInfo()

Output only. [Output Only] Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached to is of type DEDICATED.

` optional .google.cloud.compute.v1.InterconnectAttachmentPrivateInfo private_interconnect_info = 237270531; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentPrivateInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentPrivateInfo)` | The privateInterconnectInfo.  
  
### getPrivateInterconnectInfoOrBuilder()
    
    
    public abstract InterconnectAttachmentPrivateInfoOrBuilder getPrivateInterconnectInfoOrBuilder()

Output only. [Output Only] Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached to is of type DEDICATED.

` optional .google.cloud.compute.v1.InterconnectAttachmentPrivateInfo private_interconnect_info = 237270531; `

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentPrivateInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentPrivateInfoOrBuilder)` |   
  
### getRegion()
    
    
    public abstract String getRegion()

Output only. [Output Only] URL of the region where the regional interconnect attachment resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The region.  
  
### getRegionBytes()
    
    
    public abstract ByteString getRegionBytes()

Output only. [Output Only] URL of the region where the regional interconnect attachment resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for region.  
  
### getRemoteService()
    
    
    public abstract String getRemoteService()

Output only. [Output Only] If the attachment is on a Cross-Cloud Interconnect connection, this field contains the interconnect's remote location service provider. Example values: "Amazon Web Services" "Microsoft Azure".

The field is set only for attachments on Cross-Cloud Interconnect connections. Its value is copied from the InterconnectRemoteLocation remoteService field.

`optional string remote_service = 391954364;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The remoteService.  
  
### getRemoteServiceBytes()
    
    
    public abstract ByteString getRemoteServiceBytes()

Output only. [Output Only] If the attachment is on a Cross-Cloud Interconnect connection, this field contains the interconnect's remote location service provider. Example values: "Amazon Web Services" "Microsoft Azure".

The field is set only for attachments on Cross-Cloud Interconnect connections. Its value is copied from the InterconnectRemoteLocation remoteService field.

`optional string remote_service = 391954364;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for remoteService.  
  
### getRouter()
    
    
    public abstract String getRouter()

URL of the Cloud Router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured.

`optional string router = 148608841;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The router.  
  
### getRouterBytes()
    
    
    public abstract ByteString getRouterBytes()

URL of the Cloud Router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured.

`optional string router = 148608841;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for router.  
  
### getSatisfiesPzs()
    
    
    public abstract boolean getSatisfiesPzs()

Output only. [Output Only] Reserved for future use.

`optional bool satisfies_pzs = 480964267;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
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
  
### getStackType()
    
    
    public abstract String getStackType()

The stack type for this interconnect attachment to identify whether the IPv6 feature is enabled or not. If not specified, IPV4_ONLY will be used.

This field can be both set at interconnect attachments creation and update interconnect attachment operations. Check the StackType enum for the list of possible values.

`optional string stack_type = 425908881;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stackType.  
  
### getStackTypeBytes()
    
    
    public abstract ByteString getStackTypeBytes()

The stack type for this interconnect attachment to identify whether the IPv6 feature is enabled or not. If not specified, IPV4_ONLY will be used.

This field can be both set at interconnect attachments creation and update interconnect attachment operations. Check the StackType enum for the list of possible values.

`optional string stack_type = 425908881;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stackType.  
  
### getState()
    
    
    public abstract String getState()

Output only. [Output Only] The current state of this attachment's functionality. Enum values ACTIVE and UNPROVISIONED are shared by DEDICATED/PRIVATE, PARTNER, and PARTNER_PROVIDER interconnect attachments, while enum values PENDING_PARTNER, PARTNER_REQUEST_RECEIVED, and PENDING_CUSTOMER are used for only PARTNER and PARTNER_PROVIDER interconnect attachments. This state can take one of the following values:

  * ACTIVE: The attachment has been turned up and is ready to use.
  * UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete.
  * PENDING_PARTNER: A newly-created PARTNER attachment that has not yet been configured on the Partner side.
  * PARTNER_REQUEST_RECEIVED: A PARTNER attachment is in the process of provisioning after a PARTNER_PROVIDER attachment was created that references it.
  * PENDING_CUSTOMER: A PARTNER or PARTNER_PROVIDER attachment that is waiting for a customer to activate it.
  * DEFUNCT: The attachment was deleted externally and is no longer functional. This could be because the associated Interconnect was removed, or because the other side of a Partner attachment was deleted. Check the State enum for the list of possible values.



`optional string state = 109757585;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The state.  
  
### getStateBytes()
    
    
    public abstract ByteString getStateBytes()

Output only. [Output Only] The current state of this attachment's functionality. Enum values ACTIVE and UNPROVISIONED are shared by DEDICATED/PRIVATE, PARTNER, and PARTNER_PROVIDER interconnect attachments, while enum values PENDING_PARTNER, PARTNER_REQUEST_RECEIVED, and PENDING_CUSTOMER are used for only PARTNER and PARTNER_PROVIDER interconnect attachments. This state can take one of the following values:

  * ACTIVE: The attachment has been turned up and is ready to use.
  * UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete.
  * PENDING_PARTNER: A newly-created PARTNER attachment that has not yet been configured on the Partner side.
  * PARTNER_REQUEST_RECEIVED: A PARTNER attachment is in the process of provisioning after a PARTNER_PROVIDER attachment was created that references it.
  * PENDING_CUSTOMER: A PARTNER or PARTNER_PROVIDER attachment that is waiting for a customer to activate it.
  * DEFUNCT: The attachment was deleted externally and is no longer functional. This could be because the associated Interconnect was removed, or because the other side of a Partner attachment was deleted. Check the State enum for the list of possible values.



`optional string state = 109757585;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for state.  
  
### getSubnetLength()
    
    
    public abstract int getSubnetLength()

Input only. Length of the IPv4 subnet mask. Allowed values:

  * 29 (default)
  * 30

The default value is 29, except for Cross-Cloud Interconnect connections that use an InterconnectRemoteLocation with a constraints.subnetLengthRange.min equal to 30. For example, connections that use an Azure remote location fall into this category. In these cases, the default value is 30, and requesting 29 returns an error.

Where both 29 and 30 are allowed, 29 is preferred, because it gives Google Cloud Support more debugging visibility.




`optional int32 subnet_length = 279831048;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The subnetLength.  
  
### getType()
    
    
    public abstract String getType()

The type of interconnect attachment this is, which can take one of the following values:

  * DEDICATED: an attachment to a Dedicated Interconnect.
  * PARTNER: an attachment to a Partner Interconnect, created by the customer.
  * PARTNER_PROVIDER: an attachment to a Partner Interconnect, created by the partner.

  * L2_DEDICATED: a L2 attachment to a Dedicated Interconnect. Check the Type enum for the list of possible values.




`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

The type of interconnect attachment this is, which can take one of the following values:

  * DEDICATED: an attachment to a Dedicated Interconnect.
  * PARTNER: an attachment to a Partner Interconnect, created by the customer.
  * PARTNER_PROVIDER: an attachment to a Partner Interconnect, created by the partner.

  * L2_DEDICATED: a L2 attachment to a Dedicated Interconnect. Check the Type enum for the list of possible values.




`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### getVlanTag8021Q()
    
    
    public abstract int getVlanTag8021Q()

The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4093. Only specified at creation time.

`optional int32 vlan_tag8021q = 119927836;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The vlanTag8021q.  
  
### hasAdminEnabled()
    
    
    public abstract boolean hasAdminEnabled()

Determines whether this Attachment will carry packets. Not present for PARTNER_PROVIDER.

`optional bool admin_enabled = 445675089;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adminEnabled field is set.  
  
### hasAttachmentGroup()
    
    
    public abstract boolean hasAttachmentGroup()

Output only. [Output Only] URL of the AttachmentGroup that includes this Attachment.

`optional string attachment_group = 63442019;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the attachmentGroup field is set.  
  
### hasBandwidth()
    
    
    public abstract boolean hasBandwidth()

Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, and can take one of the following values:

  * BPS_50M: 50 Mbit/s
  * BPS_100M: 100 Mbit/s
  * BPS_200M: 200 Mbit/s
  * BPS_300M: 300 Mbit/s
  * BPS_400M: 400 Mbit/s
  * BPS_500M: 500 Mbit/s
  * BPS_1G: 1 Gbit/s
  * BPS_2G: 2 Gbit/s
  * BPS_5G: 5 Gbit/s
  * BPS_10G: 10 Gbit/s
  * BPS_20G: 20 Gbit/s
  * BPS_50G: 50 Gbit/s
  * BPS_100G: 100 Gbit/s
  * BPS_400G: 400 Gbit/s Check the Bandwidth enum for the list of possible values.



`optional string bandwidth = 181715121;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bandwidth field is set.  
  
### hasCandidateCloudRouterIpAddress()
    
    
    public abstract boolean hasCandidateCloudRouterIpAddress()

Single IPv4 address + prefix length to be configured on the cloud router interface for this interconnect attachment.

  * Both candidate_cloud_router_ip_address and candidate_customer_router_ip_address fields must be set or both must be unset.
  * Prefix length of both candidate_cloud_router_ip_address and candidate_customer_router_ip_address must be the same.
  * Max prefix length is 31.



`optional string candidate_cloud_router_ip_address = 311379276;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the candidateCloudRouterIpAddress field is set.  
  
### hasCandidateCloudRouterIpv6Address()
    
    
    public abstract boolean hasCandidateCloudRouterIpv6Address()

Single IPv6 address + prefix length to be configured on the cloud router interface for this interconnect attachment.

  * Both candidate_cloud_router_ipv6_address and candidate_customer_router_ipv6_address fields must be set or both must be unset.
  * Prefix length of both candidate_cloud_router_ipv6_address and candidate_customer_router_ipv6_address must be the same.
  * Max prefix length is 126.



`optional string candidate_cloud_router_ipv6_address = 417499660;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the candidateCloudRouterIpv6Address field is set.  
  
### hasCandidateCustomerRouterIpAddress()
    
    
    public abstract boolean hasCandidateCustomerRouterIpAddress()

Single IPv4 address + prefix length to be configured on the customer router interface for this interconnect attachment.

`optional string candidate_customer_router_ip_address = 339113389;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the candidateCustomerRouterIpAddress field is set.  
  
### hasCandidateCustomerRouterIpv6Address()
    
    
    public abstract boolean hasCandidateCustomerRouterIpv6Address()

Single IPv6 address + prefix length to be configured on the customer router interface for this interconnect attachment.

`optional string candidate_customer_router_ipv6_address = 226436653;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the candidateCustomerRouterIpv6Address field is set.  
  
### hasCloudRouterIpAddress()
    
    
    public abstract boolean hasCloudRouterIpAddress()

Output only. [Output Only] IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.

`optional string cloud_router_ip_address = 287392776;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudRouterIpAddress field is set.  
  
### hasCloudRouterIpv6Address()
    
    
    public abstract boolean hasCloudRouterIpv6Address()

Output only. [Output Only] IPv6 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.

`optional string cloud_router_ipv6_address = 451922376;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudRouterIpv6Address field is set.  
  
### hasCloudRouterIpv6InterfaceId()
    
    
    public abstract boolean hasCloudRouterIpv6InterfaceId()

This field is not available.

`optional string cloud_router_ipv6_interface_id = 521282701;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudRouterIpv6InterfaceId field is set.  
  
### hasConfigurationConstraints()
    
    
    public abstract boolean hasConfigurationConstraints()

Output only. [Output Only] Constraints for this attachment, if any. The attachment does not work if these constraints are not met.

` optional .google.cloud.compute.v1.InterconnectAttachmentConfigurationConstraints configuration_constraints = 179681389; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the configurationConstraints field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasCustomerRouterIpAddress()
    
    
    public abstract boolean hasCustomerRouterIpAddress()

Output only. [Output Only] IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.

`optional string customer_router_ip_address = 332475761;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customerRouterIpAddress field is set.  
  
### hasCustomerRouterIpv6Address()
    
    
    public abstract boolean hasCustomerRouterIpv6Address()

Output only. [Output Only] IPv6 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.

`optional string customer_router_ipv6_address = 290127089;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customerRouterIpv6Address field is set.  
  
### hasCustomerRouterIpv6InterfaceId()
    
    
    public abstract boolean hasCustomerRouterIpv6InterfaceId()

This field is not available.

`optional string customer_router_ipv6_interface_id = 380994308;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customerRouterIpv6InterfaceId field is set.  
  
### hasDataplaneVersion()
    
    
    public abstract boolean hasDataplaneVersion()

Output only. [Output Only] Dataplane version for this InterconnectAttachment. This field is only present for Dataplane version 2 and higher. Absence of this field in the API output indicates that the Dataplane is version 1.

`optional int32 dataplane_version = 34920075;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataplaneVersion field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

An optional description of this resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasEdgeAvailabilityDomain()
    
    
    public abstract boolean hasEdgeAvailabilityDomain()

Input only. Desired availability domain for the attachment. Only available for type PARTNER, at creation time, and can take one of the following values:

  * AVAILABILITY_DOMAIN_ANY
  * AVAILABILITY_DOMAIN_1
  * AVAILABILITY_DOMAIN_2



For improved reliability, customers should configure a pair of attachments, one per availability domain. The selected availability domain will be provided to the Partner via the pairing key, so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY. Check the EdgeAvailabilityDomain enum for the list of possible values.

`optional string edge_availability_domain = 71289510;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the edgeAvailabilityDomain field is set.  
  
### hasEncryption()
    
    
    public abstract boolean hasEncryption()

Indicates the user-supplied encryption option of this VLAN attachment (interconnectAttachment). Can only be specified at attachment creation for PARTNER or DEDICATED attachments. Possible values are:

  * NONE - This is the default value, which means that the VLAN attachment carries unencrypted traffic. VMs are able to send traffic to, or receive traffic from, such a VLAN attachment.
  * IPSEC - The VLAN attachment carries only encrypted traffic that is encrypted by an IPsec device, such as an HA VPN gateway or third-party IPsec VPN. VMs cannot directly send traffic to, or receive traffic from, such a VLAN attachment. To use _HA VPN over Cloud Interconnect_ , the VLAN attachment must be created with this option. Check the Encryption enum for the list of possible values.



`optional string encryption = 97980291;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryption field is set.  
  
### hasGoogleReferenceId()
    
    
    public abstract boolean hasGoogleReferenceId()

Output only. [Output Only] Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity issues. [Deprecated] This field is not used.

`optional string google_reference_id = 534944469;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the googleReferenceId field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasInterconnect()
    
    
    public abstract boolean hasInterconnect()

URL of the underlying Interconnect object that this attachment's traffic will traverse through.

`optional string interconnect = 224601230;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the interconnect field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output Only] Type of the resource. Alwayscompute#interconnectAttachment for interconnect attachments.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasL2Forwarding()
    
    
    public abstract boolean hasL2Forwarding()

L2 Interconnect Attachment related config. This field is required if the type is L2_DEDICATED.

The configuration specifies how VLAN tags (like dot1q, qinq, or dot1ad) within L2 packets are mapped to the destination appliances IP addresses. The packet is then encapsulated with the appliance IP address and sent to the edge appliance.

` optional .google.cloud.compute.v1.InterconnectAttachmentL2Forwarding l2_forwarding = 84784022; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the l2Forwarding field is set.  
  
### hasLabelFingerprint()
    
    
    public abstract boolean hasLabelFingerprint()

A fingerprint for the labels being applied to this InterconnectAttachment, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve an InterconnectAttachment.

`optional string label_fingerprint = 178124825;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the labelFingerprint field is set.  
  
### hasMtu()
    
    
    public abstract boolean hasMtu()

Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Valid values are 1440, 1460, 1500, and 8896. If not specified, the value will default to 1440.

`optional int32 mtu = 108462;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mtu field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasOperationalStatus()
    
    
    public abstract boolean hasOperationalStatus()

Output only. [Output Only] The current status of whether or not this interconnect attachment is functional, which can take one of the following values:

  * OS_ACTIVE: The attachment has been turned up and is ready to use.
  * OS_UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete. Check the OperationalStatus enum for the list of possible values.



`optional string operational_status = 201070847;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the operationalStatus field is set.  
  
### hasPairingKey()
    
    
    public abstract boolean hasPairingKey()

[Output only for type PARTNER. Input only for PARTNER_PROVIDER. Not present for DEDICATED]. The opaque identifier of a PARTNER attachment used to initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"

`optional string pairing_key = 439695464;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pairingKey field is set.  
  
### hasParams()
    
    
    public abstract boolean hasParams()

Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.

`optional .google.cloud.compute.v1.InterconnectAttachmentParams params = 78313862;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the params field is set.  
  
### hasPartnerAsn()
    
    
    public abstract boolean hasPartnerAsn()

Optional BGP ASN for the router supplied by a Layer 3 Partner if they configured BGP on behalf of the customer. Output only for PARTNER type, input only for PARTNER_PROVIDER, not available for DEDICATED.

`optional int64 partner_asn = 438166149;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partnerAsn field is set.  
  
### hasPartnerMetadata()
    
    
    public abstract boolean hasPartnerMetadata()

Informational metadata about Partner attachments from Partners to display to customers. Output only for PARTNER type, mutable for PARTNER_PROVIDER, not available for DEDICATED.

` optional .google.cloud.compute.v1.InterconnectAttachmentPartnerMetadata partner_metadata = 65908934; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partnerMetadata field is set.  
  
### hasPrivateInterconnectInfo()
    
    
    public abstract boolean hasPrivateInterconnectInfo()

Output only. [Output Only] Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached to is of type DEDICATED.

` optional .google.cloud.compute.v1.InterconnectAttachmentPrivateInfo private_interconnect_info = 237270531; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateInterconnectInfo field is set.  
  
### hasRegion()
    
    
    public abstract boolean hasRegion()

Output only. [Output Only] URL of the region where the regional interconnect attachment resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the region field is set.  
  
### hasRemoteService()
    
    
    public abstract boolean hasRemoteService()

Output only. [Output Only] If the attachment is on a Cross-Cloud Interconnect connection, this field contains the interconnect's remote location service provider. Example values: "Amazon Web Services" "Microsoft Azure".

The field is set only for attachments on Cross-Cloud Interconnect connections. Its value is copied from the InterconnectRemoteLocation remoteService field.

`optional string remote_service = 391954364;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the remoteService field is set.  
  
### hasRouter()
    
    
    public abstract boolean hasRouter()

URL of the Cloud Router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured.

`optional string router = 148608841;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the router field is set.  
  
### hasSatisfiesPzs()
    
    
    public abstract boolean hasSatisfiesPzs()

Output only. [Output Only] Reserved for future use.

`optional bool satisfies_pzs = 480964267;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzs field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasStackType()
    
    
    public abstract boolean hasStackType()

The stack type for this interconnect attachment to identify whether the IPv6 feature is enabled or not. If not specified, IPV4_ONLY will be used.

This field can be both set at interconnect attachments creation and update interconnect attachment operations. Check the StackType enum for the list of possible values.

`optional string stack_type = 425908881;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stackType field is set.  
  
### hasState()
    
    
    public abstract boolean hasState()

Output only. [Output Only] The current state of this attachment's functionality. Enum values ACTIVE and UNPROVISIONED are shared by DEDICATED/PRIVATE, PARTNER, and PARTNER_PROVIDER interconnect attachments, while enum values PENDING_PARTNER, PARTNER_REQUEST_RECEIVED, and PENDING_CUSTOMER are used for only PARTNER and PARTNER_PROVIDER interconnect attachments. This state can take one of the following values:

  * ACTIVE: The attachment has been turned up and is ready to use.
  * UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete.
  * PENDING_PARTNER: A newly-created PARTNER attachment that has not yet been configured on the Partner side.
  * PARTNER_REQUEST_RECEIVED: A PARTNER attachment is in the process of provisioning after a PARTNER_PROVIDER attachment was created that references it.
  * PENDING_CUSTOMER: A PARTNER or PARTNER_PROVIDER attachment that is waiting for a customer to activate it.
  * DEFUNCT: The attachment was deleted externally and is no longer functional. This could be because the associated Interconnect was removed, or because the other side of a Partner attachment was deleted. Check the State enum for the list of possible values.



`optional string state = 109757585;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the state field is set.  
  
### hasSubnetLength()
    
    
    public abstract boolean hasSubnetLength()

Input only. Length of the IPv4 subnet mask. Allowed values:

  * 29 (default)
  * 30

The default value is 29, except for Cross-Cloud Interconnect connections that use an InterconnectRemoteLocation with a constraints.subnetLengthRange.min equal to 30. For example, connections that use an Azure remote location fall into this category. In these cases, the default value is 30, and requesting 29 returns an error.

Where both 29 and 30 are allowed, 29 is preferred, because it gives Google Cloud Support more debugging visibility.




`optional int32 subnet_length = 279831048;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subnetLength field is set.  
  
### hasType()
    
    
    public abstract boolean hasType()

The type of interconnect attachment this is, which can take one of the following values:

  * DEDICATED: an attachment to a Dedicated Interconnect.
  * PARTNER: an attachment to a Partner Interconnect, created by the customer.
  * PARTNER_PROVIDER: an attachment to a Partner Interconnect, created by the partner.

  * L2_DEDICATED: a L2 attachment to a Dedicated Interconnect. Check the Type enum for the list of possible values.




`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
### hasVlanTag8021Q()
    
    
    public abstract boolean hasVlanTag8021Q()

The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4093. Only specified at creation time.

`optional int32 vlan_tag8021q = 119927836;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vlanTag8021q field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
