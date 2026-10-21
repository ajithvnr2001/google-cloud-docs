---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/failure-mode-analysis/
title: Understand the impact of failures in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:02.845913+00:00
---

# Understand the impact of failures in Google Distributed Cloud  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/failure-mode-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Understand the impact of failures in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud is designed to limit the scope of failures and to prioritize functionality that's critical to business continuity. This document explains how the functionality of your clusters are impacted when there's a failure. This information can help you prioritize areas to troubleshoot if you have a problem.

The core functionality of Google Distributed Cloud includes the following categories:

  * **Run workloads** : Existing workloads can continue to run. This is the most important consideration to maintain business continuity. Even if your cluster has a problem the existing workloads might continue to run without interruption.
  * **Manage workloads** : You can create, update, and delete workloads. This is the second most important consideration to scale workloads when traffic increases, even if the cluster has a problem.
  * **Manage user clusters** : You can manage nodes, update, upgrade, and delete user clusters. This is less important than the application lifecycle considerations. If there's available capacity on the existing nodes, the inability to modify user clusters doesn't affect user workloads.
  * **Manage admin clusters** : You can update and upgrade the admin cluster. 
    * For deployments that use separate admin and user clusters, this is the least important consideration because the admin cluster doesn't host any user workloads. If your admin cluster has a problem, your application workloads on other clusters continue to run without interruption.
    * If you use other deployment models, such as hybrid or standalone, the admin cluster runs application workloads. If the admin cluster has a problem and the control plane is down, you also can't manage application workloads or user cluster components.



The following sections use these categories of core functionality to describe the impact of specific types of failure scenarios. When there is disruption as part of a failure scenario, the duration (order) of the disruption is also noted, where possible.

