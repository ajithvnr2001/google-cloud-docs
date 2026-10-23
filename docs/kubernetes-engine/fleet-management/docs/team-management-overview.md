---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview/
title: Use the team management overview \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:38.924572+00:00
---

# Use the team management overview  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Use the team management overview Stay organized with collections  Save and categorize content based on your preferences. 

With fleet team management, you can view team-scoped information such as resource utilization aggregated by team and by namespace, enabling you to optimize spending and resource allocation. The **Monitoring** tab within the **Teams** page in the Google Cloud console provides an overview of a specific team scope in your fleet.

This page assumes that you are familiar with resource management in Kubernetes. If you need to learn more, see [Resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the Kubernetes documentation.

## View the dashboard

To view the Monitoring dashboard:

  1. With your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) selected, go to the **Teams** section in the Google Cloud console.

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. In the **Teams** page, select the team scope whose details you want to view, and then click the **Monitoring** tab.




## Select a time filter

By default the team scope overview shows resource utilization over the past seven days. To change this time window, use the time filter options at the top of the page:

  * Select the time window over which you want to view the average resource utilization of the scope containers. Choose one of the predefined options, or select **Custom** to specify a custom time window.



## View team summary

The row below the time filters provides an at-a-glance view of your team scope including the number of clusters and namespaces, and total resource utilization over time. Resource utilization metrics are generated using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) data from your team's clusters. This section shows you:

  * The number of clusters and namespaces associated with the team. Click **View all clusters** or **View all namespaces** to see your team's full cluster or namespace list.
  * The number of errors in the team scope, if any. If an error is displayed, click **View in error logs** to get more details in the Logs Explorer.
  * The number of restarts across containers for your selected time interval. Click **View in restart logs** to view more details in the Logs Explorer.
  * The estimated monthly cost for the team scope. Click **View in Cost Optimization** to see more detailed [cost-related utilization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics) for the scope.
  * The average amount of CPU, Memory, and Disk utilization across namespaces for the selected time interval. For more information, see [Fleet resource utilization metrics](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics).

**Note:** If you have newly-created clusters in your team scope, depending on the time window you have chosen, you may not see any data in the **Total Utilization** card and the rest of the dashboard. For more information, see [Fleet resource utilization metrics](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics#troubleshooting).

## View detailed resource utilization

This section provides a detailed view of how your team is using its resources, including resource utilization by team, and top resource utilization by namespace. You can read about how these metrics are calculated in more detail in [Fleet resource utilization metrics](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics).

### View resource utilization over time

The **CPU/memory/disk utilization by team** sections show how your team uses resources over time, and how the clusters within your scope request resources compared with the set resource limits. Each panel shows a graph of your team-aggregated CPU, memory, or disk usage over the time window you have chosen, with the following information displayed as separate lines:

  * **Limit** : The maximum amount of the resource that containers across your team scope are allowed to use, for example, 42.5 CPUs.
  * **Requested** : The amount of the resource that containers across your scope have requested, for example, 3.8 CPUs.
  * **Used** : The actual amount of the resource that your containers used, for example, 0.64 CPUs.



To see details for a given point on the graph, scroll across the graph to the time that you are interested in (for example, a visible spike in actual usage on the graph). The resource limit, and requested and actual resource usage information for that time is displayed.

To toggle the display of one or more of the lines in the chart, click the relevant metric or metrics below the graph.

### View top resource utilization by namespace

The **Top CPU/memory/disk utilization by namespace** row shows you the five namespaces that are the biggest users of their resources. Each panel lists your top namespaces in order of utilization (highest first). For each namespace, you can see both a graph of their usage of the resource, and an average of their resource usage relative to the resource limit, and used and requested resources over the chosen time window. This view can help you, for example, to see namespaces that are overutilized.

To view resource utilization for all your namespaces for your chosen time window, click on **View all namespaces by CPU/memory/disk utilization**.

### View error distribution by namespace

This card indicates the namespaces with the most error logs for the time window you have chosen. To view log details, click on **View all errors in Cloud Logging**.

### View restart counts distribution by namespace

This section shows you the namespaces with the highest number of container restarts for the time window you have selected. This can help you assess, for example, if you need to adjust the CPU limit and requested CPU amount if a container has restarted because of CPU usage. To view log details, click on **View all restarts in Cloud Logging**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
