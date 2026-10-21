---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/observability/
title: Troubleshoot Distributed Cloud observability issues \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:55.964930+00:00
---

# Troubleshoot Distributed Cloud observability issues  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/observability/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot Distributed Cloud observability issues Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/observability)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/observability)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document helps you troubleshoot observability issues in Google Distributed Cloud. If you experience any of these issues, review the suggested fixes and workarounds.

If you need additional assistance, reach out to [Google Support](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/getting-support).

## Cloud Audit Logs aren't collected

Cloud Audit Logs are enabled by default unless there's a `disableCloudAuditLogging` flag set under the `clusterOperations` section of cluster config. 

If Cloud Audit Logs are enabled, permissions are the most common reason that logs aren't collected. In this scenario, permission denied error messages are displayed in the Cloud Audit Logs proxy container.

The Cloud Audit Logs proxy container runs as a DaemonSet in all Google Distributed Cloud clusters. 

If you see permission errors, [follow the steps to troubleshoot and resolve permission issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/known-issues#cloud-audit-logging-failure-due-to-permission-denied).

## `kube-state-metrics` metrics aren't collected

`kube-state-metrics` (KSM) runs as a single replica Deployment in the cluster and generates metrics on almost all resources in the cluster. When KSM and the `gke-metrics-agent` run on the same node, there's a greater risk of outage among metrics agents on all nodes.

KSM metrics have names that follow the pattern of `kube_<ResourceKind>`, like `kube_pod_container_info`. Metrics that start with `kube_onpremusercluster_` are from the on-premises cluster controller, not from KSM.

If KSM metrics are missing, review the following troubleshooting steps:

  * In Cloud Monitoring, check the CPU, memory, and restart count of KSM using the summary API metrics like `kubernetes.io/anthos/container/...` . This is a separate pipeline with KSM. Confirm that the KSM Pod isn't limited by not enough resources. 
    * If these summary API metrics aren't available for KSM, `gke-metrics-agent` on the same node probably also has the same issue.
  * In the cluster, check the status and logs of the KSM Pod and the `gke-metrics-agent` Pod on the same node with KSM.



## `kube-state-metrics` crash looping

**Symptom**

No metrics from `kube-state-metrics` (KSM) are available from Cloud Monitoring.

**Cause**

This scenario is more likely to occur in large clusters, or clusters with large amounts of resources. KSM runs as a single replica Deployment and lists almost all resources in the cluster like Pods, Deployments, DaemonSets, ConfigMaps, Secrets, and PersistentVolumes. Metrics are generated on each of these resource objects. If any of the resources has many objects, like a cluster with over 10,000 Pods, KSM potentially runs out of memory.

**Affected versions**

This issue could be experienced in any version of Google Distributed Cloud.

The default CPU and memory limit have been increased in the last few Google Distributed Cloud versions, so these resource issues should be less common.

**Fix and workaround**

To check if your problem is because of out of memory problems, review the following steps:

  * Use `kubectl describe pod` or `kubectl get pod -o yaml` and check the error status message.
  * Check the memory consumption and utilization metric for KSM and confirm if it's reaching the limit before getting restarted.



If you confirm that out of memory problems are the issue, use either one of the following solutions:

  * **Increase the memory request and limit for KSM.**

**Note:** Even if KSM becomes stable after resource increases, the `gke-metrics-agent` on the same node might remain a bottleneck in scraping large amounts of metrics from KSM.

To adjust the CPU and memory of KSM use the Stackdriver custom resource's [resourceOverride](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring#overriding_the_default_cpu_and_memory_requests_and_limits_for_a_stackdriver_component) for `kube-state-metrics`. 

  * **Reduce the number of metrics from KSM.**

For Google Distributed Cloud 1.13, KSM only exposes a smaller number of metrics called Core Metrics by default. This behavior means that resource usage is smaller than previous versions, but the same procedure can be followed to further reduce the number of KSM metrics.

For Google Distributed Cloud versions earlier than 1.13, KSM uses the [default flags](https://github.com/kubernetes/kube-state-metrics/blob/master/docs/cli-arguments.md). This configuration exposes a large number of metrics.




## `gke-metrics-agent` crash looping

If `gke-metrics-agent` only experiences out of memory issues on the node where `kube-state-metrics` exists, the cause is a large number of `kube-state-metrics` metrics. To mitigate this issue, scale down `stackdriver-operator` and modify KSM to expose a small set of needed metrics as detailed in the previous section. Remember to scale back up `stackdriver-operator` after the cluster is upgraded to Google Distributed Cloud 1.13 where KSM by default exposes a smaller number of Core Metrics.

For issues that aren't related to out of memory events, check the Pods logs of `gke-metric-agent`. You can adjust CPU and memory for all `gke-metrics-agent` Pods by adding the [`resourceAttrOverride` field](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring#overriding_the_default_cpu_and_memory_requests_and_limits_for_a_stackdriver_component) to the Stackdriver custom resource. 

## `stackdriver-metadata-agent` crash looping

**Symptom**

No system metadata label is available when filtering metrics in Cloud Monitoring.

**Cause**

The most common case of `stackdriver-metadata-agent` crash looping is because of out of memory events. This event is similar to `kube-state-metrics`. Although `stackdriver-metadata-agent` isn't listing all resources, it still lists all objects for the relevant resource types like Pods, Deployments, and NetworkPolicy. The agent runs as a single replica Deployment, which increases the risk of out of memory events if the number of objects is too great.

**Affected version**

This issue could be experienced in any version of Google Distributed Cloud.

The default CPU and memory limit has been increased in the last few Google Distributed Cloud versions, so these resource issues should be less common.

**Fix and workaround**

To check if your problem is because of out of memory problems, review the following steps:

  * Use `kubectl describe pod` or `kubectl get pod -o yaml` and check the error status message.
  * Check the memory consumption and utilization metric for `stackdriver-metadata-agent` and confirm if it's reaching the limit before getting restarted.

If you confirm that out of memory issues are causing problems, increase the memory limit in the [`resourceAttrOverride` field](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring#overriding_the_default_cpu_and_memory_requests_and_limits_for_a_stackdriver_component) of the Stackdriver custom resource. 

## `metrics-server` crash looping

**Symptom**

Horizontal Pod Autoscaler and `kubectl top` don't work in your cluster.

**Cause and affected versions**

This issue isn't very common, but is caused by out of memory errors in large clusters or in clusters with high Pod density.

This issue could be experienced in any version of Google Distributed Cloud.

**Fix and workaround**

[Increase metrics server resource limits](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring#metrics_server). In Google Distributed Cloud version 1.13 and later, the namespace of `metrics-server` and its config has been moved from `kube-system` to `gke-managed-metrics-server`.

For Google Distributed Cloud, editing of the nanny config would be reverted in an event of cluster update or upgrade. You would need to reapply your configuration changes. To work around this limitation, [scale down `metrics-server-operator` and manually change the `metrics-server` pod](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues#low-cpu-limit-for-metrics-server-in-edge-clusters). 

## What's next

If you need additional assistance, reach out to [Google Support](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
