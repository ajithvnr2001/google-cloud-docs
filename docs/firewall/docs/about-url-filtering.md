---
url: https://docs.cloud.google.com/firewall/docs/about-url-filtering/
title: URL filtering service overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:10.662981+00:00
---

# URL filtering service overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-url-filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  URL filtering service overview Stay organized with collections  Save and categorize content based on your preferences. 

The URL filtering service for Cloud Next Generation Firewall (Cloud NGFW) lets you control access to websites and webpages by blocking or allowing their URLs. It lets you filter your workload traffic by using domain and Server Name Indication (SNI) information that is available in the egress HTTP(S) messages.

Because the URL filtering service inspects HTTP message headers, you can use the service to block access to specific domains even when the destination server hosts trusted sites that you don't want to block or when DNS-based access restrictions are ineffective. You can use the URL filtering service along with the intrusion detection and prevention service to deny traffic to malicious URLs, prevent access to malicious command-and-control (C2) servers, and detect malware in executable files.

Cloud NGFW URL filtering service works by creating Google-managed zonal firewall endpoints that use Google Cloud's packet intercept technology to redirect and inspect traffic for a match against a list of configured domain names and SNIs.

Packet intercept is a Google Cloud capability that transparently inserts network appliances in the path of selected network traffic without modifying their existing routing policies.

## Benefits of using the URL filtering service

The URL filtering service helps you reduce required maintenance that is caused by frequently changing IP addresses, by DNS changes, and by other time-consuming IP address-based firewall changes. The service lets you gain precise control over which remote URLs you can access. It lets you gain finer control than what is possible with IP addresses, which can host multiple services and domains.

## TLS inspection

The URL filtering service can process both encrypted and unencrypted traffic. For encrypted traffic, you can configure TLS inspection to let the URL filtering service decrypt message headers and inspect the domain name in the message's host header.

The URL filtering service can then use the domain details along with the plaintext SNI sent during TLS negotiation to find a match against the configured URLs defined by the associated security profile.

Without TLS inspection, the URL filtering service can still process the encrypted HTTP(S) traffic, but the URL filtering service relies only on the SNI from `clientHello` during TLS negotiation for URL matching. For unencrypted HTTP traffic, the URL filtering service uses the HTTP host header for URL filtering regardless of whether you have enabled TLS inspection.

Cloud NGFW only supports TLS interception and decryption to access the domain information in the host header of the selected encrypted traffic.

The URL filtering service inspects both inbound and outbound connections, including traffic to and from the internet and traffic within Google Cloud.

To learn more about TLS inspection in Cloud NGFW, see [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection).

To learn how to enable TLS inspection in Cloud NGFW, see [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection).

## URL filtering service deployment model

The following diagram shows an example of the URL filtering service deployment with a firewall endpoint, configured for a Virtual Private Cloud (VPC) network in a single zone of a region.

