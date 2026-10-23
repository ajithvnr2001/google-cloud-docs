---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/versions/v1.35.3-gke.300/metrics/
title: Metrics available in 1.35.3-gke.300 \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:43.192991+00:00
---

# Metrics available in 1.35.3-gke.300  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/versions/v1.35.3-gke.300/metrics/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Metrics available in 1.35.3-gke.300

## Container resource metrics (control plane)

Metrics that measure resource usage of each container of each static pod on the control plane.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/container/cpu/core_usage_time  
k8s_container | kubernetes.io/anthos/container/cpu/limit_cores  
k8s_container | kubernetes.io/anthos/container/cpu/request_cores  
k8s_container | kubernetes.io/anthos/container/ephemeral_storage/limit_bytes  
k8s_container | kubernetes.io/anthos/container/ephemeral_storage/request_bytes  
k8s_container | kubernetes.io/anthos/container/ephemeral_storage/used_bytes  
k8s_container | kubernetes.io/anthos/container/memory/limit_bytes  
k8s_container | kubernetes.io/anthos/container/memory/page_fault_count  
k8s_container | kubernetes.io/anthos/container/memory/request_bytes  
k8s_container | kubernetes.io/anthos/container/memory/used_bytes  
k8s_container | kubernetes.io/anthos/container/restart_count  
k8s_container | kubernetes.io/anthos/container/uptime  
  
## Node resource metrics (control plane)

Metrics that measure resource usage of each control plane replica.

Resource | Metric name  
---|---  
k8s_node | kubernetes.io/anthos/node/cpu/core_usage_time  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/inodes_free  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/inodes_total  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/total_bytes  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/used_bytes  
k8s_node | kubernetes.io/anthos/node/memory/used_bytes  
k8s_node | kubernetes.io/anthos/node/network/received_bytes_count  
k8s_node | kubernetes.io/anthos/node/network/sent_bytes_count  
k8s_node | kubernetes.io/anthos/node_daemon/cpu/core_usage_time  
k8s_node | kubernetes.io/anthos/node_daemon/memory/used_bytes  
  
## Pod resource metrics (control plane)

Metrics that measure resource usage of each static pod on the control plane.

Resource | Metric name  
---|---  
k8s_pod | kubernetes.io/anthos/pod/network/received_bytes_count  
k8s_pod | kubernetes.io/anthos/pod/network/sent_bytes_count  
k8s_pod | kubernetes.io/anthos/pod/volume/total_bytes  
k8s_pod | kubernetes.io/anthos/pod/volume/used_bytes  
  
## audit-proxy

Metrics for the "audit-proxy" container in the "audit-proxy" pod in the "gke-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
  
## etcd

Metrics for the "kube-etcd" container in the "etcd" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/etcd_cluster_version  
k8s_container | kubernetes.io/anthos/etcd_disk_backend_commit_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_backend_defrag_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_backend_snapshot_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_wal_fsync_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_wal_write_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_cache_hits_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_cache_keys_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_cache_misses_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_events_coalescing_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_watchers_coalescing_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_db_open_read_transactions  
k8s_container | kubernetes.io/anthos/etcd_mvcc_db_total_size_in_bytes  
k8s_container | kubernetes.io/anthos/etcd_mvcc_db_total_size_in_use_in_bytes  
k8s_container | kubernetes.io/anthos/etcd_mvcc_delete_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_hash_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_mvcc_hash_rev_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_mvcc_put_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_range_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_txn_total  
k8s_container | kubernetes.io/anthos/etcd_network_active_peers  
k8s_container | kubernetes.io/anthos/etcd_network_client_grpc_received_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_client_grpc_sent_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_peer_received_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_peer_round_trip_time_seconds  
k8s_container | kubernetes.io/anthos/etcd_network_peer_sent_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_peer_sent_failures_total  
k8s_container | kubernetes.io/anthos/etcd_server_client_requests_total  
k8s_container | kubernetes.io/anthos/etcd_server_go_version  
k8s_container | kubernetes.io/anthos/etcd_server_has_leader  
k8s_container | kubernetes.io/anthos/etcd_server_health_failures  
k8s_container | kubernetes.io/anthos/etcd_server_health_success  
k8s_container | kubernetes.io/anthos/etcd_server_heartbeat_send_failures_total  
k8s_container | kubernetes.io/anthos/etcd_server_id  
k8s_container | kubernetes.io/anthos/etcd_server_is_leader  
k8s_container | kubernetes.io/anthos/etcd_server_is_learner  
k8s_container | kubernetes.io/anthos/etcd_server_leader_changes_seen_total  
k8s_container | kubernetes.io/anthos/etcd_server_learner_promote_successes  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_applied_total  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_committed_total  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_failed_total  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_pending  
k8s_container | kubernetes.io/anthos/etcd_server_quota_backend_bytes  
k8s_container | kubernetes.io/anthos/etcd_server_read_indexes_failed_total  
k8s_container | kubernetes.io/anthos/etcd_server_slow_apply_total  
k8s_container | kubernetes.io/anthos/etcd_server_slow_read_indexes_total  
k8s_container | kubernetes.io/anthos/etcd_server_snapshot_apply_in_progress_total  
k8s_container | kubernetes.io/anthos/etcd_server_version  
k8s_container | kubernetes.io/anthos/etcd_snap_db_fsync_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_snap_db_save_total_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_snap_fsync_duration_seconds  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
  
