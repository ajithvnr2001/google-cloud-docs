---
url: https://docs.cloud.google.com/ull-solution/participants/firewall/overview/
title: Firewall for ULL VPC networks \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:22.469091+00:00
---

# Firewall for ULL VPC networks  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/firewall/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Firewall for ULL VPC networks

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

Cloud Next Generation Firewall (Cloud NGFW) for Ultra Low Latency (ULL) Virtual Private Cloud (VPC) networks provides a security configuration for ULL Solution.

The [standard Cloud NGFW](https://docs.cloud.google.com/firewall/docs/about-firewalls#firewall-standard) performs packet processing, which can affect network speed. Because ULL VPC networks require high performance and availability, Cloud NGFW uses a firewall policy type `ULL_POLICY`. This policy type lets network administrators enforce essential security boundaries while maintaining the performance required for high-frequency trading. For more information about ULL Solution, see [ULL Solution overview](https://docs.cloud.google.com/ull-solution/participants).

## Specifications

This section describes firewall specifications for ULL Solution.

  * ULL VPC networks support firewall rules in regional network firewall policies only. They don't support global network firewall policies, hierarchical firewall policies, or VPC firewall rules.

  * To prevent the configuration of latency-inducing features, ULL VPC networks require the `ULL_POLICY` firewall policy type. The firewall `POLICY_TYPE` field is set at policy creation and can't be changed later.

  * You can associate a firewall policy with a ULL VPC network if you create the policy with the `--policy_type=ULL_POLICY` flag.

  * ULL firewall policies maintain the same statefulness behavior as regular VPC networks. If a firewall rule allows an ingress connection, the firewall automatically allows the return egress traffic for that connection without requiring a separate rule.




## Supported and unsupported features

The following table lists the supported and unsupported features for firewall in ULL VPC networks. The checkmark indicates supported attributes, and  indicates unsupported features.

Feature category | Feature name | Status  
---|---|---  
Policy scope | Regional network firewall policies |   
Global network firewall policies |   
Hierarchical firewall policies |   
Rule types | Policy-based rules |   
Legacy VPC firewall rules |   
Match criteria | Secure tags |   
Address groups |   
5-Tuple (IP, Port, Protocol) |   
Legacy network tags, fully qualified domain name (FQDN) objects, geolocation objects, and threat intelligence |   
Advanced services | Firewall rules logging |   
[Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull) |   
Intrusion detection and prevention service |   
Traffic types | Unicast traffic (traffic that is secured and evaluated by the `ULL_POLICY` firewall rules) |   
[ULL Multicast](https://docs.cloud.google.com/ull-solution/participants/multicast-overview) traffic |   
  
## What's next

  * [Create and manage firewall policies for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/firewall/create-firewall-rules)
  * [Ultra Low Latency Solution overview](https://docs.cloud.google.com/ull-solution/participants)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
