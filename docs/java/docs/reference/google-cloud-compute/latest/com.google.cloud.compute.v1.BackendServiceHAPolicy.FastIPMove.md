---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceHAPolicy.FastIPMove
title: Enum BackendServiceHAPolicy.FastIPMove (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:31.507180+00:00
---

# Enum BackendServiceHAPolicy.FastIPMove (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceHAPolicy.FastIPMove

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum BackendServiceHAPolicy.FastIPMove (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public enum BackendServiceHAPolicy.FastIPMove extends Enum<BackendServiceHAPolicy.FastIPMove> implements ProtocolMessageEnum

Specifies whether fast IP move is enabled, and if so, the mechanism to achieve it.

Supported values are:

  * DISABLED: Fast IP Move is disabled. You can only use the haPolicy.leader API to update the leader.
  * >GARP_RA: Provides a method to very quickly define a new network endpoint as the leader. This method is faster than updating the leader using the haPolicy.leader API. Fast IP move works as follows: The VM hosting the network endpoint that should become the new leader sends either a Gratuitous ARP (GARP) packet (IPv4) or an ICMPv6 Router Advertisement(RA) packet (IPv6). Google Cloud immediately but temporarily associates the forwarding rule IP address with that VM, and both new and in-flight packets are quickly delivered to that VM.



Note the important properties of the Fast IP Move functionality:

  * The GARP/RA-initiated re-routing stays active for approximately 20 minutes. After triggering fast failover, you must also appropriately set the haPolicy.leader.
  * The new leader instance should continue to send GARP/RA packets periodically every 10 seconds until at least 10 minutes after updating the haPolicy.leader (but stop immediately if it is no longer the leader).
  * After triggering a fast failover, we recommend that you wait at least 3 seconds before sending another GARP/RA packet from a different VM instance to avoid race conditions.
  * Don't send GARP/RA packets from different VM instances at the same time. If multiple instances continue to send GARP/RA packets, traffic might be routed to different destinations in an alternating order. This condition ceases when a single instance issues a GARP/RA packet.
  * The GARP/RA request always takes priority over the leader API. Using the haPolicy.leader API to change the leader to a different instance will have no effect until the GARP/RA request becomes inactive.
  * The GARP/RA packets should follow the GARP/RA Packet Specifications..
  * When multiple forwarding rules refer to a regional backend service, you need only send a GARP or RA packet for a single forwarding rule virtual IP. The virtual IPs for all forwarding rules targeting the same backend service will also be moved to the sender of the GARP or RA packet.



The following are the Fast IP Move limitations (that is, when fastIPMove is not DISABLED):

  * Multiple forwarding rules cannot use the same IP address if one of them refers to a regional backend service with fastIPMove.
  * The regional backend service must set the network field, and all NEGs must belong to that network. However, individual NEGs can belong to different subnetworks of that network.
  * The maximum number of network endpoints across all backends of a backend service with fastIPMove is 32.
  * The maximum number of backend services with fastIPMove that can have the same network endpoint attached to one of its backends is 64.
  * The maximum number of backend services with fastIPMove in a VPC in a region is 64.
  * The network endpoints that are attached to a backend of a backend service with fastIPMove cannot resolve to Gen3+ machines for IPv6.
  * Traffic directed to the leader by a static route next hop will not be redirected to a new leader by fast failover. Such traffic will only be redirected once an haPolicy.leader update has taken effect. Only traffic to the forwarding rule's virtual IP will be redirected to a new leader by fast failover.



haPolicy.fastIPMove can be set only at backend service creation time. Once set, it cannot be updated.

By default, fastIpMove is set to DISABLED.

Protobuf enum `google.cloud.compute.v1.BackendServiceHAPolicy.FastIPMove`

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
`DISABLED` | `DISABLED = 516696700;`  
`DISABLED_VALUE` | `DISABLED = 516696700;`  
`GARP_RA` | `GARP_RA = 527352630;`  
`GARP_RA_VALUE` | `GARP_RA = 527352630;`  
`UNDEFINED_FAST_I_P_MOVE` |  A value indicating that the enum field is not set. `UNDEFINED_FAST_I_P_MOVE = 0;`  
`UNDEFINED_FAST_I_P_MOVE_VALUE` |  A value indicating that the enum field is not set. `UNDEFINED_FAST_I_P_MOVE = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceHAPolicy.FastIPMove#com_google_cloud_compute_v1_BackendServiceHAPolicy_FastIPMove_forNumber_int_) instead._  
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
