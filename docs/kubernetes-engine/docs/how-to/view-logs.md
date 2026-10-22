---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs/
title: View GKE logs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:40.186310+00:00
---

# View GKE logs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  View GKE logs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of how to find and use your Google Kubernetes Engine (GKE) logs.

## Accessing your logs

You can access your GKE logs in many ways:

  * From the Google Cloud console, you can view logs from the following pages:

    * **Kubernetes Engine** :

      * Select a cluster on the **Clusters** page, and then select the **Logs** tab. This tab also offers suggested queries for your cluster logs.
      * Select a workload on the **Workloads** page. You can then click the **Container logs** or **Audit logs** links on the **Overview** tab to view your logs in Logs Explorer, or select the **Logs** tab to view your logs in context.
      * View details for your AI/ML workloads in the **AI/ML** section.
    * **Logging** : Select **Logs Explorer** , and then use logging filters to select the Kubernetes resources, such as cluster, node, namespace, pod, or container logs. For example queries to help you get started, see [Kubernetes-related queries](https://docs.cloud.google.com/logging/docs/view/query-library-preview#kubernetes-filters).

    * **Monitoring** : GKE dashboards display metrics and logs for GKE resources like clusters, nodes, and pods. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

  * From the Google Cloud CLI: Query logs from clusters, nodes, pods, and containers by using the [`gcloud logging read`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#reading_log_entries) command.




For custom log aggregation, log analytics, or integration with third-party systems, you can also use the logging sinks feature to export logs to BigQuery, Cloud Storage, and Pub/Sub.

## Understanding your logs

A log in Cloud Logging is a collection of [log entries](https://docs.cloud.google.com/logging/docs/log-entry-data-model), and each log entry applies to a certain type of [logging resource](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

### Resource types

These are the resource types that are specific to GKE clusters:

Log resource types |  | `gke_cluster` | GKE cluster operations logs  
---|---  
`gke_nodepool` | GKE node pool operations logs  
`k8s_cluster` | Kubernetes cluster logs  
`k8s_node` | Kubernetes node logs  
`k8s_pod` | Kubernetes Pod logs  
`k8s_container` | Kubernetes container logs  
`k8s_control_plane_component` | Kubernetes control plane component logs  
  
When GKE writes your cluster's logs, each log entry includes the resource type. Understanding where your logs appear makes it easier to find your logs when you need them.

### System logs

**System logs** include logs from the following sources:

  * All Pods running in namespaces `kube-system`, `istio-system`, `knative-serving`, `gke-system`, and `config-management-system`.

  * Key services that are not containerized including `docker`/`containerd` runtime, `kubelet`, `kubelet-monitor`, `node-problem-detector`, and `kube-container-runtime-monitor`.

  * The node's serial ports' output, if the VM instance metadata `serial-port-logging-enable` is set to true. As of GKE 1.16-13-gke.400, [serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) for nodes is collected by the Logging agent. To disable serial port output logging, set `--metadata serial-port-logging-enable=false` during cluster creation. Serial port output is useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues with GKE nodes. Disabling these logs might limit troubleshooting.

  * All Kubernetes Events from components in the cluster. For more information, see Kubernetes Event logs.




Your system audit logs will appear in Cloud Logging with the following names:

  * projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access – Data Access logs
  * projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity – Admin Activity logs
  * projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event – System Event logs
  * projects/PROJECT_ID/logs/events - Kubernetes Event logs



For detailed information about log entries that apply to the Kubernetes Cluster and GKE Cluster Operations resource types, refer to the [Audit logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging) documentation.

There are additional system logs such as those for the kube-system that are written which are described in [Controlling the collection of your application logs](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing#controlling_the_collection_of_application_logs).

#### Kubernetes Event logs

In Kubernetes, Events are objects that provide information about resources, such as state changes, node errors, Pod errors, or scheduling failures. Various Kubernetes components, such as the `kubelet` or workload controllers, create Events to report changes in objects. For example, the StatefulSet controller might create an Event when the number of replicas in a StatefulSet changes. For more information about Events, see the [Event API reference page](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/) and the [Kubernetes glossary entry for Event](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-event).

You can find the logs for Kubernetes Events in Logging with the `projects/PROJECT_ID/logs/events` log name. Log entries for Events use one of the following resource types, depending on the component that created the Event in the Kubernetes API:

  * `k8s_pod`: Pod Events
  * `k8s_node`: Node Events
  * `k8s_cluster`: all Events that aren't Pod or Node Events



### Application logs

Kubernetes containers collect logs for your workloads written to `STDOUT` and `STDERR`. You can find your workload application logs using the `k8s_container` resource type. Your logs will appear in Logging with the following names:

  * projects/PROJECT_ID/logs/stderr – logs written to standard error

  * projects/PROJECT_ID/logs/stdout – logs written to standard out




### Control plane component logs

**Caution:** To apply your changes to log collection settings for control plane components, GKE restarts the control plane. In zonal Standard clusters, the control plane becomes unavailable until the restart operation completes. In regional clusters and Autopilot clusters, the control plane remains available.

If control plane logs are enabled for your GKE cluster, then logs emitted by certain Kubernetes control plane components (for instance, the API server, Scheduler, and Controller Manager) are exported to Cloud Logging.

These logs use the `k8s_control_plane_component` resource type and appear in Cloud Logging with the following names:

  * projects/PROJECT_ID/logs/container.googleapis.com%2Fapiserver

  * projects/PROJECT_ID/logs/container.googleapis.com%2Fscheduler

  * projects/PROJECT_ID/logs/container.googleapis.com%2Fcontroller-manager




### Control plane access logs

If you use GKE control plane authority, you can enable _optional logs_ for all incoming network connections to control plane instances and when SSH events occur in your control plane instances. You can then correlate these control plane access logs with logs from Access Transparency and with logs from the Kubernetes API server to optionally verify that connections to your control plane instances were the result of authorized _administrative access_ by Google personnel. For details, see [Verify Google connections to the cluster control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-google-connections-control-plane).

These logs use the `gke_cluster` resource type and appear in Cloud Logging with the following names:

  * `projects/PROJECT_ID/logs/container.googleapis.com%2Fkcp_connection`
  * `projects/PROJECT_ID/logs/container.googleapis.com%2Fkcp_ssh`



### Cluster identity issuance logs

If you use GKE control plane authority to run your own certificate authorities (CAs) and signing keys for your cluster, GKE generates audit logs for when those CAs and keys are used to issue X.509 certificates or JSON Web Tokens (JWTs) in your cluster. You can then correlate these identity issuance logs with logs from the Kubernetes API server, from Certificate Authority Service, and from Cloud Key Management Service to track the usage of those certificates and JWTs in your cluster. For details, see [Verify identity issuance and usage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage).

These logs are System Event audit logs use the `gke_cluster` resource type and appear in Cloud Logging with the following name:

  * `projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event`



## Finding your logs in the Logging user interface

You can view your logs using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the Logging user interface.

### Logs Explorer

Using the Query Builder, you can build a query either by selecting fields from a drop-down or by adding query parameters manually. For example, if you're reviewing logs for GKE clusters, you can start with selecting or searching for the Kubernetes Cluster resource type and then select the location and cluster name. You can then refine your search by selecting the Activity logs in the **Log Name** selector.

The Logs Explorer offers an additional way to build your search queries using the **Logs field explorer**. It shows the count of log entries, sorted by decreasing count, for the given log field. Using the **Logs field explorer** is particularly useful for GKE logs because the **Logs field explorer** provides a way to select the Kubernetes values for your resources to build a query. For example, using the **Logs field explorer** , you can select logs for a specific cluster, namespace, pod name, and then container name.

You can find more details in the Logging documentation about using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Sample queries

If you're looking for specific logs, use the following sample queries to help you find your GKE logs:

  * Sample Kubernetes-related log queries

    * [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library-preview#kubernetes-filters)
  * Sample Kubernetes Engine control plane log queries

    * [Audit log queries](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#example_filters_for_your_admin_activity_log)



## Troubleshoot common issues with logs

For advice about troubleshooting, see [Troubleshoot missing logs](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging).

## What's next

  * Learn more [about GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).
  * Learn how to [audit logging information](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).
  * Learn how to [control log ingestion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exclude-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
