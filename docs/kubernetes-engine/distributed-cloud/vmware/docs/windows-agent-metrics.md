---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/windows-agent-metrics/
title: Windows agent metrics \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:19.475575+00:00
---

# Windows agent metrics  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/windows-agent-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)



Send feedback 

#  Windows agent metrics Stay organized with collections  Save and categorize content based on your preferences. 

This topic lists metrics captured by the Windows agent.
    
    
    # Summary API metrics:
    kubernetes.io/anthos/container/cpu/core_usage_time
    kubernetes.io/anthos/container/cpu/limit_cores
    kubernetes.io/anthos/container/cpu/request_cores
    kubernetes.io/anthos/container/ephemeral_storage/limit_bytes
    kubernetes.io/anthos/container/ephemeral_storage/request_bytes
    kubernetes.io/anthos/container/ephemeral_storage/used_bytes
    kubernetes.io/anthos/container/memory/limit_bytes
    kubernetes.io/anthos/container/memory/request_bytes
    kubernetes.io/anthos/container/memory/used_bytes
    kubernetes.io/anthos/container/restart_count
    kubernetes.io/anthos/container/uptime
    kubernetes.io/anthos/node/cpu/allocatable_cores
    kubernetes.io/anthos/node/cpu/core_usage_time
    kubernetes.io/anthos/node/cpu/total_cores
    kubernetes.io/anthos/node_daemon/cpu/core_usage_time
    kubernetes.io/anthos/node_daemon/memory/used_bytes
    kubernetes.io/anthos/node/ephemeral_storage/allocatable_bytes
    kubernetes.io/anthos/node/ephemeral_storage/total_bytes
    kubernetes.io/anthos/node/ephemeral_storage/used_bytes
    kubernetes.io/anthos/node/memory/allocatable_bytes
    kubernetes.io/anthos/node/memory/total_bytes
    kubernetes.io/anthos/node/memory/used_bytes
    kubernetes.io/anthos/pod/network/received_bytes_count
    kubernetes.io/anthos/pod/network/sent_bytes_count
    kubernetes.io/anthos/pod/volume/total_bytes
    kubernetes.io/anthos/pod/volume/used_bytes
     
    # kubelet metrics:
    kubernetes.io/anthos/apiserver_audit_event_total
    kubernetes.io/anthos/apiserver_audit_requests_rejected_total
    kubernetes.io/anthos/apiserver_client_certificate_expiration_seconds
    kubernetes.io/anthos/apiserver_envelope_encryption_dek_cache_fill_percent
    kubernetes.io/anthos/apiserver_storage_data_key_generation_duration_seconds
    kubernetes.io/anthos/apiserver_storage_data_key_generation_failures_total
    kubernetes.io/anthos/apiserver_storage_envelope_transformation_cache_misses_total
    kubernetes.io/anthos/authentication_token_cache_active_fetch_count
    kubernetes.io/anthos/authentication_token_cache_fetch_total
    kubernetes.io/anthos/authentication_token_cache_request_duration_seconds
    kubernetes.io/anthos/authentication_token_cache_request_total
    kubernetes.io/anthos/get_token_count
    kubernetes.io/anthos/get_token_fail_count
    kubernetes.io/anthos/go_goroutines
    kubernetes.io/anthos/go_info
    kubernetes.io/anthos/go_memstats_alloc_bytes
    kubernetes.io/anthos/go_memstats_alloc_bytes_total
    kubernetes.io/anthos/go_memstats_buck_hash_sys_bytes
    kubernetes.io/anthos/go_memstats_frees_total
    kubernetes.io/anthos/go_memstats_gc_cpu_fraction
    kubernetes.io/anthos/go_memstats_gc_sys_bytes
    kubernetes.io/anthos/go_memstats_heap_alloc_bytes
    kubernetes.io/anthos/go_memstats_heap_idle_bytes
    kubernetes.io/anthos/go_memstats_heap_inuse_bytes
    kubernetes.io/anthos/go_memstats_heap_objects
    kubernetes.io/anthos/go_memstats_heap_released_bytes
    kubernetes.io/anthos/go_memstats_heap_sys_bytes
    kubernetes.io/anthos/go_memstats_last_gc_time_seconds
    kubernetes.io/anthos/go_memstats_lookups_total
    kubernetes.io/anthos/go_memstats_mallocs_total
    kubernetes.io/anthos/go_memstats_mcache_inuse_bytes
    kubernetes.io/anthos/go_memstats_mcache_sys_bytes
    kubernetes.io/anthos/go_memstats_mspan_inuse_bytes
    kubernetes.io/anthos/go_memstats_mspan_sys_bytes
    kubernetes.io/anthos/go_memstats_next_gc_bytes
    kubernetes.io/anthos/go_memstats_other_sys_bytes
    kubernetes.io/anthos/go_memstats_stack_inuse_bytes
    kubernetes.io/anthos/go_memstats_stack_sys_bytes
    kubernetes.io/anthos/go_memstats_sys_bytes
    kubernetes.io/anthos/go_threads
    kubernetes.io/anthos/kubelet_certificate_manager_client_expiration_renew_errors
    kubernetes.io/anthos/kubelet_certificate_manager_client_ttl_seconds
    kubernetes.io/anthos/kubelet_certificate_manager_server_rotation_seconds
    kubernetes.io/anthos/kubelet_certificate_manager_server_ttl_seconds
    kubernetes.io/anthos/kubelet_container_log_filesystem_used_bytes
    kubernetes.io/anthos/kubelet_containers_per_pod_count
    kubernetes.io/anthos/kubelet_docker_operations_duration_seconds
    kubernetes.io/anthos/kubelet_docker_operations_errors_total
    kubernetes.io/anthos/kubelet_docker_operations_total
    kubernetes.io/anthos/kubelet_http_inflight_requests
    kubernetes.io/anthos/kubelet_http_requests_duration_seconds
    kubernetes.io/anthos/kubelet_http_requests_total
    kubernetes.io/anthos/kubelet_network_plugin_operations_duration_seconds
    kubernetes.io/anthos/kubelet_network_plugin_operations_errors_total
    kubernetes.io/anthos/kubelet_network_plugin_operations_total
    kubernetes.io/anthos/kubelet_node_config_error
    kubernetes.io/anthos/kubelet_node_name
    kubernetes.io/anthos/kubelet_pleg_discard_events
    kubernetes.io/anthos/kubelet_pleg_last_seen_seconds
    kubernetes.io/anthos/kubelet_pleg_relist_duration_seconds
    kubernetes.io/anthos/kubelet_pleg_relist_interval_seconds
    kubernetes.io/anthos/kubelet_pod_start_duration_seconds
    kubernetes.io/anthos/kubelet_pod_worker_duration_seconds
    kubernetes.io/anthos/kubelet_pod_worker_start_duration_seconds
    kubernetes.io/anthos/kubelet_running_containers
    kubernetes.io/anthos/kubelet_running_pods
    kubernetes.io/anthos/kubelet_run_podsandbox_duration_seconds
    kubernetes.io/anthos/kubelet_run_podsandbox_errors_total
    kubernetes.io/anthos/kubelet_runtime_operations_duration_seconds
    kubernetes.io/anthos/kubelet_runtime_operations_errors_total
    kubernetes.io/anthos/kubelet_runtime_operations_total
    kubernetes.io/anthos/kubelet_server_expiration_renew_errors
    kubernetes.io/anthos/kubernetes_build_info
    kubernetes.io/anthos/process_cpu_seconds_total
    kubernetes.io/anthos/process_max_fds
    kubernetes.io/anthos/process_open_fds
    kubernetes.io/anthos/process_resident_memory_bytes
    kubernetes.io/anthos/process_start_time_seconds
    kubernetes.io/anthos/process_virtua
    kubernetes.io/anthos/process_virtual_memory_bytes
    kubernetes.io/anthos/rest_client_exec_plugin_certificate_rotation_age
    kubernetes.io/anthos/rest_client_exec_plugin_ttl_seconds
    kubernetes.io/anthos/rest_client_request_duration_seconds
    kubernetes.io/anthos/rest_client_requests_total
    kubernetes.io/anthos/storage_operation_duration_seconds
    kubernetes.io/anthos/storage_operation_status_count
    kubernetes.io/anthos/volume_manager_total_volumes
    kubernetes.io/anthos/workqueue_adds_total
    kubernetes.io/anthos/workqueue_depth
    kubernetes.io/anthos/workqueue_longest_running_processor_seconds
    kubernetes.io/anthos/workqueue_queue_duration_seconds
    kubernetes.io/anthos/workqueue_retries_total
    kubernetes.io/anthos/workqueue_unfinished_work_seconds
    kubernetes.io/anthos/workqueue_work_duration_seconds
     
    # Open Telemetry metrics:
    kubernetes.io/anthos/otelcol_exporter_send_failed_metric_points
    kubernetes.io/anthos/otelcol_exporter_sent_metric_points
    kubernetes.io/anthos/otelcol_googlecloudmonitoring_point_count
    kubernetes.io/anthos/otelcol_process_cpu_seconds
    kubernetes.io/anthos/otelcol_process_memory_rss
    kubernetes.io/anthos/otelcol_process_runtime_heap_alloc_bytes
    kubernetes.io/anthos/otelcol_process_runtime_total_alloc_bytes
    kubernetes.io/anthos/otelcol_process_runtime_total_sys_memory_bytes
    kubernetes.io/anthos/otelcol_process_uptime
    kubernetes.io/anthos/otelcol_receiver_accepted_metric_points
    kubernetes.io/anthos/otelcol_receiver_refused_metric_points
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
