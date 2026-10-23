---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference/
title: Network Topology metrics \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:14.159745+00:00
---

# Network Topology metrics  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network Topology metrics

This document describes Cloud Monitoring metrics and metadata, which you can view in a Network Topology visualization for each entity and connection.

  * **Metadata** describes data such as name, description, and location.
  * **Metrics** describe data such as traffic, latency, and packet loss, which are the supported metrics for connections.



For each Network Topology hierarchy, the Google Cloud console displays a single metric for Compute Engine virtual machine (VM) instance entities and region entities, as well as for connections. You can change this default metric.

For more information, see the [Network Topology overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview) and [Graph interface elements](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview).

For steps describing how to work with metrics and metadata, see [Audit your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology).

## Metrics for VM or regional entities

This section lists metrics for VMs or regional entities.

Entity | Metrics  
---|---  
VM | 

  * CPU utilization
  * Memory usage percentage
  * Disk usage percentage

  
GKE entities such as clusters, nodes, and pods | 

  * CPU utilization
  * Memory usage percentage
  * Disk usage percentage

  
Region | 

  * Traffic

  
  
## Metrics for connections between entities

This section lists metrics for connections between entities.

Some connections support packet loss or latency metrics. Packet loss is based on probers that estimate the packet loss that you might experience, while latency and other metrics are based on your own traffic.

If there are not enough probes or traffic to calculate a high confidence value for packet loss or latency, Network Topology displays an asterisk (*) next to the value on the graph. For more information about how these metrics are calculated, see the [Metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview#metrics) section of the Performance Dashboard overview.

### Connections in the VM hierarchy

This section lists metrics for connections in the aggregation hierarchy where VM is the base entity. For more information about entities and their aggregation hierarchies, see [Resources and traffic](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#supported_resources).

Connection | Metrics  
---|---  
VM to VM1 | 

  * Average hourly throughput
  * Latency: based on `round-trip time (RTT)`
  * Packet loss2

  
  
1 VM-to-VM flows are not available at all aggregation levels. For example, the VM-to-VM flow is not available, but the VM-to-region flow is available. 

2 Packet loss is available only for regions and zones. 

### Connections in the GKE hierarchy

This section lists metrics for connections in the aggregation hierarchy where the GKE node is the base entity. For more information about entities and their aggregation hierarchies, see [Resources and traffic](https://cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#supported_resources).

  
**Connection** |   
**Metrics**  
---|---  
  
Pod to Pod1 | 

  * Average hourly throughput
  * Latency: based on round-trip time (RTT)

  
  
Cluster to Cluster | 

  * Average hourly throughput
  * Latency: based on round-trip time (RTT)

  
  
1 Pod-to-Pod flows are not available at all aggregation levels. For example, the Pod-to-Pod flow is not available, but the Pod-to-region flow is available. 

### Client to load balancing

This section lists metrics and metadata for traffic from external or internal clients to different types of Cloud Load Balancing.

Entity (node or edge) | Metrics  
---|---  
External client3 to an external Application Load Balancer | 

  * Traffic: based on `request bytes count` and `response bytes count`
  * Latency: based on `Frontend RTT`
  * Request count
  * HTTP error response count: based on `responses by response code class`
  * HTTP error response percent: based on `response fraction by code class`
  * Client-side error rate (total): based on CSM metrics

  
External client to an external proxy Network Load Balancer | 

  * Traffic: based on `inbound traffic` and `outbound traffic`
  * Latency: based on `Frontend RTT`
  * Current open connections: based on `open connections`
  * Connections open rate: based on `new connections per second`
  * Connections close rate: based on `closed Connections per second`

  
External client to an external passthrough Network Load Balancer | 

  * Traffic: based on `external bytes count` for egress and ingress

  
  
3For external clients, Network Topology supports only aggregation levels from `Country` and higher. 

### Load balancing to backend instance groups

This section lists metrics and metadata from different types of Cloud Load Balancing to instance group backends.

Entity or connection | Metrics  
---|---  
External Application Load Balancer to backend (instance group) | 

  * Traffic: based on `backend request bytes count` and `backend response bytes count`
  * Latency: based on `backend latencies`
  * Request Count: based on `backend request count`

  
External proxy Network Load Balancer to backend (instance group) | 

  * Traffic: based on `inbound traffic` and `outbound traffic`

  
Internal passthrough Network Load Balancer to backend (instance group) | 

  * Traffic: based on `inbound traffic` and `outbound traffic`

  
External passthrough Network Load Balancer to backend (instance group) | 

  * Traffic: based on `external bytes count` for egress and ingress

  
  
### Load balancing to GKE node pools and nodes

This section lists metrics and metadata from different types of Cloud Load Balancing to GKE node pools and nodes.

Entity or connection | Metrics  
---|---  
Application Load Balancer to GKE node pool and GKE node | Traffic: based on `bytes count` for egress and ingress  
Classic proxy Network Load Balancer to GKE node pools and GKE nodes | Traffic: based on `external bytes count` for egress and ingress  
Internal passthrough Network Load Balancer to GKE node pools | Traffic: based on `bytes count` for egress and ingress  
  
### VLAN attachments

This section lists metrics and metadata for the data transferred between your VPC network and the on-premises network, as counted by the VLAN attachment. An on-premises network can refer to any remote network that is outside the Google Cloud domain. The connection between Google Cloud and on-premises can traverse either dedicated or partner Interconnect devices.

Entity or connection | Metrics  
---|---  
VPC network to the on-premises network | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
### VPN tunnels

This section lists metrics and metadata for the data transferred between your VPC network and the on-premises network, as counted by the VPN tunnel.

Entity or connection | Metrics  
---|---  
VPC network to the on-premises network | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
### VM to VLAN attachments

This section lists metrics and metadata for the data transferred between your VM and VLAN attachment. The connection between Google Cloud and on-premises can traverse either dedicated or partner Interconnect devices.

Entity or connection | Metrics  
---|---  
VM to VLAN attachments | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
### VM to VPN tunnels

This section lists metrics and metadata for the data transferred between your VM and VPN tunnels.

Entity or connection | Metrics  
---|---  
VM to VPN tunnels | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
### Client to Google services

This section lists metrics and metadata for traffic from internal clients to different types of [Google-managed services](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#google-services).

Entity or connection | Metrics  
---|---  
VPC network to Google-managed services | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
### Router appliance

This section lists metrics and metadata for the data transferred between your VPC network and the on-premises network, as counted by the router appliance instance.

Entity or connection | Metrics  
---|---  
VPC network to the on-premises network | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
### VM to router appliance instance

This section lists metrics and metadata for the data transferred between your VM and router appliance instances.

Entity or connection | Metrics  
---|---  
VM to router appliance instance | Traffic: based on `egress bytes count` and `ingress bytes count`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
