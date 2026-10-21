---
url: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull/
title: Packet Mirroring for ULL VPC networks \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:21.763164+00:00
---

# Packet Mirroring for ULL VPC networks  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Packet Mirroring for ULL VPC networks

**Preview — ULL Packet Mirroring for exchange participants**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Packet Mirroring clones traffic from your Ultra Low Latency (ULL) Virtual Private Cloud (VPC) networks and forwards it to your appliances for analysis. By default, the service automatically mirrors all traffic from every eligible ULL VPC network; you can't disable this feature.

Packet Mirroring for ULL VPC networks is a zonal service that you enable for a zone. You can use the service to replicate and send traffic for the following tasks:

  * Observe network traffic to detect packet loss and measure latency.
  * Analyze network traffic to detect intrusions and other security threats.
  * Observe traffic for compliance and reporting, such as verifying the timely execution of market trading traffic.



## Key features

Packet Mirroring for ULL VPC networks provides the following features:

  * **Purpose-built for ULL VPC network** : no impact on the latency and performance of your core ULL VPC network applications. The service automatically mirrors all traffic from every eligible ULL VPC network by default.

  * **Comprehensive traffic capture** : mirrors all IP traffic to and from every Compute Engine instance in ULL VPC networks. Packet Mirroring captures traffic at all zonal NIC points. As a result, each packet is mirrored twice: once on egress and once on ingress.



  * **Flexible deployment** : the collector receives mirrored traffic from VPC networks in the same project where you create the collector resource (`UllMirroringCollector`). The collector appliance (`compute.Instance`) does not need to be in the same project as the `UllMirroringCollector`.

A _collector instance_ , also known as a _collector appliance_ , is a `compute.Instance` that you configure to receive, store, and analyze mirrored network traffic.



  * **Granular traffic filtering** : supports filter rules for each collector. Use filter rules to isolate specific traffic flows and reduce the data volume sent to your mirroring collectors.

  * **Scalable collection** : uses Google Cloud internal passthrough Network Load Balancers to distribute mirrored traffic to a group of collector instances.




### Components of ULL Packet Mirroring

  * **ULL Packet Mirroring collector (`UllMirroringCollector`)**: the customer-owned resource that you connect to the exchange operator's engine (`UllMirroringEngine`) to receive mirrored packets. The collector references an internal passthrough Network Load Balancer that forwards mirrored traffic to your collector instances.

The state of `UllMirroringCollector` determines whether the collector receives packets. The state can be one of the following:

    * `ACTIVE` (default): applies filtering rules.
    * `INACTIVE`: ignores filtering rules and doesn't receive traffic.
  * **ULL Packet Mirroring collector filter rule (`UllMirroringCollectorRule`)**: the customer-owned child resource of `UllMirroringCollector` that lets you control mirrored traffic reaching the ULL Packet Mirroring collector. You can set up filters and define the specific conditions that a packet must meet to be forwarded to your collector.

By default, no `UllMirroringCollectorRule` resources are attached to a `UllMirroringCollector` resource, and traffic is not mirrored.




## Security and privacy

Packet Mirroring for ULL VPC networks integrates with the Google Cloud security framework.

### Encryption in transit

Google Cloud automatically encrypts mirrored traffic while it is in transit between the infrastructure and your collector appliances. The service also encapsulates network packets by using [Generic Network Virtualization Encapsulation (GENEVE)](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/geneve).

### Logging and monitoring

To maintain data privacy, Packet Mirroring for ULL VPC networks doesn't persist packet payloads. For debugging or health monitoring, the service temporarily logs only packet headers, which are encrypted at rest.

In certain limited operational scenarios, Google Cloud might temporarily log packet headers for the following reasons:

  * **Service debugging** : to diagnose software bugs or investigate unexpected service behavior, Google Cloud might log headers to resolve the issue.

  * **Network health monitoring** : Google Cloud might log a small, random sample of packet headers as part of routine operations to ensure network performance and health.




When Google Cloud generates these logs, the following mandatory safeguards protect your information:

  * Google Cloud retains only packet headers and never logs the actual payload of your packets.

  * Google Cloud encrypts all temporarily stored header information by default.

  * Google Cloud keeps information only for the time required to complete the analysis. It then securely deletes the information in accordance with Google Cloud data deletion policies.

  * Google Cloud restricts access to the logged data to authorized personnel with a valid business justification, and logs and audits every instance of access.




## Quota and limits

  * A ULL Packet Mirroring collector supports up to 100 rules. The quota is measured per collector, where each rule represents one unit.

If you create more than 100 rules, the API returns a `ResourceExhausted` error.

  * For each rule, the number of items in any repeated field must not exceed 10.




## Limitations

  * You can mirror a single packet to up to two ULL Packet Mirroring collector resources.



## What's next

  * [Set up Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull)
  * [Configure VPC Service Controls](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/configure-vpc-service-controls)
  * [Understand GENEVE format](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/geneve)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
