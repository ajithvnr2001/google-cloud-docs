---
url: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/geneve/
title: Understand GENEVE format \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:48.563479+00:00
---

# Understand GENEVE format  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/geneve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand GENEVE format

**Preview — ULL Packet Mirroring for exchange participants**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

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
Protocol type | The protocol type allows for ethertype: IPv4 (`0x0800`) or IPv6 (`0x86DD`). | 16-bits  
Virtual Network Identifier (VNI) | A unique identifier for a virtual network element. The VNI is set to zero (0). For more information, see GENEVE options. | 24-bits  
Rsvd | Reserved field, which must be zero (0) on transmission and must be ignored on receipt. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields). | 8-bits  
  
## GENEVE options for Packet Mirroring in ULL VPC networks

The GENEVE header uses a [Type-Length-Value (TLV)](https://en.wikipedia.org/wiki/Type%e2%80%93length%e2%80%93value) format for its options. Each option is encoded with a type identifier, a length field that indicates the value's size, and the value itself. This format provides flexibility and extensibility, allowing new options to be added without disrupting existing implementations. The following sections describe the options. Because the number and order of options might change, parse the GENEVE header based on the TLV fields to ensure forward-compatibility for your device implementation.

The GENEVE options specific to ULL Packet Mirroring are as follows:

  * Network ID (Network cookie)
  * Timestamp
  * Network stable ID
  * Primary IP Address



### Network ID

The network ID option, also known as "network cookie", identifies the virtual network associated with GENEVE-encapsulated traffic in ULL Packet Mirroring. This option is identified by option class `0x0132` (Google) and type `0x1` (Network ID).

For ULL Packet Mirroring, the network cookie is set to zero (0). The option data contains 32 bits; the first 31 bits are reserved and the final bit indicates the direction of the original packet.

ULL Packet Mirroring uses a modified version of the network ID option. In this version, all bits except the direction and reserved bits are set to 0. For more information about the capture point, see Network stable ID.

The following diagram shows the option format in the GENEVE packet.
    
    
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |    Type=01    |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                            Reserved                         |D|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x1` designates the Network ID option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The network ID payload is 32 bits (4 bytes), so the length for this option is set to 1. | 5-bits  
Reserved | Must be set to zero (0) on transmission and must be ignored on receipt. | 31-bits  
D | Indicates the direction of the original packet. Zero (0) indicates ingress and one (1) indicates an egress packet on the original mirrored resource. | 1-bit  
  
### Timestamp

The timestamp option indicates the original packet capture time on the capture point (the Compute Engine instance where the packet was captured or mirrored). This option is identified by option class `0x0132` (Google) and type `0x0f` (Timestamp).

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
Timestamp | The capture time of the original packet, represented as nanoseconds since epoch. The nanosecond granularity doesn't guarantee nanosecond accuracy. | 64-bits  
  
### Network stable ID

The Network stable ID option identifies the mirrored instance's network. This option is identified by option class `0x0132` (Google) and type `0x10` (Network stable ID).

The following diagram shows the option format in the GENEVE packet. The Network stable ID comprises a project number and a network ID.
    
    
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
Type | Identifies the type of the option within a class. The value `0x10` designates the Network stable ID option. For more information, see [Tunnel Options](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-options). | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The network ID payload is 64 bits (8 bytes), so the length for this option is set to 4. | 5-bits  
Project number | Project number of Google Cloud project. | 64-bits  
Network ID | The ID of ULL VPC network. | 64-bits  
  
### Primary IP Address

The Primary IP Address option identifies the IP address of the capture point (the Compute Engine instance where the packet was captured or mirrored). This option is identified by option class `0x0132` (Google) and type `0x11` (Primary IP Address).

The following diagram shows the option format in the GENEVE packet.
    
    
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option class=0x0132 (Google) |   Type=0x11   |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                       Primary IP Address                      |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the option fields shown in the preceding diagram:

Field | Description | Field length  
---|---|---  
Option class | Identifies the organization or entity that has defined the option. The value `0x0132` designates Google as the defining entity. | 16-bits  
Type | Identifies the type of the option within a class. The value `0x11` designates the Primary IP Address option. | 8-bits  
R | The option control flags reserved for future use. These bits must be zero (0) on transmission and must be ignored on receipt. | 3-bits  
Len | The length of the option's payload in 4-byte increments. The IP address payload is 32 bits (4 bytes), so the length for this option is set to 1. | 5-bits  
Primary IP Address | The primary IP address of the capture point (the Compute Engine instance NIC where the packet was captured or mirrored). | 32-bits  
  
## GENEVE header formats

This section describes the GENEVE header formats used by Packet Mirroring for ULL VPC networks.

### IPv4 header

The GENEVE packet format encapsulates a compact tunnel header in UDP over IPv4. A small fixed tunnel header provides control information and base-level capabilities and interoperability.

The following diagram shows IPv4 header fields for the GENEVE packet.
    
    
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
       

The following table describes the Google Cloud-specific IPv4 header fields shown in the preceding diagram. For information about common IPv4 header fields, see [RFC 8926](https://datatracker.ietf.org/doc/html/rfc8926).

Field | Description  
---|---  
Proto=17 (always UDP for GENEVE) | Indicates that the encapsulated payload uses the UDP protocol.  
Source address | The local subnet's gateway IP address.  
Destination address | The customer-owned load balancer's VIP.  
  
### UDP header

The UDP [RFC 0768](https://datatracker.ietf.org/doc/html/rfc768) header encapsulates data while maintaining the connectionless semantics of Ethernet and IP addresses. It also provides entropy to routers that perform equal cost multipath (ECMP).

The following diagram shows the header format for a GENEVE packet encapsulated within a UDP.
    
    
           0                   1                   2                   3
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |      Source port = <hash>     |   Dest port = 6081 (Geneve)   |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |           UDP length          |          UDP checksum         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The following table describes the UDP header fields shown in the preceding diagram:

Field | Description  
---|---  
Source port | An opaque hash over the entire 16-bit range. The value is the same for all packets belonging to a single encapsulated flow (both directions).  
Dest port | The designated destination port number for GENEVE traffic, set to 6081.  
UDP length | The total length of the UDP datagram, including the UDP header and the encapsulated GENEVE packet.  
UDP checksum | The checksum value for the UDP datagram, used for error detection.  
  
### GENEVE options

The Google Cloud-specific GENEVE options used in Packet Mirroring for ULL VPC networks are network cookie, timestamp, network stable ID, primary IP address, and fair order processing timestamp. For more information, see GENEVE options for Packet Mirroring in ULL VPC networks.

The following diagram shows how Google Cloud-specific GENEVE options are used in Packet Mirroring for ULL VPC networks.
    
    
           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |    Type=01    |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                          Network Cookie                     |D|
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |   Type=0x0f   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Timestamp                           +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |    Type=0x10   |R|R|R|  Len=4  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                         Project Number                        +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                           Network ID                          +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |   Type=0x11   |R|R|R|  Len=1  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                       Primary IP Address                      |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |  Option Class=0x0132 (Google) |   Type=0x13   |R|R|R|  Len=2  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                                                               |
          +                Fair order processing timestamp                +
          |                                                               |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       

The `Opt len` in the preceding diagram represents the length of the option fields in 4-byte multiples. This length doesn't include the 8-byte fixed tunnel header. For more information, see [Tunnel Header Fields](https://datatracker.ietf.org/doc/html/rfc8926#name-tunnel-header-fields).

## GENEVE encapsulation and MTU requirements

The maximum transmission unit (MTU) is the size, in bytes, of the largest possible IP packet that can fit inside an Ethernet frame, including IP headers, Layer 4 protocol headers, and Layer 4 data. For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

ULL VPC networks have a maximum MTU of 1500 bytes. However, ULL Packet Mirroring requires 308 bytes for GENEVE encapsulation overhead. To ensure that mirrored traffic reaches your collector instances without fragmentation, the network where your collector resides must have an MTU of at least 1808 bytes (1500 bytes for standard traffic plus 308 bytes for GENEVE encapsulation overhead).

If the MTU limits are insufficient to accommodate the GENEVE encapsulation, packets might be dropped. This can occur at the virtual network level or in the operating system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
