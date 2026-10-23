---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb/
title: About utilization-based load balancers for GKE Services \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:51.422672+00:00
---

# About utilization-based load balancers for GKE Services  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About utilization-based load balancers for GKE Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page introduces utilization-based load balancing for Google Kubernetes Engine (GKE) Services, which evaluates the resource utilization of your backend Pods and uses actual workload capacity to intelligently rebalance traffic for increased application availability and flexible routing.

This page is for Cloud architects and Networking specialists who manage Services on GKE and want to optimize traffic distribution based on real-time resource utilization.

Before reading this page, make sure that you are familiar with the following:

  * **[GKE concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts)** : including GKE clusters, nodes, and Pods.
  * **[Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)** : how applications are exposed within Kubernetes.
  * **[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)** : a general understanding of Cloud Load Balancing, especially how Google Cloud load balancers work.
  * **[Kubernetes Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)** : the recommended method for exposing Services and managing traffic in GKE.
  * **[Network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs)** : how GKE Services use NEGs to integrate with Cloud Load Balancing.
  * **[Basic resource utilization metrics](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)** : for example, CPU utilization, which is the current metric used for utilization-based load balancing.



## Overview

The Cloud Load Balancing infrastructure routes traffic to GKE Services based on standard reachability metrics—including HTTP, HTTPS, HTTP/2, and gRPC—that determine Pod health and eligibility. By default, it forwards traffic to all healthy backend Pods by factoring in Pod availability and optionally defined traffic distribution policies, such as `GCPTrafficDistributionPolicy`.

Modern applications track CPU usage so you can understand costs, monitor performance, and effectively manage capacity. To meet this need, load balancers use real-time resource utilization data as a metric, which allows them to determine the optimal traffic volume each backend Pod can process for intelligent traffic distribution.

Utilization-based load balancing for GKE Services evaluates resource utilization as a metric to determine the ability of backend Pods to process application traffic. It then rebalances traffic to other backends if one or more Pods are over-utilized.

## Features and benefits

Utilization-based load balancing provides the following benefits:

  * **Increases application availability** : prioritizes traffic to Pods with lower resource utilization when backends are under pressure, which helps maintain application performance, prevents slowdowns and outages, and helps ensure a reliable experience for users.

  * **Offers flexible routing** : provides an additional set of metrics that let you define traffic distribution policies that align precisely with your business use cases.




## How utilization-based load balancing works

Utilization-based load balancing for GKE Services enhances how traffic is managed for your applications that run in GKE by making the process more responsive to resource load. Your application runs in GKE by using many instances (Pods) on different machines. It receives traffic in two main ways:

  * **From outside your cluster (north-south traffic)** : your cluster receives traffic from the internet or other external sources, which is known as north-south traffic. A GKE-managed Load Balancer (Gateway) directs this traffic from outside your cluster.

  * **From inside your cluster (east-west traffic)** : your cluster receives traffic flows between different parts of your application, from other services within your GKE cluster, or across multiple clusters. This internal traffic flow is known as east-west traffic.




Utilization-based load balancing for GKE Services involves a continuous process, where GKE agents collect Pod utilization metrics that enable the Cloud Load Balancing infrastructure to intelligently distribute traffic. The following steps summarize how utilization-based load balancing for GKE Services manages your application traffic based on real-time resource usage:

  1. When you set up your GKE Service with an Application Load Balancer (Gateway), GKE automatically creates NEGs for each zone and assigns your application's Pods to these NEGs. Initially, traffic distribution relies on basic health checks and your default settings.

  2. You configure your GKE Service to use resource utilization, like CPU, as a key metric for load balancing.

In addition to the default CPU utilization metric, you can expose custom metrics from your application for the load balancer to use. Using metrics from your application lets you define your own signals that are specific to your workload. For example, you can use the `gpu_cache_usage_perc metric` from a vLLM workload to help the load balancer direct traffic to the region with more available resources. To learn how to expose custom metrics for your load balancer, see [Expose custom metrics for load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics).

  3. A special GKE agent continuously monitors your Pods resource usage (for example, CPU) and sends this data to the Cloud Load Balancing infrastructure regularly. If a Pod has multiple containers, the agent calculates their combined utilization.

**Note:** Utilization-based load balancing works best when your Service's utilization changes gradually because utilization data updates at fixed intervals.
  4. The Cloud Load Balancing infrastructure analyzes real-time utilization data to dynamically adjust traffic distribution. It determines how much traffic to send to each group of Pods (each zonal NEG) by evaluating their average resource utilization (such as CPU load) and other factors like network latency. This process automatically shifts traffic from Pods with higher load to those with lower load, ensuring efficient resource utilization across your closest region.




The following example demonstrates how utilization-based load balancing works.

**Example** : Handling over-utilized Pods

When your Service runs multiple containers within the same Pod, the GKE metrics agent reports each container's resource use separately. The Cloud Load Balancing infrastructure then calculates a weighted average of their utilization to get the Pod's total capacity.

![Utilization-based load balancing for GKE Services.](https://docs.cloud.google.com/static/kubernetes-engine/images/ubb-traffic-handling.png)**Figure 1:** Intelligent traffic distribution based on backend CPU utilization in a GKE-managed load balancer setup.

Figure 1 shows how Cloud Load Balancing uses real-time CPU utilization metrics from GKE to optimize traffic distribution across Pods deployed in multiple zones. The client request is routed through the GKE Gateway to backend Pods that are grouped in NEGs across three zones.

  * In Zone 1, the Pod reports 90% CPU usage. The load balancer reduces traffic to this Pod to prevent overload.

  * In Zone 2, the Pod is moderately utilized at 60% CPU and continues to receive traffic.

  * In Zone 3, the Pod reports low CPU usage at 40% and might receive more traffic. GKE continuously sends metadata and utilization metrics to the Cloud Load Balancing infrastructure, which intelligently adjusts traffic routing to maintain application performance and availability.




Consider a scenario where your service is configured for a maximum CPU utilization of 80%. If Pods in Zone 1 report 90% CPU utilization, which exceeds the threshold, the following occurs:

  1. The Cloud Load Balancing infrastructure detects this over-utilization.
  2. It then intelligently rebalances traffic and reduces the amount of traffic that it sends to Pods in Zone 1. This rebalancing continues until the average CPU utilization for Pods in that zone falls back below the 80% utilization threshold.
  3. As Pods in Zone 1 report lower CPU utilization (under the 80% threshold), the Cloud Load Balancing infrastructure re-evaluates traffic distribution. It then gradually rebalances traffic across all of the Pods that back the service, and continues to distribute the traffic efficiently based on utilization.



## What's next

  * [Configure utilization-based load balancing for GKE Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-ubb)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
