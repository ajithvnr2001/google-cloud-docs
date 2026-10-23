---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview/
title: Network Topology overview \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:10.309620+00:00
---

# Network Topology overview  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network Topology overview

Network Topology is a visualization tool that shows the topology of your network infrastructure:

  * Infrastructure view: Shows Virtual Private Cloud (VPC) networks, hybrid connectivity to and from your on-premises networks, connectivity to Google-managed services, and the associated metrics.
  * GKE Enterprise view (for GKE Enterprise enabled projects): Shows the infrastructure of your Google Kubernetes Engine (GKE) deployments: clusters, namespaces, workloads, pods, and their associated metrics.



You can also view metrics and details of network traffic to other Shared VPC networks and inter-region traffic. Network Topology combines configuration information with real-time operational data in a single view. This view makes it easier to understand networking relationships between various workloads on Google Cloud and their current state, such as the traffic paths and throughput between virtual machine (VM) instances.

Network Topology lays out information in a [graph](http://wikipedia.org/wiki/Graph_\(discrete_mathematics\)) format, where the nodes and lines represent _entities_ and _connections_ in your network.

## How it works

Network Topology collects real-time telemetry and configuration data from Google's infrastructure to visualize your resources. It captures elements such as configuration information, metrics, and logs to infer relationships between resources in a project or in multiple projects. After collecting each element, Network Topology combines them to generate a graph that represents your deployment.

## Benefits

Using Network Topology provides the following benefits:

  * You can view the topology of your deployments. No additional configurations or agents are required to use Network Topology.

  * You can use Network Topology graphs to understand your Google Cloud infrastructure. You don't need to view multiple logs or use third-party tools.

  * You can use Network Topology to help you analyze the performance of your network. You can drill down and view various metrics that can help you identify unexpected patterns.

  * You can use filters to help you highlight and focus on specific resources, especially when you need to diagnose and troubleshoot issues.

  * You can view cross-project metrics for network traffic sent across Shared VPC or VPC Network Peering boundaries within the same organization.

  * You can view insights for entities with high egress metric values for further analysis and troubleshooting.




## Considerations

**Important:** If there are many projects and the topology graph is too large to be displayed in a browser, a truncated graph is displayed. Some connections and nodes might be missing from the displayed graph. You can remove some projects or resources from this metrics scope. Or, to reduce the graph's size, show data only for the current project. Note that the metrics are not sampled or truncated. A message appears below the graph saying that the graph is too large.

Network Topology captures six weeks of history.

Network Topology visualizes entities and connections only if they have communicated (sent or received traffic) during the selected time period. A connection between entities exists if base entities in their respective hierarchies are in communication. For example, Network Topology connects regions `us-east4` and `europe-west1` if at least one VM instance in each region communicates with the other. Although other resources might exist, Network Topology doesn't show them if they didn't receive or send traffic.

For more information, see Data collection and freshness.

## Resources and traffic

A Network Topology graph shows your resources and traffic as entities and connections. Network Topology aggregates related resources into hierarchical entities, where each resource type has its own hierarchy. The following sections describe the resources (entities) and traffic paths (connections) that Network Topology can graph.

### Entities

A base entity is the lowest level of a particular hierarchy and represents a resource that can directly communicate with other resources over a network, such as a VM instance or a GKE pod for Google Kubernetes Engine (GKE) Enterprise edition projects.

When you have multiple networks and many base entities, displaying everything in a flat view can be overwhelming. To address this issue, Network Topology aggregates base entities into hierarchical entities that you can expand or collapse. When you first view a Network Topology graph, it aggregates all of the base entities into their top-level hierarchy.

For example, Network Topology aggregates the entities as follows:

  * VM instances into their instance group, then aggregates instance groups into a Google Cloud zone
  * GKE pods into their GKE workloads, then aggregates GKE workloads into GKE namespaces, and then the GKE namespaces into a GKE cluster. This is available only for GKE Enterprise enabled projects.



Network Topology represents a base or hierarchical entity as a circular node in a graph. Each base entity possesses its own hierarchy. For example, load balancers have a different hierarchy than VM instances.

**Note:** When you drill down into a hierarchy, Network Topology might skip a level. If a particular hierarchy contains only one entity, Network Topology skips that level until it reaches a level that contains multiple entities or base entities. For an example, see the [Auditing network performance](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance) use case.

The following table shows the base entities and their aggregation hierarchies. In a graph, Network Topology represents each base entity by using an icon shown in the table.

Base entity | Icon | Description | Aggregation hierarchy  
(top to bottom)  
---|---|---|---  
VM instance | ![Icon for VM instance.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/instance.svg) | A Compute Engine VM instance |  region >  
network >  
subnet >  
zone >  
instance group >  
instance  
  
VM instance group | ![Icon for VM instance group.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/instance-group.svg) | The collection of VM instances that you can manage as a single entity. |  region >  
network >  
subnet >  
zone >  
instance group >  
  
Classic Application Load Balancer External passthrough Network Load Balancer External proxy Network Load Balancer | ![Icon for load balancer.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/load-balancer.svg) | The base entity for external load balancer components, such as the forwarding rule and backend service. |  external load balancing >  
load balancer  
  
Internal load balancer | ![Icon for load balancer.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/load-balancer.svg) | The base entity for internal load balancer components, such as the forwarding rule and backend service. |  internal load balancing >  
load balancer  
  
Cloud NAT gateway | ![Icon for NAT gateway.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/cloud-nat.svg) | A NAT gateway |  region >  
network >  
NATs >  
NAT gateway  
  
VPC Network Peering | ![Icon for peer networks.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/network-peering.svg) | A VPC peering endpoint that is shown when you don't have permissions to view the peer network. If you do, Network Topology shows the resources of the peer network. |  peer networks >  
network  
  
Country | ![Icon for countries where external clients are located.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-public.svg) | Network Topology shows the country where external clients are located. These clients are outside of Google Cloud. They are typically hosts that communicate with resources in your network over external IP addresses. |  business region* >  
country#  
  
Cloud Interconnect | ![Icon for Interconnect connection.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-interconnect.svg) | Network Topology shows the Dedicated Interconnect or Partner Interconnect connections. For more information, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview). |  interconnect   
VLAN attachments | ![Icon for VLAN attachments.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-interconnect.svg) | Network Topology shows the VLAN attachments to Dedicated Interconnect or Partner Interconnect connections.  |  interconnect >  
interconnect attachments  
  
