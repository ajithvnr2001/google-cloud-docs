---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metric-com/
title: Controller Manager (COM) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:23.657586+00:00
---

# Controller Manager (COM)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metric-com/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Controller Manager (COM) Stay organized with collections  Save and categorize content based on your preferences. 

## Metrics list

Name and Description | Type | Scrape interval | Labels  
---|---|---|---  
`up`  
A binary metric that indicates whether a target, which is usually a server or service, is up. | Gauge | 5 m | 

  * **pod_name** : The name of the pod.
  * **job** : The name of the job.

  
`kube_pod_container_status_restarts_total`  
The number of container restarts per container. | Counter | 5 m | 

  * **container** : The name of the container.
  * **pod** : The name of the pod.
  * **namespace** : The namespace of the pod.
  * **uid** : The unique ID of the pod.

  
`kube_pod_container_status_waiting_reason`  
The reason the container is currently in the waiting state. | Gauge | 5 m | 

  * **container** : The name of the container.
  * **pod** : The name of the pod.
  * **namespace** : The namespace of the pod.
  * **reason** : The reason for the waiting state of the container.
  * **uid** : The unique ID of the pod.

  
`container_cpu_usage_seconds_total`  
The cumulative CPU time consumed. | Counter | 5 m |   
`kube_pod_container_resource_requests`  
The number of resources a container requested. If possible, use the `kube_pod_resource_requests` metric exposed by the kube-scheduler instead, as it is more precise. | Gauge | 5 m | 

  * **resource** : The name of the resource.
  * **unit** : The resource unit.
  * **container** : The name of the container.
  * **pod** : The name of the pod.
  * **namespace** : The namespace of the pod.
  * **node** : The name of the node.
  * **uid** : The unique ID of the pod.

  
`kube_pod_container_resource_limits`  
The number of resource limits a container requested. If possible, use the `kube_pod_resource_limits` metric exposed by the kube-scheduler instead, as it is more precise. | Gauge | 5 m | 

  * **resource** : The name of the resource.
  * **unit** : The resource unit.
  * **container** : The name of the container.
  * **pod** : The name of the pod.
  * **namespace** : The namespace of the pod.
  * **node** : The name of the node.
  * **uid** : The unique ID of the pod.

  
`container_memory_working_set_bytes`  
The current working set. | Gauge | 5 m |   
`controller_runtime_reconcile_total`  
The total number of reconciliations per controller. | Counter | 5 m | 

  * **controller** : The name of the controller.
  * **result** : The resulting quantity of reconciliations.

  
`controller_runtime_webhook_requests_total`  
The total number of requests that the webhook server has received. | Counter | 5 m | 

  * **webhook** : The name of the webhook.
  * **succeeded** : The resulting succeeded quantity of requests.

  
`controller_runtime_reconcile_time_seconds`  
The duration of a reconciliation in seconds per controller. | Histogram | 5 m |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
