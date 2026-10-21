---
url: https://docs.cloud.google.com/network-security-integration/docs/understand-geneve/
title: Understand GENEVE format \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:21.175331+00:00
---

# Understand GENEVE format  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/understand-geneve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Understand GENEVE format Stay organized with collections  Save and categorize content based on your preferences. 

Generic Network Virtualization Encapsulation ([GENEVE](https://datatracker.ietf.org/doc/html/rfc8926)) is a network encapsulation protocol that encapsulates the original packet with additional metadata. This additional metadata helps to enable flexible and extensible network virtualization.

The following diagram shows the header format of a GENEVE packet.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |Ver|  Opt len  |O|C|   Rsvd.   |         Protocol type         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |        Virtual network identifier (VNI)       |     Rsvd.     |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the GENEVE header fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Ver | The version of the GENEVE protocol. The only supported version is zero (0). For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 2-bits  
Opt len | The length of the option fields, expressed in 4-byte multiples, not including the 8-byte fixed tunnel header. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 6-bits  
O | The control packet bit. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 1-bit  
C | The critical options bit. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 1-bit  
Rsvd | Reserved field, which must be zero (0) on transmission and must be ignored on receipt. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 6-bits  
Protocol type | The protocol type allows for any ethertype, however, Network Security Integration only allows IPv4 (`0x0800`) or IPv6 (`0x86DD`). | 16-bits  
Virtual Network Identifier (VNI) | A unique identifier for a virtual network element. Network Security Integration does not populate this field, which means the VNI is set to zero (0). For more information, see Out-of-band integration GENEVE. | 24-bits  
Rsvd | Reserved field, which must be zero (0) on transmission and must be ignored on receipt. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 8-bits  
  
## Google Cloud-specific GENEVE options

The GENEVE header uses a [Type-Length-Value (TLV)](https://en.wikipedia.org/wiki/Type%e2%80%93length%e2%80%93value) format for its options. This means that each option is encoded with a type identifier, a length field indicating the size of the value, and the value itself. This format allows for flexibility and extensibility, as new options can be added without disrupting existing implementations. The following sections describe the order and number of options. Note that the number and order of options will vary as the product evolves. Therefore, to ensure forward-compatibility for your device implementation, parse the GENEVE header based on the TLV fields.

The GENEVE options specific to Google Cloud are as follows:

  * Network ID (network cookie)
  * Endpoint ID (endpoint cookie)
  * Profile ID
  * Timestamp ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Network Stable ID ([Preview](https://cloud.google.com/products#product-launch-stages))



### Network ID

The network ID option, also known as "network cookie", identifies the virtual network associated with GENEVE-encapsulated traffic in Google Cloud. This option is identified by option class `0x0132` (Google) and type `0x01` (Network ID). The option data contains 32-bits, of which the first 28 represent an opaque network ID. The purpose of the remaining 4-bits is described in the following diagram and table.

The following diagram shows the option format in the GENEVE packet.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x01   R|R|R|  Len=1   |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                     Network cookie                    |R|R|T|D|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x01` designates the Network ID option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The network ID payload is 32 bits (4 bytes), so the length for this option is set to 1. | 5-bits  
Network cookie | The opaque network cookie, identifying a virtual network. | 28-bits  
R | Reserved for future implementation. Must be set to zero (0) on transmission and must be ignored on receipt. | 2-bits  
T | Indicates TLS-offload for the encapsulated packet. Not used. | 1-bit  
D | Denotes the direction of the packet. A value of zero (0) signifies an ingress packet and one (1) signifies an egress packet on the mirrored virtual machine (VM). For direct internet egress responses, the network appliance flips this bit from `1` to `0`. | 1-bit  
  
### Endpoint ID

The endpoint ID option, also known as "endpoint cookie", uniquely identifies the capture point, which is a network interface controller on a Google Cloud VM. This option is identified by option class `0x0132` (Google) and type `0x02` (Endpoint ID). The option data is a 128-bit opaque value.

The following diagram shows the option format in the GENEVE packet.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x02   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                                                               +
          |                                                               |
          +                        Endpoint cookie                        +
          |                                                               |
          +                                                               +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x02` designates the Endpoint ID option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the payload in 4-byte increments. The endpoint ID payload is 128 bits (16 bytes), so the length for this option is set to 4. | 5-bits  
Endpoint cookie | An opaque identifier for the capture point (a VM NIC). | 128-bits  
  
### Profile ID

The profile ID option identifies the mirroring [security profile group](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview) that is applied to the traffic. This option is identified by option class `0x0132` (Google) and type `0x03` (Profile ID). The option data is a 64-bit identifier that corresponds to the `data_path_id` field in the security profile group. The target device may enforce security policies based on the profile group identifier.

The following diagram shows the option format in the GENEVE packet.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x03   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Profile ID                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x03` designates the Profile ID option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The profile ID payload is 64 bits (8 bytes), so the length for this option is set to 2. | 5-bits  
Profile ID | The identifier of the mirroring security profile group. | 64-bits  
  
### Timestamp

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The timestamp option indicates the original packet's capture time on the source VM. This option is identified by option class `0x0132` (Google) and type `0x0f` (Timestamp).

**Note:** This option is available only for the [broker mode of mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#oob-modes).

The following diagram shows the option format in the GENEVE packet.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x0f   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Timestamp                           +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x0f` designates the timestamp option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The timestamp payload is 64 bits (8 bytes), so the length for this option is set to 2. | 5-bits  
Timestamp | The capture time of the original packet, represented as nanoseconds since epoch. The nanosecond granularity doesn't guarantee nanosecond accuracy. To understand the specific accuracy Service Level Objective (SLO), refer to the product's documentation. | 64-bits  
  
### Network Stable ID

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Network Stable ID option identifies the mirrored VM's network. This option is identified by option class `0x0132` (Google) and type `0x10` (Network Stable ID).

**Note:** This option is available only for the [broker mode of mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#oob-modes).

The following diagram shows the option format in the GENEVE packet. The Network Stable ID comprises of Project Number and Network ID.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x10   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                       Project Number                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                         Network ID                            +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x10` designates the Network Stable ID option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The network ID payload is 128 bits (16 bytes), so the length for this option is set to 4. | 5-bits  
Network Stable ID | The mirrored VM's network. | 128-bits (64 bits of Project Number and 64 bits of Network ID)  
  
## GENEVE header formats for Network Security Integration

This section describes the GENEVE header formats that are utilized by Network Security Integration services.

### GENEVE packet format over IPv4

The GENEVE packet format encapsulates a compact tunnel header in UDP over IPv4. A small fixed tunnel header provides control information and base-level capabilities and interoperability.

The following diagram shows the GENEVE packet format over IPv4.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |Version|  IHL  |Type of service|          Total length         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |         Identification        |Flags|     Fragment offset     |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Time to live | Proto=17 (UDP)|        Header checksum        |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                         Source address                        |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                      Destination address                      |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the IPv4 header fields that's shown in the preceding diagram:

**Note:** The table describes the IPv4 header fields that are Google Cloud-specific. For information on common IPv4 header fields, see [RFC 8926](https://datatracker.ietf.org/doc/html/rfc8926).Field | Description  
---|---  
Proto=17 (always UDP for GENEVE) | Indicates that the encapsulated payload uses the UDP protocol.  
Source address | The producer subnet's gateway IP address.  
Destination address | The customer-owned load balancer's VIP.  
  
### UDP header

The UDP [RFC 0768](https://datatracker.ietf.org/doc/html/rfc768) header encapsulates data, maintaining the connectionless semantics of ethernet and IP address. It also provides entropy to routers that perform equal cost multipath (ECMP).

The following diagram shows the header format for a Geneve packet encapsulated within a UDP.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |      Source port = <hash>    | Dest port = 6081 (Geneve)|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |           UDP length          |          UDP checksum         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the UDP header fields that's shown in the preceding diagram:

Fields | Description  
---|---  
Source port | An opaque hash over the entire 16-bit range. The value is the same for all packets belonging to a single encapsulated flow (both directions).  
Dest port | The designated destination port number for GENEVE traffic, set to 6081.  
UDP length | The total length of the UDP datagram, including the UDP header and the encapsulated GENEVE packet.  
UDP checksum | The checksum value for the UDP datagram, used for error detection.  
  
## Out-of-band integration

Out-of-band integration uses a GENEVE tunnel to encapsulate and deliver mirrored packets. The collector's internal load balancer virtual IP address (VIP) receives the packets annotated with Google Cloud-specific metadata, such as the network cookie.

out-of-band integration uses the following Google Cloud-specific GENEVE options: network cookie, endpoint cookie, and profile ID. For more information, see  Google Cloud-specific GENEVE options.

The following diagram shows how out-of-band integration uses Google Cloud-specific GENEVE options for the direct mode of mirroring.
    
    
           0                    1                   2                  3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |V=0|  Opt len  |O|C|   Rsvd    |         Protocol type         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |        Virtual network identifier (VNI) = 0   |     Rsvd.     |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x01   |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                     Network cookie                    |R|R|T|D|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x02   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                                                               +
          |                                                               |
          +                        Endpoint cookie                        +
          |                                                               |
          +                                                               +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x03   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Profile ID                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following diagram shows how out-of-band integration uses Google Cloud-specific GENEVE options for the broker mode of mirroring ([Preview](https://cloud.google.com/products#product-launch-stages)).
    
    
           0                    1                   2                  3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |V=0|  Opt len  |O|C|   Rsvd    |         Protocol type         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |        Virtual network identifier (VNI) = 0   |     Rsvd.     |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x01   |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                     Network cookie                    |R|R|T|D|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x02   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                                                               +
          |                                                               |
          +                        Endpoint cookie                        +
          |                                                               |
          +                                                               +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x03   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Profile ID                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x0f   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Timestamp                           +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x10   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                         Project Number                        +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Network ID                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

**Note:** The `Opt len` in the preceding diagram represents the length of the option fields in 4-byte multiples. This length doesn't include the 8-byte fixed tunnel header. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields%22).

## In-band integration

In-band integration uses a GENEVE tunnel to encapsulate and deliver intercepted packets. The producer's internal load balancer virtual IP address (VIP) receives the packets annotated with Google Cloud-specific metadata, such as the network cookie.

in-band integration uses the following Google Cloud-specific GENEVE options: network cookie, endpoint cookie, and profile ID. For more information, see Google Cloud-specific GENEVE options.

in-band integration supports packet reinjection to the original endpoint using a logical bidirectional GENEVE tunnel, which consists of two unidirectional GENEVE tunnels. After the producer network appliance intercepts and inspects a packet, it can either drop the packet or reinject it.

The reinjection behavior depends on the integration deployment model:

  * **Standard in-band reinjection** :

For internal and inbound traffic, the network appliance inspects and reinjects the original packet back to the consumer network. During reinjection, the appliance does the following:

    * Re-encapsulates the original packet using the original GENEVE header (same options).
    * Preserves the Direction bit (`D`) in the Network ID option as received.
    * Swaps the source and destination addresses in the outer IP header.
    * Validates that the packet checksums are correct.
  * **Direct internet egress response reinjection** :

When configured for [direct internet egress](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview#direct-internet-egress), the network appliance sends the inspected outbound packet directly to the internet and reinjects the internet response packet back to the consumer VM. During reinjection, the appliance does the following:

    * Encapsulates the response packet received from the internet using GENEVE, including the options from the original outbound packet.
    * Flips the Direction bit (`D`) in the Network ID option from `1` (egress) to `0` (ingress).
    * Validates that the packet checksums are correct.



The following diagram shows how Google Cloud-specific GENEVE options are used in in-band integration.
    
    
           0                    1                   2                  3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |V=0|  Opt len  |O|C|   Rsvd    |         Protocol type         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |        Virtual network identifier (VNI) = 0   |     Rsvd.     |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |   Type=0x01   |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                     Network Cookie                    |R|R|T|D|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |   Type=0x02   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                                                               +
          |                                                               |
          +                        Endpoint Cookie                        +
          |                                                               |
          +                                                               +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |   Type=0x03   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Profile ID                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

**Note:** The `Opt len` in the preceding diagram represents the length of the option fields in 4-byte multiples. This length doesn't include the 8-byte fixed tunnel header. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields%22).

## GENEVE encapsulation and MTU requirements

The maximum transmission unit (MTU) is the size, in bytes, of the largest possible IP packet that can fit inside an Ethernet frame, including IP headers, Layer 4 protocol headers, and Layer 4 data. For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

In Google Cloud networks, the MTU allowed is 8588 bytes. However, for Network Security Integration, 308 bytes need to be retained for the GENEVE encapsulation overhead. This retention need has implications for both consumer and producer networks:

  * **Consumer network MTU** : The MTU for the consumer network must not be more than 8588 bytes. This limit ensures that there's enough space for the GENEVE overhead without exceeding the maximum MTU.

  * **Producer network MTU** : The MTU for the producer network must be at least 396 bytes more than the consumer network MTU. This allowance accommodates the additional GENEVE encapsulation.




If there aren't enough MTU limits to accommodate the GENEVE encapsulation, the packet can be dropped. This can happen either at the virtual network level or in the VM's operating system.

## What's next

  * [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)
  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