Cloud VPN gateway | ![Icon for VPN gateway.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/cloud-nat.svg) | Network Topology shows the Cloud VPN gateway connections. For more information, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview). |  gateway >  
  
Cloud VPN | ![Icon for VPN gateway.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-public.svg) | Network Topology shows the Cloud VPN connections. |  gateway >  
vpn tunnel  
  
On-premises | ![Icon for on-premises entities.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-on-prem.svg) | Network Topology shows the on-premises networks. An on-premises network can refer to any remote network that is outside the Google Cloud domain. |  on-premises   
Router appliance instances | ![Icon for router appliance instances.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-ra.svg) | Network Topology shows the Router appliance instances.   
Google-managed services | ![Icon for Google-managed services.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-gms.svg) | Network Topology shows the Google-managed service instance.  |  Google services >  
Google service  
  
  
*A business region can be one of the following entities: **Americas** for North and South America, **APAC** for Asia and Oceania, and **EMEA** for Europe, the Middle East, and Africa.  
#Google uses the external IP addresses to categorize the origin of the external client. However, the IP address might not indicate the actual location of the client. For example, if you deliver content through Cloud CDN, the IP address observed by Network Topology might not be the actual address of the external client. 

The following table shows the base entities and their aggregation hierarchies in the GKE Enterprise view, which is available only for GKE Enterprise projects. In a graph, Network Topology represents each base entity by using an icon shown in the table.

