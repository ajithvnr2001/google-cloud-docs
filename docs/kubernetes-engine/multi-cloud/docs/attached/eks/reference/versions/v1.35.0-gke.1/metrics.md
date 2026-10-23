---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.35.0-gke.1/metrics/
title: Metrics available in 1.35.0-gke.1 \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:55.659730+00:00
---

# Metrics available in 1.35.0-gke.1  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.35.0-gke.1/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)



Send feedback 

#  Metrics available in 1.35.0-gke.1 Stay organized with collections  Save and categorize content based on your preferences. 

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
