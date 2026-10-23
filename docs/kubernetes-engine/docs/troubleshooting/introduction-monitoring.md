---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring/
title: Perform proactive monitoring with Cloud Monitoring \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:32.547330+00:00
---

# Perform proactive monitoring with Cloud Monitoring  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Perform proactive monitoring with Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Reacting to issues after they occur can lead to downtime. To maintain a resilient system in Google Kubernetes Engine (GKE), you need to identify potential problems _before_ they affect your users.

Use this page to proactively monitor your GKE environment with Cloud Monitoring by tracking key performance indicators, visualizing trends, and setting up alerts to detect issues like rising error rates or resource constraints.

This information is important for Platform admins and operators responsible for ensuring the health, reliability, and efficiency of the GKE environment. It also helps Application developers understand their app's performance in real-world conditions, detect regressions across deployments, and gain insights for optimization. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Review useful metrics

GKE automatically sends a set of metrics to Cloud Monitoring. The following sections list some of the most important metrics for troubleshooting:

  * Container performance and health metrics
  * Node performance and health metrics
  * Pod performance and health metrics



For a complete list of GKE metrics, see [GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).

### Container performance and health metrics

Start with these metrics when you suspect a problem with a specific app. These metrics help you monitor the health of your app, including discovering if a container is restarting frequently, running out of memory, or being throttled by CPU limits.

Metric | Description | Troubleshooting significance  
---|---|---  
`kubernetes.io/container/cpu/limit_utilization` | The fraction of the CPU limit that is currently in use on the instance. This value can be greater than 1 as a container might be allowed to exceed its CPU limit. | Identifies CPU throttling. High values can lead to performance degradation.  
`kubernetes.io/container/memory/limit_utilization` | The fraction of the memory limit that is currently in use on the instance. This value cannot exceed 1. | Monitors for risk of OutOfMemory (OOM) errors.  
`kubernetes.io/container/memory/used_bytes` | Actual memory consumed by the container in bytes. | Tracks memory consumption to identify potential memory leaks or risk of OOM errors.  
`kubernetes.io/container/memory/page_fault_count` | Number of page faults, broken down by type: major and minor. | Indicates significant memory pressure. Major page faults mean memory is being read from disk (swapping), even if memory limits aren't reached.  
`kubernetes.io/container/restart_count` | Number of times the container has restarted. | Highlights potential problems such as crashing apps, misconfigurations, or resource exhaustion through a high or increasing number of restarts.  
`kubernetes.io/container/ephemeral_storage/used_bytes` | Local ephemeral storage usage in bytes. | Monitors temporary disk usage to prevent Pod evictions due to full ephemeral storage.  
`kubernetes.io/container/cpu/request_utilization` | The fraction of the requested CPU that is currently in use on the instance. This value can be greater than 1 as usage can exceed the request. | Identifies over or under-provisioned CPU requests to help you optimize resource allocation.  
`kubernetes.io/container/memory/request_utilization` | The fraction of the requested memory that is currently in use on the instance. This value can be greater than 1 as usage can exceed the request. | Identifies over or under-provisioned memory requests to improve scheduling and prevent OOM errors.  
  
### Node performance and health metrics

Examine these metrics when you need to diagnose issues with the underlying GKE infrastructure. These metrics are crucial for understanding the overall health and capacity of your nodes, helping you investigate whether the node is unhealthy or under pressure, or whether the node has enough memory to schedule new Pods.

Metric | Description | Troubleshooting significance  
---|---|---  
`kubernetes.io/node/cpu/allocatable_utilization` | The fraction of the allocatable CPU that is currently in use on the instance. | Indicates if the sum of Pod usage is straining the node's available CPU resources.  
`kubernetes.io/node/memory/allocatable_utilization` | The fraction of the allocatable memory that is currently in use on the instance. This value cannot exceed 1 as usage cannot exceed allocatable memory bytes. | Suggests that the node lacks memory for scheduling new Pods or for existing Pods to operate, especially when values are high.  
`kubernetes.io/node/status_condition` (BETA) | Condition of a node from the node status condition field. | Reports node health conditions like `Ready`, `MemoryPressure`, or `DiskPressure`.  
`kubernetes.io/node/ephemeral_storage/used_bytes` | Local ephemeral storage bytes used by the node. | Helps prevent Pod startup failures or evictions by providing warnings about high ephemeral storage usage.  
`kubernetes.io/node/ephemeral_storage/inodes_free` | Free number of index nodes (inodes) on local ephemeral storage. | Monitors the number of free inodes. Running out of inodes can halt operations even if disk space is available.  
`kubernetes.io/node/interruption_count` (BETA) | Interruptions are system evictions of infrastructure while the customer is in control of that infrastructure. This metric is the current count of interruptions by type and reason. | Explains why a node might disappear unexpectedly due to system evictions.  
  
