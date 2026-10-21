---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/detect-invalid-configuration/
title: Detect invalid configurations \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:56.954924+00:00
---

# Detect invalid configurations  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/detect-invalid-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Detect invalid configurations Stay organized with collections  Save and categorize content based on your preferences. 

Network Analyzer lets you detect configurations that are not working as expected. These invalid configurations can be due to some setup errors or regressions caused by other changes. When different teams own the services affected by such invalid configuration, it can be hard to troubleshoot such issues. Discovering such failures as they happen and identifying the root causes can help in faster troubleshooting and effective communication between different teams.

## Configuration errors due to blocking firewalls

Firewall configuration errors that block Google Cloud services can happen during or after the initial setup.

### During initial setup

Some of the common firewall errors that block Google Cloud services from functioning are as follows:

  * Missing firewall configuration. For example, the load balancer's health check firewall has not been configured.
  * Typos in the manual configuration process that cause faulty configurations.
  * Inconsistent configuration caused by missing VM tags. For example, you configure the firewall rule with the expected target VM tags, but some of the backend VMs have not been associated with the specific tag.



### After the initial setup

An unintended firewall configuration change can break a service that has been functioning properly. For example, you can unintentionally create a higher priority firewall deny rule that blocks connectivity to GKE or Cloud SQL services.

### Scenario: Health check firewall is not configured for the load balancer

In this example, Network Analyzer reports an insight in the category of _load balancer insights_ of type _[health check firewall is not configured](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/load-balancer#health-check-firewall-not-configured)_. The insight details page shows the implied **deny ingress rule** in the network where the load balancer is configured. The **deny ingress rule** blocks the health check range. This indicates that the load balancer's backends do not have firewall rules configured to allow the health check range.

Configure the health check firewall rule to explicitly allow the health check range to access the load balancer backends.

### Scenario: GKE node to control plane connectivity blocked by a firewall rule

In this example, an insight that belongs to the category of _GKE node connectivity insights_ of type _[GKE node to control plane connectivity](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-node-to-control-plane#public-endpoint-blocked-by-egress-firewall)_ is generated.

The insight details page shows that a firewall rule is denying the connection from the GKE node to the control plane in a cluster. This issue is because of a denying rule; remove this rule or set up a higher priority allowing rule to address the issue.

## Routing configuration errors

Routes with invalid next hops can cause partial or total traffic loss. Such loss can be due to having routes to next hop VMs that are not running or have been deleted.

Configuration changes that can cause unintended routing change include the following scenarios:

  * Adding a new subnet with IP address ranges that overlap with a dynamic route, results in shadowing the dynamic route and this might lead to a traffic drop.
  * Adding a new default route through a VPN can cause capacity bottlenecks that affect network performance.



### Scenario: The VM in the next hop is deleted

In this example, an insight from the category of routes with invalid next hops with the _[VM is deleted](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/route-invalid-next-hop#vm-deleted)_ type appears.

The insight details page shows that the next hop VM in this route is deleted, so this route is reported as invalid.

Either delete the route or create a new VM instance to be used as the next hop of the route. A configuration change that might cause this insight is displayed in the insight details page. Click the link to go to the Cloud Logging page to see the details of the configuration such as the user who made the change and the time of the change.

### Scenario: The dynamic route is shadowed

In this example, an insight from the _shadowed dynamic routes insights_ category of _[fully shadowed by peering subnet route](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/hybrid-connectivity/dynamic-route-shadowed#fully-shadowed-by-peering-subnet-route)_ type is generated.

This insight details page shows that an imported dynamic route learned from the network peer with next hop peering network dynamic-routes is being shadowed. The IP address range of the dynamic route overlaps with a new subnet route and thus it is fully shadowed. Traffic that goes to the peering network to this IP address range is forwarded to a subnet in the VPC network.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
