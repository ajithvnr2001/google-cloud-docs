---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-masq-config/
title: GKE IP masquerade configuration insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:07.131609+00:00
---

# GKE IP masquerade configuration insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-masq-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  GKE IP masquerade configuration insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for Google Kubernetes Engine (GKE) IP masquerade configuration. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

Network analyzer detects the `ip-masq-agent` configuration and compares it with the cluster's Pod CIDR ranges.

## ConfigMap is missing part of the Pod CIDR range

The [ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) for the `ip-masq-agent` configuration deployed on your GKE cluster appears to be missing the Pod CIDR ranges. This corresponds to the following warning message: **Cluster's`ip-masq-agent` config map's `nonMasqueradeCIDRs` does not fully cover the Pod CIDR ranges.** This means that intra-cluster traffic among the Pods uses the source node's IP address for Source Network Address Translation (SNAT), which can lead to connectivity issues when a firewall or network policy is in place.

This insight includes the following information:

  * **`ip-masq-agent` ConfigMap**: the [ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) of the `ip-masq-agent` component.
  * **nonMasqueradeCIDRs** : the field that specifies a list of destination IP address ranges in [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) for which source IP address SNAT is disabled.
  * **Pod CIDR** : the Pod CIDR range is a dedicated block of IP addresses that are reserved exclusively for assigning unique IP addresses to Pods within the cluster. Every Pod that runs in the cluster receives its own IP address from this range, which enables network communication.



### Related topics

For more information, see [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) and [Configuring an IP masquerade agent in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

### Recommendations

Check the value of the [Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#cluster-view-pod-ip-ranges) assigned to the cluster, and [edit the `ip-masq-agent` ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#edit-ip-masq-agent-configmap) to include all the Pod CIDR ranges in the `nonMasqueradeCIDRs` field. Including the Pod CIDR ranges helps ensure that traffic within the cluster isn't subject to IP masquerading.

## ConfigMap is missing part of the Pod CIDR range and default SNAT disabled

[Default SNAT](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#disable-default-snat-flag) is disabled in your GKE cluster because of the `--disable-default-snat=true` flag, and the self-deployed `ip-masq-agent` configuration is managing IP masquerade rules instead. Your custom configuration for the ip-masq-agent [ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) might not properly include the Pod CIDR ranges. This corresponds to the following warning message: **Cluster's`ip-masq-agent` config map's `nonMasqueradeCIDRs` does not fully cover the Pod CIDR ranges and the flag disable-default-snat is set to true.** As a result, Pod traffic might not be correctly masqueraded according to your intended policy.

This insight includes the following information:

  * **`ip-masq-agent` ConfigMap**: the [ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) of the `ip-masq-agent` component.
  * **nonMasqueradeCIDRs** : the field that specifies a list of destination IP address ranges in [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) for which source IP address SNAT is disabled.
  * **Pod CIDR** : the Pod CIDR range is a dedicated block of IP addresses that are reserved exclusively for assigning unique IP addresses to Pods within the cluster. Every Pod that runs in the cluster receives its own IP address from this range, which enables network communication.
  * **custom config** : the [custom configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) for the `ip-masq-agent` ConfigMap overwrites the [default nonMasqueradeCIDRs list](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-non-masq-dests). Your custom configuration entirely replaces the default ranges provided by the agent.
  * **disable-default-snat flag** : the [`--disable-default-snat`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#disable-default-snat-flag) flag changes the default GKE SNAT behavior so that source Pod IP addresses are preserved for packets sent to all destinations.



### Related topics

For more information, see [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) and [Configuring an IP masquerade agent in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

### Recommendations

Check the value of the [Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#cluster-view-pod-ip-ranges) and [custom configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) assigned to the cluster. [Edit the `ip-masq-agent` ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#edit-ip-masq-agent-configmap) to include all the Pod CIDR ranges in the `nonMasqueradeCIDRs` field. Including the Pod CIDR ranges helps ensure that traffic within the cluster isn't subject to IP masquerading.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
