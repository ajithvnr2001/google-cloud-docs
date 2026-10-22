---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard/
title: Use the GKE overview dashboard \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:46.818666+00:00
---

# Use the GKE overview dashboard  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Use the GKE overview dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The GKE overview dashboard in the Google Cloud console provides a "big picture" overview of your fleet. The overview helps you use your GKE features by showing you how many security concerns your fleet has, your fleet-wide Policy Controller coverage, and the synchronization status of your Config Sync packages. In addition, the dashboard provides a fleet-level view of resource utilization of your fleets, clusters, and teams. You can use this information to help optimize spending, application design, and resource allocation, including CPU, memory, and disk utilization.

Before reading this page, ensure that you're familiar with Kubernetes resource management, as described in the [Resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) Kubernetes documentation.

## View the overview

To view the overview dashboard:

  * With your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) selected, go to the GKE overview in the Google Cloud console.

[Go to the GKE overview](https://console.cloud.google.com/kubernetes/overview/)




## Select a time filter

By default the GKE overview shows resource utilization over the past one hour. To change this time period, use the time filter option:

  * Select the period over which you want to view the average resource utilization of the fleet containers. Choose one of the predefined options, or select **Custom** to specify a custom time period.



## View clusters, team scopes, cost, and total resource utilization

The first section provides an at-a-glance view of your clusters, team scopes, estimated cost of your fleet, and the total CPU/memory/disk utilization over the time period that you've chosen. Resource utilization metrics are generated using system [ Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) data from your fleet's clusters.

If you see the **Missing data from...** notification, see the Enable system Cloud Monitoring for fleet clusters section to resolve the problem.

### View cluster status

In the **Clusters in this Fleet** section, you can see how many clusters are in your fleet. If there are any issues with the cluster's connectivity to the fleet, there are warnings or errors displayed: for example, if you have deleted a cluster without unregistering it first, or if you need to [log in to a cluster outside Google Cloud](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#view_registered_clusters) to see its details.

  * If an error or warning is displayed, click the notification to see the problem cluster or clusters and fix the issue.
  * Click **View all clusters** to see the full cluster list of your fleet.



### View team scopes

In the **Team scopes** section, you can see the number of team scopes in this fleet. Team scopes let you define subsets of fleet resources on a per-team basis. After you've defined these scopes you can use [team management features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management) so that each team can act as a separate "tenant" on your fleet.

  * Click **View all team scopes** to see the full list of team scopes in your fleet.



### View estimated monthly cost

In the **Estimated monthly cost** section, you can see the estimated monthly cost of all your fleet resources.

  * Click **View in Cost Optimization** to see more detailed [cost-related utilization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics) for your fleet.



### View total resource utilization

The **Total utilization** section shows the average usage of all your fleet containers' actual CPU, memory, and disk resources, relative to allocatable resources across cluster nodes in this fleet. Data is displayed over the time period that you have chosen. _Allocatable_ on a Kubernetes node is defined as the amount of resources that can be used by regular Pods on that node.

This view gives you a quick overview of your fleet's resource utilization and available resources, and can indicate possible issues to investigate further with more detailed metrics. For example, if total CPU utilization is very low, you can use the "by cluster" metrics to identify clusters that you could resize.

## View feature management

### View security concerns

To help you identify security issues that affect your fleet's member clusters, such as active vulnerabilities or workload configuration issues, view the **Security concerns** section. This section shows you the following information:

  * The total number of concerns found in your fleet. Concerns are grouped by severity, and severity is assigned based on the [CVSS Qualitative Severity Rating Scale](https://www.first.org/cvss/specification-document#Qualitative-Severity-Rating-Scale).
  * A breakdown of concerns by type. This helps you to identify whether the issues are coming from configuration problems, a security bulletin, or a vulnerability.



To see an overview of your GKE security, and to view actionable advice on how to resolve any concerns that were discovered, click **View security posture**. If you haven't used the security posture dashboard before, click **Enable security posture** to enable the Container Security API and access the security posture dashboard.

You can learn more in [About the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard).

### View Policy Controller coverage

Policy Controller enables the enforcement of fully programmable policies for your clusters. These policies act as "guardrails" and prevent any changes to the configuration of the Kubernetes API from violating your organization's security, operational, or compliance controls.

The **Policy status** section shows you how many clusters have Policy Controller enabled.

Click **View Policy** to view the [Policy Controller dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status). If you haven't installed Policy Controller on a cluster, click **Enable Policy**.

You can learn more about Policy Controller in its [documentation](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller).

### View Config Sync package health

Config Sync is a GitOps service that lets cluster operators and platform administrators deploy packages from a source of truth. A package contains all of the configurations that are contained in each source that you sync your cluster from. The source might be a Git repository, a directory in a Git repository, an OCI image, or a Helm repository. Because you can sync your cluster from multiple sources, you might have multiple packages per cluster.

The **Config status** section shows you the following information:

  * The total number of packages in your fleet
  * The synchronization status of the packages in your fleet



Click **View Config overview** to view the [Config Sync dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/use-config-sync-dashboard). If you haven't installed Config Sync on a cluster, click **Enable Config Sync**.

You can learn more about Config Sync in its [documentation](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview).

## View fleet efficiency

This section provides a detailed view of how your fleet is using its cloud or on-premises resources, including resource utilization by fleet, and top and low resource utilization by cluster. This can help you see, for example, where you have potentially underutilized or overutilized clusters that you might want to resize. You can read about how these metrics are calculated in more detail in [Fleet resource utilization metrics](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics).

### View resource utilization over time

The **CPU/memory/disk utilization by fleet** row lets you dig deeper into how your fleet uses resources over time. It also lets you see requested resources from your clusters, allocatable resources, and actual usage. Each panel shows a graph of your fleet-aggregated CPU, memory, or disk usage over the time period you have chosen, with the following information displayed as separate lines:

  * **Allocatable** : The amount of the resource that is allocatable across your fleet cluster nodes
  * **Requested** : The amount of the resource that containers across your fleet have requested
  * **Used** : The actual amount of the resource that your containers used



To see details for a given point on the graph, scroll across the graph to the time that you are interested in (for example, a visible spike in actual usage on the graph). The allocatable, requested, and actual resource usage information for that time is displayed.

To toggle the display of one or more of the lines in the chart, click the relevant metric or metrics under the graph.

### View top resource utilization by cluster

The next row shows your fleet's **Top CPU/memory/disk utilization by cluster** , letting you quickly see which specific clusters are the biggest users of their allocatable resources. Each panel lists your top five clusters in order of utilization (highest first). For each cluster, you can see both a graph of their usage of the resource, and an average of their resource usage relative to their allocatable resources over the chosen time period. This view can help you, for example, to see clusters that are overutilized. Clusters that don't have enough resources available might not be able to schedule Pods.

Click the name of the cluster that you're interested in to see more details about how the cluster is using its resources. In the utilization view, you can also see how many container restarts and error logs your cluster has.

Click **View all clusters by CPU/memory/disk utilization** to view a sorted list of all clusters in your fleet.

### View low resource utilization by cluster

The final resource utilization row shows your fleet's **Low CPU/memory/disk utilization by cluster** , so that you can quickly see which clusters are underutilized. The five clusters using the least resources appear at the top of each panel, with a graph of their usage, and an average of the resource usage relative to their allocatable resources over the chosen time period.

Click the name of the cluster that you're interested in to see more details about how the cluster is using its resources. In the utilization view, you can also see how many container restarts and error logs your cluster has.

Click **View all clusters by CPU/memory/disk utilization** to view a sorted list of all clusters in your fleet.

## View team efficiency

This section provides an overview view of how your teams are using their cloud or on-premises resources. It also helps you monitor which teams are encountering issues.

Click the team that you're interested in to drill down further in the [team dashboard](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview). In the team dashboard, you can see more details about resource utilization and the team's namespaces. This can help you see which namespaces are affecting the team's resource usage.

### View top resource utilization by team scope

**CPU/memory/disk utilization by scope** lets you quickly see which specific teams are the biggest users of their resources. Each panel lists your top teams in order of utilization (highest first). For each team, you can see both a graph of their usage of the resource, and an average of their resource usage relative to the request.

To view resource utilization for all your teams for your chosen time window, click **View all teams by CPU/Memory/Disk utilization**.

### View error distribution by scope

This card indicates the teams with the most error logs for the time window you have chosen.

To view a list of teams sorted by error count, click **View all scopes by error counts**.

### View restart counts by scope

This section shows you the teams with the highest number of container restarts for the time window that you have selected.

To view a list of teams sorted by restarts, click **View all scopes by restarts**.

## Enable system Cloud Monitoring for fleet clusters

As mentioned in the View clusters, team scopes, and total resource utilization section, the metrics in the dashboard are generated using Cloud Monitoring data for cluster components (such as workloads in the `kube-system` and `gke-connect` namespaces). Because of this, Cloud Monitoring must be enabled for all system, control plane, and kube state metrics components of your fleet member clusters.

Most GKE clusters have Cloud Logging and Cloud Monitoring enabled by default, but you still need to manually enable Cloud Monitoring for all cluster components. Attached clusters _always_ require you to set up Cloud Monitoring manually.

If any of your fleet's cluster components do _not_ have Cloud Monitoring enabled, a panel is displayed at the top of the page showing the number of clusters with missing data.

To enable Cloud Monitoring for components on these clusters, see the following guides for your cluster type:

  * [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing)
  * [Use Cloud Logging and Cloud Monitoring with Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/logging-and-monitoring#stackdriver)
  * [Configuring Cloud Logging and Cloud Monitoring for Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring)
  * Monitoring for attached clusters: 
    * [Install Cloud Monitoring on EKS attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/install-cloud-monitoring)
    * [Install Cloud Monitoring on AKS attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/install-cloud-monitoring)
    * [Install Cloud Monitoring on other conformant cluster types](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/install-cloud-monitoring)
  * [Authorize logging and monitoring for GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/how-to/create-cluster#telemetry-agent-auth)
  * [Authorize logging and monitoring for GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure/how-to/create-cluster#telemetry-agent-auth)
  * [Logging and monitoring for GKE on AWS (previous generation)](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/how-to/logging-and-monitoring)

**Note:** If you've just enabled Cloud Monitoring, it might take some time for your cluster's data to appear in the Google Cloud console.

### Enable monitoring for cross-project registered clusters

To gather and view metrics across multiple Google Cloud projects, Cloud Monitoring lets you create [multi-project metrics scopes](https://docs.cloud.google.com/monitoring/settings). When you register a GKE cluster [from a different project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project) to your fleet host project, a new metrics scope is automatically created that includes both projects (if it doesn't already exist). This lets you see utilization data from the cluster in the overview.

## What's next

  * Learn more about the resource utilization metrics in the dashboard and how to use them in [Fleet resource utilization metrics](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics)
  * Learn more about using [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) and [ Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to observe your clusters and their workloads.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
