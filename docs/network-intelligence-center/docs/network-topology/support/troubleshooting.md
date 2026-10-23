---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting/
title: Troubleshoot Network Topology \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:35.310462+00:00
---

# Troubleshoot Network Topology  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Network Topology

Use the following guidance to troubleshoot common issues with Network Topology. To learn more about Network Topology, see the [overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview).

## No nodes were found for this graph

Check that your resources aren't hidden by a filter. For more information, see [Filtering specific entities](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology#filter-entities).

Only resources that are created by the current project are visible to that project. If you are using Shared VPC, you might have your network in the host project and resources in service projects. In the host project, Network Topology doesn't visualize the Shared VPC network or its resources because the resources are in service projects. For information about how to visualize resources in the Shared VPC network, see [Adding multiple projects to a single graph](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology#multi-project).

### Why don't I see traffic between entities?

For information about why you might not see traffic between entities, see the following:

  * At least one supported resource on either end of a connection must communicate with the other for traffic between them to become visible.
  * Network Topology might not display connections for resources that have a very low amount of traffic between them.



For more information, see the Communication section and [Resources and traffic](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#supported_resources) in the overview.

## An instance or load balancer is missing

You might have an existing instance or load balancer that isn't shown in a Network Topology graph. The following sections describe scenarios when a resource isn't shown.

### Projects and metrics scope

The Network Topology graph shows communication between resources in your existing project or Monitoring's [metrics scope](https://docs.cloud.google.com/monitoring/settings). If a missing resource is in a different project than the currently selected project, check that both projects are visible to the selected project's metrics scope. For more information, see [Adding multiple projects to a single graph](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology#multi-project).

### Communication

The Network Topology graph shows only the resources that are communicating with at least one other entity in the selected hourly segment. If an instance or load balancer didn't send or receive traffic during the selected hour, Network Topology doesn't visualize it. Check that you've selected a segment when the instance or load balancer is in communication with another entity. For more information, see [Data collection and freshness](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#data).

### Filters and entity selection

In a Network Topology graph, you can add filters to view the specified resources and the resources that they communicate with. All other resources are hidden. Check that your filters include the instances or load balancers that you want to view.

Network Topology also includes a pane where you can choose to hide or show particular entities. Check that you are showing (have selected) the resource types that you want to view. For example, if you clear the **Instances** checkbox, all instances are hidden.

For more information, see [Filtering specific entities](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology#filter-entities).

## When I expand some entities, Network Topology skips some levels of the hierarchy

In cases when there's only a single entity at any particular level, Network Topology skips that level or levels until it reaches a level where multiple entities can be aggregated or until it reaches the base entity.

Network Topology always shows some levels of a hierarchy, such as the region for a virtual machine (VM) instance. For example, if you have a single VM in a region, Network Topology shows that region, but when you expand the region, Network Topology skips directly to the VM instance without showing its zone.

You can still view the full hierarchy for an entity by clicking it and viewing its [details pane](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview).

## Some lines don't show metric values

For information about why some lines don't show metric values, see the following:

  * In some cases, Network Topology has metric values but doesn't have enough room to show them. Network Topology shows a bulge in the line to indicate that metric values are available. Drag the connecting objects further apart to show the metric value.

  * Metrics might not be available between entities at all levels of their aggregation hierarchies. For example, metrics are available from VMs to regions, but not from VMs to other VMs.

  * Not all metrics apply to all connections. For information about the supported metrics for each connection, see the [Metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference).

  * For packet loss and latency, metric values show `Not available` if the sample rate for the metric is too low to be reliable or if the Cloud Monitoring API does not return a value. For more information about how these metrics are calculated, see the [Metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview#metrics) section of the Performance Dashboard overview.

  * Latency appears only on lines that represent a single connection. It is not aggregated on lines that branch into multiple connections.




## Displayed throughput is higher than expected

To view details about a throughput value, click the metric to see a time series chart. You can see how throughput evolved over time.

If you have [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) enabled and export those logs to BigQuery, you can use an automatically generated query to see the flows related to the throughput values. For more information, see [Using generated queries](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology#queries).

## The graph contains too many nodes and connections

Use filtering or the entity selection pane to reduce the clutter. For more information, see [Filtering specific entities](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/using-network-topology#filter-entities).

## The full graph is too big to be handled

If the topology graph is too large to be displayed in a browser, a truncated graph is displayed. Some connections and nodes might be missing from the displayed graph.

**Note:** Metrics are still accurate; the truncation only affects the existence of some connections and possibly some nodes.

  * Remove some projects or resources from this metrics scope.
  * To reduce the graph's size, show data only for the current project.



## In a Google Cloud zone, there are two GKE clusters with the same name

GKE cluster names are unique for each GKE location, such as a Google Cloud region or a Google Cloud zone. You can set up a GKE cluster in a Google Cloud zone and a second GKE cluster with the same name in the encompassing Google Cloud region. In the **Network Topology GKE** view, these clusters are shown as two clusters with the same name in the same zone. You can see the cluster location below the name of the cluster and in the right panel after you click the node.

## What's next

  * [Get support](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
