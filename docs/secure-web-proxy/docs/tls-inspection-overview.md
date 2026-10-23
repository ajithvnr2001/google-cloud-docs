---
url: https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview/
title: TLS inspection overview \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:59:30.152597+00:00
---

# TLS inspection overview  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  TLS inspection overview Stay organized with collections  Save and categorize content based on your preferences. 

Transport Layer Security (TLS) encrypted traffic accounts for the vast majority of web traffic. Because threat actors often use these encrypted channels to hide malicious activity, it's critical to inspect this traffic before it reaches its destination.

Secure Web Proxy provides an integrated TLS inspection service that lets you intercept and decrypt HTTPS traffic. By gaining visibility into the encrypted request, Secure Web Proxy can apply advanced security policies—such as URL filtering on the full request path and HTTP header inspection—to protect your environment from threats hidden within encrypted tunnels.

**Note:** If you want to use [`ApplicationMatcher`](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference) in your security rules for HTTPS traffic, then you must [enable TLS Inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection) for your Secure Web Proxy instance.

## How it works

TLS inspection works by establishing two separate encrypted connections, with Secure Web Proxy acting as a secure intermediary.

  * **Client handshake** : when a client tries to connect to an external site, such as `www.example.com`, Secure Web Proxy intercepts the request.

  * **Certificate generation** : Secure Web Proxy generates a temporary certificate for `www.example.com` in real time. Depending on the configured certificate issuance mode, the proxy either requests leaf certificates directly from the CA Service for each domain or signs them locally by using a cached intermediate CA certificate from the CA pool.

  * **Trust validation** : the client then receives that temporary certificate.

  * **Inspection point** : traffic is decrypted within the Secure Web Proxy instance. At this stage, security policies are applied to the plain-text HTTP data.

  * **Server handshake** : Secure Web Proxy then initiates a second TLS connection to the actual destination server. The traffic is re-encrypted and sent to the destination address.




## Key features

The Secure Web Proxy TLS inspection service offers a flexible, scalable framework for managing encrypted traffic through the following capabilities:

  * **Integrated private trust** : built-in integration with CA Service provides a highly available, Google-managed repository for your private CAs.

  * **Flexible root of trust** : use an existing on-premises root certificate authority (CA) to sign subordinate CAs that are hosted in CA Service. You can then generate and manage a completely new root certificate directly within CA Service.

  * **Specific decryption** : use `SessionMatcher` to define precisely which traffic to decrypt. You can trigger the TLS inspection based on the following parameters:

    * **Website domain names** : match specific websites by using regular expressions and domain lists.
    * **Network criteria** : target specific source IP address ranges or Classless Inter-Domain Routing (CIDR) blocks, such as `10.0.0.0/24`, to define network boundaries.
    * **Boolean logic** : combine multiple conditions—such as a source IP and a destination URL—to create highly specific security rules.
  * **Scalable policy architecture** :

    * **Dedicated policies** : assign a unique TLS inspection policy and CA pool to each Secure Web Proxy policy for strict isolation.

    * **Shared policies** : simplify policy management by sharing a single TLS inspection configuration across multiple proxy policies.

  * **Full Uniform Resource Identifier (URI) visibility** : inspect the entire URI (including the domain, path, and query strings, such as `www.example.com/downloads/malware.exe`) rather than just the domain name.

  * **Precise access control** : use TLS inspection to enforce policies for specific paths of a website. For example, you can allow access to `www.example.com/documentation`, but block `www.example.com/uploads`.

  * **Intermediate CA support** : reduce CA Service usage fees by locally caching a single intermediate CA to sign leaf certificates, instead of issuing per-domain requests directly to CA Service. For more information, see Certificate issuance modes.




## Role of certificate authorities in TLS inspection

To inspect encrypted traffic, Secure Web Proxy acts as a trusted intermediary. This involves a coordinated process between the proxy, the CA Service, and the client device.

### Client trust requirements

TLS inspection is designed for environments where an organization has administrative control over the client devices, such as managed laptops, servers, or virtual machines (VMs).

  * **Private trust anchor** : Because Secure Web Proxy presents certificates that are signed by your internal CA rather than a public CA, clients trust the connection only if your private root CA is pre-installed.
  * **Administrative scope** : Connections from unmanaged hardware typically trigger `Insecure connection` warnings because these devices lack your organization's specific trust anchor.



### Handle interception failures

Even on managed devices, certain connections can't be intercepted due to _certificate pinning_. Certificate pinning occurs when an application is hardcoded to accept only a specific public key or a specific public CA chain.

  * **Examples of certificate pinning** : common services that use pinning include Windows and macOS system updates, Google Chrome updates, and certain high-security mobile applications.
  * **Result of certificate pinning** : when Secure Web Proxy presents its signed certificate, the application detects that the certificate doesn't match its hardcoded expectations and terminates the connection.



### Mitigation and precise control

To prevent service disruptions for _pinned_ applications or to maintain privacy for sensitive websites, you can use the `SessionMatcher` attribute to bypass inspection. You can restrict or skip inspection based on the following parameters:

  * **Destination attributes** : specific fully qualified domain names (FQDNs).
  * **Source attributes** : [secure tags](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags), [service accounts](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts), or [IP addresses](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic).
  * **Custom logic** : use boolean expressions to exclude specific traffic while inspecting the rest of the environment.



## Certificate issuance modes

Secure Web Proxy supports two modes to provision the certificates that it uses to decrypt traffic during the TLS inspection process. The choice depends on your cost, performance, and audit logging requirements.

For more information, see [Configure a local intermediate CA signing](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#ca-pool-intermediate-ca-config).

### Local intermediate CA signing

If you set `certificateIssuanceMode` to `LOCAL_INTERMEDIATE_CA_SIGNING`, Secure Web Proxy requests a single intermediate CA certificate from your CA pool. The proxy caches this intermediate CA and signs the individual leaf certificates locally for required domains.

The features of the local intermediate CA signing certificate issuance mode are as follows:

  * **Lower CA Service costs** : requests to CA Service are limited to the refresh cycle of the intermediate CA (typically once per day) rather than occurring for every domain, leading to lower transaction costs.

  * **Reduced observability** : individual leaf certificates that your proxy signs locally aren't recorded in the CA Service audit logs.




### Direct leaf provisioning

If you set `certificateIssuanceMode` to `DIRECT_LEAF_PROVISIONING`, Secure Web Proxy directly communicates with your CA Service pool for each unique domain to request a leaf certificate.

The features of the direct leaf provisioning certificate issuance mode are as follows:

  * **Greater observability** : every generated certificate request is recorded in CA Service audit logs, letting you track and audit all certificate-generation activities.

  * **Higher CA Service costs** : because requests are sent to CA Service for every domain, this process can lead to higher transaction fees in environments that have several unique domains or proxy tasks.




## Certificate authority configuration methods

To enable TLS inspection, set up your certificate authority (CA) by using any of the following methods:

  * **Subordinate CA in CA Service** : use an existing external root CA to sign a subordinate CA stored within Google Cloud.

  * **External root CA** : use an external root CA to sign certificates that are generated at runtime through subordinate CAs.

  * **Google-managed root CA** : generate a new root certificate directly within CA Service to sign your subordinate CAs.




For more information about these methods, see [Create a subordinate CA pool](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#create-sub-ca-pool).

## What's next

  * [Rule evaluation order](https://docs.cloud.google.com/secure-web-proxy/docs/tls-rule-evaluation)
  * [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
