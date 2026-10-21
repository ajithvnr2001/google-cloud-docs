---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview/
title: Topology interface elements \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:03.550805+00:00
---

# Topology interface elements  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Topology interface elements

Network Topology visualizes your Google Cloud network as a [graph](http://wikipedia.org/wiki/Graph_\(discrete_mathematics\)). You can use the graph to explore your existing configurations and quickly troubleshoot networking issues. To view a Network Topology graph, see [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues).

The Network Topology graph includes the following elements.

Element name | Description  
---|---  
**View options** | A control pane where you can select or clear [entities](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#entities) that Network Topology displays in the graph.  
**Metrics and insights** | A section to select the average hourly [metrics](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference) or insights for entities with high metric values.  
**Types of egress** |  In the Infrastructure view, a drop-down menu to filter by traffic type: 

  * **Cross-zonal** : Displays a ranked table of outliers with the traffic between Google Cloud zones, and excludes the traffic between entities within the same zone.
  * **To the internet** : Displays a ranked table of outliers with the traffic from Google Cloud to external endpoints, excluding hybrid traffic.
  * **Hybrid** : Displays a ranked table of outliers with the traffic through Cloud VPN, Cloud Interconnect, and router appliances.
  * **All measured egress** : Displays a ranked table of outliers with the traffic from an entity.

In the GKE view, a drop-down menu to filter by traffic type:

  * **Cross-zonal:** Displays a ranked table of outliers with the traffic between Google Cloud zones, and excludes the traffic between entities within the same zone.
  * **All measured egress:** Displays a ranked table of outliers with the traffic from an entity.

  
**Show all projects in the Workspace** | In the Infrastructure view, select the checkbox to display all the projects in your [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/settings).  
**Project aggregation** | Select the checkbox to group your resources by the projects they belong to.  
**Show connections for child nodes only on focus** | Select the checkbox to display only the traffic paths between top-level entities, such as regions. To view the traffic paths between lower-level entities, select or hold the pointer over the entities. To display all the traffic paths, clear the checkbox.  
**Filter** | Use **entity-type:entity_name** or just **entity_name** values that specify the entities that you want to find in the topology along with their communication peers. Filters for entity names can contain asterisks. [Filters](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues#filter-entities) can help you quickly highlight and focus on specific entities, especially when you need to quickly diagnose and troubleshoot issues. For example, you can specify a region filter that shows the `us-east4` region and all entities that are communicating with its resources. You can also use the asterisk (`*`) to create advanced patterns and search for entities. For example, you can use the value `*replica*` to search for all entities containing _replica_ in their name. You can put asterisks anywhere within the pattern, matching arbitrary sequences of characters in entity names.  
**Entity details pane** | Shows the name of the resource and its hierarchy. You can also view connection details for a selected entity by clicking each connection. If metrics are available for either the entity or the connection, Network Topology shows time-series charts for those metrics.  
**Traffic paths** | Lines that show the communication paths between entities. If you hold the pointer over or click an entity, metric values are overlaid on the relevant [traffic paths](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#connections).  
**Entities and connections** | To view information about one or more entities, hold the pointer over or click the entities.

  * To _expand or collapse an entity_ , hold the pointer over it and click its icon to move between different hierarchies of an entity. For more information about expanding and collapsing entities, see [Navigate entity hierarchies](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues#entity-hierarchies). 
  * To _view your selected metric for all traffic paths to an entity_ , hold the pointer over the entity. All entities that have a connection to this entity remain active, but all other entities are blurred. In the top-right corner of the screen, a card appears to list the name, type, and hierarchy of the entity. 
  * To _continue viewing the traffic paths of the entity_ , left-click the entity. This action selects the entity and puts a ring around its icon. 
  * To _select more entities_ and view their traffic paths, hold down the key that you use to select multiple files on your workstation (usually `control` or `shift`) and left-click each additional entity. 
  * To _remove an entity from the group of selected entities_ , hold down the `control` key on your keyboard and left-click the selected entity. 
  * To _discard the selected group of entities and select the current entity_ , click an entity without using the `control` key.

  
**Timeline** | Shows the full range of data that Network Topology has collected. The timeline is broken into hourly segments that you can select by using the slider. When you select a different time segment, the graph reloads. You can also select the current hour with incomplete data.  
**Date picker** | A control for choosing the date for which to show data.  
**Time slider** | Indicates the hourly segment for which Network Topology shows the data; you can drag it to select another segment.  
  
## What's next

  * [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)
  * [Troubleshoot Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting)
  * [Use case: Troubleshoot hybrid connectivity](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-hybrid-connectivity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
