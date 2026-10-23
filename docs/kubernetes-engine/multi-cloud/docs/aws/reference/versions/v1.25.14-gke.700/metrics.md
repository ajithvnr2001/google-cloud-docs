---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versions/v1.25.14-gke.700/metrics/
title: Metrics available in 1.25.14-gke.700 \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:27.215200+00:00
---

# Metrics available in 1.25.14-gke.700  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versions/v1.25.14-gke.700/metrics/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)



Send feedback 

#  Metrics available in 1.25.14-gke.700 Stay organized with collections  Save and categorize content based on your preferences. 

## Container resource metrics (node pool)

Metrics that measure resource usage of each container of each pod in the cluster.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/container/cpu/core_usage_time  
k8s_container | kubernetes.io/container/cpu/limit_cores  
k8s_container | kubernetes.io/container/cpu/request_cores  
k8s_container | kubernetes.io/container/ephemeral_storage/limit_bytes  
k8s_container | kubernetes.io/container/ephemeral_storage/request_bytes  
k8s_container | kubernetes.io/container/ephemeral_storage/used_bytes  
k8s_container | kubernetes.io/container/memory/limit_bytes  
k8s_container | kubernetes.io/container/memory/page_fault_count  
k8s_container | kubernetes.io/container/memory/request_bytes  
k8s_container | kubernetes.io/container/memory/used_bytes  
k8s_container | kubernetes.io/container/restart_count  
k8s_container | kubernetes.io/container/uptime  
  
## Node resource metrics (node pool)

Metrics that measure resource usage of each worker node in the cluster.

Resource | Metric name  
---|---  
k8s_node | kubernetes.io/node/cpu/allocatable_cores  
k8s_node | kubernetes.io/node/cpu/core_usage_time  
k8s_node | kubernetes.io/node/cpu/total_cores  
k8s_node | kubernetes.io/node/ephemeral_storage/allocatable_bytes  
k8s_node | kubernetes.io/node/ephemeral_storage/inodes_free  
k8s_node | kubernetes.io/node/ephemeral_storage/inodes_total  
k8s_node | kubernetes.io/node/ephemeral_storage/total_bytes  
k8s_node | kubernetes.io/node/ephemeral_storage/used_bytes  
k8s_node | kubernetes.io/node/memory/allocatable_bytes  
k8s_node | kubernetes.io/node/memory/total_bytes  
k8s_node | kubernetes.io/node/memory/used_bytes  
k8s_node | kubernetes.io/node_daemon/cpu/core_usage_time  
k8s_node | kubernetes.io/node_daemon/memory/used_bytes  
  
## Pod resource metrics (node pool)

Metrics that measure resource usage of each pod in the cluster.

Resource | Metric name  
---|---  
k8s_pod | kubernetes.io/pod/network/received_bytes_count  
k8s_pod | kubernetes.io/pod/network/sent_bytes_count  
k8s_pod | kubernetes.io/pod/volume/total_bytes  
k8s_pod | kubernetes.io/pod/volume/used_bytes  
  
## anet-operator

Metrics for the "cilium-operator" container in the "anet-operator" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/cilium_operator_ces_queueing_delay_seconds  
k8s_container | kubernetes.io/anthos/cilium_operator_ces_sync_errors_total  
k8s_container | kubernetes.io/anthos/cilium_operator_identity_gc_entries  
k8s_container | kubernetes.io/anthos/cilium_operator_identity_gc_runs  
k8s_container | kubernetes.io/anthos/cilium_operator_number_of_ceps_per_ces  
k8s_container | kubernetes.io/anthos/cilium_operator_process_cpu_seconds_total  
k8s_container | kubernetes.io/anthos/cilium_operator_process_max_fds  
k8s_container | kubernetes.io/anthos/cilium_operator_process_open_fds  
k8s_container | kubernetes.io/anthos/cilium_operator_process_start_time_seconds  
  
## anetd

