---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versions/v1.23.9-gke.2200/metrics/
title: Metrics available in 1.23.9-gke.2200 \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:22.520755+00:00
---

# Metrics available in 1.23.9-gke.2200  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versions/v1.23.9-gke.2200/metrics/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)



Send feedback 

#  Metrics available in 1.23.9-gke.2200 Stay organized with collections  Save and categorize content based on your preferences. 

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
