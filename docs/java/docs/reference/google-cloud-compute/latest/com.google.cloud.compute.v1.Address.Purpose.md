---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.Purpose
title: Enum Address.Purpose (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:59.277203+00:00
---

# Enum Address.Purpose (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.Purpose

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Address.Purpose (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public enum Address.Purpose extends Enum<Address.Purpose> implements ProtocolMessageEnum

The purpose of this resource, which can be one of the following values:

  * GCE_ENDPOINT for addresses that are used by VM instances, alias IP ranges, load balancers, and similar resources.
  * DNS_RESOLVER for a DNS resolver address in a subnetwork for a Cloud DNS inbound forwarder IP addresses (regional internal IP address in a subnet of a VPC network)
  * VPC_PEERING for global internal IP addresses used for

private services access allocated ranges.

  * NAT_AUTO for the regional external IP addresses used by Cloud NAT when allocating addresses using

automatic NAT IP address allocation.

  * IPSEC_INTERCONNECT for addresses created from a private IP range that are reserved for a VLAN attachment in an _HA VPN over Cloud Interconnect_ configuration. These addresses are regional resources.
  * `SHARED_LOADBALANCER_VIP` for an internal IP address that is assigned to multiple internal forwarding rules.
  * `PRIVATE_SERVICE_CONNECT` for a private network address that is used to configure Private Service Connect. Only global internal addresses can use this purpose.
  * `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0` for addresses that can only be assigned to global external Passthrough Network Load Balancer forwarding rules, as an Availability Group 0 address.
  * `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1` for addresses that can only be assigned to global external Passthrough Network Load Balancer forwarding rules, as an Availability Group 1 address.



Protobuf enum `google.cloud.compute.v1.Address.Purpose`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`DNS_RESOLVER` |  DNS resolver address in the subnetwork. `DNS_RESOLVER = 476114556;`  
`DNS_RESOLVER_VALUE` |  DNS resolver address in the subnetwork. `DNS_RESOLVER = 476114556;`  
`GCE_ENDPOINT` |  VM internal/alias IP, Internal LB service IP, etc. `GCE_ENDPOINT = 230515243;`  
`GCE_ENDPOINT_VALUE` |  VM internal/alias IP, Internal LB service IP, etc. `GCE_ENDPOINT = 230515243;`  
`IPSEC_INTERCONNECT` |  A regional internal IP address range reserved for the VLAN attachment that is used in HA VPN over Cloud Interconnect. This regional internal IP address range must not overlap with any IP address range of subnet/route in the VPC network and its peering networks. After the VLAN attachment is created with the reserved IP address range, when creating a new VPN gateway, its interface IP address is allocated from the associated VLAN attachment's IP address range. `IPSEC_INTERCONNECT = 340437251;`  
`IPSEC_INTERCONNECT_VALUE` |  A regional internal IP address range reserved for the VLAN attachment that is used in HA VPN over Cloud Interconnect. This regional internal IP address range must not overlap with any IP address range of subnet/route in the VPC network and its peering networks. After the VLAN attachment is created with the reserved IP address range, when creating a new VPN gateway, its interface IP address is allocated from the associated VLAN attachment's IP address range. `IPSEC_INTERCONNECT = 340437251;`  
`NAT_AUTO` |  External IP automatically reserved for Cloud NAT. `NAT_AUTO = 163666477;`  
`NAT_AUTO_VALUE` |  External IP automatically reserved for Cloud NAT. `NAT_AUTO = 163666477;`  
`PRIVATE_SERVICE_CONNECT` |  A private network IP address that can be used to configure Private Service Connect. This purpose can be specified only forGLOBAL addresses of Type INTERNAL `PRIVATE_SERVICE_CONNECT = 48134724;`  
`PRIVATE_SERVICE_CONNECT_VALUE` |  A private network IP address that can be used to configure Private Service Connect. This purpose can be specified only forGLOBAL addresses of Type INTERNAL `PRIVATE_SERVICE_CONNECT = 48134724;`  
`SERVERLESS` |  A regional internal IP address range reserved for Serverless. `SERVERLESS = 270492508;`  
`SERVERLESS_VALUE` |  A regional internal IP address range reserved for Serverless. `SERVERLESS = 270492508;`  
`SHARED_LOADBALANCER_VIP` |  A private network IP address that can be shared by multiple Internal Load Balancer forwarding rules. `SHARED_LOADBALANCER_VIP = 294447572;`  
`SHARED_LOADBALANCER_VIP_VALUE` |  A private network IP address that can be shared by multiple Internal Load Balancer forwarding rules. `SHARED_LOADBALANCER_VIP = 294447572;`  
`UNDEFINED_PURPOSE` |  A value indicating that the enum field is not set. `UNDEFINED_PURPOSE = 0;`  
`UNDEFINED_PURPOSE_VALUE` |  A value indicating that the enum field is not set. `UNDEFINED_PURPOSE = 0;`  
`UNRECOGNIZED` |   
`VPC_PEERING` |  IP range for peer networks. `VPC_PEERING = 400800170;`  
`VPC_PEERING_VALUE` |  IP range for peer networks. `VPC_PEERING = 400800170;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.Purpose#com_google_cloud_compute_v1_Address_Purpose_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
