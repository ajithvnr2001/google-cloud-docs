---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.RouteInfo.NextHopType
title: Enum RouteInfo.NextHopType (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:55.892560+00:00
---

# Enum RouteInfo.NextHopType (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.RouteInfo.NextHopType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum RouteInfo.NextHopType (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 
    
    
    public enum RouteInfo.NextHopType extends Enum<RouteInfo.NextHopType> implements ProtocolMessageEnum

Type of next hop:

Protobuf enum `google.cloud.networkmanagement.v1.RouteInfo.NextHopType`

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
`NEXT_HOP_BLACKHOLE` |  Next hop is blackhole; that is, the next hop either does not exist or is unusable. `NEXT_HOP_BLACKHOLE = 9;`  
`NEXT_HOP_BLACKHOLE_VALUE` |  Next hop is blackhole; that is, the next hop either does not exist or is unusable. `NEXT_HOP_BLACKHOLE = 9;`  
`NEXT_HOP_ILB` |  Next hop is the forwarding rule of an Internal Load Balancer. `NEXT_HOP_ILB = 10;`  
`NEXT_HOP_ILB_VALUE` |  Next hop is the forwarding rule of an Internal Load Balancer. `NEXT_HOP_ILB = 10;`  
`NEXT_HOP_INSTANCE` |  Next hop is a Compute Engine instance. `NEXT_HOP_INSTANCE = 2;`  
`NEXT_HOP_INSTANCE_VALUE` |  Next hop is a Compute Engine instance. `NEXT_HOP_INSTANCE = 2;`  
`NEXT_HOP_INTERCONNECT` |  Next hop is an interconnect. `NEXT_HOP_INTERCONNECT = 5;`  
`NEXT_HOP_INTERCONNECT_VALUE` |  Next hop is an interconnect. `NEXT_HOP_INTERCONNECT = 5;`  
`NEXT_HOP_INTERNET_GATEWAY` |  Next hop is an internet gateway. `NEXT_HOP_INTERNET_GATEWAY = 8;`  
`NEXT_HOP_INTERNET_GATEWAY_VALUE` |  Next hop is an internet gateway. `NEXT_HOP_INTERNET_GATEWAY = 8;`  
`NEXT_HOP_IP` |  Next hop is an IP address. `NEXT_HOP_IP = 1;`  
`NEXT_HOP_IP_VALUE` |  Next hop is an IP address. `NEXT_HOP_IP = 1;`  
`NEXT_HOP_NCC_HUB` |  Next hop is an NCC hub. This scenario only happens when the user doesn't have permissions to the project where the next hop resource is located. `NEXT_HOP_NCC_HUB = 12;`  
`NEXT_HOP_NCC_HUB_VALUE` |  Next hop is an NCC hub. This scenario only happens when the user doesn't have permissions to the project where the next hop resource is located. `NEXT_HOP_NCC_HUB = 12;`  
`NEXT_HOP_NETWORK` |  Next hop is a VPC network gateway. `NEXT_HOP_NETWORK = 3;`  
`NEXT_HOP_NETWORK_VALUE` |  Next hop is a VPC network gateway. `NEXT_HOP_NETWORK = 3;`  
`NEXT_HOP_PEERING` |  Next hop is a peering VPC. This scenario only happens when the user doesn't have permissions to the project where the next hop resource is located. `NEXT_HOP_PEERING = 4;`  
`NEXT_HOP_PEERING_VALUE` |  Next hop is a peering VPC. This scenario only happens when the user doesn't have permissions to the project where the next hop resource is located. `NEXT_HOP_PEERING = 4;`  
`NEXT_HOP_ROUTER_APPLIANCE` |  Next hop is a [router appliance instance](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview). `NEXT_HOP_ROUTER_APPLIANCE = 11;`  
`NEXT_HOP_ROUTER_APPLIANCE_VALUE` |  Next hop is a [router appliance instance](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview). `NEXT_HOP_ROUTER_APPLIANCE = 11;`  
`NEXT_HOP_TYPE_UNSPECIFIED` |  Unspecified type. Default value. `NEXT_HOP_TYPE_UNSPECIFIED = 0;`  
`NEXT_HOP_TYPE_UNSPECIFIED_VALUE` |  Unspecified type. Default value. `NEXT_HOP_TYPE_UNSPECIFIED = 0;`  
`NEXT_HOP_VPN_GATEWAY` |  Next hop is a VPN gateway. This scenario only happens when tracing connectivity from an on-premises network to Google Cloud through a VPN. The analysis simulates a packet departing from the on-premises network through a VPN tunnel and arriving at a Cloud VPN gateway. `NEXT_HOP_VPN_GATEWAY = 7;`  
`NEXT_HOP_VPN_GATEWAY_VALUE` |  Next hop is a VPN gateway. This scenario only happens when tracing connectivity from an on-premises network to Google Cloud through a VPN. The analysis simulates a packet departing from the on-premises network through a VPN tunnel and arriving at a Cloud VPN gateway. `NEXT_HOP_VPN_GATEWAY = 7;`  
`NEXT_HOP_VPN_TUNNEL` |  Next hop is a VPN tunnel. `NEXT_HOP_VPN_TUNNEL = 6;`  
`NEXT_HOP_VPN_TUNNEL_VALUE` |  Next hop is a VPN tunnel. `NEXT_HOP_VPN_TUNNEL = 6;`  
`SECURE_WEB_PROXY_GATEWAY` |  Next hop is Secure Web Proxy Gateway. `SECURE_WEB_PROXY_GATEWAY = 13;`  
`SECURE_WEB_PROXY_GATEWAY_VALUE` |  Next hop is Secure Web Proxy Gateway. `SECURE_WEB_PROXY_GATEWAY = 13;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.RouteInfo.NextHopType#com_google_cloud_networkmanagement_v1_RouteInfo_NextHopType_forNumber_int_) instead._  
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
