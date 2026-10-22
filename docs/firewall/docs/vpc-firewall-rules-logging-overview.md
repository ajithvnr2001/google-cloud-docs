---
url: https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview/
title: VPC firewall rules logging overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:15.317599+00:00
---

# VPC firewall rules logging overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  VPC firewall rules logging overview Stay organized with collections  Save and categorize content based on your preferences. 

VPC firewall rules logging lets you audit, verify, and analyze the effects of your VPC firewall rules. For example, you can determine if a VPC firewall rule designed to deny traffic is functioning as intended. VPC firewall rules logging is also useful if you need to determine how many connections are affected by a given VPC firewall rule.

You enable VPC firewall rules logging individually for each VPC firewall rule whose connections you need to log. VPC firewall rules logging is an option for any VPC firewall rule, regardless of the action (`allow` or `deny`) or direction (`ingress` or `egress`) of the rule.

VPC firewall rules logging logs traffic to and from [Compute Engine virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances). This includes Google Cloud products built on Compute Engine VMs, such as [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) and [Google Kubernetes Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible) instances.

When you enable logging for a VPC firewall rule, Google Cloud creates an entry called a _connection record_ each time the rule allows or denies traffic. You can view these records in [Cloud Logging](https://docs.cloud.google.com/logging/docs/log-analytics), and you can export logs to any destination that Cloud Logging export supports.

Each connection record contains the source and destination IP addresses, the protocol and ports, date and time, and a reference to the VPC firewall rule that applied to the traffic.

**Note:** After you create a VPC firewall rule or enable logging on an existing rule, you might observe some delay before log entries appear. Logging data takes time to synchronize and fully propagate. Initial log entries might be missing some rule details.

For information about viewing logs, see [Manage VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging#viewing_logs).

## Specifications

VPC firewall rules logging has the following specifications:

  * **Supported deployments** : you can enable VPC firewall rules logging for VPC firewall rule within hierarchical, global network, regional network, and regional system firewall policies associated with a regular VPC network, and regional network firewall policies associated with a [RoCE VPC network](https://docs.cloud.google.com/firewall/docs/firewall-for-roce).

  * **Unsupported rules** : VPC firewall rules logging is not supported for rules in [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy), [Implied deny ingress and implied allow egress rules](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules) in a regular VPC network, or [Implied allow ingress and egress rules](https://docs.cloud.google.com/firewall/docs/firewall-for-roce#implied_firewall_rules) of an RoCE VPC network.

  * **Protocol support** : VPC firewall rules logging only records `TCP` and `UDP` connections. If you want to monitor other protocols, consider using [Out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview).

  * **Connection-based logging** : VPC firewall rules logging are created when a connection is established, not for every individual packet. A connection remains active as long as packets are exchanged at least once every 10 minutes. Each new packet resets the idle timer. Therefore, a continuous stream of traffic generates only one log entry for its entire duration. If you need continuous visibility into active, long-lived streams without idle periods, use [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs).

  * **Existing connections** : if you enable logging on a rule that matches an already active `TCP` or `UDP` connection, a new log entry is not generated. The VPC firewall rule logs the connection only if it remains idle for at least 10 minutes and a new packet is subsequently sent.

  * **Allow and deny behavior** :

    * **Allow + Logging** : an allowed connection is logged only once, and the entry is not repeated even if the connection endures, because firewall rules are stateful, reply traffic is allowed automatically and is not logged.

    * **Deny + Logging** : each dropped packet corresponding to a unique 5-tuple is logged as a failed attempt. The log entry repeats every 5 seconds as long as packets are observed for that denied connection.

  * **Log generation perspective** : log entries are only created if a VPC firewall rule has logging enabled and if the rule applies to traffic sent to or from the VM. Entries are created subject to the connection logging limits.

  * **Rate limits** : the number of connections logged per unit of time is determined by the VM's machine type for regular VPC networks, or by the monitoring or logging action of the rule for RoCE VPC networks. For more information, see [Connection logging limits](https://docs.cloud.google.com/vpc/docs/quota#logging_limits) and [Monitoring and logging](https://docs.cloud.google.com/firewall/docs/firewall-for-roce#monitoring_and_logging)



  * **Legacy scope** : VPC firewall rules logging applies only to legacy VPC firewall rules operating within a regular VPC network.

  * **Protocol limits** : legacy VPC firewall rules logging supports setting the IP protocol field to `ALL`.

  * **Audit logs** : you can view configuration changes to the VPC firewall rule in VPC audit logs. For more information, see [VPC audit logs](https://docs.cloud.google.com/vpc/docs/audit-logging).




## Limitations

VPC firewall rules logging is a legacy format and doesn't support logging for advanced Cloud NGFW metadata fields such as the following:

  * `source_region_code`
  * `destination_region_code`
  * `source_fqdn`
  * `destination_fqdn`
  * `source_threat_intelligence`
  * `destination_threat_intelligence`
  * `source_address_groups`
  * `destination_address_groups`
  * `source_secure_tag`
  * `target_secure_tag`



## What's next

  * [Manage VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging).
  * [ VPC firewall rules logging examples](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-log-examples).
  * [ VPC firewall rules logging format](https://docs.cloud.google.com/firewall/docs/vpc-log-format).
  * [Cloud Logging overview](https://docs.cloud.google.com/logging/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