Base entity | Icon | Description | Aggregation hierarchy  
(top to bottom)  
---|---|---|---  
GKE Pod | ![Icon for GKE pod.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-gke-pod.svg) | The base entity for GKE entities such as clusters, workloads, and namespaces. | region >  
network >  
subnet >  
zone >  
GKE cluster >  
GKE namespace >  
GKE workload >  
GKE pod   
GKE Workload | ![Icon for GKE workload.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-gke-workload.svg) | A GKE workload | region >  
network >  
subnet >  
zone >  
GKE cluster >  
GKE namespace >  
GKE workload   
GKE namespace | ![Icon for GKE namespace.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-gke-namespace.svg) | A GKE namespace | region >  
network >  
subnet >  
zone >  
GKE cluster >  
GKE namespace  
GKE cluster | ![Icon for GKE cluster.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/netviz-gke-cluster.svg) | A GKE cluster | region >  
network >  
subnet >  
zone >  
GKE cluster   
**Note:** In the topology view and as part of the Pod metrics, Network Topology does not show the IPv6 IP address of the dual stack Pods.

### Connections

Network Topology represents traffic between entities as lines, such as traffic between VM instances. Network Topology connects entities if at least one side of the connection is sending traffic.

Network Topology shows connections at various levels of a hierarchy as long as their base entities are in communication. For example, Network Topology shows a connection between two regions if at least one VM instance in each region is communicating with the other.

Network Topology supports TCP, UDP, ICMP, ICMPV6, ESP, and GRE traffic for certain traffic paths. The following list describes the paths that Network Topology visualizes between entities:

  * **Traffic in a VPC network** such as traffic between VM instances and internal load balancers that are in the same network.
  * **Traffic across peered VPC networks** such as traffic between VM instances and internal load balancers that are in peer VPC networks.
  * **Traffic between Google Cloud and the internet** such as traffic between clients on the internet and entities (for example, VM instances or external Application Load Balancers that have external IP addresses).
  * **Traffic to and from Cloud VPN gateways, Cloud Interconnect connections, and router appliance instances.**



The following list describes the paths that Network Topology visualizes between entities in the GKE Enterprise view, available only for GKE Enterprise projects:

  * **Traffic within a GKE cluster** such as the traffic between pairs of GKE pods on different GKE nodes. Network Topology doesn't show metrics for the traffic between the GKE nodes within a cluster.
  * **Traffic between two pods** within the same GKE node if intranode visibility is enabled.
  * **Traffic between GKE clusters** and external IP addresses such as service flows. These connections might flow through load balancers.



#### Google-managed services

Network Topology also visualizes traffic to and from Google-managed services. Google Cloud users can use Network Topology to audit their networking configuration and troubleshoot networking issues related to the different Google services in use.

