---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/egress-dscp-tagging/
title: Quality of Service DSCP tagging overview \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:07.030967+00:00
---

# Quality of Service DSCP tagging overview  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/egress-dscp-tagging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Quality of Service DSCP tagging overview Stay organized with collections  Save and categorize content based on your preferences. 

Quality of Service (QoS) manages network traffic and ensures the performance of critical applications by controlling factors like bandwidth, latency, and packet loss. This technology prioritizes certain types of network traffic over others when network resources are limited or congested. You can use Differentiated Services Code Point (DSCP) tagging to prioritize traffic on modern IP networks.

For information on how to use DSCP tagging, see [Configure DSCP tagging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-egress-dscp-tagging).

## How EgressDSCP tagging works

Quality of Service (QoS) manages network traffic to ensure critical applications perform in situations with low bandwidth. Egress DSCP tagging enables you to tag packets with a DSCP value in the IP header to communicate the priority level to downstream network devices.

## Supported workloads

Egress DSCP tagging supports prioritizing traffic for the following Google Distributed Cloud workloads:

  * Container workloads: Kubernetes pods and services running on the cluster.
  * Virtual Machines (VMs): VM workloads running via the VM runtime, provided they are connected to the default network.



## Resource types for DSCP tagging

Distributed Cloud uses specific custom resources to manage DSCP tags. You define the priority of your packets using these objects:

  * `EgressDSCP`: A custom resource that defines the specific DSCP value to insert into the IP header of selected traffic packets. This object accepts an integer value from `0` to `63`.
  * `TrafficSelector`: A custom resource that precisely selects network traffic flows. This resource accepts a priority integer from `0` to `65535`, with a default of `1000`. The `TrafficSelector` object references an `EgressDSCP` object to apply a specific action to the identified traffic. Even when using a namespace-scoped `TrafficSelector`, you must include a namespace selector to explicitly identify the namespace of the pods initiating the targeted traffic.



## Conflict resolution

When multiple `TrafficSelector` resources apply to the same subject, the system uses a specific hierarchy to determine precedence. The system resolves conflicts using the following principles in order:

  1. Priority: The system applies the `TrafficSelector` with the numerically lowest priority value.
  2. CIDR range specificity: If rules share the same priority, the system applies the rule with the most specific CIDR limit (the longest prefix match).
  3. Port specificity: If rules share the same priority and CIDR range, the system applies the rule with the most specific port.



If a more specific CIDR rule has a numerically higher priority (lower precedence), the system applies the broader rule and ignores the more specific rule.

### Shadowing example

Consider the following two `TrafficSelector` rules applied to the same destination:

  * Rule A: Priority `100`, Destination CIDR `192.168.1.0/24`, marks DSCP `40`.
  * Rule B: Priority `200`, Destination CIDR `192.168.1.15/32`, marks DSCP `46`.



Even though Rule B specifies a more precise destination CIDR (`192.168.1.15/32`), the system prioritizes Rule A because it has a numerically lower priority value (`100`). As a result, the system ignores Rule B and applies DSCP tag `40` to all outgoing traffic directed to `192.168.1.15`.

## Limitations

The DSCP tagging feature includes several constraints for its current implementation:

  * External egress traffic: You can only tag north-south traffic leaving the cluster, like outgoing traffic initiated by workloads and return traffic from Kubernetes services to external clients.
  * No internal enforcement: Although the system tags intra-cluster traffic, Kubernetes does not enforce QoS policies internally based on these tags.
  * Marking only: The system only tags IP headers. You must configure your upstream physical network infrastructure to handle actual QoS enforcement.
  * Supported protocols: You can only tag IPv4 traffic.
  * Supported services: You can only tag traffic for `LoadBalancer` and `NodePort` services.
  * Virtual Machine networks: You can only tag VM workloads connected to the default network.
  * Feature enablement: You must enable the feature by adding the `preview.baremetal.cluster.gke.io/traffic-selector: "enable"` annotation to the cluster resource.
  * Return path defaults: For return path traffic, the DSCP value defaults to `0` unless explicitly configured otherwise.



## Security considerations

Unauthorized users could mark non-essential traffic with elevated DSCP values, disrupting critical services across the cluster.

To mitigate security risks, limit access using Kubernetes Role-Based Access Control (RBAC):

  * Cluster-wide controls: Restrict permission to create or modify cluster-scoped `EgressDSCP` resources to trusted cluster administrators.
  * Namespace controls: Manage `TrafficSelector` resources by namespace so users can only affect their specific workloads.



## What's next

  * [Configure DSCP tagging for workloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-egress-dscp-tagging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
