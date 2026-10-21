---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-kub/
title: User Clusters (KUB) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:30:41.092345+00:00
---

# User Clusters (KUB)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-kub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  User Clusters (KUB) Stay organized with collections  Save and categorize content based on your preferences. 

Name and description  |  Type  |  Emit duration  |  Labels   
---|---|---|---  
` cluster_total_pods_count `  
Number of pods in a cluster. An aggregated metric type based on `kube_pod_info`.  
  
|  Gauge  |  15 s  |  **cluster**  
` cluster_total_services_count `  
Number of services in a cluster. An aggregated metric type based on `kube_service_info`.  
  
|  Gauge  |  15 s  |  **cluster**  
` cluster_total_nodes_count `  
Number of nodes in a cluster. An aggregated metric type based on `kube_node_info`.  
  
|  Gauge  |  15 s  |  **cluster**  
` cluster_cpu_utilization `  
Cluster CPU utilization rate. An aggregated metric type based on `node_cpu_seconds_total`.  
  
|  Gauge  |  15 s  | **cluster**  
` cluster_memory_utilization `  
Cluster memory utilization rate. An aggregated metric type based on `node_memory_MemAvailable_bytes`.  
  
|  Gauge  |  15 s  |  **cluster**  
` cluster_apiserver_request_total `  
Number of requests to the cluster API server. An aggregated metric type based on `apiserver_request_total`.  
  
|  Counter  |  15 s  |  **cluster**  
` cluster_etcd_storage_size_in_bytes `  
Storage size of the cluster etcd. An aggregated metric type based on `etcd_db_total_size_in_bytes`.  
  
|  Gauge  |  15 s  |  **cluster**  
` cluster_apiserver_request_latency_bucket_in_seconds `  
The latency for each request to the cluster API server in seconds. An aggregated metric type based on `apiserver_request_duration_seconds_bucket`.  
  
|  Histogram  |  15 s  | 

  * **cluster**
  * **verb**
  * **le**

  
` cluster_operation_duration_seconds_sum `  
Duration in seconds of cluster operations, such as installation.  |  Counter  |  1 m  | 

  * **cluster_type**
  * **instance**
  * **job**
  * **operation**
  * **operation_id**
  * **source**
  * **status**
  * **target_cluster_name**
  * **target_cluster_version**

  
` cluster_operation_duration_seconds_count `  
Count of cluster operations, such as installation.  |  Counter  |  1 m  | 

  * **cluster_type**
  * **instance**
  * **job**
  * **operation**
  * **operation_id**
  * **source**
  * **status**
  * **target_cluster_name**
  * **target_cluster_version**

  
` cluster_apc_reconciliation_error_count `  
Count of errors during an address pool claim reconciliation.  |  Counter  |  1 m  | 

  * **address_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_apc_reconciliation_count `  
Count of reconciliations for an address pool claim.  |  Counter  |  1 m  | 

  * **address_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_apc_update_count `  
Count of updates or resizing operations for an address pool claim.  |  Counter  |  1 m  | 

  * **address_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_sc_reconciliation_count `  
Count of reconciliations for a subnet claim.  |  Counter  |  1 m  | 

  * **subnet_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_sc_reconciliation_error_count `  
Count of errors during a subnet claim reconciliation.  |  Counter  |  1 m  | 

  * **subnet_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_cidr_claim_reconciliation_count `  
Count of reconciliations for a Classless Inter-Domain Routing (CIDR) claim.  |  Counter  |  1 m  | 

  * **cidr_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_cidr_claim_reconciliation_error_count `  
Count of errors during a CIDR claim reconciliation.  |  Counter  |  1 m  | 

  * **cidr_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_apc_total `  
Number of address pool claims in a cluster.  |  Gauge  |  1 m  | 

  * **cluster**
  * **organization**

  
` cluster_apc_requested_size `  
Number of requested IPs for an address pool claim.  |  Gauge  |  1 m  | 

  * **address_pool_claim**
  * **namespace**
  * **category**
  * **ip_family**
  * **subnet_claim**
  * **cluster**
  * **organization**

  
` cluster_apc_allocated_size `  
Number of allocated IPs for an address pool claim.  |  Gauge  |  1 m  | 

  * **address_pool_claim**
  * **namespace**
  * **category**
  * **ip_family**
  * **subnet_claim**
  * **cluster**
  * **organization**

  
` cluster_sc_total `  
Number of subnet claims in a cluster.  |  Gauge  |  1 m  |  **organization**  
` cluster_sc_available_ip_size `  
Number of available IP range size for a subnet claim.  |  Gauge  |  1 m  | 

  * **subnet_claim**
  * **namespace**
  * **category**
  * **ip_family**
  * **overlay_network**
  * **cidr_claim**
  * **organization**

  
` cluster_cidr_total `  
Number of CIDR claims in a cluster.  |  Gauge  |  1 m  | 

  * **cluster**
  * **organization**

  
` cluster_npc_reconciliation_count `  
Count of reconciliations for a node pool claim.  |  Counter  |  1 m  | 

  * **node_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_npc_reconciliation_error_count `  
Count of errors during a node pool claim reconciliation.  |  Counter  |  1 m  | 

  * **node_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_npc_update_count `  
Count of updates or resizing operations for a node pool claim.  |  Counter  |  1 m  | 

  * **node_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_npc_total `  
Number of node pool claims in a cluster.  |  Gauge  |  1 m  | 

  * **node_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**

  
` cluster_npc_requested_size `  
Number of requested nodes from a node pool claim.  |  Gauge  |  1 m  | 

  * **node_pool_claim**
  * **namespace**
  * **cluster**
  * **organization**
  * **machine_class**

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
