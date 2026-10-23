---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues/
title: Quickstart: Monitor your networking configuration with Network Topology \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:59.446434+00:00
---

# Quickstart: Monitor your networking configuration with Network Topology  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor your networking configuration with Network Topology

You can use Network Topology to audit your networking configuration or troubleshoot networking issues. Network Topology provides a graph view of your networking infrastructure.

You can start using Network Topology by going to the Google Cloud console. No additional configurations are required.

## Before you begin

Get an overview of [Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview) and its [topology interface](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview).

### Required roles and permissions

To get the permissions that you need to view network topology and metrics, ask your administrator to grant you the following IAM roles on your project: 

  * [Network Management Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view network topology and metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view network topology and metrics:

  * View the Network Topology graph for a project or monitored projects: `networkmanagement.topologygraphs.read`
  * View a Network Topology graph for multiple projects: `networkmanagement.topologygraphs.read`
  * View the metrics on the Network Topology graph: `monitoring.timeSeries.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about the required permissions and roles, see [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/access-control).

### Add multiple projects to a single graph

Network Topology can visualize entities from multiple projects in a single graph. For example, in Shared VPC scenarios, you can view a graph that includes entities from the host and service projects.

To include multiple projects in a graph, see [View metrics for multiple Cloud projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

If you have a multi-project graph, you can aggregate entities by project.

The following sections describe how to use different features of the Network Topology interface such as filtering or navigating entity hierarchies.

### Disable cross-project telemetry

Google Cloud collects cross-project network telemetry. By default, cross-project telemetry is enabled for your organization. The collected network telemetry is not exported to monitoring and diagnostic services such as Cloud Monitoring and Network Intelligence Center.

If you don't want Google Cloud to collect cross-project telemetry, you can disable collection for your entire organization. Telemetry data collected earlier is stored for the retention period. For more information, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkmanagement.config.get`
  * `networkmanagement.config.update`



**Roles**

  * Network Management Admin (`roles/networkmanagement.admin`)



###  Console 

  1. In the Google Cloud console, go to the **Cross-project telemetry** page. 

[Go to Cross-project telemetry](https://console.cloud.google.com/net-intelligence/cross-project-metric)

  2. Select **Disable cross-project telemetry**.
  3. Click **Save Changes**.



## Show or hide hierarchies and particular levels

You can select which hierarchy and their levels to show in the graph. You might want to do this to show or hide certain resource types. For example, you can clear the entire **External clients** hierarchy checkbox so that you see only the communication between your Google Cloud resources. In the graph, external clients and any traffic to and from them are hidden.

If you clear a specific level of a hierarchy, Network Topology hides it. For example, if you clear the **Region network** and **Subnetwork** checkboxes for VM instances, Network Topology shows instances by zone in each region, which is the next level in the hierarchy after networks and subnets.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the **View options** > **Topology configuration** , select or clear a hierarchy checkbox to include or exclude an entire hierarchy, including its base entities.
  3. To toggle a specific level of a hierarchy, click more_vert**More** next to the relevant hierarchy. You cannot clear some levels because they are required for visualizing entities in the graph.



## Filter specific entities

Use filtering to show specific entities, such as a certain region, zone, or instance group. If you already know which resources you're investigating, use filtering to view them in the graph. Network Topology shows the filtered entities and any peers that communicated with them. The filter feature lets you do the following:

  * Filter entities of any level in the hierarchy.

  * Use the asterisk (*) while specifying the names of entities to search and filter. For example, you can use the value `*replica*` to search for all entities containing _replica_ in their name. You can place an asterisk anywhere within the pattern. For example, the `Instance: www-*europe*` filter matches both `www-service-europe-f9vq` and `www-static-europe-a5hj` instances.

  * Specify multiple filters. Network Topology shows any entity that matches at least one of the filters.




Filtering is case-insensitive.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the **View options** , select the **Topology configuration** section.
  3. In the **Filter** field, select an entity type key such as **Region** or **HTTPS load balancer**.

Network Topology shows filtering hints that correspond to entities present in the displayed graph. For example, if you clear the **Load balancers** checkbox in the topology configuration panel, Network Topology doesn't show filtering hints that are related to load balancers.

  4. Select a value for the filter such as **us-east4** or **my-load-balancer**.

Network Topology provides values that apply to your graph. For example, Network Topology doesn't show all Google Cloud regions for the **Region** filter. It shows only the regions that contain resources.




## Filter nodes in the GKE Enterprise view

You can filter and view specific nodes such as clusters, workloads, and Pods in the GKE Enterprise view.

**Note:** GKE Enterprise view is available only for GKE Enterprise projects.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the **View options** , select a metric from the **Metrics and insights** section.
  3. In the **Filter** section, click **Add filter** to select a node and its peers. This section is available only for metric views and not for the insights views.
  4. Select the type of the node from the **Type** list.
  5. Select the node from the **Node** list.



## Navigate entity hierarchies

When you load a graph, all of the top-level entities are aggregated into their top-level hierarchies. You can expand an entity to view its lower-level entities. You can also collapse entities that you have expanded.

For example, you can expand a region to see all of the VPC networks that are in that region. The parent entity continues to visually wrap the lower-level entities. If, for example, you drag the region entity, the networks that are inside the region move with it.

For more information about entities and their hierarchies, see [Entities](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#entities) in the Network Topology overview.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. Hold the pointer over an entity to display the **Expand** ![icon for expanding](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/expand.svg) or **Collapse** ![icon for collapsing](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/icons/collapse.svg) icon.

If an entity is collapsed, Network Topology shows the **Expand** icon. If an entity is expanded, Network Topology shows the **Collapse** icon.

  3. Click the **Expand** or **Collapse** icon.

  4. In the configuration pane, to display only the traffic paths between top-level entities, such as regions, select the **Show connections for child nodes only on focus** checkbox.

To view the traffic paths between lower-level entities, select or hold the pointer over the lower-level entities.

To display all the traffic paths, clear the checkbox.




## View metrics for traffic between entities

By default, Network Topology overlays throughput values on each connection so that you can see the amount of traffic going between entities. You can also change which metric Network Topology overlays on connections. If the selected metric is not relevant for a connection, Network Topology does not overlay a value for that connection.

  * For information about the supported metrics for each connection, see [Network Topology metrics](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference).
  * For information about the various metrics in the Infrastructure view and the GKE Enterprise view, see [Metrics for entities](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#view-metrics).
  * For information about the Network Topology interface, including where you can change the overlay metric, see [View graph interface elements](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/graph-overview).



Metric values are based on the selected hour. For more information, see [Data collection and freshness](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#data).

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. Select the **Infrastructure** view or the **GKE Enterprise** view.
  3. In the **View options** , select a metric from the **Metrics and insights** section.

  4. Navigate to a specific entity hierarchy to view traffic that is related to that entity.

For example, if you want to view throughput between a zone and other regions, you must expand entities until you see that zone.

  5. Click the entity to highlight all of its traffic paths.

Network Topology displays metric values for each connection that supports the selected metric.




### View the most forwarded and most dropped traffic flows in the GKE Enterprise view

You can view the following traffic flow details in the GKE view:

  * **Most forwarded flows** displays the current traffic within the GKE cluster.
  * **Most dropped flows** helps to identify or debug issues in the GKE applications. You can also view the reasons for the drops in the charts available in the details panel.

**Note:** GKE Enterprise view is available only for GKE Enterprise projects.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. Select the **GKE Enterprise** view.
  3. In the **View options** , select **Network verdict** from the **Metrics and insights** section.
  4. Enter the name of the cluster or select a cluster from the available options.
  5. Select one of the traffic flow options to view a ranked table of outliers with the traffic from selected cluster.
  6. Click **Download CSV** to download the table for further processing of the details.

  7. Navigate to a specific entity hierarchy to view traffic that is related to that entity.

  8. Click the entity to highlight all of its traffic paths.

Network Topology displays metric values for each connection that supports the selected metric.




## View time series charts

Network Topology can show time series charts for some entities. For example, Network Topology can show the CPU utilization for an instance or the latency between a load balancer and one of its backends.

These charts show minute-by-minute values. Data for the charts are available to you within seven minutes after an activity.

### View metrics related to traffic

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. Navigate to a specific entity hierarchy to view traffic that is related to that entity.

For example, if you want to see latency between a load balancer and other entities, you must expand entities until you see the load balancer.

  3. Click the entity to highlight all of its traffic paths.

  4. Click the metrics overlaid on the connection to view its details.

Network Topology shows charts in the details pane. The information includes ingress and egress traffic between your selected entity and the connected entity. The metric values are for the selected hourly segment. If you're viewing the most recent segment, the metrics show real-time values.




### View metrics related to an entity

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. Find and expand the entity hierarchy until you see the entity that you want to view metrics for.

  3. Click the entity.

Network Topology shows charts in the details pane. For example, for a VM instance, you can view the CPU utilization rate and the percentage of memory used. The metric values are for the selected hourly segment. If you're viewing the most recent segment, the metrics show real-time values.




## View insights for entities with high metric values

View ranked outlier egress metrics for instances and instance groups in addition to the average hourly throughput, average hourly packet loss, and median latency metrics.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the **Metrics and insights** section, select an insight from the options.

The **Types of egress** list appears when you select **High egress instances** , **High egress instance groups** , or **High egress GKE workloads**.

  3. Select the traffic type from the **Types of egress** list. In the Infrastructure view, select one of the following options:

     * **Cross-zonal:** displays a ranked table of outliers with the traffic between Google Cloud zones and excludes the traffic between entities within the same zone
     * **To the internet:** displays a ranked table of outliers with the traffic from Google Cloud to external endpoints, excluding hybrid traffic
     * **Hybrid:** displays a ranked table of outliers with the traffic through Cloud VPN, Cloud Interconnect, and router appliances
     * **All measured egress:** displays a ranked table of outliers with the traffic from an entity

In the **GKE Enterprise** view, select one of the following options: \- **Cross-zonal:** displays a ranked table of outlier GKE workloads with the traffic between Google Cloud zones and excludes the traffic between entities within the same zone \- **All measured egress:** displays a ranked table of outlier GKE workloads with the traffic from an entity

  4. To highlight all the traffic paths of an entity, click or point to the entity.

  5. To view the metric details, click the metrics overlaid on the connection.




Network Topology shows charts in the details pane. The information includes ingress and egress traffic between your selected entity and the connected entity. The metric values are for the selected hourly interval. If you're viewing the most recent time interval, the metrics show current values.

## View metrics, alerts, events, and logs for Pods, workloads, and clusters

View specific details such as metrics, alerts, events, and logs in addition to the average hourly throughput and median latency metrics.

**Note:** GKE Enterprise view is available only for GKE Enterprise projects.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page.

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology/gke)

  2. On the **GKE Enterprise** tab, you can view metrics related to an entity. Network Topology shows charts in the details pane.

  3. Click **Operations**. Network Topology shows the details panel.

  4. In the Pod details panel, you can perform the following actions:

     * **Metrics:** View container metrics, Pod metrics, and node metrics. You can also download the metric-related graphs in PNG and CSV format.
     * **Alerts:** View existing alerts or create new alert policies.
     * **Events:** View any Kubernetes events or choose to view in Logging.
     * **Logs:** View logs based on the chosen severity. You can also filter further using fields and values.



## Select an hourly segment

You can select a particular hourly segment to view the entities and their communication relationships that existed during that hour. When you first load a graph, Network Topology visualizes the most recently completed hour, but the metrics are from the last few minutes. For more information about data freshness, see [Data collection and freshness](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#data).

To select different hourly segments, use the timeline and drag the slider to a particular hour.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the timeline, drag the slider to the hourly segment to view.

Network Topology refreshes the graph with information for that segment.




## Show only the current project or all projects

In [multi-project scenarios](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#multi-project), you can select the **Show all projects in the Workspace** checkbox to show all the projects in your [metrics scope](https://docs.cloud.google.com/monitoring/settings) or only your current project.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the **View options** , select the **Topology configuration** section.
  3. Select the **Show all projects in the Workspace** checkbox. To show only your current project, clear the checkbox.

Network Topology redraws the graph and shows all the projects in your [metrics scope](https://docs.cloud.google.com/monitoring/settings) or only your current project.




## Aggregate entities by project

In [multi-project scenarios](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#multi-project), you can aggregate entities by project. That way, you can view and filter your resources by project and then by their standard hierarchies.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the **View options** , select the **Topology configuration** section.
  3. Select **Project aggregation**.

Network Topology redraws the graph and aggregates Google Cloud entities by project.




## Use generated queries to retrieve detailed logs

If you have VPC Flow Logs enabled, you can look up detailed flows between an instance and another entity. If the logs are exported to BigQuery, you can copy queries that are generated by Network Topology and use them in BigQuery to view detail logs for a particular flow.

Network Topology generates queries for certain VM flows. If Network Topology overlays throughput metrics on a connection, it can generate a query for it. The generated query limits logs to the selected hourly segment.

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. Expand the entities that contain the instance to investigate.

  3. Click the instance to highlight all of its connections.

  4. Click the throughput metric to view the connection's details pane.

  5. In the details pane, under **View flows in BigQuery** , click **Instructions**.

  6. If you have not already, follow the instructions under **Before you begin** to configure log exporting to a BigQuery sink and enable VPC Flow Logs. The instructions provide a table that lists the subnets that are relevant to the selected connection. The **VPC Flow Logs status** column indicates whether VPC Flow Logs is enabled.

  7. Follow the instructions under **Running the query** to copy the generated query and run it in BigQuery.

BigQuery returns logs that you can use to further investigate or troubleshoot issues.




## What's next

  * [Use case: Audit network performance](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance)
  * [Use case: Troubleshoot network connectivity](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-network-connectivity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
