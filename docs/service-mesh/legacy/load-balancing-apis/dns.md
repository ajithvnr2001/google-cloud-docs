---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/dns/
title: DNS name resolution \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:00.486273+00:00
---

# DNS name resolution  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/dns/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DNS name resolution

This document applies to Cloud Service Mesh with Envoy and the older load-balancing APIs, which include forwarding rules.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document explains the relationship between a forwarding rule's virtual IP address and how the forward rule is associated with a service. The document also outlines how to plan and configure DNS for a service-to-service communication in a Cloud Service Mesh service mesh.

Consider this example, in which there are three services, `service-a`, `service-b`, and `service-c`, that communicate with each other. Developers often use fully- qualified-domain names in their code for service-to-service communication. If your domain name is example.com, the three services might be represented as:

  * `service-a.example.com`
  * `service-b.example.com`
  * `service-c.example.com`



When you configure Cloud Service Mesh resources to create a service mesh, you configure a forwarding rule for each of the services. A forwarding rule represents the `IP:Port` pair of the destination service. For egress traffic to be intercepted by an Envoy sidecar proxy, the destination IP address must match with the IP address associated with the forwarding rule. Therefore, you need to provision an IP address for each service. For example:

  * `service-a.example.com` has the IP address `10.0.0.100`
  * `service-b.example.com` has the IP address `10.0.0.101`
  * `service-c.example.com` has the IP address `10.0.0.102`



The corresponding Cloud Service Mesh configuration has three forwarding rules, FR1, FR2, and FR3, each using port `80`:

  * FR1 has IP address `10.0.0.100:80`, which is associated with `service-a.example.com`.
  * FR2 has IP address `10.0.0.101:80`, which is associated with `service-b.example.com`.
  * FR3 has IP address `10.0.0.102:80`, which is associated with `service-c.example.com`.



When `service-a` invokes `service-b` using the fully qualified domain name (FQDN) `service-b.example.com`, three things happen:

  1. `service-a` first performs a DNS lookup for `service-b.example.com` to resolve `service-b`'s IP address.
  2. The domain is resolved to `10.0.0.101` so that it matches the configured IP address of `service-b`'s forwarding rule.
  3. The Envoy proxy is now able to intercept traffic and route it to the backend service that has `service-b`'s backends, whether those are NEGs or MIGs.



You can configure a Cloud DNS managed private zone to host the resource records for your services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