### Pod performance and health metrics

These metrics help you troubleshoot issues related to a Pod's interaction with its environment, such as networking and storage. Use these metrics when you need to diagnose slow-starting Pods, investigate potential network connectivity issues, or proactively manage storage to prevent write failures from full volumes.

Metric | Description | Troubleshooting significance  
---|---|---  
`kubernetes.io/pod/network/received_bytes_count` | Cumulative number of bytes received by the Pod over the network. | Identifies unusual network activity (high or low) that can indicate app or network issues.  
`kubernetes.io/pod/network/policy_event_count` (BETA) | Change in the number of network policy events seen in the dataplane. | Identifies connectivity issues caused by network policies.  
`kubernetes.io/pod/volume/utilization` | The fraction of the volume that is currently being used by the instance. This value cannot be greater than 1 as usage cannot exceed the total available volume space. | Enables proactive management of volume space by warning when high utilization (approaching 1) might lead to write failures.  
`kubernetes.io/pod/latencies/pod_first_ready` (BETA) | The Pod end-to-end startup latency (from Pod `Created` to `Ready`), including image pulls. | Diagnoses slow-starting Pods.  
  
## Visualize metrics with Metrics Explorer

To visualize the state of your GKE environment, create charts based on metrics with Metrics Explorer.

To use Metrics Explorer, complete the following steps:

  1. In the Google Cloud console, go to the **Metrics Explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Metrics** field, select or enter the metric that you want to inspect.

  3. View the results and observe any trends over time.




For example, to investigate the memory consumption of Pods in a specific namespace, you can do the following:

  1. In the **Select a metric** list, choose the metric `kubernetes.io/container/memory/used_bytes` and click **Apply**.
  2. Click **Add filter** and select **namespace_name**.
  3. In the **Value** list, select the namespace you want to investigate.
  4. In the **Aggregation** field, select **Sum** > **pod_name** and click **OK**. This setting displays a separate time series line for each Pod.
  5. Click **Save chart**.



The resulting chart shows you the memory usage for each Pod over time, which can help you visually identify any Pods with unusually high or spiking memory consumption.

Metrics Explorer has a great deal of flexibility in how to construct the metrics that you want to view. For more information about advanced Metrics Explorer options, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) in the Cloud Monitoring documentation.

## Create alerts for proactive issue detection

To receive notifications when things go wrong or when metrics breach certain thresholds, set up alerting policies in Cloud Monitoring.

For example, to set up an alerting policy that notifies you when the container CPU limit is over 80% for five minutes, do the following:

  1. In the Google Cloud console, go to the **Alerting** page.

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)

  2. Click **Create policy**.

  3. In the **Select a metric** box, filter for `CPU limit utilization` and then select the following metric: **kubernetes.io/container/cpu/limit_utilization**.

  4. Click **Apply**.

  5. Leave the **Add a filter** field blank. This setting triggers an alert when any cluster violates your threshold.

  6. In the **Transform data** section, do the following:

     1. In the **Rolling window** list, select **1 minute**. This setting means that Google Cloud calculates an average value every minute.
     2. In the **Rolling window function** list, select **mean**.

Both of these settings average the CPU limit utilization for each container every minute.

  7. Click **Next.**

  8. In the **Configure alert** section, do the following:

     1. For **Condition type** , select **Threshold**.
     2. For **Alert trigger** , select **Any time series violates**.
     3. For **Threshold position** , select **Above threshold**.
     4. For **Threshold value** , enter `0.8`. This value represents the 80% threshold that you want to monitor for.
     5. Click **Advanced options**.
     6. In the **Retest window** list, select **5 min**. This setting means that the alert triggers only if the CPU utilization stays over 80% for a continuous five-minute period, which reduces false alarms from brief spikes.
     7. In the **Condition name** field, give the condition a descriptive name.
     8. Click **Next**.
  9. In the **Configure the notifications and finalize the alert** section, do the following:

     1. In the **Notification channels** list, select the channel where you want to receive the alert. If you don't have a channel, click **Manage notification channels** to create one.
     2. In the **Name the alert policy** field, give the policy a clear and descriptive name.
     3. Leave all other fields with their default values.
     4. Click **Next**.
  10. Review your policy, and if it all looks correct, click **Create policy**.




To learn about the additional ways that you can create alerts, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts) in the Cloud Monitoring documentation.

## What's next

  * Read [Accelerate diagnosis with Gemini Cloud Assist](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-gemini) (the next page in this series).

  * See these concepts applied in the [example troubleshooting scenario](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
