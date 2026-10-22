---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters/
title: Best practices for planning for large GKE clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:32.658269+00:00
---

# Best practices for planning for large GKE clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for planning for large GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the best practices you can follow when planning and designing very large-size clusters. For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Why plan for large GKE clusters

Every computer system including Kubernetes has some architectural limits. Exceeding the limits may affect the performance of your cluster or in some cases even cause downtimes. Follow the best practices and execute recommended actions to ensure your clusters run your workloads reliably at scale.

## Limitations of large GKE clusters

When GKE scales a cluster to a large number of nodes, GKE makes an effort to change the amount of resources available to match your system needs while staying within its [service-level objectives (SLOs)](https://landing.google.com/sre/sre-book/chapters/service-level-objectives/). Google Cloud supports large clusters. However, based on your use case, you must consider the limitations of large clusters to better respond to your infrastructure scale requirements.

This section describes the limitations and considerations when designing large GKE clusters based on the expected number of nodes.

### General cluster migration considerations

Regardless of your target cluster size, consider the following when migrating to higher node limits:

  * Migrating from zonal to regional Standard clusters requires you to re-create the cluster to access higher node quota limits.
  * Migrating to clusters that use Private Service Connect requires you to re-create the cluster to access the higher node quota limit.



### Cluster size limits and requirements

The following table summarizes GKE's scaling limits and requirements, based on your target node count:

Node limit | Infrastructure requirements | Networking requirements | Access restrictions | Use case examples  
---|---|---|---|---  
Up to 1,000 | Available for all clusters. | No additional requirements. | None. Scaling up to 1,000 nodes is automatic. | General workloads, development, and testing.  
1,000 to 5,000 | Available for regional Standard clusters and Autopilot clusters. | 

  * GKE Dataplane V2 required. For more information, see [GKE Dataplane V2 node limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#node-limits).
  * Private Service Connect required.

| None. Scaling up to 5,000 nodes is automatic if you meet the other requirements. | High volume, short-lived jobs and enterprise services.  
5,000 to 15,000 | 

  * Available only for regional Standard clusters.
  * We recommend using GKE version 1.36 or later to take advantage of performance improvements for scaling large clusters.

| 

  * GKE Dataplane V2 required. For more information, see [GKE Dataplane V2 node limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#node-limits).
  * Private Service Connect required.

| To increase the cluster size and quota limit, [contact Cloud Customer Care](https://cloud.google.com/support-hub). | HPC and data processing workloads.  
15,000 to 65,000 | 

  * Requires GKE version 1.31 or later.
  * We recommend using GKE version 1.36 or later to take advantage of performance improvements for scaling large clusters.
  * Available only for regional Standard clusters.
  * The [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) is not supported. Instead, [scale node pools up or down](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#scale-node-pool) using the GKE API.
  * Services with more than 100 Pods must be [headless](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#headless_service).
  * Every Pod should run on its own node, with the exception of system DaemonSets. To schedule Pods on specific nodes, use [Kubernetes Pod affinity or anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#more-practical-use-cases).

| 

  * GKE Dataplane V2 required. For more information, see [GKE Dataplane V2 node limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#node-limits).
  * Private Service Connect required.
  * [Multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods) is not available.

| To request a quota increase and get assistance with scaling up to the higher limits, [contact Cloud Customer Care](https://cloud.google.com/support-hub). | Large model training.  
  
## Best practices for splitting workloads between multiple clusters

You can run your workloads on a single, large cluster. This approach is easier to manage, more cost efficient, and provides better resource utilization than multiple clusters. However, in some cases you need to consider splitting your workload into multiple clusters:

  * Review [Multi-cluster use cases](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/multi-cluster-use-cases) to learn more about general requirements and scenarios for using multiple clusters.
  * In addition, from the scalability point of view, split your cluster when it could exceed one of the limits described in the section below or one of [GKE quotas](https://docs.cloud.google.com/kubernetes-engine/quotas). Lowering any risk to reach the GKE limits, reduces the risk of downtime or other reliability issues.



If you decide to split your cluster, use [Fleet management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) to simplify management of a multi-cluster fleet.

## Limits and best practices

To ensure that your architecture supports large-scale GKE clusters, review the following limits and related best practices. Exceeding these limits may cause degradation of cluster performance or reliability issues.

These best practices apply to any default Kubernetes cluster with no extensions installed. Extending Kubernetes clusters with webhooks or [custom resource definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) is common but can constrain your ability to scale the cluster.

The following table extends the main [GKE quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster). You should also familiarize yourself with the open-source [Kubernetes limits](https://github.com/kubernetes/community/blob/master/sig-scalability/configs-and-limits/thresholds.md) for large-scale clusters.

The GKE version requirements mentioned in the table apply to both the nodes and the control plane. 

GKE limit | Description | Best practices  
---|---|---  
The etcd database size | The maximum size of the etcd database is 6 GB. You should proactively monitor your cluster's etcd database size and configure alerts to be notified when usage approaches this limit. Exceeding the limit can cause control plane issues. | You can use the following resources to help monitor your use:

  * To view your current usage, go to the [Quotas page](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com/quota/etcd_database_size_bytes) to view a pre-filtered list of GKE quotas.
  * Use [insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) to get alerts for clusters at 80%, 90%, and 95% consumption level.

For more information about how to respond when you approach the limit, see [Identify clusters where etcd usage is approaching the limit](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/scalability#identify-fix-etcd-usage).  
Total size of etcd objects per type | The total size of all objects of the given resource type should not exceed 800 MB. For example, you can create 750 MB of Pod instances and 750 MB of Secrets, but you cannot create 850 MB of Secrets. If you create more than 800 MB of objects, this could lead your Kubernetes or customized controllers to fail to initialize and cause disruptions. |  Keep the total size of all objects of each type stored in etcd below 800 MB. This is especially applicable to clusters using many large-sized Secrets or ConfigMaps, or a high volume of CRDs. **Note:** [Helm](https://helm.sh/) uses Secrets as the default release information storage. In large clusters, the use of Helm can often lead to exceeding the limit of Secrets or ConfigMaps total size. Use [Helm's SQL storage backend](https://helm.sh/docs/topics/advanced/#sql-storage-backend) instead.  
Number of Services for clusters where [ GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) is not enabled | The performance of iptables used by kube-proxy degrades if any of the following occurs: 

  * There are too many Services.
  * The number of backends behind a Service is high.

This limit is eliminated when [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) is enabled. |  Keep the number of Services in the cluster below 10,000. To learn more, see [Exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).  
Number of Services per namespace | The number of environment variables generated for Services might outgrow shell limits. This might cause Pods to crash on startup. |  Keep the number of Services per namespace below 5,000. You can opt-out from having those environment variables populated. See the documentation for how to [set `enableServiceLinks` in PodSpec to false.](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/#accessing-the-service) To learn more, see [Exposing applications using Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).  
Number of Pods behind a single Service for clusters where [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) is not enabled |  Every node runs a kube-proxy that uses [watches](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) for monitoring any Service change. The larger a cluster, the more change-related data the agent processes. This is especially visible in clusters with more than 500 nodes. Information about the endpoints is split between separate `EndpointSlices`. This split reduces the amount of data transferred on each change. Endpoint objects are still available for components, but any endpoint above 1,000 Pods is automatically [truncated](https://kubernetes.io/docs/concepts/services-networking/service/#over-capacity-endpoints). |  Keep the number of Pods behind a single Service lower than 10,000. To learn more, see [exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps). **Caution:** The limit of 10,000 Pods does not apply to [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).  
Number of Pods behind a single Service for clusters where [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) is enabled |  [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) contains limits on the number of Pods exposed by a single Service.  The same limit is applicable to Autopilot clusters as they use GKE Dataplane V2. |  In GKE 1.23 and earlier, keep the number of Pods behind a single Service lower than 1,000. In GKE 1.24 and later, keep the number of Pods behind a single Service lower than 10,000. To learn more, see [Exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).  
DNS records per headless Service |  The number of DNS records per Headless Service is limited for both [kube-dns](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kube-dns#key-components) and [Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#quotas). |  Keep the number of DNS records per headless Service below 1,000 for kube-dns and [3,500/2,000 (IPv4/IPv6) for Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#quotas).  
Number of all Service endpoints | The number of endpoints across all Services may hit limits. This may increase programming latency or result in an inability to program new endpoints at all. |  Keep the number of all endpoints in all services below 260,000. GKE Dataplane V2, which is the default dataplane for GKE Autopilot, relies on eBPF maps that are currently [limited to 260,000 endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#scalability) across all Services.  
Number of HorizontalPodAutoscaler objects per cluster |  Each [HorizontalPodAutoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) is processed every 15 seconds. By default, GKE supports up to 300 HPA objects. For higher limits, the [Performance HPA profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile) increases support to 1,000 HPA objects on version 1.31 and later, and up to 5,000 HPA objects on version 1.33 and later. Exceeding these limits can cause linear performance degradation. |  Keep the number of HPA objects within the supported limit for your cluster's profile (300, 1,000, or 5,000 objects). Otherwise, you might experience linear degradation of the frequency of HPA processing. For example, 2,000 HPAs with standard settings causes each HPA to be reprocessed only once every 1 minute and 40 seconds. To learn more, see [Autoscaling based on resource utilization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#resource-utilization), [Horizontal pod autoscaling scalability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#scalability), and [Configure the Performance HPA profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile).  
Number of Pods per node | In Standard clusters, GKE has a limit of 512 Pods per node. This assumes an average of two or fewer containers per Pod. If you increase the number of containers per Pod, this limit might be lower because GKE allocates more resources per container.  |  We recommend you use worker nodes with at least one vCPU per each 10 pods. To learn more, see [manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).  
Rate of pod changes |  Kubernetes has internal limits that impact the rate of creating or deleting Pods (Pods churn) in response to scaling requests. Additional factors like deleting a pod that is a part of a Service also can impact this Pod churn rate. For clusters with up to 500 nodes, you can expect an average rate of 20 pods created per second and 20 pods deleted per second. For clusters larger than 500 nodes, you can expect an average rate of 100 pods created per second and 100 pods deleted per second. |  Take the Pod creation and deletion rate limit under consideration when planning how to scale your workloads. Pods share the same deletion throughput with other resource types (for example, EndpointSlices). You can reduce deletion throughput when you define Pods as part of a Service. To allow Cluster Autoscaler to effectively remove pods from underutilized nodes, avoid too restrictive [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets.) and long [termination grace periods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination). Wildcard [Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) are also discouraged, as they can cause workloads to be scheduled on nodes that are in the process of being removed.  
Number of open [watches](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) | Nodes create a watch for every [Secret](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/secret) and [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) you configure for Pods. The combined amount of watches created by all nodes might generate substantial load on the cluster control plane. Having more than 200,000 watches per cluster might affect the initialization time of the cluster. This issue can cause the control plane to frequently restart. |  Define larger nodes to decrease the likelihood and severity of issues caused by a large number of watches. Higher pod density (fewer large-sized nodes) might reduce the number of watches and mitigate the severity of the issue. To learn more, see the [machine series comparison](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison).  
Number of Secrets per cluster if application-layer secrets encryption is enabled | A cluster must decrypt all Secrets during cluster startup when [application-layer secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) is enabled. If you store more than 30,000 secrets, your cluster might become unstable during startup or upgrades, causing workload outages. | Store less than 30,000 Secrets when using application-layer secrets encryption. To learn more, see [encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#limitations).  
Log bandwidth per node |  There is a limit on the maximum amount of logs sent by each node to Cloud Logging API. The default limit varies between 100 Kbps and 500 Kbps, depending on the load. For Standard clusters, you can raise the limit to 10 MiB by deploying a high-throughput Logging agent configuration. Going beyond this limit might cause log entries to be dropped. |  Configure your Logging to stay within the default limits or configure a high throughput Logging agent. To learn more, see [Adjusting log throughput](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput).  
Node pools | Having a large number of node pools can impact infrastructure autoscaling latency because it increases the set of nodes that can potentially be added to the cluster. Features like [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) or [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) increase the number of node pools.  | Keep the number of node pools below 200.  
The average and maximum admission webhook delay |  The admission webhooks are called in parallel (validation) or sequentially (mutating). In each case, some delay is added to each configured request that matches the webhook selectors. When executing the webhook, consistent short delays, such as 50-100ms, can lead to significant performance degradation.  |  Configure your webhooks so their execution latency averages below 10ms. Specify the operation, resource types, and namespaces that the webhook should refer to. Avoid capturing events because this can lead to performance issues, for example, slower image prefetching. Run multiple instances of webhook endpoints on separate nodes from workload and maintain low latency. Consider running `failurePolicy: Ignore` and a low timeout (configured with `timeoutSeconds`).  
Backup for GKE limits |  You can use [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) to backup and restore your GKE workloads.  Backup for GKE is subject to limits that you need to keep in mind when defining your backup plans.  |  Review [the limits of Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/quotas-and-limits).  If it's possible for your workload to exceed these limits, we recommend creating multiple backup plans to partition your backup and stay within the limits.  
Config Connector limits |  You can use [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to manage Google Cloud resources through Kubernetes. Config Connector has two modes of operation:

  * [Cluster](https://docs.cloud.google.com/config-connector/docs/how-to/advanced-install#addon-configuring) mode, where there is a single Config Connector instance per GKE cluster. In this mode, a single Config Connector instance loads all the resources.
  * [Namespace](https://docs.cloud.google.com/config-connector/docs/how-to/advanced-install#namespaced-mode) mode, where each namespace within a cluster has a separate Config Connector instance. In this mode, you can partition managed resources via namespaces. This setup reduces the amount of resources that a single Config Connector instance needs to manage, lowering its CPU and memory usage.

Each mode has different scalability characteristic and limitations.  |  For details on resource limits, see [Config Controller scalability guidelines](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/scalability). For information on managing a large number of resources, see [Config Connector best practices](https://docs.cloud.google.com/config-connector/docs/best-practices).  
  
## What's next?

  * [Plan for large workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