[ ![Sample deployment model of the URL filtering service.](https://docs.cloud.google.com/static/firewall/images/firewall-urlf/urlf-simple-deployment-model.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-urlf/urlf-simple-deployment-model.svg) Sample deployment model of the URL filtering service (click to enlarge).

## Components of URL filtering service

The URL filtering service requires three main entities that you must configure. The URL filtering security profile and its associated security profile group, a firewall endpoint to receive traffic, and the firewall policies attached to the endpoint.

### Security profiles and security profile groups

Cloud NGFW uses security profiles and security profile groups to implement the URL filtering service.

  * **URL filtering security profiles** are generic policy structures of type `url-filtering` that include URL filters with [matcher strings](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles#url-matcher-strings). The URL filtering service uses these strings to match against the domain name and SNI of the HTTP(S) message. Each URL filter contains a list of matcher strings, a unique priority, and an action.

To learn more about URL filtering security profiles, see [URL filtering security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles#url-filtering-profile).

  * **Security profile groups** act as containers for security profiles. Each group contains one or more security profiles of different types. For example, a security profile group can contain security profiles belonging to `url-filtering` and `threat-prevention` types. A firewall policy rule references a security profile group to enable either the URL filtering service or the intrusion detection and prevention service, or both, for the network traffic.

To learn more about security profile groups, see [Security profile group overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups).




### Firewall endpoint

A firewall endpoint is an organizational resource, created at the zonal level that can inspect Layer 7 traffic in the same zone in which it is deployed. The endpoints are associated with one or more VPCs in the same zone. To filter traffic for a target virtual machine (VM) instance, create the firewall endpoint in the same zone as the VPC where the target VM is located.

For the URL filtering service, the firewall endpoint matches the domain from the message's host header, or the SNI obtained during TLS negotiation for encrypted traffic without TLS inspection, against the URL filters in the URL filtering security profile. If the endpoint detects a match, it performs the action associated with the URL filter on the connection. This action can be the default action or a configured action in the URL filtering security profile.

To learn more about firewall endpoints and how to configure them, see [Firewall endpoint overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints).

### Firewall policies

[Firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) apply directly to all ingress and egress traffic of a VM. You can use [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies) and [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) to configure firewall policy rules with Layer 7 inspection.

**Note:** Cloud NGFW Enterprise capabilities are only available through firewall policies. In this document, the term _firewall rules_ refers to the firewall policy rules, not the VPC firewall rules.

#### Firewall policy rules

Firewall policy rules let you control the type of traffic that is intercepted and inspected. To configure the URL filtering service, create a firewall policy rule that does the following:

  * Identifies the type of traffic to be inspected by using multiple Layer 3 and Layer 4 [firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * Specifies the security profile group name for the `apply_security_profile_group` action on the matched traffic.



For the complete URL filtering service workflow, see [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering).

You can also use [secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) in firewall rules to configure the URL filtering service. You can build on any segmentation that you have set up by using tags in your network, and enhance the traffic inspection logic to include the URL filtering service.

To configure a firewall policy rule that uses a security profile group for wildcard domain filtering (such as `*.example.com`), set the destination IP range to `0.0.0.0/0`. This is required because wildcard matching is performed at Layer 7 by the security profile. To restrict the firewall rule to match internet-bound traffic, use network contexts set to `INTERNET`.

**Note:** If you configure a firewall rule to apply a security profile group and set the destination to `0.0.0.0/0`, traffic originating from VMs in zones without an attached firewall endpoint doesn't undergo Layer 7 inspection. The firewall rule allows all traffic matching the other rule parameters (such as source, port, and protocol). To ensure consistent policy enforcement, deploy firewall endpoints in all zones within the VPC network where you have workloads that require Layer 7 inspection.

## How the URL filtering service works

The URL filtering service processes the HTTP(S) traffic in the following sequence:

  1. The URL filtering service applies firewall policy rules to the traffic to and from the VM instances or Google Kubernetes Engine (GKE) clusters in the network.

  2. The URL filtering service intercepts and sends matched traffic to the firewall endpoint for Layer 7 inspection.

  3. For encrypted traffic where TLS inspection is enabled, the URL filtering service decrypts the message headers and uses the domain specified in the host header along with the SNI sent during TLS negotiation to check for a match against the configured URLs.

If the traffic is encrypted but TLS Inspection isn't enabled, the message header remains encrypted. Instead, the URL filtering service uses the domain specified in the SNI during TLS negotiation.

For unencrypted traffic, the URL filtering service always uses the domain specified in the host header to check for a match.

  4. If the URL information matches, the URL filtering service performs the action configured in the security profile on that connection.

If the URL filtering service allows the egress traffic, the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) (if enabled) can further scan the traffic for threats.




## Limitations

  * URL filtering only supports `http/1._x_` and `http/2`. It doesn't support QUIC, encrypted SNI (ESNI), or Encrypted Client Hello (ECH) with TLS inspection enabled.

If you enable TLS inspection, Cloud NGFW doesn't pass QUIC, ESNI, or ECH traffic. However, if you disable TLS inspection, Cloud NGFW passes such traffic without access to the domain and SNI information. In this scenario, Cloud NGFW allows QUIC, ESNI, and ECH traffic only when an explicit allow URL filter is available. In the absence of an explicit allow filter, the default implicit deny URL filter blocks the QUIC, ESNI, and ECH traffic. For more information about explicit allow and implicit deny URL filters, see [Implicit deny URL filter](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles#implicit-deny-url-filter).

  * Firewall endpoints can support IP packets of a limited size only. For more information, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

  * Inspecting egress traffic from serverless workloads is not supported. This limitation applies to traffic routed using both [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) and [Serverless VPC Access connectors](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access). For more information, see [Compare Direct VPC egress and connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).




## What's next

  * [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