## etcd-events

Metrics for the "kube-etcd-events" container in the "etcd-events" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/etcd_cluster_version  
k8s_container | kubernetes.io/anthos/etcd_disk_backend_commit_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_backend_defrag_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_backend_snapshot_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_wal_fsync_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_disk_wal_write_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_cache_hits_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_cache_keys_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_cache_misses_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_events_coalescing_total  
k8s_container | kubernetes.io/anthos/etcd_grpc_proxy_watchers_coalescing_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_db_open_read_transactions  
k8s_container | kubernetes.io/anthos/etcd_mvcc_db_total_size_in_bytes  
k8s_container | kubernetes.io/anthos/etcd_mvcc_db_total_size_in_use_in_bytes  
k8s_container | kubernetes.io/anthos/etcd_mvcc_delete_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_hash_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_mvcc_hash_rev_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_mvcc_put_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_range_total  
k8s_container | kubernetes.io/anthos/etcd_mvcc_txn_total  
k8s_container | kubernetes.io/anthos/etcd_network_active_peers  
k8s_container | kubernetes.io/anthos/etcd_network_client_grpc_received_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_client_grpc_sent_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_peer_received_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_peer_round_trip_time_seconds  
k8s_container | kubernetes.io/anthos/etcd_network_peer_sent_bytes_total  
k8s_container | kubernetes.io/anthos/etcd_network_peer_sent_failures_total  
k8s_container | kubernetes.io/anthos/etcd_server_client_requests_total  
k8s_container | kubernetes.io/anthos/etcd_server_go_version  
k8s_container | kubernetes.io/anthos/etcd_server_has_leader  
k8s_container | kubernetes.io/anthos/etcd_server_health_failures  
k8s_container | kubernetes.io/anthos/etcd_server_health_success  
k8s_container | kubernetes.io/anthos/etcd_server_heartbeat_send_failures_total  
k8s_container | kubernetes.io/anthos/etcd_server_id  
k8s_container | kubernetes.io/anthos/etcd_server_is_leader  
k8s_container | kubernetes.io/anthos/etcd_server_is_learner  
k8s_container | kubernetes.io/anthos/etcd_server_leader_changes_seen_total  
k8s_container | kubernetes.io/anthos/etcd_server_learner_promote_successes  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_applied_total  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_committed_total  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_failed_total  
k8s_container | kubernetes.io/anthos/etcd_server_proposals_pending  
k8s_container | kubernetes.io/anthos/etcd_server_quota_backend_bytes  
k8s_container | kubernetes.io/anthos/etcd_server_read_indexes_failed_total  
k8s_container | kubernetes.io/anthos/etcd_server_slow_apply_total  
k8s_container | kubernetes.io/anthos/etcd_server_slow_read_indexes_total  
k8s_container | kubernetes.io/anthos/etcd_server_snapshot_apply_in_progress_total  
k8s_container | kubernetes.io/anthos/etcd_server_version  
k8s_container | kubernetes.io/anthos/etcd_snap_db_fsync_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_snap_db_save_total_duration_seconds  
k8s_container | kubernetes.io/anthos/etcd_snap_fsync_duration_seconds  
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
  
## gke-connect-agent

Metrics for the "gke-connect-agent" pod in the "gke-connect" namespace.

Resource | Metric name  
---|---  
k8s_pod | kubernetes.io/anthos/gkeconnect_dialer_connection_attempts_total  
k8s_pod | kubernetes.io/anthos/gkeconnect_dialer_connection_errors_total  
k8s_pod | kubernetes.io/anthos/gkeconnect_dialer_connections  
k8s_pod | kubernetes.io/anthos/gkeconnect_http_requests_total  
k8s_pod | kubernetes.io/anthos/process_start_time_seconds  
  
