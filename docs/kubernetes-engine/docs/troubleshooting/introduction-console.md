---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-console/
title: Assess cluster and workload health in the Google Cloud console \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:34:33.008434+00:00
---

# Assess cluster and workload health in the Google Cloud console  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Assess cluster and workload health in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When you need to quickly check the health of your Google Kubernetes Engine (GKE) clusters and workloads, it can be hard to know where to start. Visualizing the health of your clusters and workloads in the Google Cloud console helps you quickly assess the state of your environment. _Cluster health_ refers to the health of the underlying GKE infrastructure like nodes and networking, while _workload health_ refers to the status and performance of your apps running on the cluster.

Use this page to learn how to navigate the Kubernetes clusters and workloads pages to get a high-level overview, identify potential issues (like nodes under resource pressure or failing Pods), and drill down into specific resources for more details.

This information is important for Platform admins and operators who are responsible for maintaining cluster stability and need to perform quick health assessments and resource checks. It's also essential for Application developers who need to understand the runtime status of their deployments and investigate failures. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

To provide a complete picture of your app's health, the Google Cloud console also gives you access to powerful logging and monitoring tools, letting you investigate the root cause of past failures and proactively prevent future ones. For more information about these tools, see [Conduct historical analysis with Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging) and [Perform proactive monitoring with Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring).

## Find cluster issues

The **Kubernetes clusters** page provides you with an overview of the health of your clusters. To identify problems with any of your clusters, start on this page.

  * To get started, in the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)




Here are some examples of how you can use this page for troubleshooting:

  * For advice on improving the health of your cluster, your upgrade strategy, and cost optimization, click **View recommendations**.
  * To identify unhealthy clusters, review the **Status** column. Any cluster that doesn't have a green checkmark needs attention.
  * To see potential issues, review the **Notifications** column. Click any notification messages for more information.



## Investigate a specific cluster

After you discover a problem with a cluster, explore the cluster's **Details** page for in-depth information that helps you troubleshoot your cluster and understand its configuration.

To go to a cluster's **Details** page, do the following:

  1. Go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Review the **Name** column and click the name of the cluster that you want to investigate.




Here are some examples of how to use the cluster **Details** page to troubleshoot your cluster:

  * For general health checks, try the following options:

    * To view cluster-level dashboards, go to the **Observability** tab. By default, GKE enables Cloud Monitoring when you create a cluster. When Cloud Monitoring is enabled, GKE automatically sets up the dashboards on this page. Here are some of the views you might find most useful for troubleshooting:

      * **Overview** : view a high-level summary of your cluster's health, resource utilization, and key events. This dashboard helps you quickly assess the overall state of your cluster and identify potential issues.
      * **Traffic metrics** : view node-based networking metrics for insights into the traffic between your Kubernetes workloads.
      * **Workload state** : view the state of Deployments, Pods, and containers. Identify failing or unhealthy instances, and detect resource constraints.
      * **Control plane** : view the control plane's health and performance. This dashboard lets you monitor key metrics of components such as `kube-apiserver` and `etcd`, identify performance bottlenecks, and detect component failures.

**Tip:** These dashboards can serve as a starting point for creating customized dashboards. You can copy a predefined dashboard and then customize it to include specific metrics, filters, or visualizations relevant to your needs.
    * To view recent app errors, go to the **App errors** tab. The information on this tab can help you prioritize and resolve errors by showing the number of occurrences, when an error first appeared, and when it last happened.

To investigate an error further, click the error message to view a detailed error report, including links to relevant logs.

  * If you're troubleshooting issues after a recent upgrade or change, check the **Cluster basics** section in the cluster **Details** tab. Confirm that the version listed in the **Version** field is what you expect. For further investigation, click **Show upgrade history** in the **Upgrades** section.

  * If you're using a Standard cluster and your Pods are stuck in a `Pending` state, or you suspect that nodes are overloaded, check the **Nodes** tab. The **Nodes** tab isn't available for Autopilot clusters because GKE manages nodes for you.

    * In the **Node Pools** section, check that autoscaling is configured correctly and that the machine type is appropriate for your workloads.
    * In the **Nodes** section, look for any node with a status other than `Ready`. A `NotReady` status indicates a problem with the node itself, such as resource pressure or an issue with the kubelet (the kubelet is the agent that runs on each node to manage containers).



## Find workload issues

When you suspect that there's a problem with a specific app, like a failed Deployment, go to the **Workloads** page in the Google Cloud console. This page provides a centralized view of all of the apps that run within your clusters.

  * To get started, in the Google Cloud console, go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)


**Tip:** If you work in a project with many resources, use the **Filter** bar to narrow the view to a specific cluster or namespace.

Here are some examples of how you can use this page for troubleshooting:

  * To identify unhealthy workloads, review the **Status** column. Any workload that doesn't have a green checkmark needs attention.
  * If an app is unresponsive, review the **Pods** column. For example, a status like **1/3** means only one of three app replicas is running, indicating a problem.



## Investigate a specific workload

After you identify a problematic workload from the overview, explore the workload **Details** page to begin to isolate the root cause.

To go to a workload's **Details** page, do the following:

  1. Go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. View the **Name** column and click the name of the workload that you want to investigate.




Here are some examples of how to use the workload **Details** page to troubleshoot your workloads:

  * To check the workload's configuration, use the workload **Overview** and **Details** tabs. You can use this information to verify events such as whether the correct container image tag was deployed or check the workload's resource requests and limits.

**Note:** Depending on your workload type, you might not have an **Overview** tab. For example, StatefulSets have only a **Details** tab. However, both tabs help you review your configuration.
  * To find the name of a specific crashing Pod, go to the **Managed Pods** section. You might need this information for `kubectl` commands. This section lists all the Pods controlled by the workload, along with their statuses.

  * To see a history of recent changes to a workload, go to the **Revision history** tab. If you notice performance issues after a new Deployment, then use this section to identify which revision is active. You can then compare the configurations of the current revision with previous ones to pinpoint the source of the problem. If this tab isn't visible, the workload is either a type that doesn't use revisions or it hasn't yet had any updates.

  * If a Deployment seems to have failed, go to the **Events** tab. This page is often the most valuable source of information because it shows Kubernetes-level events.

  * To look at your app's logs, click the **Logs** tab. This page helps you understand what's happening inside your cluster. Look here for error messages and stack traces that can help you diagnose issues.

  * To confirm exactly what was deployed, view the **YAML** tab. This page shows the live YAML manifest for the workload as it exists on the cluster. This information is useful for finding any discrepancies from your source-controlled manifests. If you're viewing a single Pod's YAML manifest, this tab also shows you the status of the Pod, which provides insights about Pod-level failures.




## What's next

  * Read [Investigate a cluster's state with `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-kubectl) (the next page in this series).

  * See these concepts applied in the [example troubleshooting scenario](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
