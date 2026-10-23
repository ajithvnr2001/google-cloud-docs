---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers/
title: Supported IKE ciphers \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:24.320920+00:00
---

# Supported IKE ciphers  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Supported IKE ciphers Stay organized with collections  Save and categorize content based on your preferences. 

Cloud VPN supports the following ciphers and configuration parameters for peer VPN devices or VPN services. Cloud VPN automatically negotiates the connection as long as the peer side uses a supported Internet Key Exchange (IKE) cipher setting.

For configuration instructions, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).

Cloud VPN operates in IPsec ESP Tunnel Mode.

The following IKE ciphers are supported for Classic VPN and HA VPN.

**Note:** IPv6 traffic, which is only supported by HA VPN, requires IKEv2.

IPv6 address support for HA VPN gateway interfaces is in [Preview](https://cloud.google.com/products#product-launch-stages).

## Proposal order

Cloud VPN can act as an initiator or a responder to IKE requests depending on the origin of traffic when a new security association is needed.

When Cloud VPN initiates a VPN connection, Cloud VPN proposes the [cipher algorithms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#configure-ciphers) configured in the Cloud VPN tunnel. If you have not configured the cipher algorithms, then the Cloud VPN tunnel proposes the cipher algorithms in the order shown in the [supported cipher tables](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#tables) for each cipher role. The peer side receiving the proposal selects an algorithm.

If the peer side initiates the connection, then Cloud VPN selects a cipher from the proposal by using the same order as configured or shown in the table for each cipher role.

Depending on which side is the initiator or the responder, the selected cipher can be different. For example, the selected cipher might even change over time as new security associations (SAs) are created during key rotation. Because a change in cipher selection can impact important tunnel characteristics such as performance or MTU, use a stable cipher selection. For more information about MTU, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

To prevent frequent changes in cipher selection, configure your peer VPN gateway and the Cloud VPN tunnel to propose and accept only one cipher for each cipher role. This cipher must be supported by both Cloud VPN and your peer VPN gateway. Do not provide a list of ciphers for each cipher role. This best practice ensures that both sides of your Cloud VPN tunnel always select the same IKE cipher during IKE negotiation.

Cloud Location Finder helps you identify the closest Google Cloud regions and zones to your physical locations worldwide. By using Cloud Location Finder, you can make informed decisions about which Google Cloud region to deploy your Cloud VPN gateways in, potentially optimizing for latency, geographic location, and carbon energy usage. For more information, see the [Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/overview) documentation.

For HA VPN tunnel pairs, configure both HA VPN tunnels on your peer VPN gateway to use the same cipher and IKE Phase 2 lifetime values.

**Note:** You can configure cipher algorithms for HA VPN topologies that connect VPC networks. If you don't configure cipher algorithms, then the HA VPN gateways auto-negotiate the cipher consistently no matter which side initiates the connection.

## IKE fragmentation

Cloud VPN supports IKE fragmentation as described by the IKEv2 fragmentation protocol ([RFC 7383](https://www.rfc-editor.org/rfc/rfc7383)).

For best results, Google recommends that you enable IKE fragmentation, if it is not already enabled, on your peer VPN device.

If you don't have IKE fragmentation enabled, IKE packets from Google Cloud to the peer VPN device that are larger than the gateway MTU are dropped.

Some IKE messages can't be fragmented, including the following messages:

  * `IKE_SA_INIT`
  * `IKE_SESSION_RESUME`



For more information, see the [Limitations section in RFC 7383](https://www.rfc-editor.org/rfc/rfc7383#section-2.2).

## Supported cipher tables

The following sections list the supported ciphers for Cloud VPN.

**Note:** You will notice identical entries in the PRF, DH Group, and PFS Algorithm lists for both AEAD and Non-AEAD configurations. This is expected. These parameters handle the initial key exchange and key derivation, which are independent of the final encryption mode. The difference between an AEAD and Non-AEAD suite depends on the Encryption & Integrity ciphers.

### IKEv2 ciphers that use AEAD

The following ciphers use [authenticated encryption with associated data (AEAD)](https://wikipedia.org/wiki/Authenticated_encryption).

#### Phase 1

Cipher role | Cipher name | Configuration value  
(case-sensitive) | Notes  
---|---|---|---  
Encryption & Integrity | 

  * AES-GCM-16-128
  * AES-GCM-16-192
  * AES-GCM-16-256

| 

  * AES-GCM-16-128
  * AES-GCM-16-192
  * AES-GCM-16-256

| In this list, the first number is the size of the ICV parameter in _bytes (octets)_ , and the second is the key length in _bits_. Some documentation might express the ICV parameter (the first number) in bits instead (8 becomes 64, 12 becomes 96, and 16 becomes 128).  
Pseudo-Random Function (PRF) | 

  * PRF-AES128-XCBC
  * PRF-AES128-CMAC
  * PRF-HMAC-SHA1
  * PRF-HMAC-MD5
  * PRF-HMAC-SHA2-256
  * PRF-HMAC-SHA2-384
  * PRF-HMAC-SHA2-512

| 

  * PRF-AES128-XCBC
  * PRF-AES128-CMAC
  * PRF-HMAC-SHA1
  * PRF-HMAC-MD5
  * PRF-HMAC-SHA2-256
  * PRF-HMAC-SHA2-384
  * PRF-HMAC-SHA2-512

| Many devices don't require an explicit PRF setting.  
Diffie-Hellman (DH) | 

  * modp_2048 (Group 14)
  * modp_2048_224 (modp_2048s224)
  * modp_2048_256 (modp_2048s256)
  * modp_1536 (Group 5)
  * modp_3072 (Group 15)
  * modp_4096 (Group 16)
  * modp_8192 (Group 18)
  * modp_1024 (Group 2)
  * modp_1024_160 (modp_1024s160)
  * ecp_256 (Group 19)
  * ecp_384 (Group 20)
  * ecp_521 (Group 21)
  * curve_25519 (Group 31)

| 

  * Group-14
  * modp-2048-224
  * modp-2048-256
  * Group-5
  * Group-15
  * Group-16
  * Group-18
  * Group-2
  * modp-1024-160
  * Group-19
  * Group-20
  * Group-21
  * Group-31

| The modp_8192 cipher is not supported for HA VPN gateways with IPv6 interfaces (`gatewayIpVersion=IPv6`).  
Phase 1 lifetime | 36,000 seconds (10 hours) |  | When you generate a configuration template for a peer VPN device, the template might use shorter lifetimes, such as 28,800 seconds, for Phase 1 for better compatibility with the default settings of most third-party VPN vendors. As a best practice, don't change the generated template values unless your third-party vendor explicitly recommends a different configuration.  
  
#### Phase 2

Cipher role | Cipher name | Configuration value  
(case-sensitive) | Notes  
---|---|---|---  
Encryption & Integrity | 

  * AES-GCM-16-128
  * AES-GCM-16-256
  * AES-GCM-16-192

| 

  * AES-GCM-16-128
  * AES-GCM-16-256
  * AES-GCM-16-192

|  The first number in each algorithm is the size of the ICV parameter in _bytes (octets)_ , and the second is its key length in _bits_. Some documentation might express the ICV parameter (the first number) in bits instead (8 becomes 64, 12 becomes 96, 16 becomes 128).  
PFS Algorithm (required) | 

  * modp_2048 (Group 14)
  * modp_2048_224 (modp_2048s224)
  * modp_2048_256 (modp_2048s256)
  * modp_1536 (Group 5)
  * modp_3072 (Group 15)
  * modp_4096 (Group 16)
  * modp_8192 (Group 18)
  * modp_1024 (Group 2)
  * modp_1024_160 (modp_1024s160)
  * ecp_256 (Group 19)
  * ecp_384 (Group 20)
  * ecp_521 (Group 21)
  * curve_25519 (Group 31)

| 

  * Group-14
  * modp-2048-224
  * modp-2048-256
  * Group-5
  * Group-15
  * Group-16
  * Group-18
  * Group-2
  * modp-1024-160
  * Group-19
  * Group-20
  * Group-21
  * Group-31

| The modp_8192 cipher is not supported for HA VPN gateways with IPv6 interfaces (`gatewayIpVersion=IPv6`).  
Diffie-Hellman (DH) | Refer to Phase 1. | Refer to Phase 1. | If your VPN gateway requires DH settings for Phase 2, use the same settings that you used for Phase 1.  
Phase 2 lifetime | 10,800 seconds (3 hours) |  | When you generate a configuration template for a peer VPN device, the template might use shorter lifetimes, such as 3,600 seconds for Phase 2 for better compatibility with the default settings of most third-party VPN vendors. As a best practice, don't change the generated template values unless your third-party vendor explicitly recommends a different configuration.  
  
### IKEv2 ciphers that don't use AEAD

#### Phase 1

Cipher role | Cipher name | Configuration value  
(case-sensitive) | Notes  
---|---|---|---  
Encryption | 

  * AES-CBC-128
  * AES-CBC-192
  * AES-CBC-256
  * 3DES-CBC

| 

  * AES-CBC-128
  * AES-CBC-192
  * AES-CBC-256
  * 3DES-CBC

|   
Integrity | 

  * AES-XCBC-96
  * AES-CMAC-96
  * HMAC-SHA1-96
  * HMAC-MD5-96
  * HMAC-SHA2-256-128
  * HMAC-SHA2-384-192
  * HMAC-SHA2-512-256

| 

  * AES-XCBC-96
  * AES-CMAC-96
  * HMAC-SHA1-96
  * HMAC-MD5-96
  * HMAC-SHA2-256-128
  * HMAC-SHA2-384-192
  * HMAC-SHA2-512-256

|  Documentation for your on-premises VPN gateway might use a slightly different name for the algorithm. For example, `HMAC-SHA2-512-256` might be referred to as `SHA2-512` or `SHA-512`, dropping the truncation length number and other extraneous information.  
Pseudo-Random Function (PRF) | 

  * PRF-AES-128-XCBC
  * PRF-AES-128-CMAC
  * PRF-HMAC-SHA1
  * PRF-HMAC-MD5
  * PRF-HMAC-SHA2-256
  * PRF-HMAC-SHA2-384
  * PRF-HMAC-SHA2-512

| 

  * PRF-AES128-XCBC
  * PRF-AES128-CMAC
  * PRF-HMAC-SHA1
  * PRF-HMAC-MD5
  * PRF-HMAC-SHA2-256
  * PRF-HMAC-SHA2-384
  * PRF-HMAC-SHA2-512

| Many devices don't require an explicit PRF setting.  
Diffie-Hellman (DH) | 

  * modp_2048 (Group 14)
  * modp_2048_224 (modp_2048s224)
  * modp_2048_256 (modp_2048s256)
  * modp_1536 (Group 5)
  * modp_3072 (Group 15)
  * modp_4096 (Group 16)
  * modp_8192 (Group 18)
  * modp_1024 (Group 2)
  * modp_1024_160 (modp_1024s160)
  * ecp_256 (Group 19)
  * ecp_384 (Group 20)
  * ecp_521 (Group 21)
  * curve_25519 (Group 31)

| 

  * Group-14
  * modp-2048-224
  * modp-2048-256
  * Group-5
  * Group-15
  * Group-16
  * Group-18
  * Group-2
  * modp-1024-160
  * Group-19
  * Group-20
  * Group-21
  * Group-31

| The modp_8192 cipher is not supported for HA VPN gateways with IPv6 interfaces (`gatewayIpVersion=IPv6`).  
Phase 1 lifetime | 36,000 seconds (10 hours) |  |   
  
#### Phase 2

Cipher role | Cipher name | Configuration value  
(case-sensitive) | Notes  
---|---|---|---  
Encryption | 

  * AES-CBC-128
  * AES-CBC-256
  * AES-CBC-192

| 

  * AES-CBC-128
  * AES-CBC-256
  * AES-CBC-192

|   
Integrity | 

  * HMAC-SHA2-256-128
  * HMAC-SHA2-512-256
  * HMAC-SHA1-96

| 

  * HMAC-SHA2-256-128
  * HMAC-SHA2-512-256
  * HMAC-SHA1-96

|  Documentation for your on-premises VPN gateway might use a slightly different name for the algorithm. For example, `HMAC-SHA2-512-256` might be referred to as `SHA2-512` or `SHA-512`, dropping the truncation length number and other extraneous information.  
PFS Algorithm (required) | 

  * modp_2048 (Group 14)
  * modp_2048_224 (modp_2048s224)
  * modp_2048_256 (modp_2048s256)
  * modp_1536 (Group 5)
  * modp_3072 (Group 15)
  * modp_4096 (Group 16)
  * modp_8192 (Group 18)
  * modp_1024 (Group 2)
  * modp_1024_160 (modp_1024s160)
  * ecp_256 (Group 19)
  * ecp_384 (Group 20)
  * ecp_521 (Group 21)
  * curve_25519 (Group 31)

| 

  * Group-14
  * modp-2048-224
  * modp-2048-256
  * Group-5
  * Group-15
  * Group-16
  * Group-18
  * Group-2
  * modp-1024-160
  * Group-19
  * Group-20
  * Group-21
  * Group-31

| The modp_8192 cipher is not supported for HA VPN gateways with IPv6 interfaces (`gatewayIpVersion=IPv6`).  
Diffie-Hellman (DH) | Refer to Phase 1. | Refer to Phase 1. | If your VPN gateway requires DH settings for Phase 2, use the same settings that you used for Phase 1.  
Phase 2 lifetime | 10,800 seconds (3 hours) |  |   
  
### IKEv1 ciphers

#### Phase 1

Cipher role | Cipher  
---|---  
Encryption | AES-CBC-128  
Integrity | HMAC-SHA1-96  
Pseudo-Random Function (PRF)1 | PRF-SHA1-96  
Diffie-Hellman (DH) | modp_1024 (Group 2)  
Phase 1 lifetime | 36,600 seconds (10 hours, 10 minutes)  
  
1For more information about PRF in IKEv1, see [RFC 2409](https://tools.ietf.org/html/rfc2409#page-7). 

#### Phase 2

Cipher role | Cipher  
---|---  
Encryption | AES-CBC-128  
Integrity | HMAC-SHA1-96  
PFS Algorithm (required) | modp_1024 (Group 2)  
Diffie-Hellman (DH) | If you need to specify DH for your VPN gateway, use the same setting that you used for Phase 1.  
Phase 2 lifetime | 10,800 seconds (3 hours)  
  
### IKE SA and IPsec SA lifetimes

To establish an encrypted VPN tunnel, Cloud VPN and your peer VPN gateway negotiate security associations (SAs) with defined lifetimes.

  * Peer VPN device configuration templates are downloadable configuration files available in the Google Cloud console. They contain vendor-specific configuration commands, such as for Cisco, Palo Alto Networks, or Juniper, to simplify the setup of your peer gateway.

  * Depending on the peer device vendor, the downloadable templates might generate shorter lifetime values than the Cloud VPN defaults to match vendor-recommended standards.




Use the following table to synchronize your lifetime settings. Ensure that the lifetime values configured on your peer VPN gateway match the Cloud VPN values exactly to prevent tunnel drops.

Security Association (SA) phase | Google Cloud VPN default | UI configuration template value | Best practice  
---|---|---|---  
**Phase 1 (IKE SA) Lifetime** | `36000` seconds (10 hours) | `28800` or `36000` seconds (depending on vendor) | Ensure the peer gateway value matches Cloud VPN exactly. See [VPN Best Practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices) for details.  
**Phase 2 (IPsec/Child SA) Lifetime** | `10800` seconds (3 hours) | `3600` or `10800` seconds (depending on vendor) | Ensure the peer gateway value matches the Cloud VPN value exactly. For more information, see [VPN Best Practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices) for details.  
  
## What's next

  * To learn about the basic concepts of Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