## gke-metrics-agent-cp

Metrics for the "gke-metrics-agent-cp" container in the "gke-metrics-agent-cp" pod in the "gke-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/otelcol_exporter_send_failed_metric_points  
k8s_container | kubernetes.io/anthos/otelcol_exporter_sent_metric_points  
k8s_container | kubernetes.io/anthos/otelcol_receiver_accepted_metric_points  
k8s_container | kubernetes.io/anthos/otelcol_receiver_refused_metric_points  
  
## gke-multicloud-agent

Metrics for the "gke-multicloud-agent" pod in the "gke-system" namespace.

Resource | Metric name  
---|---  
k8s_pod | kubernetes.io/anthos/gkeconnect_dialer_connection_attempts_total  
k8s_pod | kubernetes.io/anthos/gkeconnect_dialer_connection_errors_total  
k8s_pod | kubernetes.io/anthos/gkeconnect_dialer_connections  
k8s_pod | kubernetes.io/anthos/gkeconnect_http_requests_total  
k8s_pod | kubernetes.io/anthos/process_start_time_seconds  
  
## kube-apiserver

Metrics for the "kube-apiserver" container in the "kube-apiserver" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/aggregator_unavailable_apiservice  
k8s_container | kubernetes.io/anthos/apiserver_admission_controller_admission_duration_seconds  
k8s_container | kubernetes.io/anthos/apiserver_admission_step_admission_duration_seconds  
k8s_container | kubernetes.io/anthos/apiserver_admission_webhook_admission_duration_seconds  
k8s_container | kubernetes.io/anthos/apiserver_admission_webhook_rejection_count  
k8s_container | kubernetes.io/anthos/apiserver_admission_webhook_request_total  
k8s_container | kubernetes.io/anthos/apiserver_audit_event_total  
k8s_container | kubernetes.io/anthos/apiserver_audit_level_total  
k8s_container | kubernetes.io/anthos/apiserver_audit_requests_rejected_total  
k8s_container | kubernetes.io/anthos/apiserver_client_certificate_expiration_seconds  
k8s_container | kubernetes.io/anthos/apiserver_current_inflight_requests  
k8s_container | kubernetes.io/anthos/apiserver_current_inqueue_requests  
k8s_container | kubernetes.io/anthos/apiserver_kube_aggregator_x509_insecure_sha1_total  
k8s_container | kubernetes.io/anthos/apiserver_longrunning_requests  
k8s_container | kubernetes.io/anthos/apiserver_request_duration_seconds  
k8s_container | kubernetes.io/anthos/apiserver_request_total  
k8s_container | kubernetes.io/anthos/apiserver_requested_deprecated_apis  
k8s_container | kubernetes.io/anthos/apiserver_response_sizes  
k8s_container | kubernetes.io/anthos/apiserver_storage_objects  
k8s_container | kubernetes.io/anthos/apiserver_watch_events_total  
k8s_container | kubernetes.io/anthos/apiserver_webhooks_x509_insecure_sha1_total  
k8s_container | kubernetes.io/anthos/etcd_request_duration_seconds  
k8s_container | kubernetes.io/anthos/kubernetes_build_info  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
k8s_container | kubernetes.io/anthos/workqueue_work_duration_seconds  
  
## kube-controller-manager

Metrics for the "kube-controller-manager" container in the "kube-controller-manager" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/endpoint_slice_controller_changes  
k8s_container | kubernetes.io/anthos/endpoint_slice_controller_desired_endpoint_slices  
k8s_container | kubernetes.io/anthos/endpoint_slice_controller_endpoints_added_per_sync  
k8s_container | kubernetes.io/anthos/endpoint_slice_controller_endpoints_desired  
k8s_container | kubernetes.io/anthos/endpoint_slice_controller_endpoints_removed_per_sync  
k8s_container | kubernetes.io/anthos/endpoint_slice_controller_num_endpoint_slices  
k8s_container | kubernetes.io/anthos/ephemeral_volume_controller_create_failures_total  
k8s_container | kubernetes.io/anthos/garbagecollector_controller_resources_sync_error_total  
k8s_container | kubernetes.io/anthos/leader_election_master_status  
k8s_container | kubernetes.io/anthos/node_collector_evictions_total  
k8s_container | kubernetes.io/anthos/node_collector_unhealthy_nodes_in_zone  
k8s_container | kubernetes.io/anthos/node_collector_zone_health  
k8s_container | kubernetes.io/anthos/node_collector_zone_size  
k8s_container | kubernetes.io/anthos/node_ipam_controller_cidrset_cidrs_allocations_total  
k8s_container | kubernetes.io/anthos/node_ipam_controller_cidrset_usage_cidrs  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
k8s_container | kubernetes.io/anthos/running_managed_controllers  
k8s_container | kubernetes.io/anthos/workqueue_adds_total  
k8s_container | kubernetes.io/anthos/workqueue_depth  
k8s_container | kubernetes.io/anthos/workqueue_longest_running_processor_seconds  
k8s_container | kubernetes.io/anthos/workqueue_queue_duration_seconds  
k8s_container | kubernetes.io/anthos/workqueue_retries_total  
k8s_container | kubernetes.io/anthos/workqueue_unfinished_work_seconds  
k8s_container | kubernetes.io/anthos/workqueue_work_duration_seconds  
  
