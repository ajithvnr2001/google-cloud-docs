---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/cipher-changes/
title: Cloud VPN cipher changes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:10.316487+00:00
---

# Cloud VPN cipher changes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/cipher-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/vpn/resources)



Send feedback 

#  Cloud VPN cipher changes Stay organized with collections  Save and categorize content based on your preferences. 

To provide enhanced security defaults, Cloud VPN is rolling out changes to the default order of IKE ciphers, so that Cloud VPN prefers more secure cipher algorithms first.

Furthermore, Google is dropping support for DH algorithm group 22. For more information, see Deprecated configurations.

If the new default order of the cipher algorithms causes a new cipher selection and rekey, these changes may disrupt traffic on your Cloud VPN connection.

The rest of this document helps you plan and implement your VPN cipher changes.

## Order modification

When Cloud VPN initiates a VPN connection, a cipher is selected as described in the [Cloud VPN documentation](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers) using the order in the [supported cipher tables](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#tables).

Currently, the ciphers are not ordered based on security. Some less-secure algorithms are listed before more secure algorithms. After Cloud VPN cipher changes are implemented, the Cloud VPN algorithm preferences change so that more secure cipher algorithms are preferred. The cipher order modification is planned to progressively roll out to all of our Cloud VPN gateways.

The following table shows the existing IKEv2 DH algorithm order and the new order:

**Existing IKEv2 DH algorithm order** | **New IKEv2 DH algorithm order**  
---|---  
MODP_2048_BIT | CURVE_25519  
MODP_2048_224 | ECP_256_BIT  
MODP_2048_256 | ECP_384_BIT  
MODP_1536_BIT | ECP_521_BIT  
MODP_3072_BIT | MODP_3072_BIT  
MODP_4096_BIT | MODP_4096_BIT  
MODP_8192_BIT | MODP_6144_BIT  
MODP_1024_BIT | MODP_8192_BIT  
MODP_1024_160 | MODP_2048_BIT  
ECP_256_BIT | MODP_2048_224  
ECP_384_BIT | MODP_2048_256  
ECP_521_BIT | MODP_1536_BIT  
CURVE_25519 | MODP_1024_BIT  
  
The following table shows the existing IKEv2 pseudo-random function algorithm order and the new order:

**Existing IKEv2 pseudo-random function algorithm order** | **New IKEv2 pseudo-random function algorithm order**  
---|---  
PRF_AES128_XCBC | PRF_HMAC_SHA2_256  
PRF_AES128_CMAC | PRF_HMAC_SHA2_384  
PRF_HMAC_SHA1 | PRF_HMAC_SHA2_512  
PRF_HMAC_MD5 | PRF_HMAC_SHA1  
PRF_HMAC_SHA2_256 | PRF_HMAC_MD5  
PRF_HMAC_SHA2_384 | PRF_AES128_CMAC  
PRF_HMAC_SHA2_512 | PRF_AES128_XCBC  
  
The following table shows the existing integrity algorithm order and the new order:

**Existing integrity algorithm order** | **New integrity algorithm order**  
---|---  
AUTH_HMAC_SHA2_256_128 | AUTH_HMAC_SHA2_256_128  
AUTH_HMAC_SHA2_384_192 | AUTH_HMAC_SHA2_384_192  
AUTH_HMAC_SHA2_512_256 | AUTH_HMAC_SHA2_512_256  
AUTH_HMAC_MD5_96 | AUTH_HMAC_SHA1_96  
AUTH_HMAC_SHA1_96 | AUTH_HMAC_MD5_96  
  
The following table shows the existing encryption algorithm order and the new algorithm order:

**Existing encryption algorithm order** | **New encryption algorithm order**  
---|---  
  
ENCR_AES_CBC, 128 |   
ENCR_AES_CBC, 128  
  
ENCR_AES_CBC, 192 |   
ENCR_AES_CBC, 256  
  
ENCR_AES_CBC, 256 |   
ENCR_AES_CBC, 192  
  
You may experience disrupted traffic on your Cloud VPN connection when the changes are implemented due to the new cipher maximum transmission unit (MTU). Specifically, if your peer device chooses a different algorithm than it did previously, traffic disruption can occur due to a decrease in the size of the maximum payload in the encrypted ESP packet. For more information about avoiding traffic disruptions, see Recommendations.

The Cloud VPN payload MTU depends on the selected cipher. The potential disruption only affects traffic that uses the full payload capacity. Any disruption is expected to be transient until the network adapts to the new maximum Cloud VPN payload MTU.

### Deprecated configurations

Cloud VPN is dropping support for Diffie-Hellman (DH) algorithm group 22\. As published in [RFC 8247](https://www.rfc-editor.org/rfc/rfc8247), DH group 22 is no longer considered a strong nor safe algorithm.

If your connection currently uses DH algorithm group 22, you will experience traffic disruption on your Cloud VPN connection when the changes go into effect.

### Supported configurations

Cloud VPN previously added support for DH algorithm groups 19, 20, and 21.

If you want to use algorithms from DH algorithm groups 19, 20, and 21, you can configure your peer VPN gateway to propose and accept the algorithms after the changes go into effect. However, making that change could disrupt traffic over your Cloud VPN connection.

## Recommendations

If you don't enforce DH group 22 and you can tolerate potential temporary traffic disruptions during MTU changes, no further action is required.

To avoid traffic disruptions, we recommend that you configure your peer VPN gateway to propose and accept only one supported cipher for each cipher role. A VPN gateway that proposes and accepts only one supported cipher for each cipher role isn't affected by Google's new cipher algorithm proposal order.

After this change, DH group 22 is no longer supported by Cloud VPN for existing tunnels. If your cipher algorithm proposal set doesn't contain other supported DH groups, your router and Cloud VPN will be unable to establish a VPN tunnel.

For more information about MTU, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

## Billing changes

There are no billing changes for Cloud VPN cipher changes.

## Where to get help

If you have any questions or require assistance, [contact Google Cloud Support](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
