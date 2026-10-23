---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/observability/
title: Troubleshoot Google Distributed Cloud observability issues \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:01.297507+00:00
---

# Troubleshoot Google Distributed Cloud observability issues  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot Google Distributed Cloud observability issues Stay organized with collections  Save and categorize content based on your preferences. 

To restore missing audit logs, metrics, or metadata labels in Google Distributed Cloud clusters, you can use the following fixes for common observability issues. Most of these issues are caused by permission errors or by out-of-memory crashes in components such as `kube-state-metrics` in large clusters. Some issues also affect Horizontal Pod Autoscaler and `kubectl top`.

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



## Cloud Audit Logs aren't collected

Cloud Audit Logs are enabled by default unless there's a `disableCloudAuditLogging` flag set under the `clusterOperations` section of cluster config. 

If Cloud Audit Logs are enabled, permissions are the most common reason that logs aren't collected. In this scenario, permission denied error messages are displayed in the Cloud Audit Logs proxy container.

The Cloud Audit Logs proxy container runs as a DaemonSet in all Google Distributed Cloud clusters. 

If you see permission errors, [follow the steps to troubleshoot and resolve permission issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/known-issues#cloud-audit-logging-failure-due-to-permission-denied).

Another possible cause is your project might have reached the supported service account limit, see Cloud Audit Logs service account leaked.

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

    * For Google Distributed Cloud versions 1.16.0 or later, Google Cloud Observability manages KSM. To update KSM, see [Overriding the default CPU and memory requests and limits for a Stackdriver component](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#overriding_the_default_cpu_and_memory_requests_and_limits_for_a_stackdriver_component).

    * For versions earlier than 1.16.0, to adjust the CPU and memory of KSM use the Stackdriver custom resource's [resourceOverride](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring#overriding_the_default_cpu_and_memory_requests_and_limits_for_a_stackdriver_component) for `kube-state-metrics`.

  * **Reduce the number of metrics from KSM.**

For Google Distributed Cloud 1.13, KSM only exposes a smaller number of metrics called Core Metrics by default. This behavior means that resource usage is smaller than previous versions, but the same procedure can be followed to further reduce the number of KSM metrics.

For Google Distributed Cloud versions earlier than 1.13, KSM uses the [default flags](https://github.com/kubernetes/kube-state-metrics/blob/main/docs/developer/cli-arguments.md). This configuration exposes a large number of metrics.




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

## Not all resources are removed during Cloud Audit Logs service account deletion

When you delete a service account used for Cloud Audit Logs, not all Google Cloud resources are deleted. If you routinely delete and recreate service accounts used for Cloud Audit Logs, eventually audit logging begins to fail.

**Symptom**

Permission denied error messages are displayed in the Cloud Audit Logs proxy container.

To confirm that the audit log failure is caused by this issue, run the following command:
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://gkehub.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/global/features/cloudauditlogging
    

Replace `PROJECT_NUMBER` with your project number.

The response returns all service accounts used with Cloud Audit Logs in the project including service accounts that have been deleted.

**Cause and affected versions**

Not all Google Cloud resources are removed when you delete a service account used for Cloud Audit Logs, and eventually you hit the 1000 service account limit for the project.

This issue could be experienced in any version of Google Distributed Cloud.

**Fix and workaround**

  1. Create an environment variable containing a comma-separated list of all the service accounts that you want to keep. Surround each service account email with single quotation marks, and surround the entire list with double quotation marks. You can use the following as a starting point:
         
         SERVICE_ACCOUNT_EMAILS="'SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com'"
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `SERVICE_ACCOUNT_NAME`: the service account name.

The completed list should be similar to the following example:
    
    "'sa_name1@example-project-12345.iam.gserviceaccount.com','sa_name2@example-project-12345.iam.gserviceaccount.com','sa_name3@example-project-12345.iam.gserviceaccount.com'"
    

  2. Run the following command to remove the Cloud Audit Logs feature from the project:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         https://gkehub.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/FLEET_REGION /features/cloudauditlogging
         

Replace the following:

     * `PROJECT_NUMBER`: the project number.
     * `FLEET_REGION`: the fleet membership location for your clusters. This could be a specific region such as `us-central1` or `global`. You can run the `gcloud container fleet memberships list` command to get membership location.

This command completely deletes all service accounts.

  3. Recreate the Cloud Audit Logs feature with only the service accounts that you want to keep:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://gkehub.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/FLEET_REGION/features?feature_id=cloudauditlogging \
             -d '{"spec":{"cloudauditlogging":{"allowlistedServiceAccounts":[$SERVICE_ACCOUNT_EMAILS]}}}'
         




## Metadata Labels disappear from metrics

**Symptom**

Metadata labels, for example, node_name is not populated in Cloud Monitoring.

**Cause and affected versions**

This issue could be experienced in any version of Google Distributed Cloud.

**Fix and workaround**

Any changes to the Pod will bring the metadata labels back. For example, running commands like `kubectl rollout restart deployment <workload_name>`.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