## kube-scheduler

Metrics for the "kube-scheduler" container in the "kube-scheduler" pod in the "kube-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/leader_election_master_status  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
k8s_container | kubernetes.io/anthos/scheduler_pending_pods  
k8s_container | kubernetes.io/anthos/scheduler_pod_scheduling_attempts  
k8s_container | kubernetes.io/anthos/scheduler_preemption_attempts_total  
k8s_container | kubernetes.io/anthos/scheduler_preemption_victims  
k8s_container | kubernetes.io/anthos/scheduler_queue_incoming_pods_total  
k8s_container | kubernetes.io/anthos/scheduler_schedule_attempts_total  
k8s_container | kubernetes.io/anthos/scheduler_scheduling_algorithm_duration_seconds  
k8s_container | kubernetes.io/anthos/scheduler_scheduling_attempt_duration_seconds  
  
## kubelet (control plane)

Metrics for kubelet on each control plane replica.

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
  
## kubestore-collector

Metrics for the "kubestore-collector" container in the "kubestore-collector" pod in the "gke-system" namespace.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/process_start_time_seconds  
  
## Container resource metrics (node pool)

Metrics that measure resource usage of each container of each pod in the cluster.

Resource | Metric name  
---|---  
k8s_container | kubernetes.io/anthos/container/cpu/core_usage_time  
k8s_container | kubernetes.io/anthos/container/cpu/limit_cores  
k8s_container | kubernetes.io/anthos/container/cpu/request_cores  
k8s_container | kubernetes.io/anthos/container/ephemeral_storage/limit_bytes  
k8s_container | kubernetes.io/anthos/container/ephemeral_storage/request_bytes  
k8s_container | kubernetes.io/anthos/container/ephemeral_storage/used_bytes  
k8s_container | kubernetes.io/anthos/container/memory/limit_bytes  
k8s_container | kubernetes.io/anthos/container/memory/page_fault_count  
k8s_container | kubernetes.io/anthos/container/memory/request_bytes  
k8s_container | kubernetes.io/anthos/container/memory/used_bytes  
k8s_container | kubernetes.io/anthos/container/restart_count  
k8s_container | kubernetes.io/anthos/container/uptime  
  
## Node resource metrics (node pool)

Metrics that measure resource usage of each worker node in the cluster.

Resource | Metric name  
---|---  
k8s_node | kubernetes.io/anthos/node/cpu/allocatable_cores  
k8s_node | kubernetes.io/anthos/node/cpu/core_usage_time  
k8s_node | kubernetes.io/anthos/node/cpu/total_cores  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/allocatable_bytes  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/inodes_free  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/inodes_total  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/total_bytes  
k8s_node | kubernetes.io/anthos/node/ephemeral_storage/used_bytes  
k8s_node | kubernetes.io/anthos/node/memory/allocatable_bytes  
k8s_node | kubernetes.io/anthos/node/memory/total_bytes  
k8s_node | kubernetes.io/anthos/node/memory/used_bytes  
k8s_node | kubernetes.io/anthos/node/network/received_bytes_count  
k8s_node | kubernetes.io/anthos/node/network/sent_bytes_count  
k8s_node | kubernetes.io/anthos/node_daemon/cpu/core_usage_time  
k8s_node | kubernetes.io/anthos/node_daemon/memory/used_bytes  
  
## Pod resource metrics (node pool)

Metrics that measure resource usage of each pod in the cluster.

Resource | Metric name  
---|---  
k8s_pod | kubernetes.io/anthos/pod/network/received_bytes_count  
k8s_pod | kubernetes.io/anthos/pod/network/sent_bytes_count  
k8s_pod | kubernetes.io/anthos/pod/volume/total_bytes  
k8s_pod | kubernetes.io/anthos/pod/volume/used_bytes  
  
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