Metrics for the "cilium-agent" container in the "anetd" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/cilium_agent_api_process_time_seconds  
k8s_container | kubernetes.io/anthos/cilium_bpf_map_ops_total  
k8s_container | kubernetes.io/anthos/cilium_datapath_conntrack_gc_duration_seconds  
k8s_container | kubernetes.io/anthos/cilium_datapath_conntrack_gc_entries  
k8s_container | kubernetes.io/anthos/cilium_datapath_conntrack_gc_runs_total  
k8s_container | kubernetes.io/anthos/cilium_drop_bytes_total  
k8s_container | kubernetes.io/anthos/cilium_drop_count_total  
k8s_container | kubernetes.io/anthos/cilium_endpoint_regeneration_time_stats_seconds  
k8s_container | kubernetes.io/anthos/cilium_endpoint_regenerations_total  
k8s_container | kubernetes.io/anthos/cilium_errors_warnings_total  
k8s_container | kubernetes.io/anthos/cilium_identity  
k8s_container | kubernetes.io/anthos/cilium_ipam_events_total  
k8s_container | kubernetes.io/anthos/cilium_policy_import_errors_total  
k8s_container | kubernetes.io/anthos/cilium_process_start_time_seconds  
k8s_container | kubernetes.io/anthos/cilium_triggers_policy_update_call_duration_seconds  
k8s_container | kubernetes.io/anthos/cilium_version  
k8s_container | kubernetes.io/anthos/policy_logging_allow_latency_microseconds  
k8s_container | kubernetes.io/anthos/policy_logging_deny_latency_seconds  
k8s_container | kubernetes.io/anthos/policy_logging_ready  
  
## coredns

Metrics for the "coredns" container in the "coredns" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/coredns_cache_entries  
k8s_container | kubernetes.io/anthos/coredns_cache_hits_total  
k8s_container | kubernetes.io/anthos/coredns_cache_misses_total  
k8s_container | kubernetes.io/anthos/coredns_dns_request_duration_seconds  
k8s_container | kubernetes.io/anthos/coredns_dns_requests_total  
k8s_container | kubernetes.io/anthos/coredns_dns_responses_total  
k8s_container | kubernetes.io/anthos/coredns_forward_request_duration_seconds  
k8s_container | kubernetes.io/anthos/coredns_forward_requests_total  
k8s_container | kubernetes.io/anthos/coredns_forward_responses_total  
k8s_container | kubernetes.io/anthos/coredns_health_request_duration_seconds  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
  
## fluentbit-gke

Metrics for the "fluentbit-gke" container in the "fluentbit-gke" pod in the "gke-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/fluentbit_input_bytes_total  
k8s_container | kubernetes.io/anthos/fluentbit_input_records_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_dropped_records_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_errors_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_proc_bytes_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_proc_records_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_retried_records_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_retries_failed_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_retries_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_stackdriver_failed_requests_total  
k8s_container | kubernetes.io/anthos/fluentbit_output_stackdriver_successful_requests_total  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
  
## gke-metrics-agent

Metrics for the "gke-metrics-agent" container in the "gke-metrics-agent" pod in the "gke-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/otelcol_exporter_send_failed_metric_points  
k8s_container | kubernetes.io/anthos/otelcol_exporter_sent_metric_points  
k8s_container | kubernetes.io/anthos/otelcol_receiver_accepted_metric_points  
k8s_container | kubernetes.io/anthos/otelcol_receiver_refused_metric_points  
  
## konnectivity-agent

Metrics for the "konnectivity-agent" container in the "konnectivity-agent" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
  
## kubelet (worker node)

Metrics for kubelet on each worker node.

Resource | Metric name  
---|---  
k8s_node | kubernetes.io/anthos/kubelet_http_requests_total  
k8s_node | kubernetes.io/anthos/kubelet_pod_start_duration_seconds  
k8s_node | kubernetes.io/anthos/kubelet_runtime_operations_duration_seconds  
k8s_node | kubernetes.io/anthos/kubelet_runtime_operations_errors_total  
k8s_node | kubernetes.io/anthos/kubelet_runtime_operations_total  
k8s_node | kubernetes.io/anthos/process_start_time_seconds  
k8s_node | kubernetes.io/anthos/rest_client_requests_total  
k8s_node | kubernetes.io/anthos/storage_operation_duration_seconds  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
