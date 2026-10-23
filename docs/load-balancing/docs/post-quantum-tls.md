---
url: https://docs.cloud.google.com/load-balancing/docs/post-quantum-tls/
title: Post-quantum TLS \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:05.104609+00:00
---

# Post-quantum TLS  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/post-quantum-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Post-quantum TLS Stay organized with collections  Save and categorize content based on your preferences. 

Advances in quantum computing threaten the cryptographic mechanisms long used by TLS. Google believes that the security of asymmetric cryptography used in TLS [could be broken by quantum computers as soon as 2029](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) if research progress continues at its current pace.

To mitigate this risk, Google Cloud load balancers support _post-quantum key exchange_ capabilities, designed to resist the theoretical capabilities of quantum computers. These algorithms were developed and vetted by the National Institute of Standards and Technology (NIST), and their use in TLS conforms with standards being developed under the IETF.

To learn more, see [Post-quantum cryptography in Google Cloud](https://cloud.google.com/security/resources/post-quantum-cryptography).

## How quantum computing threatens TLS security

Cryptographically-relevant quantum computers will be able to enable attacks against two critical components of TLS security: key exchange and authentication.

### Attacks against key exchange

Cryptographically-relevant quantum computers will be able to break the key exchange algorithms used during the TLS handshake, revealing the symmetric keys that encrypt TLS sessions and exposing application-layer traffic in plaintext. This is true even for TLS connections that use perfect forward secrecy key exchange methods such as ECDHE. An attacker who records an entire TLS session today could even decrypt it years in the future when quantum computing capabilities become available, in what is called a _harvest now, decrypt later attack_.

### Attacks against authentication

Cryptographically-relevant quantum computers will be able to break the keys used in TLS certificates or certificate authorities, allowing an attacker to falsely assert a client or server identity. Used with a man-in-the-middle attack, this could allow an attacker to see and manipulate the contents of TLS-encrypted sessions. Unlike attacks against key exchange, attacks against authentication cannot be done retrospectively against recorded traffic. However, attacks against authentication significantly threaten the integrity of web authentication.

### Symmetric ciphers are not threatened

The symmetric cryptographic ciphers, such as `AES-128`, `AES-256`, and `ChaCha20`, used to encrypt TLS sessions once the handshake and authentication completes are not threatened by quantum computing.

## Post-quantum key exchange

To mitigate the risk of harvest now, decrypt later attacks, we recommend that you enable post-quantum key exchange for connections between clients and load balancers.

Post-quantum key exchange is supported only for frontend TLS connections, that is, for connections between the client and the load balancer.

Post-quantum key exchange can be enabled for the following load balancers:

  * Global external Application Load Balancers
  * Classic Application Load Balancers
  * Regional external Application Load Balancers
  * Cross-region internal Application Load Balancers
  * Regional internal Application Load Balancers
  * Global external proxy Network Load Balancers
  * Classic proxy Network Load Balancers



`X25519MLKEM768` is the particular form of post-quantum key exchange supported in Google Cloud load balancers. This is a _hybrid_ key exchange method, which means that it is secured by both classical and post-quantum cryptographic mechanisms.

When post-quantum key exchange is enabled, the load balancer uses it when connecting to clients that advertise support for TLS 1.3 and `X25519MLKEM768`. Connections to clients that don't support TLS 1.3 or `X25519MLKEM768` are unaffected.

When post-quantum key exchange is enabled, the load balancer uses it when a connecting client advertises support for TLS 1.3 and the `X25519MLKEM768` key exchange mechanism. Connections from clients that don't support TLS 1.3 or `X25519MLKEM768` are unaffected.

### Enable post-quantum key exchange

You can enable post-quantum key exchange on your load balancer by using the `post-quantum-key-exchange` setting in an SSL policy, either by attaching a new SSL policy to your existing [`TargetHttpsProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies) or [`TargetSslProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies), or by modifying an already attached SSL policy.

To learn more about how to create SSL policies with the post-quantum key exchange setting, see [Create SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#create_ssl_policies).

We recommend that you enable post-quantum key exchange now, as it provides immediate protection against harvest now, decrypt later attacks. Correctly implemented clients are not expected to experience issues. However, if your client application is incompatible, you can set `post-quantum-key-exchange` to `DEFERRED`, which lets you delay enabling post-quantum key exchange until October 2027, giving you time to make your application compatible.

### Post-quantum key exchange rollout

Because the security protection offered by post-quantum key exchange is important, Google Cloud will begin enabling it by default in October 2026. This will affect load balancers that have no SSL policy attached, or that use an SSL policy with no post-quantum key exchange setting. If required, you can defer enabling post-quantum key exchange until October 2027 by using the `DEFERRED` setting.

The following timeline shows the planned rollout of post-quantum key exchange support for load balancers.

Timeline | Post-quantum key exchange status  
---|---  
Now | Disabled by default, enabled only when set to `ENABLED`  
After October 2026 | Enabled by default, disabled when set to `DEFERRED`  
After October 2027 | Enabled always  
  
## What's next

  * [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
