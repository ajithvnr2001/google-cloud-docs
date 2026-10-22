---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads/
title: Best practices for planning for large workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:06.074719+00:00
---

# Best practices for planning for large workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for planning for large workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the best practices you can follow when managing large workloads on multiple GKE clusters. These best practices cover considerations for distributing workloads across multiple projects and adjusting required quotas. For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Best practices for distributing GKE workloads across multiple Google Cloud projects

To better define your Google Cloud project structure and GKE workloads distribution, based on your business requirements, we recommend you consider the following designing and planning actions:

  1. Follow the guidance in [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) to make initial decisions for your organization's structure for folders and projects. Google Cloud recommends using [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) elements like folders and projects to divide your workload based on your own organizational boundaries or access policies.
  2. Consider if you need to split your workloads because of project quotas. Google Cloud uses per project quotas to restrict usage of shared resources. You need to follow the recommendations described below and adjust the project quotas for large workloads. For most of the workloads you should be able to achieve required, higher quotas in just a single project. This means that quotas should not be the primary driver for splitting your workload between multiple projects. Keeping your workloads in a smaller number of projects simplifies the administration of your quotas and workloads.
  3. Consider if you plan to run very large workloads (scale of hundreds of thousands of CPUs or more). In such a case splitting your workload into several projects can increase availability of cloud resources (like CPUs or GPUs). This is possible because of using optimized configuration of the [zone virtualization](https://docs.cloud.google.com/compute/docs/regions-zones). In such cases please contact your Account Manager to get special support and recommendations.



## Best practices for adjusting quotas for large GKE workloads

This section describes guidelines for adjusting quotas for Google Cloud resources used by GKE workloads. Adjust the quotas for your projects based on the following guidelines. To learn how to manage your quota using the Google Cloud console, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

### Compute Engine quotas and best practices

GKE clusters, running in both Autopilot and Standard mode, use Compute Engine resources to run your workloads. In contrast to Kubernetes control plane resources that are internally managed by Google Cloud, you can manage and evaluate Compute Engine quotas that your workflows use.

[Compute Engine quotas](https://docs.cloud.google.com/compute/quotas), for both resources and APIs, are shared by all GKE clusters hosted in the same project and region. The same quotas are also shared with other (not GKE related) Compute Engine resources (like standalone VM instances or instance groups).

Default quota values can support several hundred of worker nodes and require adjustment for larger workloads. However, as a platform administrator, you can proactively adjust Compute Engine quotas to ensure that your GKE clusters have enough resources. You should also consider future resource needs when evaluating or adjusting the quota values.

#### Quotas for Compute Engine resources used by GKE worker nodes

The following table lists resource quotas for the most common Compute Engine resources used by GKE worker nodes. These quotas are configured per project, and per region. The quotas must cover the maximum combined size of the GKE worker nodes used by your workload and also other Compute Engine resources not related to GKE.

Resource quota | Description  
---|---  
CPUs | Number of CPUs used by all worker nodes of all clusters.  
Type of CPUs | Number of each specific type of CPU used by all worker nodes of all clusters.  
VM instances | Number of all worker nodes. This quota is automatically calculated as 10x the number of CPUs.  
Instances per VPC network | Number of all worker nodes connected to the VPC network.  
Persistent Disk standard (GB) | Total size of standard persistent boot disks attached to all worker nodes.  
Persistent Disk SSD (GB) | Total size of SSD persistent boot disks attached to all worker nodes.  
Local SSD (GB) | Total size of local SSD ephemeral disks attached to all worker nodes.  
  
Make sure to also adjust quotas used by resources that your workload might require, such as GPUs, IP addresses, or preemptive resources.

#### Quotas for Compute Engine API calls

Large or scalable clusters require a higher number of [Compute Engine API calls](https://docs.cloud.google.com/compute/quotas#api-rate-limits). GKE makes these Compute Engine API calls during activities such as:

  * Checking state of the compute resources.
  * Adding or removing new nodes to the cluster.
  * Adding or removing new node pools.
  * Periodic labeling of resources.



When planning your large-size cluster architecture, we recommend you do the following:

  1. Observe [historical quota consumption](https://docs.cloud.google.com/docs/quotas/view-manage).
  2. Adjust the quotas as needed while keeping a reasonable buffer. You can refer to the following best practice recommendations as a starting point, and adjust the quotas based on your workload needs.
  3. Because quotas are configured per region, adjust quotas only in the regions where you plan to run large workloads.



The following table lists quotas for Compute Engine API calls. These quotas are configured per project, independently per each region. Quotas are shared by all GKE clusters hosted in the same project and in the same region.

API quota | Description | Best practices  
---|---|---  
[Queries per minute per region](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com%2fdefault_per_region) | These calls are used by GKE to perform various checks against the state of the various compute resources. |  For projects and regions with several hundreds of dynamic nodes, adjust this value to 3,500. For projects and regions with several thousands of highly dynamic nodes, adjust this value to 6,000.  
[Read requests per minute pe region ](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com%2fread_requests_per_region)| These calls are used by GKE to monitor the state of VM instances (nodes). |  For projects and regions with several hundreds of nodes, adjust this value to 12,000. For projects and regions with thousands of nodes, adjust this value to 20,000.  
[List requests per minute per region](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com%2flist_requests_per_region) | These calls are used by GKE to monitor the state of instance groups (node pools). |  For projects and regions with several hundreds of dynamic nodes, don't change the default value because it is enough. For projects and regions with thousands of highly dynamic nodes, in multiple node pools, adjust this value to 2,500.  
[Instance List Referrer requests per minute per region](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com%2finstance_list_referrers_requests_per_region) | These calls are used by GKE to obtain information about running VM instances (nodes). |  For projects and regions with thousands of highly dynamic nodes, adjust this value to 6,000.  
[Operation read requests per minute per region](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com%2foperation_read_requests_per_region) | These calls are used by GKE to obtain information about ongoing Compute Engine API operations. |  For projects and regions with thousands of highly dynamic nodes, adjust this value to 3,000.  
  
### Cloud Logging API and Cloud Monitoring API quotas and best practices

Depending on your cluster configuration, large workloads running on GKE clusters might generate a large volume of diagnostic information. When exceeding Cloud Logging API or Cloud Monitoring API quotas, the logging and monitoring data might be lost. We recommend you configure the verbosity of the logs and adjust [Cloud Logging API](https://docs.cloud.google.com/logging/quotas) and [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/quotas) quotas to capture generated diagnostic information. [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) consumes Cloud Monitoring quotas.

Because every workload is different, we recommend you do the following:

  1. Observe [historical quota consumption](https://docs.cloud.google.com/docs/quotas/view-manage).
  2. Adjust the quotas or adjust logging and monitoring configuration as needed. Keep a reasonable buffer for unexpected issues.



The following table lists quotas for Cloud Logging APIs and Cloud Monitoring APIs calls. These quotas are configured per project and are shared by all GKE clusters hosted in the same project.

Service | Quota | Description | Best practices  
---|---|---|---  
Cloud Logging API | [Write requests per minute](https://console.cloud.google.com/iam-admin/quotas?service=logging.googleapis.com&metric=logging.googleapis.com%2fwrite_requests) | GKE uses this quota when adding entries to log files stored in Cloud Logging. |  Log insertion rate is dependent on the amount of logs generated by the pods in your cluster. Increase your quota based on the number of pods, verbosity of applications logging, and logging configuration. To learn more, see [managing GKE logs](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-logs).  
Cloud Monitoring API | [Time series ingestion requests per minute](https://console.cloud.google.com/iam-admin/quotas?service=monitoring.googleapis.com&metric=monitoring.googleapis.com%2fingestion_requests) |  GKE uses this quota when sending Prometheus metrics to Cloud Monitoring: 

  * Prometheus metrics consume about 1 call per second for every 200 samples per second you collect. This ingestion volume depends on your GKE workload and configuration; exporting more Prometheus time series will result in more quota consumed.

|  Monitor and adjust this quota as appropriate. To learn more, see [managing GKE metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics).  
  
### GKE node scaling limits and quota

GKE Standard clusters support scaling up to 65,000 nodes. Depending on your target node count, there are specific infrastructure requirements, and you might need to contact Cloud Customer Care. For detailed information, see [Cluster size limits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes).

When preparing to scale, you should also complete the following tasks:

  * Review [GKE quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas) to confirm overall support levels.
  * Update and raise Compute Engine quotas as required for your scaled workload.



## Best practices for using validating and mutating admission webhooks

On a large scale the requests start to compete for the resources on the kube-apiserver component. If the configured webhooks introduce an unnecessary delay or cover too wide scope of requests, a degradation in performance of the basic cluster operations might occur.

**Important:** Do not run webhooks at all at large scale. If you must run webhooks, ensure that they have multiple replicas, they are running on separate nodes from workload, and you have low average webhook latency. Also, consider running `failurePolicy: Ignore` and a low timeout (configured with `timeoutSeconds`).

We recommend that you keep webhooks scoped to the precise subset of operations, resources, and namespaces that you require to achieve the desired behaviour. A delay of 100ms can cause even twice slower Pod creation on a 65,000 node scale.

## Best practices for avoiding other limits for large workloads

### Limit for number of clusters using VPC Network Peering per network per location

You can create a maximum of 75 clusters that use VPC Network Peering in the same VPC network per location (zones and regions are treated as separate locations). Attempts to create additional clusters above the limit would fail with an error similar to the following:
    
    
    CREATE operation failed. Could not trigger cluster creation:
    Your network already has the maximum number of clusters: (75) in location us-central1.
    

GKE clusters with private nodes created before version 1.29 use VPC Network Peering to provide internal communication between Kubernetes API Server (managed by Google) and private nodes having only internal addresses.

To solve this issue, you can use clusters that use [Private Service Connect (PSC)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect) connectivity. Clusters with PSC connectivity provide the same isolation as a cluster using VPC Network Peering, without the 75 clusters limitation. Clusters with PSC connectivity don't use VPC Network Peering and are not impacted by the limit of the number of VPC peerings.

You can use instructions provided in [VPC Network Peering reuse](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation#vpc_peering_reuse) to identify if your clusters use VPC Network Peering.

To avoid hitting the limit while creating new clusters, do the following steps:

  1. Ensure that your [cluster uses PSC](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect).
  2. Configure the isolation for node pools to become private by using `enable-private-nodes` parameter for each node pool.
  3. Optionally, configure the isolation for the control plane by using `enable-private-endpoint` parameter on cluster level. To learn more, see [Customize your network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation).



Alternatively, contact the Google Cloud support team to raise the limit of 75 clusters using VPC Network Peering. Such requests are evaluated on a case-by-case basis and when increasing the limit is possible, a single digit increase is applied.

### Optimize for scalability and reliability with HTTP/2

To run large-scale workloads on GKE, use [HTTP/2](https://http2.github.io/) instead of HTTP/1.1. HTTP/2 improves performance and connection reliability in high-traffic or high-latency environments.

#### Benefits of HTTP/2

  * Reduces the number of connections: HTTP/2 lets you send many requests and receive many responses over one connection. This lowers the load on system components like [load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), proxies, and NAT gateways.

  * Improves performance consistency: With HTTP/1.1, each request usually needs its own connection. If one connection has issues, it can delay or break the request. For example, if one TCP connection drops packets or experiences high latency, it might affect all requests made on that connection, which can cause delays or errors in the application. With HTTP/2, multiple requests share the same connection, so network issues impact all requests in the same way, making the performance more predictable.

  * Includes built-in features to keep connections reliable:

    * **Flow control** : Flow control helps manage how much data is sent at one time. It prevents senders from overwhelming receivers and helps avoid network congestion.

    * **Ping frames** : Ping frames are lightweight signals that check if a connection is still active. These signals help maintain persistent connections and prevent dropped connections caused by intermediate systems (like firewalls or proxies) that might close idle connections.

In HTTP/1.1, connections can drop unexpectedly if there's no traffic for a period of time. This situation is especially common when firewalls or proxies close idle connections to free up resources. In HTTP/2, ping frames keep connections alive by regularly checking the connection's status.

    * **Multiplexing** : In HTTP/1.1, when multiple requests are sent at the same time using separate connections, the order in which responses are received can cause issues if one request depends on another. For example, if one request completes first but another has a network delay, the result could be an incorrect or out-of-order response. This issue can cause a race condition. HTTP/2 prevents this by multiplexing all requests over a single connection, which helps to make sure that responses are properly aligned.




#### Best practices for using HTTP/2

  * Use HTTP/2 for applications that handle a high volume of traffic or need low-latency communication.
  * Set up application-level keepalives to keep connections open. For more information, see [How connections work](https://docs.cloud.google.com/load-balancing/docs/https#how-connections-work).
  * Monitor your traffic to make sure it uses HTTP/2.



For more information, see [HTTP/2 support in Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https#http2-support).

## What's next?

  * See our episodes about [building large GKE clusters](https://www.youtube.com/watch?v=542XwAPKh4g).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
