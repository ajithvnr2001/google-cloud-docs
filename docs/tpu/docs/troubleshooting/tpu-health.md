---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health/
title: Monitor Cloud TPU health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:12.730901+00:00
---

# Monitor Cloud TPU health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor Cloud TPU health

Cloud TPU health monitoring provides real-time information on the health status of TPU VMs and slices. Using either the [Cloud Monitoring](https://cloud.google.com/monitoring) console or [ Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can identify hardware failures as they occur and reallocate resources, avoiding job failures and minimizing performance degradation.

TPU health monitoring assigns either a `HEALTHY` or `UNHEALTHY` status to each TPU instance in use. TPUs functioning as expected are assigned a `HEALTHY` status, and those that are no longer functional or performing at a severely reduced level are assigned an `UNHEALTHY` status.

Along with a health status, TPU health monitoring provides logging metrics for specific jobs. You can use these metrics to further diagnose TPU health and performance issues that are not caused by hardware issues.

## Unhealthy TPU detection

When TPU health monitoring assigns an `UNHEALTHY` status to a TPU, it provides identifying information of the failing TPU through the `compute.googleapis.com/instance/tpu/infra_health` service endpoint.

### TPU health status causes

**Key Term:** Workers are the processes running on a TPU that compile and execute TPU programs (TPU modules).

A machine is categorized as `UNHEALTHY` when there are issues with the physical hardware. When a machine is categorized as `UNHEALTHY`, TPU health monitoring provides one of the following causes:

  * `BAD_TPU_CHIP`: A physical failure within the TPU hardware itself. The VM may be running as intended, but a TPU connected to the VM is faulty.
  * `NETWORKING_ISSUE`: Hardware issues in the underlying network communication between the different workers or components of the distributed TPU system, such as dropped transfer Remote Procedure Calls (RPCs).
  * `BAD_SC_CHIP`: A physical failure within a [SparseCore](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#sparsecore) of a TPU chip.



### Metric labels

TPU health monitoring provides the following metric labels to identify the specific unhealthy TPU:

**Label name** | **Type** | **Description**  
---|---|---  
`health_status` | `STRING` | The overall health state of the TPU instance.  
`unhealthy_category` | `STRING` | The health status cause. This label is populated only when the value of the metric is `UNHEALTHY`.  
`machine_type` | `STRING` | The Compute Engine machine type of the instance.  
`reservation_id` | `STRING` | The ID of the physical machine reservation.  
  
TPU health monitoring also provides the following resource labels:

**Label name** | **Type** | **Description**  
---|---|---  
`project` | `STRING` | The project number.  
`service` | `STRING` | The API service (`compute.googleapis.com`).  
`resource_type` | `STRING` | The VM instance.  
`location` | `STRING` | The zone of the instance.  
`resource_id` | `STRING` | The Compute Engine instance ID.  
  
TPU health monitoring provides the following additional metric labels for All Capacity mode reservations through [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview):

**Label name** | **Type** | **Description**  
---|---|---  
`machine_id` | `STRING` | The ID of the physical machine hosting the VM.  
`block_id` | `STRING` | The ID of the block within the cluster hosting the VM.  
`cluster_id` | `STRING` | The ID of the cluster hosting the VM.  
`subblock_id` | `STRING` | The ID of the sub-block hosting the VM.  
  
## Logging

**Key Term:** TPU modules contain the code running on a TPU.

A machine without any physical issues may be impaired or non-functional due to issues unrelated to hardware. In these cases, TPU health monitoring continues to categorize the machine as `HEALTHY`, but also logs potential causes of the issue with Cloud Logging in the associated project. The logs provide details about the issue, including a brief description, the suspected root cause, potential culprits, and actionable next steps.

The logs contain one of the following causes:

  * `FINGERPRINT_MISMATCH`: Programs expected to be running the same TPU module contain different binary fingerprints. This is likely due to inconsistencies caused by compiler issues.
  * `DATA_INPUT_STALL`: TPUs are stuck during Direct Memory Access (DMA) operations or data transfers. TPUs cannot continue until DMA operations complete.
  * `UNRECOVERABLE_ERROR`: One or more workers encountered an unrecoverable error and are in an undefined state.
  * `DIFFERENT_MODULE`: Workers are executing different TPU modules when they are expected to be running the same module.
  * `UNKNOWN_CAUSE`: Undetermined cause of error.



You can view logs using the Logs Explorer or Logs API. For more information about Google Cloud logging, see [ Google Cloud Logging](https://cloud.google.com/logging).

## Monitoring with the console

The Monitoring Dashboard in the Google Cloud console provides real-time visualizations of machine health status, historical trends, and total counts. The **_Failure Event_** table links job failures to their root causes.

To view a prebuilt a dashboard in Cloud Monitoring:

  1. In the Google Cloud console, go to the Cloud Monitoring page.   
[Go to the Monitoring console](https://console.cloud.google.com/monitoring)
  2. In the navigation pane, click **Dashboards**.
  3. In the **Filter search** field, enter "TPU Instance Health Dashboard".



The dashboard displays the following metrics by default:

  * **Overall TPU instance health** : The percentage of TPU instances that are categorized as `HEALTHY`.
  * **Number of instances** : The total number of TPU instances in use.
  * **Number of healthy TPU instances** : The total number of TPU instances categorized as `HEALTHY`.
  * **Number of unhealthy TPU instances** : The total number of TPU instances categorized as `UNHEALTHY`.
  * **VM infra health distribution** : The number of `HEALTHY` instances over time.



To add a custom query, click **Add Query** and write a PromQL query. For example, the following query retrieves all unhealthy TPU instances:
    
    
    count({__name__="compute.googleapis.com/instance/tpu/infra_health", monitored_resource="gce_instance", health_status="UNHEALTHY"})
    

For more information on monitoring with the Google Cloud console, see the [ Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

## Monitoring with the CLI

The Google Cloud CLI provides real-time TPU health data. The following example request retrieves all `UNHEALTHY` TPU:
    
    
    export TOKEN=$(gcloud auth application-default print-access-token)
    
    export PROMQL_QUERY='count({__name__="compute.googleapis.com/instance/tpu/infra_health", monitored_resource="gce_instance", health_status="UNHEALTHY"})'
    
    export LOCATION="global"
    
    curl -G \
      --header "Authorization: Bearer ${TOKEN}" \
      --header "Content-Type: application/json" \
      --header "X-Goog-User-Project: ${PROJECT_ID}" \
      --data-urlencode "query=${PROMQL_QUERY}" \
      "https://monitoring.googleapis.com/v1/projects/${PROJECT_ID}/location/${LOCATION}/prometheus/api/v1/query"
    

You should expect to see a response similar to the following:
    
    
    {"status":"success","data":{"resultType":"vector","result":[65]}}
    

For more information on gcloud CLI, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