**Tip:** When assessing the impact of a failure, use [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) ([Preview](https://cloud.google.com/products#product-launch-stages)) to help you interpret complex behavior patterns and identify potential cascading effects. For example, you could ask: "How would a Google Distributed Cloud control plane node failure affect my running workloads, and what are the long-term consequences if it's not restored quickly?"

## Node failures

A node in Google Distributed Cloud might stop functioning or become unreachable on the network. Depending on the node pool and cluster that the failed machine is part of, there are several different failure modes.

### Control plane node

The following table outlines the behavior for nodes that are part of the control plane in Google Distributed Cloud:

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | No disruption | Possible disruption (unknown) | Possible disruption (unknown) | Possible disruption (unknown)  
**Explanation** | — | If the node failure affects the single control plane node in a non-highly available (HA) user cluster, or if it affects not less than half of the control plane nodes in a HA user cluster, there is disruption. The control plane quorum of the user cluster is lost. | If the node failure affects the single control plane node in a non-HA admin cluster, or if it affects no less than half of the control plane nodes in a HA admin cluster, there is disruption. The control plane quorum of the admin cluster is lost. | If the node failure affects the single control plane node in a non-HA admin cluster, or if it affects no less than half of the control plane nodes in a HA admin cluster, there is disruption. The control plane quorum of the admin cluster is lost.  
**Recovery** | — | For more information, see [how to recover from quorum loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).  | For more information, see [how to recover from quorum loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).  | For more information, see [how to recover from quorum loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).   
**Prevention** | — | Deploy user clusters in HA mode to minimize the possibility of disruption. | Deploy admin clusters in HA mode to minimize the possibility of disruption.  | Deploy admin clusters in HA mode to minimize the possibility of disruption.   
**Note:** The disruption duration depends on the configuration of the liveness probe for the user workloads. In this document, the liveness probe is assumed to have granularity configured in the order of seconds.

### Load balancer node

The following table outlines the behavior for nodes that host the load balancers in Google Distributed Cloud. This guidance only applies to bundled load balancers with [layer 2 mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb). For manual load balancing, consult the failure modes of your external load balancers:

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | Possible disruption (varies) | Possible disruption (varies) | Possible disruption (varies) | Possible disruption (varies)  
**Explanation** | If external workloads rely on the data plane load balancer to communicate with workloads in the cluster and you only have one load balancer node, there is disruption. | The control plane virtual IP address of the user cluster resides on one load balancer node. If the load balancer nodepool of the user cluster is not HA, there is disruption. | The control plane virtual IP address of the admin cluster resides on one load balancer node. If the load balancer nodepool of the admin cluster is not HA, there is disruption. | The control plane virtual IP address of the admin cluster resides on one load balancer node. If the load balancer nodepool of the admin cluster is not HA, there is disruption.  
**Recovery** | If there are multiple load balancer nodes, [MetalLB failover happens within a few seconds](https://metallb.universe.tf/concepts/layer2/#limitations). If not HA, consider deploying additional load balancer nodes. | If HA, failover is automatic and is in the order of seconds. If not HA, consider deploying additional load balancer nodes | If HA, failover is automatic and is in the order of seconds. If not HA, consider deploying additional load balancer nodes. | If HA, failover is automatic and is in the order of seconds. If not HA, consider deploying additional load balancer nodes.  
**Prevention** | To minimize the possibility of disruption, deploy load balancer nodepools in HA mode. | To minimize the possibility of disruption, deploy load balancer nodepools in HA mode. | To minimize the possibility of disruption, deploy load balancer nodepools in HA mode. | To minimize the possibility of disruption, deploy load balancer nodepools in HA mode.  
  
### Worker node

The following table outlines the behavior for worker nodes in Google Distributed Cloud:

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | Possible disruption (order of seconds) | No disruption | No disruption | No disruption  
**Explanation** | The `Pods` that run on the failed node are disrupted, and are [automatically rescheduled onto other healthy nodes](https://kubernetes.io/docs/concepts/architecture/nodes/#:~:text=The%20default%20eviction%20timeout%20duration,API%20server%20is%20re%2Destablished) with a default eviction timeout of 5 minutes. If user applications have spare workload capacity and are spread across multiple nodes, the disruption isn't observable by clients that implement retries. The `Pods` are automatically restarted on healthy nodes. If the cluster doesn't have spare capacity, the disruption might last until new nodes are added to the cluster. | — | — | —  
**Recovery** | If the cluster doesn't have spare capacity, you must deploy more nodes spread across multiple failure zones and move failed workloads to the new nodes. | — | — | —  
**Prevention** | Deploy nodes that spread across multiple failure zones. Deploy workloads with multiple replicas spread across multiple failure zones to minimize the possibility of disruption. | — | — | —  
**Note:** The disruption duration depends on the configuration of the liveness probe for the user workloads. In this document, the liveness probe is is assumed to have granularity configured in the order of seconds.

## Storage failure

Storage in Google Distributed Cloud might stop functioning or become unreachable on the network. Depending on the storage that fails, there are several different failure modes.

### etcd

The contents of `/var/lib/etcd` and `/var/lib/etcd-events` directories might become corrupted if there's an ungraceful power down of the node or an underlying failure of storage. The following table outlines the behavior the core functionality due to `etcd` failures:

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | No disruption | Possible disruption (unknown) | Possible disruption (unknown) | Possible disruption (unknown)  
**Explanation** | If the existing workloads don't rely on the Kubernetes control plane, they continue to function without disruption. | If `etcd` fails on a single control plane user cluster, or fails on no less than half of the control plane nodes in a HA user cluster, there is disruption. The control plane quorum of the user cluster is lost. | If `etcd` fails on a single control plane admin cluster, or fails on no less than half of the control plane nodes in a HA admin cluster, there is disruption. The control plane quorum of the admin cluster is lost. | If `etcd` fails on a single control plane admin cluster, or fails on no less than half of the control plane nodes in a HA admin cluster, there is disruption. The control plane quorum of the admin cluster is lost.  
**Recovery** | — | For more information, see [how to recover from quorum loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).  | For more information, see [how to recover from quorum loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).  | For more information, see [how to recover from quorum loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).   
**Prevention** | — | To minimize the possibility of disruption, deploy user clusters in HA mode. | To minimize the possibility of disruption, deploy admin clusters in HA mode. | To minimize the possibility of disruption, deploy admin clusters in HA mode.  
  
### User application `PersistentVolume`

The following table outlines the behavior the core functionality due to the failure of a `PersistentVolume`:

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | Possible disruption (unknown) | No disruption | No disruption | No disruption  
**Explanation** | The workloads that use the failed `PersistentVolume` are affected.`` | — | — | —  
**Recovery** | — | — | — | —  
**Prevention** | To minimize the possibility of disruption, deploy the user workload in HA mode. | — | — | —  
  
### Fluent Bit corrupted disk

The corruption of a Fluent Bit disk doesn't affect any core functionalities, but does impact the capability to collect and inspect logs on Google Cloud.

The `SIGSEGV` event can sometimes be observed from logs of `stackdriver-log-forwarder`. This error might be caused by the corrupted buffered logs on the disk.

Fluent Bit has a mechanism to filter out and drop the broken chunks. This feature is available in the fluent-bit version (v1.8.3) used in Google Distributed Cloud.

## Out of `LoadBalancer` IP

If all the IP addresses in the assigned pools are currently occupied, newly created `LoadBalancer` services can't acquire a `LoadBalancer` IP address. This scenario impacts the capability of the clients of the service to talk to the `LoadBalancer` services.

To recover from this IP address exhaustion, [assign more IP addresses to the address pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb#address-pools) by modifying the cluster custom resource.

## Certificate expiration

Google Distributed Cloud generates a self-signed certificate authority (CA) during the cluster installation process. The CA has a 10-year expiry and is responsible for generating certificates, which expire after one year. Rotate certificates regularly to prevent cluster downtime. You can rotate certificates by [upgrading](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) your cluster, which is the recommended method. If you are unable to upgrade your cluster, you can perform an [on-demand CA rotation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation). For more information about cluster certificates, see [PKI certificates and requirements](https://kubernetes.io/docs/setup/best-practices/certificates/) in the Kubernetes documentation.

If the cluster certificates have expired, they must be [renewed manually](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs).

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | No Disruption | Possible disruption (unknown) | Possible disruption (unknown) | Possible disruption (unknown)  
**Explanation** | If the user workloads don't talk to the kubernetes control plane components, there won't be disruptions. | If the certificate authorities for user clusters expire, there will be a disruption. | If the certificate authorities for admin clusters expire, there will be a disruption. | If the certificate authorities for user clusters expire, there is disruption.  
**Recovery** | — | Follow the steps to [manually renew certificates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs) on the user cluster. | Follow the steps to [manually renew certificates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs) on the user cluster. | Follow the steps to [manually renew certificates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs) on the user cluster.  
**Prevention** | Setup monitors for certificate expiration. An example metric `kubelet_certificate_manager_server_expiration_seconds` can be found on [the list of metrics.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/metrics-anthos#anthos/kubelet_certificate_manager_server_expiration_seconds)  
  
## Upgrade failures

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption (duration)** | No Disruption | No Disruption | Possible disruption (unknown) | Possible disruption (unknown)  
**Explanation** | If the upgrade fails on the user cluster control plane, there is NO disruption to existing workloads. If the upgrade fails on a particular worker node, the workloads on that node will be drained and moved to other healthy nodes if there is extra capacity on the healthy nodes. | Upgrade will stop if any one of the control plane nodes fails to upgrade. The cluster is still functional if upgrade fails if the user cluster is HA. | If the upgrade fails on the admin cluster control plane, there is disruption until the upgrade finishes. | If the upgrade fails on the admin cluster control plane, there is disruption until the upgrade finishes.  
**Recovery** | — | — | Upgrade is retryable. For more information, see how to [diagnose upgrade issues and resume](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-upgrade). | Upgrade is retryable. For more information, see how to [diagnose upgrade issues and resume](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-upgrade).  
**Prevention** | — | — | For more information, see how to [create a backup before upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore). | For more information, see how to [create a backup before upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore).  
  
## What's next

For more information on known product issues and workarounds, see [Google Distributed Cloud known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues).

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
