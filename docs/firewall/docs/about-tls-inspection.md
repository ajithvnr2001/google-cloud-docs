---
url: https://docs.cloud.google.com/firewall/docs/about-tls-inspection/
title: TLS inspection overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:17.119212+00:00
---

# TLS inspection overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-tls-inspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  TLS inspection overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Next Generation Firewall (Cloud NGFW) offers a Transport Layer Security (TLS) interception and decryption service that can inspect encrypted and unencrypted traffic for network attacks and disruptions. TLS connections are inspected on both inbound and outbound connections, including traffic to and from the internet and traffic within Google Cloud.

Cloud NGFW decrypts the TLS traffic to enable the firewall endpoint to perform Layer 7 inspection, such as the [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering) and the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention), in your network. After the inspection, Cloud NGFW re-encrypts the traffic before sending it to its destination.

Cloud NGFW uses Google-managed [Certificate Authority Service (CAS)](https://docs.cloud.google.com/certificate-authority-service/docs) to generate short-lived intermediate certificates. Cloud NGFW uses these intermediate certificates to generate the certificates that are required to decrypt the intercepted traffic. You set up [Certificate Authority (CA) pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool), and optionally, [trust configs](https://docs.cloud.google.com/certificate-manager/docs/core-components#trust-configs), to store and maintain a list of trusted CA certificates.

This page provides a detailed overview of Cloud NGFW's TLS inspection capabilities.

## Specifications

  * Cloud NGFW supports TLS protocol versions 1.0, 1.1, 1.2, and 1.3.

  * Cloud NGFW supports the following TLS cipher suites: 

[IANA](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-4) value | Cipher suite name  
---|---  
0xCCA9 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256  
0xCCA8 | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256  
0xC02B | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256  
0xC02F | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  
0xC02C | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  
0xC030 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  
0xC009 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA  
0xC013 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA  
0xC00A | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA  
0xC014 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA  
0x009C | TLS_RSA_WITH_AES_128_GCM_SHA256  
0x009D | TLS_RSA_WITH_AES_256_GCM_SHA384  
0x002F | TLS_RSA_WITH_AES_128_CBC_SHA  
0x0035 | TLS_RSA_WITH_AES_256_CBC_SHA  
0x000A | TLS_RSA_WITH_3DES_EDE_CBC_SHA  
  * Cloud NGFW uses a [TLS inspection policy](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection#configure-tls-inspection-policy) to set up TLS inspection on a firewall endpoint.

You set up CA pools and, optionally, trust configs to generate trusted TLS certificates for TLS clients. Optionally, you can also set up trust configs to store and maintain trusted CA certificates. You include the configuration information about CA pools and trust configs in a TLS inspection policy. This policy is then attached to the firewall endpoint and target Virtual Private Cloud (VPC) network and is used to decrypt the traffic you want to inspect.

To learn more about how to set up TLS inspection in Cloud NGFW, see [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection).

  * A TLS inspection policy and a CA pool are both regional resources. Therefore, you must create a CA pool and a TLS inspection policy for each region where you're enabling TLS inspection.

  * If you want to use trust configs in your TLS inspection policy, make sure the trust config and the TLS inspection policy are in the same region.




## Role of certificate authority in TLS inspection

Cloud NGFW intercepts TLS traffic by dynamically generating certificates for clients. These certificates are signed by intermediate CAs that are configured within the firewall endpoint. These intermediate CAs are signed by CA pools within CA Service. Cloud NGFW generates new intermediate CAs every 24 hours.

Each time a client establishes a TLS connection, Cloud NGFW intercepts the connection and generates a certificate for the requested server name for the return back to the client. Cloud NGFW can also validate privately signed backend certificates by using a trust config. You can add trusted certificates to a Certificate Manager trust config.

You add trust config and CA pool configurations to a TLS inspection policy. This policy is then added to the [firewall endpoint association](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#endpoint-association) and is used to decrypt the intercepted traffic.

The CAs stored in CA Service are backed by the Hardware Security Module (HSM) and generate audit logs with each use.

The short-lived intermediate CAs generated by Cloud NGFW are stored only in memory. Each server certificate signed by an intermediate CA does not result in an audit log from CA Service. Also, because server certificates are not generated directly by CA Service, any issuance policies or name constraints configured in the CA pool don't apply to server certificates generated by Cloud NGFW. Cloud NGFW does not enforce these constraints when generating server certificates with intermediate CAs.

**Note:** If you use a CA pool with name constraints, it can result in the generation of invalid certificates by Cloud NGFW.

## Firewall policy rule `--tls-inspect` flag

To enable decryption of the traffic matching the configured firewall policy rules, use the `--tls-inspect` flag. When you configure the `--tls-inspect` flag in the firewall policy rule, Cloud NGFW generates a new server certificate for matched TLS traffic. Intermediate CAs within Cloud NGFW sign this certificate. These intermediate CAs are, in turn, signed by CA pools within CA Service. This certificate is then presented to the client, and a TLS connection is established. The generated certificate is cached for a short time for subsequent connections to the same host.

## TLS inspection over HTTP connect

Cloud NGFW supports TLS interception and decryption on the egress HTTPS traffic that a client sends by using [HTTP Connect](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.3.6).

For example, consider a scenario where a client sends an HTTP Connect request to establish a secure tunnel between the client and server by using an intermediate web proxy server such as [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview). After establishing the tunnel, Cloud NGFW intercepts and decrypts any egress TLS internet traffic that passes through the tunnel and performs a Layer 7 inspection like [intrusion detection and prevention](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).

## TLS inspection with internal load balancers

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you use Cloud NGFW Enterprise tier rules to protect cross-region internal Application Load Balancers, client traffic arrives at the load balancer first. Because cross-region internal Application Load Balancers can terminate TLS connections natively, the load balancer decrypts the traffic and forwards plain text to the zonal firewall endpoint for application layer inspection, such as [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).

Because the load balancer decrypts traffic before application layer inspection, the following happens:

  * The firewall endpoint association ignores the `--tls-inspection-policy` flag that you specify for traffic targeting the load balancer.
  * The firewall policy rules ignore any `--tls-inspect` flag when you set `--target-type` to `INTERNAL_MANAGED_LB`.



For more information about configuring application layer inspection for load balancer traffic, see [Use global network firewall policies to protect Envoy-based load balancers](https://docs.cloud.google.com/firewall/docs/global-network-app-lb).

## Limitations

  * Cloud Next Generation Firewall Enterprise doesn't support [HTTP/2](https://datatracker.ietf.org/doc/rfc9113/), [QUIC](https://datatracker.ietf.org/doc/rfc9000/), [HTTP/3](https://datatracker.ietf.org/doc/rfc9114/), or [PROXY protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) traffic with TLS inspection. However, TLS inspection is supported for TCP traffic that is not HTTPS.

  * Cloud NGFW Enterprise supports only TLS decryption. It does not support decryption of traffic that uses other encryption protocols, such as SSH.

  * Inspecting egress traffic from serverless workloads is not supported. This limitation applies to traffic routed using both [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) and [Serverless VPC Access connectors](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access). For more information, see [Compare Direct VPC egress and connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).




## What's next

  * [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
