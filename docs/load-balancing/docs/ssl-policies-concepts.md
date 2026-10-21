---
url: https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts/
title: SSL policies overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:36.272357+00:00
---

# SSL policies overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  SSL policies overview Stay organized with collections  Save and categorize content based on your preferences. 

In this document, the term _SSL_ refers to both the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols. The information in this document applies to TLS connections over the TCP transport protocol, which can use any supported version of TLS. For load balancers that use [HTTP/3](https://docs.cloud.google.com/load-balancing/docs/https#QUIC), the underlying transport protocol is QUIC, which uses TLS 1.3 exclusively.

An SSL policy defines the TLS features, such as protocol versions and cipher suites, that are supported by load balancers during a TLS handshake. An SSL policy is associated with a target HTTPS proxy or target SSL proxy.

Each predefined profile of an SSL policy specifies a set of TLS capabilities that the load balancer is configured to support. The minimum TLS version further restricts the load balancer to use only specific versions of TLS. And in cases where you need to specify support for particular cipher suites used by TLS 1.2 and earlier, a custom profile lets you do that. Each SSL policy has an associated scope, either global or regional, depending on the load balancer.

The following load balancers support global SSL policies:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Global external proxy Network Load Balancer
  * Classic proxy Network Load Balancer



The following load balancers support regional SSL policies:

  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer 



Associating an SSL policy with a target HTTPS proxy or target SSL proxy is optional. Each target HTTPS proxy or target SSL proxy can be associated with no more than one SSL policy. You can associate the same SSL policy with multiple target HTTPS proxies or multiple target SSL proxies as long as the SSL policy and target proxy use identical scopes. Changes made to SSL policies don't alter or interrupt existing load balancer connections.

The following example shows how connections from clients are established and terminated at a load balancer.

[ ![Client connections in external Application Load Balancers or external proxy Network Load Balancers.](https://docs.cloud.google.com/static/load-balancing/images/ssl-policies.svg)](https://docs.cloud.google.com/static/load-balancing/images/ssl-policies.svg) Client connections in external Application Load Balancers or external proxy Network Load Balancers (click to enlarge).

You can use an SSL policy to configure the minimum TLS version and SSL features that are enabled in the load balancer. SSL policies affect connections between clients and the load balancer (Connection-1 in the figure). SSL policies don't affect the connections between the load balancer and the backends (Connection-2 in the figure).

## Creating an SSL policy

When you create an SSL policy, you specify the following information:

  * _profile_ , which specifies a set of TLS capabilities that the load balancer is configured to support
  * _minimum TLS version_ , which further restricts the load balancer to use only specific versions of TLS
  * _post-quantum key exchange setting_ , which specifies when post-quantum key exchange is enabled on the load balancer



When connecting to the load balancer, the clients advertise the TLS protocol versions, cipher suites, and other TLS capabilities that they are able to support. During the TLS handshake, the load balancer chooses the most recent TLS protocol version that both it and the client support, and also chooses other TLS parameters (including a cipher suite) for the connection. The TLS handshake fails if the load balancer and client don't support overlapping TLS versions, cipher suites, and other capabilities.

### Predefined profiles

Google Cloud provides the following predefined profiles.

  * `COMPATIBLE`. Supports the broadest set of clients, including clients that can only use earlier TLS versions and TLS capabilities.
  * `MODERN`. Supports a wide set of TLS ciphers, allowing modern clients to negotiate TLS.
  * `RESTRICTED`. Supports a reduced set of TLS ciphers. The `RESTRICTED` profile is intended to meet stricter compliance requirements.
  * `FIPS_202205`. Supports a set of TLS capabilities that are intended to meet [FIPS 140-3 compliance](https://csrc.nist.gov/pubs/fips/140-3/final).

**Important:**

  * _SSL policies that use the`FIPS_202205` profile must use a minimum TLS version of 1.2_. No other minimum TLS version is valid for a policy that uses the `FIPS_202205` profile. For more information, see `FIPS_202205` profile details.
  * _If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the`RESTRICTED` profile_. Although other profiles support TLS 1.3, the other profiles don't let you select the minimum TLS version to 1.3.



### Custom profile

The `COMPATIBLE`, `MODERN`, and `RESTRICTED` profiles differ in the set of cipher suites they support when the load balancer negotiates TLS 1.2 and earlier versions. The table in the section _Cipher suites for TLS 1.2 and earlier_ shows these differences.

You can also create a `CUSTOM` profile and specify individually the cipher suites that the load balancer supports for TLS 1.2 and earlier. This does not affect how the load balancer negotiates TLS 1.3.

### Behavior when no SSL policy is specified

If you don't associate an SSL policy with a target HTTPS proxy or target SSL proxy, the load balancer operates as if you had associated an SSL policy with the following settings:

  * the `COMPATIBLE` profile selected, and
  * the minimum TLS version set to 1.0



## TLS version support

Note that a profile can indirectly restrict the versions of TLS that the load balancer can negotiate. For example, the cipher suites enabled in the `RESTRICTED` profile do _not_ include any cipher suites that are supported by TLS 1.0 or 1.1; choosing the `RESTRICTED` profile therefore effectively disallows clients from using TLS 1.0 and 1.1, even if the SSL policy's minimum TLS version is set to 1.0 or 1.1.

Cloud Load Balancing doesn't support SSL versions 3.0 or earlier. The following table describes the feature support for each TLS/SSL version.

TLS/SSL version | Feature support  
---|---  
TLS 1.3 |  All profiles except for the `FIPS_202205` profile support the following TLS 1.3 cipher suites:

  * `TLS_AES_128_GCM_SHA256`
  * `TLS_AES_256_GCM_SHA384`
  * `TLS_CHACHA20_POLY1305_SHA256`

The `FIPS_202205` profile supports the following two TLS 1.3 cipher suites:

  * `TLS_AES_128_GCM_SHA256`
  * `TLS_AES_256_GCM_SHA384`

  
TLS 1.2 and earlier | The profile used by the SSL policy controls which cipher suites are used with TLS 1.2 and earlier.  
SSL 3.0 or earlier | Not supported by load balancers that use SSL policies.  
  
## Cipher suites for TLS 1.2 and earlier

The following table shows cipher suites for TLS 1.2 and earlier that are included in each predefined profile. When you create an SSL policy that uses the `CUSTOM` profile, you can select these cipher suites individually. SSL policies that use the `CUSTOM` profile must include at least one cipher suite from the following list.

[IANA](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-4) value | Feature | `COMPATIBLE` | `MODERN` | `RESTRICTED` | `FIPS_202205`  
---|---|---|---|---|---  
`0xCCA9` | `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256` |  |  |  |   
`0xCCA8` | `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256` |  |  |  |   
`0xC02B` | `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` |  |  |  |   
`0xC02F` | `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` |  |  |  |   
`0xC02C` | `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` |  |  |  |   
`0xC030` | `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` |  |  |  |   
`0xC009` | `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA` |  |  |  |   
`0xC013` | `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA` |  |  |  |   
`0xC00A` | `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA` |  |  |  |   
`0xC014` | `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA` |  |  |  |   
`0x009C` | `TLS_RSA_WITH_AES_128_GCM_SHA256` |  |  |  |   
`0x009D` | `TLS_RSA_WITH_AES_256_GCM_SHA384` |  |  |  |   
`0x002F` | `TLS_RSA_WITH_AES_128_CBC_SHA` |  |  |  |   
`0x0035` | `TLS_RSA_WITH_AES_256_CBC_SHA` |  |  |  |   
`0x000A` | `TLS_RSA_WITH_3DES_EDE_CBC_SHA` |  |  |  |   
**Note:**

There are two common ways to refer to TLS cipher suites—[IANA names](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-4) and [OpenSSL](https://docs.openssl.org/1.1.1/man1/ciphers/#cipher-suite-names) names. Google Cloud exclusively uses the IANA naming convention. If you're more familiar with platforms that use OpenSSL names, you can map the OpenSSL cipher suite names to their corresponding IANA names by running the `openssl ciphers -stdname` command in the Google Cloud CLI or your local CLI.

Some [ Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/secauthn/tls-cipher-suites-in-windows-8-1) uses nonstandard cipher suite names (for example, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 __P256_). The suffix text (`P256`) indicates the elliptic curve used for key exchange. The elliptic curve isn't a part of the ciphersuite and isn't configurable by SSL policies. Cloud Load Balancing supports `P-256`, `P-384`, and `X25519` curves. When you're designing SSL policies, ignore this extra field.

## `FIPS_202205` profile details

The `FIPS_202205` profile restricts the load balancer to use a set of TLS capabilities that is intended to be compatible with the FIPS 140-3 standard. When an SSL policy uses this profile, the load balancer supports TLS 1.2 or 1.3, with the following restrictions:

  * If the TLS connection uses TLS 1.2, only the following cipher suites are allowed:

    * `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
    * `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
    * `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
    * `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
  * If the TLS connection uses TLS 1.3, only the following cipher suites are allowed:

    * `TLS_AES_128_GCM_SHA256`
    * `TLS_AES_256_GCM_SHA384`
  * For key exchange, only `secp256r1` and `secp384r1` are allowed. If post-quantum key exchange is enabled, `X25519MLKEM768` is also allowed.

  * Only the following load balancer certificate digital signatures are allowed:

    * With RSA certificates, `rsa_pkcs1_sha256`, `rsa_pkcs1_sha384`, or `rsa_pkcs1_sha512`.
    * With ECDSA certificates, `ecdsa_secp256r1_sha256` or `ecdsa_secp384r1_sha384`.



## Post-quantum key exchange

[Post-quantum key exchange](https://docs.cloud.google.com/load-balancing/docs/post-quantum-tls#post-quantum-key-exchange) protects against certain threats to TLS security posed by quantum computing technology. Over time we will be enabling it by default in Google Cloud load balancers. The post quantum key exchange setting lets you enable it sooner, and we recommend that you do this.

The particular form of post-quantum key exchange supported by Google Cloud load balancers is `X25519MLKEM768`, a hybrid of classical and post-quantum cryptographic algorithms.

You can enable `X25519MLKEM768` key exchange on all [load balancers that support SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#supported-load-balancers).

When you enable post-quantum key exchange, consider the following behavior:

  * When post-quantum key exchange is enabled, the load balancer uses `X25519MLKEM768` key exchange when connecting to clients that advertise support for TLS 1.3 and `X25519MLKEM768`. Connections to clients that don't support TLS 1.3 or `X25519MLKEM768` are unaffected.

  * Post-quantum key exchange is supported only for frontend TLS connections, that is, for connections between the client and the load balancer.

  * Post-quantum key exchange can be enabled with any of the SSL policy profiles, and any minimum TLS version setting.




### Post-quantum key exchange modes

The post-quantum key exchange setting lets you specify one of the following:

  * `ENABLED`. The load balancer uses `X25519MLKEM768` key exchange with clients that advertise support for it.

  * `DEFAULT`. The load balancer disallows `X25519MLKEM768` key exchange until October 2026. This is the default behavior if no SSL policy is attached.

  * `DEFERRED`. The load balancer disallows `X25519MLKEM768` key exchange until October 2027.




The following timeline shows the planned rollout of the post-quantum key exchange support for load balancers.

Timeline | Post-quantum key exchange status  
---|---  
Now | Disabled by default, enabled only when set to `ENABLED`  
After October 2026 | Enabled by default, disabled when set to `DEFERRED`  
After October 2027 | Enabled always  
  
For more information about how to create an SSL policy with post-quantum key exchange, see [Create SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#create-ssl-policies).

## Cross-project SSL policy referencing

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

SSL policy cross-project referencing lets you define and maintain a central SSL policy in an administrative project (the central policy project) and reference it from target HTTPS proxies or target SSL proxies in different projects (service projects). This is useful for organizations that want to enforce standardized security configurations and eliminate configuration drift across different applications and teams.

The following load balancers support cross-project referencing for global SSL policies:

  * Global external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Global external proxy Network Load Balancer



The following load balancers support cross-project referencing for regional SSL policies:

  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer



For more information about how to configure cross-project SSL policy referencing, see [Configure cross-project SSL policy referencing](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#configure-cross-project).

## Limitations

  * Disabling particular SSL versions or ciphers can result in some earlier clients being unable to connect to your proxy by using HTTPS or SSL. Disabling a sufficiently broad selection of ciphers in the `CUSTOM` profile can result in no clients being able to negotiate HTTPS.

  * An SSL certificate associated with your load balancer uses either an ECDSA or an RSA digital signature. The predefined profiles are compatible with both types of certificate signatures. A custom profile must enable ciphers that are compatible with the digital signature used by your load balancer's certificates.




## What's next

  * To create, modify, or delete an SSL policy, see [Use SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies).
  * To configure an SSL certificate, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
