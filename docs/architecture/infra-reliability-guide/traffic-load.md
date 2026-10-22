---
url: https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load/
title: Manage traffic and load for your workloads in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:37.367816+00:00
---

# Manage traffic and load for your workloads in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Manage traffic and load for your workloads in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-23 UTC

When you run an application stack on distributed resources in the cloud, network traffic must be routed efficiently to the available resources across multiple locations. This part of the [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide) describes traffic- and load-management techniques that you can use to help to improve the reliability of your cloud workloads.

## Capacity planning

To ensure that your application deployed in Google Cloud has adequate infrastructure resources, you must estimate the capacity that's required, and manage the deployed capacity. This section provides guidelines to help you plan and manage capacity.

### Forecast the application load

When you forecast the load, consider factors like the number of users and the rate at which the application might receive requests. In your forecasts, consider historical load trends, seasonal variations, load spikes during special events, and growth driven by business changes like expansion to new geographies.

### Estimate capacity requirements

Based on your deployment architecture and considering the performance and reliability objectives of your application, estimate the quantity of Google Cloud resources that are necessary to handle the expected load. For example, if you plan to use Compute Engine managed instance groups (MIGs), decide the size of each MIG, VM machine type, and the number, type, and size of persistent disks. You can use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) to estimate the cost of the Google Cloud resources.

### Plan adequate redundancy

When you estimate the capacity requirements, provide adequate redundancy for every component of the application stack. For example, to achieve [N+1 redundancy](https://en.wikipedia.org/wiki/N%2B1_redundancy), every component in the application stack must have at least one redundant component beyond the minimum that's necessary to handle the forecast load.

### Benchmark the application

Run load tests to determine the resource efficiency of your application. Resource efficiency is the relationship between the load on the application and the resources such as CPU and memory that the application consumes. The resource efficiency of an application can deteriorate when the load is exceptionally high, and the efficiency might change over time. Conduct the load tests for both normal and peak load conditions, and repeat the benchmarking tests at regular intervals.

### Manage quotas

Google Cloud service [quotas](https://docs.cloud.google.com/docs/quotas/overview) are per-project limits, which help you control the consumption of cloud resources. Quotas are of two types: _Resource quotas_ are the maximum resources that you can create, such as the number of regional [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/quotas) in a region. _Rate quotas_ limit the number of API requests that can be sent to a service in a specific period. Quotas can be zonal, regional, or global. Review the current resource quotas and API rate quotas for the services that you plan to use in your projects. Ensure that the quotas are sufficient for the capacity that you need. When required, you can [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

### Reserve compute capacity

To make sure that capacity for Compute Engine resources is available when necessary, you can create reservations. A reservation provides assured capacity in a specific zone for a specified number of VMs of a machine type that you choose. A reservation can be specific to a project, or shared across multiple projects. For more information about reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

### Monitor utilization, and reassess requirements periodically

After you deploy the required resources, monitor the capacity utilization. You might find opportunities to optimize cost by removing idle resources. Periodically reassess the capacity requirements, and consider any changes in the application behavior, performance and reliability objectives, user load, and your IT budget.

## Autoscaling

When you run an application on resources that are distributed across multiple locations, the application remains available during outages at one of the locations. In addition, redundancy helps ensure that users experience consistent application behavior. For example, when there's a spike in the load, the redundant resources ensure that the application continues to perform at a predictable level. But when the load on the application is low, redundancy can result in inefficient utilization of cloud resources.

For example, the shopping cart component of an ecommerce application might need to process payments for 99.9% of orders within 200 milliseconds after order confirmation. To meet this requirement during periods of high load, you might provision redundant compute and storage capacity. But when the load on the application is low, a portion of the provisioned capacity might remain unused or under-utilized. To remove the unused resources, you would need to monitor the utilization and adjust the capacity. Autoscaling helps you manage cloud capacity and maintain the required level of availability without the operational overhead of managing redundant resources. When the load on your application increases, autoscaling helps to improve the availability of the application by provisioning additional resources automatically. During periods of low load, autoscaling removes unused resources, and helps to reduce cost.

Certain Google Cloud services, like Compute Engine, let you configure autoscaling for the resources that you provision. Managed services like Cloud Run can scale capacity automatically without you having to configure anything. The following are _examples_ of Google Cloud services that support autoscaling. This list is not exhaustive.

  * **Compute Engine:** MIGs let you scale stateless applications that are deployed on Compute Engine VMs automatically to match the capacity with the current load. For more information, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).
  * **GKE:** You can configure GKE clusters to automatically resize the node pools to match the current load. For more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler). For GKE clusters that you provision in the [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#scaling) mode, GKE automatically scales the nodes and workloads based on the traffic.
  * **Cloud Run:** Services that you provision in Cloud Run scale out automatically to the number of container instances that are necessary to handle the current load. When the application has no load, the service automatically scales in the number of container instances to zero. For more information, see [About instance autoscaling in Cloud Run services](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).
  * **Bigtable:** When you create a cluster in a Bigtable instance, you can configure the cluster to scale automatically. Bigtable monitors the CPU and storage load, and adjusts the number of nodes in the cluster to maintain the target utilization rates that you specify. For more information, see [Bigtable autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling).
  * **Managed Service for Apache Spark:** When you submit an Apache Spark batch workload, Managed Service for Apache Spark dynamically scales the workload resources, such as the number of executors, to run the workload efficiently. For more information, see [Autoscale workload resources](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling-serverless).



## Load balancing

Load balancing helps to improve application reliability by routing traffic to only the available resources and by ensuring that individual resources aren't overloaded.

Consider the following reliability-related design recommendations when choosing and configuring load balancers for your cloud deployment.

### Load-balance internal traffic

Configure load balancing for the traffic between the tiers of the application stack as well, not just for the traffic between the external clients and the application. For example, in a 3-tier web application stack, you can use an [internal load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) for reliable communication between the web and application tiers.

### Choose an appropriate load balancer type

To load-balance external traffic to an application that's distributed across multiple regions, you can use a global load balancer or multiple regional load balancers. For more information, see [Benefits and risks of global load balancing for multi-region deployments](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#benefits-risks-global-load-balancing).

If the backends are in a single region and you don't need the features of global load balancing, you can use a regional load balancer, which is resilient to zone outages.

When you choose the load balancer type, consider other factors besides availability, such as geographic control over TLS termination, performance, cost, and the traffic type. For more information, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer).

