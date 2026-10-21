---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/supported-ike-ciphers/
title: Supported IKE ciphers \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:56.153964+00:00
---

# Supported IKE ciphers  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/supported-ike-ciphers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Supported IKE ciphers Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped VPN supports the following ciphers and configuration parameters for peer VPN gateways.

## Proposal order

GDC VPN can act as an initiator or a responder to IKE requests depending on the origin of traffic when a new security association (SA) is needed.

When GDC VPN initiates a VPN connection, GDC VPN proposes the algorithms in the order shown in the supported cipher tables for each cipher role. The peer VPN gateway receiving the proposal selects an algorithm.

If the peer VPN gateway initiates the connection, then GDC VPN selects a cipher from the proposal by using the same order shown in the table for each cipher role.

Depending on which side is the initiator or the responder, the selected cipher can be different. For example, the selected cipher might even change over time as new security associations (SAs) are created during key rotation.

To prevent frequent changes in cipher selection, configure your peer VPN gateway to propose and accept only one cipher for each cipher role. This cipher must be supported by both GDC air-gapped VPN and your peer VPN gateway. Don't provide a list of ciphers for each cipher role. This best practice ensures that both sides of your GDC air-gapped VPN tunnel always select the same IKE cipher during IKE negotiation.

## IKE fragmentation

GDC VPN supports IKE fragmentation as described by the IKEv2 fragmentation protocol: <https://www.rfc-editor.org/rfc/rfc7383>.

For best results, Google recommends that you enable IKE fragmentation, if it is not already enabled, on your peer VPN gateway.

If you don't have IKE fragmentation enabled, IKE packets from GDC to the peer VPN gateway that are larger than the gateway MTU are dropped.

Some IKE messages can't be fragmented, including the following messages:

  * `IKE_SA_INIT`
  * `IKE_SESSION_RESUME`



For more information, see the Limitations section in <https://www.rfc-editor.org/rfc/rfc7383>.

## Supported cipher tables

These supported cipher tables provide the rules for substituting characters or groups of characters during the encryption and decryption processes:

### Phase 1

Cipher role | Cipher | Notes  
---|---|---  
Encryption & Integrity | 

  * AES-GCM-16-256

| In this list, the first number is the size of the ICV parameter in _bytes (octets)_ , and the second is the key length in _bits_. Some documentation might express the ICV parameter (the first number) in bits instead (8 becomes 64, 12 becomes 96, and 16 becomes 128).  
Pseudo-Random Function (PRF) | 

  * PRF-HMAC-SHA2-512
  * PRF-HMAC-SHA2-384
  * PRF-HMAC-SHA2-256

| Many devices don't require an explicit PRF setting.  
Diffie-Hellman (DH) | 

  * MODP-4096
  * MODP-3072
  * MODP-2048
  * MODP-1536

|   
Phase 1 lifetime | 36,000 seconds (10 hours) |   
  
### Phase 2

Cipher role | Cipher | Notes  
---|---|---  
Encryption & Integrity | 

  * AES-GCM-16-256

| In this list, the first number is the size of the ICV parameter in _bytes (octets)_ , and the second is the key length in _bits_. Some documentation might express the ICV parameter (the first number) in bits instead (8 becomes 64, 12 becomes 96, and 16 becomes 128).  
Pseudo-Random Function (PRF) | 

  * PRF-HMAC-SHA2-512
  * PRF-HMAC-SHA2-384
  * PRF-HMAC-SHA2-256

| Many devices don't require an explicit PRF setting.  
Diffie-Hellman (DH) | 

  * MODP-4096
  * MODP-3072
  * MODP-2048
  * MODP-1536

|   
Phase 2 lifetime | 10,800 seconds (3 hours) |   
  
## Configure IKE

You can configure IKE on your peer VPN gateway for dynamic, route-based, and policy-based routing.

GDC VPN tunnels must use IKE v2 to support IPv6 traffic.

To configure the peer VPN gateway and tunnel for IKE, use the parameters in the following table:

**For IKEv1 and IKEv2**

Setting | Value  
---|---  
IPsec Mode | ESP+Auth Tunnel mode (Site-to-Site)  
Auth Protocol | `psk`  
Shared Secret | Also known as an IKE pre-shared key. Choose a strong password by following [these guidelines](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret). The pre-shared key is sensitive because it allows access into your network.  
Start | `auto` (if the peer device drops, it should automatically restart the connection)  
PFS (Perfect Forward Secrecy) | `on`  
DPD (Dead Peer Detection) | Recommended: `Aggressive`. DPD detects when the VPN restarts and uses alternate tunnels to route traffic.  
INITIAL_CONTACT  
(sometimes called `uniqueids`) | Recommended: `on` (sometimes called `restart`). Purpose: detect restarts faster so that perceived downtime is reduced.  
TSi (Traffic Selector - Initiator) | **Subnet networks:** the ranges specified by the `--local-traffic-selector` flag. If `--local-traffic-selector` is not specified because the VPN is in an auto mode VPC network and is announcing only the gateway's subnet, then that subnet range is used. **Legacy networks:** the range of the network.  
TSr (Traffic Selector - Responder) | **IKEv2:** The destination ranges of all the routes that have `--next-hop-vpn-tunnel` set to this tunnel. **IKEv1:** Arbitrarily, the destination range of one of the routes that has `--next-hop-vpn-tunnel` set to this tunnel.  
MTU | The maximum transmission unit (MTU) of the peer VPN device must not exceed 1460 bytes. Enable pre-fragmentation on your device so that packets are fragmented first and then encapsulated.  
  
**Additional parameters for IKEv1 only**

Setting | Value  
---|---  
IKE/ISAKMP | `aes128-sha1-modp1024`  
ESP | `aes128-sha1`  
PFS Algorithm | Group 2 (`MODP_1024`)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
