---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations/
title: MTU considerations \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:51.994750+00:00
---

# MTU considerations  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  MTU considerations Stay organized with collections  Save and categorize content based on your preferences. 

The [maximum transmission unit (MTU)](https://wikipedia.org/wiki/Maximum_transmission_unit) is the size, in bytes, of the largest packet supported by a network layer protocol, including both headers and IP packet payload.

Network packets sent over a VPN tunnel are encrypted and then encapsulated in an outer packet so that they can be routed. Cloud VPN tunnels use [IPsec and ESP](https://wikipedia.org/wiki/IPsec#Encapsulating_Security_Payload) for encryption and encapsulation. Because the encapsulated inner packet must itself fit within the MTU of the outer packet, its maximum IP packet payload must be smaller.

HA VPN over Cloud Interconnect doesn't support jumbo frames for encrypted VLAN attachments.

## Packet encapsulation and processing

To successfully transmit packets using Cloud VPN tunnels, you must enable prefragmentation on your [peer](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#peer-definition) VPN gateway so that packets that it sends are fragmented _before_ they are encrypted and encapsulated.

**Important:** Cloud VPN does _not_ support fragmentation of packets _after_ encapsulation.

As a Cloud VPN tunnel processes packets bound for your peer network:

  * Cloud VPN uses MSS clamping to ensure that TCP packets fit within the payload MTU _before_ IPsec encapsulation.

  * For other protocols, Cloud VPN processes packets before IPsec encapsulation as follows:

    * If the packet's `DF` bit is set, and the Cloud VPN gateway determines that fragmentation is necessary, the Cloud VPN gateway sends an ICMP Fragmentation Needed (IPv4) or ICMPv6 Packet Too Big message to the sender. Delivery of ICMP or ICMPv6 messages requires that you configure ingress allow firewall rules applicable to the Compute Engine VM sender – one rule to allow ICMP ingress, and, for dual-stack VMs, another rule to allow ICMPv6 ingress.
    * If the packet's `DF` bit is not set, and the Cloud VPN gateway and the packet exceeds the payload MTU, the Cloud VPN gateway _attempts_ to deliver the packet. The packet _might_ be dropped by a subsequent hop after the Cloud VPN tunnel if the packet is too large for the next hop.



For general information about how protocols handle mismatched MTUs, see [Mismatched MTUs, MSS clamping, path MTU discovery](https://docs.cloud.google.com/vpc/docs/mtu#mss-clamping-and-pmtud) in the VPC MTU documentation.

## Gateway MTU versus payload MTU

Cloud VPN differentiates between the [Cloud VPN gateway MTU](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#cloud-vpn-gateway-mtu) and the [Cloud VPN payload MTU](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#cloud-vpn-payload-mtu). The Cloud VPN _gateway MTU_ is:

  * 1460 bytes, for Cloud VPN—both Classic VPN and HA VPN
  * 1440 bytes, for HA VPN over Cloud Interconnect



Configure your peer VPN gateway to use an MTU that matches the corresponding Cloud VPN gateway MTU.

The payload MTU for a Cloud VPN tunnel depends on both of the following factors:

  * The cipher that the tunnel uses
  * The IP stack of the tunnel's gateway interface: IPv4 or IPv6
  * Whether NAT-Traversal (NAT-T) is active



For a given gateway MTU and cipher, the payload MTU of a tunnel on an IPv6 gateway interface is 20 bytes smaller than the payload MTU of a tunnel on an IPv4 gateway interface. Additionally, when NAT-T is active, an extra 8-byte UDP encapsulation header is added, which reduces the payload MTU by an additional 8 bytes. For more information, see Cloud VPN payload MTU values.

## Cloud VPN payload MTU values

The Cloud VPN payload MTU depends on the ciphers chosen in your Cloud VPN connection.

### Payload MTU for AEAD ciphers

The following table shows phase 1 and phase 2 cipher combinations for AEAD ciphers that use one of the following Cloud VPN payload MTUs:

**Important:** These values assume a standard connection without NAT-T. If NAT-T is active on your tunnel, you must subtract an additional 8 bytes from these values to account for the UDP encapsulation overhead.

  * 1406 bytes (or 1398 bytes with NAT-T): for Cloud VPN tunnels on IPv4 gateway interfaces
  * 1386 bytes (or 1378 bytes with NAT-T): for Cloud VPN tunnels on IPv6 gateway interfaces
  * 1386 bytes: for HA VPN over Cloud Interconnect tunnels on IPv4 gateway interfaces
  * 1366 bytes: for HA VPN over Cloud Interconnect tunnels on IPv6 gateway interfaces

Phase 1 | Phase 2  
---|---  
AES-GCM-16-128 | AES-GCM-16-128  
AES-GCM-16-192 | AES-GCM-16-192  
AES-GCM-16-256 | AES-GCM-16-256  
AES-GCM-16-128 | AES-GCM-16-192  
AES-GCM-16-192 | AES-GCM-16-128  
AES-GCM-16-256 | AES-GCM-16-192  
AES-GCM-16-128 | AES-GCM-16-256  
AES-GCM-16-192 | AES-GCM-16-256  
AES-GCM-16-256 | AES-GCM-16-128  
  
### Payload MTU for non-AEAD ciphers

The following table shows phase 1 and phase 2 cipher combinations for non-AEAD ciphers that use one of the following Cloud VPN payload MTUs:

  * 1374 bytes: for Cloud VPN tunnels on IPv4 gateway interfaces
  * 1354 bytes: for Cloud VPN tunnels on IPv6 gateway interfaces
  * 1354 bytes: for HA VPN over Cloud Interconnect tunnels on IPv4 gateway interfaces
  * 1334 bytes: for HA VPN over Cloud Interconnect tunnels on IPv6 gateway interfaces

Phase 1 - Encryption | Phase 1 - Integrity | Phase 2 - Encryption | Phase 2 - Integrity  
---|---|---|---  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-512-256  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-512-256  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-512-256  
  
The following table shows phase 1 and phase 2 cipher combinations for non-AEAD ciphers that use one of the following Cloud VPN payload MTUs:

  * 1390 bytes: for Cloud VPN tunnels on IPv4 gateway interfaces
  * 1370 bytes: for Cloud VPN tunnels on IPv6 gateway interfaces
  * 1370 bytes: for HA VPN over Cloud Interconnect tunnels on IPv4 gateway interfaces
  * 1350 bytes: for HA VPN over Cloud Interconnect tunnels on IPv6 gateway interfaces

Phase 1 - Encryption | Phase 1 - Integrity | Phase 2 - Encryption | Phase 2 - Integrity  
---|---|---|---  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-128 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-192 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA1-96  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-256-128  
AES-CBC-256 | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | AES-XCBC-96 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | AES-XCBC-96 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | AES-XCBC-96 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | AES-CMAC-96 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | AES-CMAC-96 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | AES-CMAC-96 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA1-96 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-MD5-96 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-MD5-96 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-MD5-96 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA256-128 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA384-192 | AES-CBC-256 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-128 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-192 | HMAC-SHA1-96  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA2-256-128  
3DES-CBC | HMAC-SHA512-256 | AES-CBC-256 | HMAC-SHA1-96  
  
## What's next

  * To learn about the basic concepts of Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