### Configure health checks

Autoscaling helps to ensure that your applications have adequate infrastructure resources to handle the current load. But even when sufficient infrastructure resources exist, an application or parts of it might not be responsive. For example, all the VMs that host your application might be in the `RUNNING` state. But the application software that's deployed on some of the VMs might have crashed. [Load-balancing health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) ensure that the load balancers route application traffic to only the backends that are responsive. If your backends are MIGs, then consider configuring an extra layer of health checks to [autoheal](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) the VMs that aren't available. When autohealing is configured for a MIG, the unavailable VMs are proactively deleted, and new VMs are created.

## Rate limiting

At times, your application might experience a rapid or sustained increase in the load. If the application isn't designed to handle the increased load, the application or the resources that it uses might fail, making the application unavailable. The increased load might be caused by malicious requests, such as network-based distributed denial-of-service (DDoS) attacks. A sudden spike in the load can also occur due to other reasons such as configuration errors in the client software. To ensure that your application can handle excessive load, consider applying suitable rate-limiting mechanisms. For example, you can set quotas for the number of API requests that a Google Cloud service can receive.

Rate-limiting techniques can also help optimize the cost of your cloud infrastructure. For example, by setting project-level quotas for specific resources, you can limit the billing that the project can incur for those resources.

## Network Service Tier

Google Cloud [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) let you optimize connectivity between systems on the internet and your Google Cloud workloads. For applications that serve users globally and have backends in more than one region, choose Premium Tier. Traffic from the internet enters the high-performance Google network at the point of presence (PoP) that's closest to the sending system. Within the Google network, traffic is routed from the entry PoP to the appropriate Google Cloud resource, such as a Compute Engine VM. Outbound traffic is sent through the Google network, exiting at the PoP that's closest to the destination. This routing method helps to improve the availability perception of users by reducing the number of network hops between the users and the PoPs closest to them.

[ Previous arrow_back  Design reliable infrastructure  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/design)

[ Next Manage and monitor infrastructure  arrow_forward  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/manage-and-monitor)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