Network Topology supports direct access of VMs to Google-managed services by using a default route with a next hop as the [`default-internet-gateway`](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) or [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options#pga). It does not support the following access methods to Google-managed services:

  * External traffic from the internet
  * Direct Google access from the VMs
  * Private Google Access from on-premises hosts



Network Topology doesn't show traffic to or from some of the Google-managed services such as App Engine Memcache, Filestore, Memorystore, Cloud SQL, and partner and marketplace solutions.

#### IP address considerations

For traffic between VM instances in Google Cloud that communicate using external IP addresses, Network Topology does not display a single connection directly between the VMs. Instead, Network Topology displays the traffic as if it were to and from an external location by using two connections: one connection between the first VM and the country of the second VM, and another connection between the second VM and the country of the first VM.

#### Network interface considerations

Network Topology only visualizes traffic to or from the first network interface (`nic0`) of a VM.

For VMs that use internal IP addresses to communicate, Network Topology only displays a connection if both VMs are communicating by using their first network interface (`nic0`-to-`nic0`).

For VMs that use external IP addresses to communicate, Network Topology normally displays two connections as described in IP address considerations. However, if only one of the VMs is using `nic0`, Network Topology only displays a connection for that VM. For example, if one VM is communicating through `nic0` and the other VM is communicating through `nic1`, Network Topology only displays a connection between the `nic0` VM and a country.

## Metrics for entities

Network Topology shows the average traffic within the selected hour. You can also view average packet loss for the hour and median latency (RTT) for many entity types.

Metrics for the selected hour on the timeline include the following:

  * Average hourly throughput available for most entities
  * Average hourly packet loss available for traffic within Google Cloud regions and zones
  * Hourly median latency (RTT) available for many entity types



In the GKE Enterprise view available for GKE Enterprise projects, the metrics for the selected hour on the timeline also include the following:

  * Average hourly throughput available for most entities
  * Median latency available for traffic within Google Cloud regions and zones with GKE clusters
  * Network verdict metrics displaying the GKE workloads with the most dropped and most forwarded traffic flows for the selected cluster



You can also download the table of outliers in a CSV format for the **High egress** and **Network verdict** traffic insights.

## Insights for entities with high metric values

In addition to the average hourly metrics, Network Topology also shows the ranking of VMs or instance groups that generate the highest egress. Network Topology provides dedicated views that rank resources where you can start your troubleshooting and analysis.

In the Infrastructure view, the insights for metrics for the selected hour on the timeline include the following:

  * **High egress instances:** aggregated hourly values for various types of egress
  * **High egress instance groups:** aggregated hourly values for various types of egress



In the GKE Enterprise view available for GKE Enterprise projects, the insights for metrics for the selected hour on the timeline include the following:

  * **High egress GKE workloads:** aggregated hourly values for various types of egress for GKE workloads, in the GKE Enterprise view



### Filter the traffic based on the traffic types

You can further filter the traffic based on the following traffic types:

  * All egress traffic for an entity
  * **Cross-zonal egress traffic:** useful for analyzing billable traffic
  * **Egress to internet:** used for analyzing billable traffic and for analyzing the traffic that reaches external endpoints
  * **Hybrid egress:** used to analyze the volume of traffic to on-premises, including Cloud Interconnect, Cloud VPN, and Router appliance connections



In the GKE Enterprise view, you can further filter the traffic based on the following traffic types:

  * All measured egress traffic from the selected entity
  * **Cross-zonal egress traffic:** useful for analyzing billable traffic between Google Cloud zones



## Multiple projects

Network Topology visualizes resources in your project, or you can use Cloud Monitoring, which can visualize metrics for multiple Google Cloud projects. When you configure Cloud Monitoring to have access to the metrics for multiple projects, Network Topology can show network traffic that crosses multiple projects.

For example, assume that you have two VM instances in two different projects. `vm-a` is in `project-a`, and `vm-b` is in `project-b`. Both VM instances communicate with each other and are in a Shared VPC network. If you only have visibility into `project-b`, Network Topology shows `vm-b` but nothing to indicate that it communicated with `vm-a`. However, if you configure Cloud Monitoring to view metrics for both projects, Network Topology shows `vm-a`, `vm-b`, and their communication.

Cloud Monitoring is especially useful for Shared VPC and VPC Network Peering scenarios, where resources or networks can be in different projects. For more information, see [View metrics for multiple Cloud projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

### Project aggregation

When you view multiple projects in a Network Topology graph, you can aggregate Google Cloud entities by project and then by their standard hierarchies. This option lets you view resources by project. Entities outside of Google Cloud, such as external clients, aren't included in project aggregation.

As an example, if you aggregate by project and then expand a project, the graph shows a region entity for each region that contains a VM instance. If you don't use project aggregation, the graph shows all of the entities as if they were in the same project. To enable project aggregation, see [Aggregate entities by project](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues#aggregating-project).

### Change project scope

To view multiple projects in Network Topology, configure a metrics scope and add monitored projects to it.

When you add projects to a metrics scope, then this metrics scope lets you monitor the data for the scoping project and the monitored projects. From this metrics scope, you can access the combined metrics of the scoping project and the monitored projects. For more information, see [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

To make use of an existing metrics scope and monitor multiple Google Cloud projects in a single view, select the scoping project using the Google Cloud console project picker or the **Change Scope** button. You can also select a single monitoring project using these options.

## Data collection and freshness

Network Topology captures six weeks of history.

The Network Topology history is divided into hourly snapshots, which start at the beginning of an hour. For each hourly snapshot, the graph shows base entities and their communication that occurred during that hour. For example, if two instances communicated with each other and then were deleted during the hour, they would appear for that hour even though they no longer exist.

The visualization of entities and their connections includes overlaid metrics on the connections where applicable. Network Topology also displays separate time series charts that show metrics such as the traffic throughput between communicating entities or the CPU utilization of VM instances. The time series charts don't have the same hourly constraints as the visualized entities, connections, and overlaid metrics.

For more information about viewing metrics, see [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues).

### Present snapshot

When you view the present time, the Network Topology graph shows an hourly snapshot from the previous hour. Each time that you load a graph, Network Topology shows the latest available snapshot.

For more details about each component and its data during the present segment, see the following table.

For this component | Data comes from this time period | And is available at this time | Example  
---|---|---|---  
Entities and connections | The previous hour | Immediately after each hour1 | If the current time is 01:19 PM, the graph visualizes entities that communicated from 12:00 PM to 01:00 PM, but the graph can change. At 01:20 PM the graph is fixed and won't change.   
Overlaid metric values | The previous hour2 | As entities and connections become available  | If the current time is 10:37 AM and the selected metric is `Traffic`, the overlaid values are an average from 09:55 AM to 10:00 AM.   
Time series charts | Real-time, with historical data from a timeframe that you specify. The default timeframe shows minute-by-minute metric values from the past hour. The available timeframes range from `1 hour` to `6 weeks`3. | At most 7 minutes after an activity  | If the current time is 10:37 AM and you open the time series charts for a VM, you see minute-by-minute metric values for the hour from 09:37 AM to 10:37 AM.   
  
1The graph can change up to 20 minutes after the end of an hour.  
2The traffic and packet loss metrics use the average of the selected hour, while latency uses the median.  
3The _aggregation interval_ , or how often the data is sampled, depends on the timeframe. For example, the `1 hour` timeframe has an aggregation interval of 1 minute, while the `1 day` timeframe has an aggregation interval of 1 hour. 

### Past snapshots

For details about each component and its data when viewing past snapshots, see the following table.

For this component | Data comes from this time period | Example  
---|---|---  
Entities and connections | An hour that you select from the past | 11:00 AM to 12:00 PM from the previous day   
Overlaid metric values | The selected hour1 | If you select the segment that runs from 11:00 AM to 12:00 PM on the previous day and the selected metric is `Traffic`, the overlaid values are an average from 11:55 AM to 12:00 PM.   
Time series charts | Real-time, with historical data from a timeframe that you specify. The default timeframe shows minute-by-minute metric values from the past hour. The available timeframes range from `1 hour` to `6 weeks`2. | If you set the timeframe of the time series chart to `1 day`, the chart shows metric values from the current time to 24 hours ago using a 5-minute aggregation interval.   
  
1The traffic and packet loss metrics use the average of the last one hour, while latency uses the median.  
2The _aggregation interval_ , or how often the data is sampled, depends on the timeframe. For example, the `1 hour` timeframe has an aggregation interval of 1 minute, while the `1 day` timeframe has an aggregation interval of 1 hour. 

## What's next

  * [View graph interface elements](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview)
  * [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)
  * [Troubleshoot Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
