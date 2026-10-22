---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/networking-overview/
title: Networking overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:25.207959+00:00
---

# Networking overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/networking-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Networking overview Stay organized with collections  Save and categorize content based on your preferences. 

The virtual networking layer on Google Distributed Cloud (GDC) air-gapped governs connectivity, firewalls, service discovery, load balancing, and observability between virtual machines and pods running in a GDC organization.

## GDC networking model

GDC contains two levels of multi-tenancy concepts: organizations and projects. Projects exist within organizations, and you deploy all virtualized and containerized workloads into one particular project within an organization.

### Organization networking

Each organization in GDC has its own isolated virtual network. The virtual network within the organization is a flat IP space, which means all workloads in the organization have direct IP address connectivity to one another. Using [project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview), you can control access between workloads in different projects in the organization.

GDC isolates each organization at the network level from all other organizations. Workloads in one organization don't have direct IP address connectivity to workloads in another organization.

An organization has two different IP ranges: an internal range and an external range. The external IP range is reachable from outside the organization, and the internal IP range is only accessible from within the organization. Workloads are always assigned an IP address from the internal range of the organization, which means they are not accessible from outside the organization by default. You must explicitly enable inbound and outbound traffic for workloads using the ingress and egress constraints described in the Project networking section.

### Project networking

You deploy all virtual machines (VM) and containerized workloads into a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management). Projects provide a network segmentation boundary within the organization.

Workloads within a project can communicate directly with one another. However, the default network policy prevents communication between workloads in different projects. [Project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview) (`ProjectNetworkPolicy`) let you configure which projects in the organization can communicate with one another. If the project network policy allows, then workloads in the organization can reach each other at the L3 network layer using their respective IP addresses. You must explicitly enable ingress and egress constraints to and from the organization for each workload that requires inbound or outbound traffic.

## Configure load balancers

Load balancers distribute traffic across your application's backend workloads, ensuring stability and availability. Create external and internal load balancers for pod and VM workloads. GDC provides three methods for configuring load balancers. For more information, see [Manage load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services).

#### Ingress constraints

The mechanism used to expose workloads outside the organization differs depending on whether the workload is based on VMs or containers.

You expose VM-based workloads outside of the organization using the VM external access capability. You enable this capability for each VM. Each VM gets its own IP address from the external range of the organization.

On the other hand, you expose containerized workloads outside the organization using the external load balancer feature. You can create an external load balancer, and GDC assigns an external IP address. Then, traffic can be load-balanced across a set of backend pod workloads.

#### Egress constraints

You must explicitly enable outbound traffic for each project and workload to communicate outside the organization. Enabling outbound traffic changes the IP from workloads to an external IP using Network Address Translation (NAT) when connecting outside the organization. For more information about allowing outbound traffic, see [NAT overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-overview).

## Network policy enforcement model

The security posture for workloads within an organization is the union of default and user-created [project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview).

Policy enforcement is based on Layer-3 and Layer-4 traffic flows. A flow describes a 5-tuple connection as follows:

  * Source IP address
  * Destination IP address
  * Source port
  * Destination port
  * Protocol, such as `TCP`, `UDP`, or `IPIP`



Network policies perform outbound traffic enforcement on traffic at the node that hosts the source workload and inbound traffic enforcement when the traffic arrives at the node that hosts the destination workload. Therefore, to establish a connection, you must allow the policy to leave the source for the destination and arrive at the destination from the source.

Reply traffic, such as the SYN-ACK (synchronize-acknowledge) segment replying to an SYN segment, is not subject to enforcement. Therefore, reply traffic is always allowed if the initiating traffic is allowed. For this reason, you only observe connection timeouts due to policy enforcement from the client initiating the connection. Denied traffic is either discarded during the outbound data transfer from the source node or the inbound data transfer at the destination node. The receiving workload never observes the connection.

Enforcement is based on allow-based policy rules that are additive. The resulting enforcement for a workload is an "any match" for the traffic flow against the union of all policies applied to that workload. When multiple policies are present, the rules applied to each workload are additively combined, allowing traffic if it matches at least one of the rules. You don't have deny rules, only allow rules.

When a network policy denies a flow, you don't receive a response packet and observe a connection timeout. For this reason, any refused or reset protocol-level connections or HTTP errors are not a direct result of networking enforcement.

For more information about Kubernetes network policies, see <https://kubernetes.io/docs/concepts/services-networking/network-policies/#the-two-sorts-of-pod-isolation>.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
