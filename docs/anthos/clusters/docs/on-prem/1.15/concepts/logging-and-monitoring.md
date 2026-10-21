---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring/
title: Logging and monitoring \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:01.195153+00:00
---

# Logging and monitoring  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/concepts/logging-and-monitoring)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/concepts/logging-and-monitoring)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud includes multiple options for cluster logging and monitoring, including cloud-based managed services, open source tools, and validated compatibility with third-party commercial solutions. This document explains these options and provides some basic guidance on selecting the proper solution for your environment.

## Options for Google Distributed Cloud

You have several logging and monitoring options for your Google Distributed Cloud:

  * [Cloud Logging](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#using-cloud-logging) and [Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#using-cloud-monitoring)
  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#using-managed-service-for-prometheus) (**Preview**)
  * [Prometheus and Grafana](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#using-prometheus-grafana)
  * Validated configurations with third-party solutions.



### Cloud Logging and Cloud Monitoring

Google Cloud Observability (formerly Stackdriver) is the built-in observability solution for Google Cloud. It offers a fully managed logging solution, metrics collection, monitoring, dashboarding, and alerting. Cloud Monitoring monitors Google Distributed Cloud clusters in a similar way as cloud-based GKE clusters.

You can configure the in-cluster agents for the scope of monitoring and logging, as well as the level of metrics collected:

  * Scope of logging and monitoring can be set to system components only (the default) or for system components and applications
  * Level of metrics collected can be configured for an optimized set of metrics or for full metrics



See Configuring logging and monitoring agents for Anthos clusters on VMware on this document for more information.

Cloud Logging and Cloud Monitoring provide an ideal solution for customers wanting a single, easy-to-configure, powerful cloud-based observability solution. We highly recommend Logging and Monitoring when running workloads only on Google Distributed Cloud, or workloads on GKE and Google Distributed Cloud. For applications with components running on Google Distributed Cloud and traditional on-premises infrastructure, you might consider other solutions for an end-to-end view of those applications.

  * For details about architecture, configuration, and what data is replicated to your Google Cloud project by default for Google Distributed Cloud, see the section How logging and monitoring for Google Distributed Cloud works.

  * For more information about Cloud Logging, see the [Cloud Logging](https://docs.cloud.google.com/logging/docs) documentation.

  * For more information about Cloud Monitoring, see the [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) documentation.




### Prometheus and Grafana

Prometheus and Grafana are two popular open source monitoring products:

  * [Prometheus](https://prometheus.io/docs/prometheus/latest) collects application and system metrics.

  * [Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) handles sending alerts out with several different alerting mechanisms.

  * [Grafana](https://grafana.com/docs/) is a dashboarding tool.




Prometheus and Grafana can be enabled on each admin cluster and user cluster. Prometheus and Grafana are recommended for application teams with prior experience with those products, or for operational teams who prefer to retain application metrics within the cluster and for troubleshooting issues when network connectivity is lost.

### Third-party solutions

Google has worked with several third-party logging and monitoring solution providers to help their products work well with Google Distributed Cloud. These include Datadog, Elastic, and Splunk. Additional validated third parties will be added in the future.

For more information about using third-party solutions with Google Distributed Cloud, see the following:

  * [Collect logs on Google Distributed Cloud with Splunk Connect](https://docs.cloud.google.com/solutions/logging-anthos-with-splunk-connect)
  * [Stretching Elastic's capabilities with historical analysis, backups, and cross-cloud monitoring on Google Cloud Platform](https://cloud.google.com/blog/products/gcp/stretching-elastics-capabilities-with-historical-analysis-backups-and-cross-cloud-monitoring-on-google-cloud-platform)



## How logging and monitoring for Google Distributed Cloud works

Logging and monitoring agents are installed and activated in each cluster when you create a new admin or user cluster. The agents collect data about system components—the scope of which you can configure.

To view the collected data on the Google Cloud console, you must configure the Google Cloud project that stores the logs and metrics you want to view.

The logging and monitoring agents on each cluster include:

  * **GKE metrics agent** (`gke-metrics-agent`). A DaemonSet that sends metrics to the Cloud Monitoring API.

  * **Log forwarder** (`stackdriver-log-forwarder`). A Fluent Bit DaemonSet that forwards logs from each machine to Cloud Logging. The log forwarder buffers the log entries on the node locally and resends them for up to four hours. If the buffer gets full or if the log forwarder can't reach the Cloud Logging API for more than four hours, then logs are dropped.

  * **Global GKE metrics agent** (`gke-metrics-agent-global`). A Deployment that sends metrics to the Cloud Monitoring API.

  * **Metadata agent** (`stackdriver-metadata-agent`). A Deployment that sends metadata for Kubernetes resources such as pods, deployments, or nodes to the Stackdriver Resource Metadata API; this data is used to enrich metric queries by enabling you to query by deployment name, node name, or even Kubernetes service name.




You can see all the Deployment agents by running the following command:
    
    
      kubectl --kubeconfig CLUSTER_KUBECONFIG get deployments -l "managed-by=stackdriver" --all-namespaces

where CLUSTER_KUBECONFIG is the path to your kubeconfig file for the cluster.

The output of this command is similar to the following:
    
    
    gke-metrics-agent-global                      1/1     Running   0   4h31m
    stackdriver-metadata-agent-cluster-level      1/1     Running   0   4h31m
    

You can see all the DaemonSet agents by running the following command:
    
    
      kubectl --kubeconfig CLUSTER_KUBECONFIG get daemonsets -l "managed-by=stackdriver" --all-namespaces

The output of this command is similar to the following:
    
    
    gke-metrics-agent                             1/1     Running   0   4h31m
    stackdriver-log-forwarder                     1/1     Running   0   4h31m
    

### Configuring logging and monitoring agents for Google Distributed Cloud

The agents installed with Google Distributed Cloud collect data about system components, subject to your settings and configuration, for the purposes of maintaining and troubleshooting issues with your clusters.

#### System components only (default scope)

Upon installation, agents collect logs and metrics, including performance details (for example, CPU and memory utilization) and similar metadata, for Google-provided system components. These include all workloads in the admin cluster, and for user clusters, workloads in the kube-system, gke-system, gke-connect, istio-system, and config-management-system namespaces. You can configure or disable the agents as described in the following sections.

The scope of logs and metrics collected can be expanded to include applications as well. For instructions to enable application logging and monitoring, see [Enabling Logging and Monitoring for user applications](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/application-logging-monitoring#enabling_and_for_user_applications).

#### Optimized metrics (default metrics)

By default, the metrics agents running in the cluster collect and report an optimized set of container, kubelet and kube-state-metrics metrics to Google Cloud Observability (formerly Stackdriver).

Fewer resources are needed to collect this optimized set of metrics, which improves overall performance and scalability. This is especially important for container-level and kube-level metrics, due to the large quantity of objects to monitor.

##### Excluded container metrics

The following container metrics are excluded from the optimized metrics:

  * container_cpu_cfs_periods_total
  * container_cpu_cfs_throttled_periods_total
  * container_cpu_load_average_10s
  * container_cpu_system_seconds_total
  * container_cpu_user_seconds_total
  * container_fs_io_current
  * container_fs_io_time_seconds_total
  * container_fs_io_time_weighted_seconds_total
  * container_fs_read_seconds_total
  * container_fs_reads_bytes_total
  * container_fs_reads_merged_total
  * container_fs_reads_total
  * container_fs_sector_reads_total
  * container_fs_sector_writes_total
  * container_fs_write_seconds_total
  * container_fs_writes_bytes_total
  * container_fs_writes_merged_total
  * container_fs_writes_total
  * container_last_seen
  * container_memory_cache
  * container_memory_failcnt
  * container_memory_mapped_file
  * container_memory_max_usage_bytes
  * container_memory_swap
  * container_network_receive_packets_dropped_total
  * container_network_receive_packets_total
  * container_network_transmit_packets_dropped_total
  * container_network_transmit_packets_total
  * container_start_time_seconds
  * container_spec_cpu_period
  * container_spec_cpu_quota
  * container_spec_cpu_shares
  * container_spec_memory_limit_bytes
  * container_spec_memory_reservation_limit_bytes
  * container_spec_memory_swap_limit_bytes
  * container_start_time_seconds
  * container_tasks_state



The complete set of Google Distributed Cloud metrics is documented in [GKE Enterprise metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos#anthos).

##### Excluded kubelet metrics

The following kubelet metrics are excluded from the optimized metrics:

  * kubelet_runtime_operations_duration_seconds
  * kubelet_runtime_operations_errors
  * kubelet_runtime_operations_duration_seconds
  * kubelet_runtime_operations_latency_microseconds
  * kubelet_runtime_operations_latency_microseconds_count
  * kubelet_runtime_operations_latency_microseconds_sum
  * rest_client_request_duration_seconds
  * rest_client_request_latency_seconds



The complete set of Google Distributed Cloud metrics is documented in [GKE Enterprise metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos#anthos).

##### Excluded kube-state-metrics metrics

The following kube-state-metrics metrics are excluded from the optimized metrics:

  * kube_certificatesigningrequest_cert_length
  * kube_certificatesigningrequest_condition
  * kube_certificatesigningrequest_created
  * kube_certificatesigningrequest_labels
  * kube_configmap_annotations
  * kube_configmap_info
  * kube_configmap_labels
  * kube_configmap_metadata_resource_version
  * kube_daemonset_annotations
  * kube_daemonset_created
  * kube_daemonset_labels
  * kube_daemonset_metadata_generation
  * kube_daemonset_status_observed_generation
  * kube_deployment_annotations
  * kube_deployment_created
  * kube_deployment_labels
  * kube_deployment_spec_paused
  * kube_deployment_spec_strategy_rollingupdate_max_surge
  * kube_deployment_spec_strategy_rollingupdate_max_unavailable
  * kube_deployment_status_condition
  * kube_deployment_status_replicas_ready
  * kube_endpoint_annotations
  * kube_endpoint_created
  * kube_endpoint_info
  * kube_endpoint_labels
  * kube_endpoint_ports
  * kube_horizontalpodautoscaler_annotations
  * kube_horizontalpodautoscaler_info
  * kube_horizontalpodautoscaler_labels
  * kube_horizontalpodautoscaler_metadata_generation
  * kube_horizontalpodautoscaler_status_condition
  * kube_job_annotations
  * kube_job_complete
  * kube_job_created
  * kube_job_info
  * kube_job_labels
  * kube_job_owner
  * kube_job_spec_completions
  * kube_job_spec_parallelism
  * kube_job_status_completion_time
  * kube_job_status_start_time
  * kube_job_status_succeeded
  * kube_lease_owner
  * kube_lease_renew_time
  * kube_limitrange
  * kube_limitrange_created
  * kube_mutatingwebhookconfiguration_info
  * kube_namespace_labels
  * kube_networkpolicy_annotations
  * kube_networkpolicy_labels
  * kube_networkpolicy_spec_egress_rules
  * kube_networkpolicy_spec_ingress_rules
  * kube_node_annotations
  * kube_node_role
  * kube_persistentvolume_annotations
  * kube_persistentvolume_labels
  * kube_persistentvolumeclaim_access_mode
  * kube_persistentvolumeclaim_annotations
  * kube_persistentvolumeclaim_labels
  * kube_pod_annotations
  * kube_pod_completion_time
  * kube_pod_container_resource_limits
  * kube_pod_container_resource_requests
  * kube_pod_container_state_started
  * kube_pod_created
  * kube_pod_init_container_info
  * kube_pod_init_container_resource_limits
  * kube_pod_init_container_resource_requests
  * kube_pod_init_container_status_last_terminated_reason
  * kube_pod_init_container_status_ready
  * kube_pod_init_container_status_restarts_total
  * kube_pod_init_container_status_running
  * kube_pod_init_container_status_terminated
  * kube_pod_init_container_status_terminated_reason
  * kube_pod_init_container_status_waiting
  * kube_pod_init_container_status_waiting_reason
  * kube_pod_labels
  * kube_pod_owner
  * kube_pod_restart_policy
  * kube_pod_spec_volumes_persistentvolumeclaims_readonly
  * kube_pod_start_time
  * kube_poddisruptionbudget_annotations
  * kube_poddisruptionbudget_created
  * kube_poddisruptionbudget_labels
  * kube_poddisruptionbudget_status_expected_pods
  * kube_poddisruptionbudget_status_observed_generation
  * kube_poddisruptionbudget_status_pod_disruptions_allowed
  * kube_replicaset_annotations
  * kube_replicaset_created
  * kube_replicaset_labels
  * kube_replicaset_metadata_generation
  * kube_replicaset_owner
  * kube_replicaset_status_observed_generation
  * kube_resourcequota_created
  * kube_secret_annotations
  * kube_secret_info
  * kube_secret_labels
  * kube_secret_metadata_resource_version
  * kube_secret_type
  * kube_service_annotations
  * kube_service_created
  * kube_service_info
  * kube_service_labels
  * kube_service_spec_type
  * kube_statefulset_annotations
  * kube_statefulset_created
  * kube_statefulset_labels
  * kube_statefulset_status_current_revision
  * kube_statefulset_status_update_revision
  * kube_storageclass_annotations
  * kube_storageclass_created
  * kube_storageclass_info
  * kube_storageclass_labels
  * kube_validatingwebhookconfiguration_info
  * kube_validatingwebhookconfiguration_metadata_resource_version
  * kube_volumeattachment_created
  * kube_volumeattachment_info
  * kube_volumeattachment_labels
  * kube_volumeattachment_spec_source_persistentvolume
  * kube_volumeattachment_status_attached
  * kube_volumeattachment_status_attachment_metadata



The complete set of Google Distributed Cloud metrics is documented in [GKE Enterprise metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos#anthos).

To disable optimized kube-state-metrics metrics (not recommended), set the `optimizedMetrics` field to `false` in your Stackdriver custom resource. For more information on changing your Stackdriver custom resource, see [Configuring Stackdriver component resources](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#configuring_stackdriver_component_resources). All Google Distributed Cloud metrics, including those excluded by default, are described in [GKE Enterprise metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos#anthos).

#### Enable and disable Stackdriver

You can enable or disable logging and monitoring agents completely by [enabling or disabling the Stackdriver custom resource](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#enable_or_disable_logging_and_monitoring_for_a_user_cluster_preview). This feature is in Preview.

Before you disable the logging and monitoring agents, see the [support page](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/getting-support) for details about how this affects Google Cloud Support's SLAs.

Logging and monitoring agents capture data stored locally, subject to your storage and retention configuration. The data is replicated to the Google Cloud project specified at installation by using a service account that is authorized to write data to that project. You can disable these agents at any time, as described earlier.

You can also manage and delete data that the logging and monitoring agents have sent to Cloud Logging and Cloud Monitoring. For more information, see [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

### Configuration requirements for logging and monitoring

To view Cloud Logging and Cloud Monitoring data, you must configure the Google Cloud project that stores the logs and metrics you want to view. This Google Cloud project is called your [logging-monitoring project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#logging_monitoring_project).

  1. Enable the following APIs in your logging-monitoring project:

     * [Stackdriver API](https://console.cloud.google.com/apis/api/stackdriver.googleapis.com/overview)
     * [Cloud Monitoring API](https://console.cloud.google.com/apis/api/monitoring.googleapis.com/overview)
     * [Cloud Logging API](https://console.cloud.google.com/apis/api/logging.googleapis.com/overview)
     * [Config Monitoring for Ops API](https://console.cloud.google.com/apis/api/opsconfigmonitoring.googleapis.com)
  2. Grant the following IAM roles to your [logging-monitoring service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#logging_monitoring_service_account) on your logging-monitoring project.

     * `logging.logWriter`
     * `monitoring.metricWriter`
     * `stackdriver.resourceMetadata.writer`
     * `monitoring.dashboardEditor`
     * `opsconfigmonitoring.resourceMetadata.writer`



### Pricing

For a GKE Enterprise cluster, there is no charge for [control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics), curated [kube state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics), [cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics), or [DCGM metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics). System logs, control plane logs, and workload logs incur [Cloud Logging charges](https://cloud.google.com/products/observability/pricing). Control plane logs, control plane metrics, kube state metrics, cAdvisor/Kubelet metrics, and DCGM metrics are [enabled by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#default-metrics-enterprise) for GKE clusters on Google Cloud that are registered at cluster creation time in a GKE Enterprise-enabled project. For the list of included GKE logs and metrics, see [What logs are collected](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#what_logs) and [Available metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics).

In a Google Distributed Cloud cluster, there is no charge for GKE Enterprise system logs and metrics, which include the following:

  * Logs and metrics from all components in an admin cluster.
  * Logs and metrics from components in these namespaces in a user cluster: `kube-system`, `gke-system`, `gke-connect`, `knative-serving`, `istio-system`, `monitoring-system`, `config-management-system`, `gatekeeper-system`, `cnrm-system`.



For more information, see [Pricing for Google Cloud Observability](https://cloud.google.com/stackdriver/pricing).

To learn about credit for Cloud Logging metrics, [contact sales for pricing](https://cloud.google.com/contact).

## How Prometheus and Grafana for Google Distributed Cloud work

Each Google Distributed Cloud cluster is created with Prometheus and Grafana disabled by default. You can follow the [installation guide](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#prometheus_and_grafana) to enable them.

**Note:** The set of logging agents includes an embedded instance of Prometheus. This instance is separate from the Prometheus and Grafana instance discussed in this section. You should not modify the Cloud Logging Prometheus instance.

The Prometheus Server is set up in a highly-available configuration with two replicas running on two separate nodes. Resource requirements are adjusted to support clusters running up to five nodes, with each handling up to 30 Pods that serve custom metrics. Prometheus has a dedicated PersistentVolume with disk space preallocated to fit data for a retention period of four days plus an added safety buffer.

The admin control plane, as well as each user cluster, has a dedicated monitoring stack that you can configure independently. Each admin and user cluster includes a monitoring stack that delivers a full set of features: Prometheus Server for monitoring, Grafana for observability, and Prometheus Alertmanager for alerting.

All monitoring endpoints, transferred metric data, and monitoring APIs are secured with Istio components by using mTLS and RBAC rules. Access to monitoring data is restricted only to cluster administrators.

### Metrics collected by Prometheus

Prometheus collects the following metrics and metadata from the admin control plane and user clusters:

  * Resource usage, such as CPU utilization on Pods and nodes.
  * Kubernetes control plane metrics.
  * Metrics from add-ons and Kubernetes system components running on nodes, such as kubelet.
  * Cluster state, such as health of Pods in a Deployment.
  * Application metrics.
  * Machine metrics, such as network, entropy, and inodes.



### Multi-cluster monitoring

The Prometheus and Grafana instance installed on the admin cluster is specially configured to provide insight across the entire Google Distributed Cloud instance, including the admin cluster and each user cluster. This enables you to:

  * Use a Grafana dashboard to access metrics from all user clusters and admin clusters.
  * View metrics from individual user clusters on Grafana dashboards; the metrics are available for direct queries in full resolution.
  * Access user clusters' node-level and workload metrics for aggregated queries, dashboards and alerting (workload metrics are limited to workloads running in the kube-system namespace).
  * Configure alerts for specific clusters.



## What's next

  * [Using Logging and Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
