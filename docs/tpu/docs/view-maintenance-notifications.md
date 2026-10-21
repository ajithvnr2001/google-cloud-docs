---
url: https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications/
title: View maintenance notifications \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:54.299606+00:00
---

# View maintenance notifications  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View maintenance notifications

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

A host maintenance event is when Google Cloud has to perform a maintenance or repair activity on your TPU. Google sends notifications for upcoming host maintenance prior to the maintenance being performed. When the maintenance window opens, Google Cloud automatically performs maintenance on your instance. By monitoring your instance's upcoming maintenance windows, you can proactively prepare your workloads to handle upcoming maintenance with minimal disruption.

Cloud TPU lets you view maintenance notifications using the Google Cloud CLI and by querying the metadata server. You can also view upcoming maintenance events in Cloud Logging. For information about viewing maintenance notifications for TPUs in GKE, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## Maintenance notification fields

Maintenance notifications contain the following fields:

  * `windowStartTime`: The start of the time window in which maintenance will occur
  * `windowEndTime`: The end of the time window in which maintenance will occur
  * `latestWindowStartTime`: The latest time that the maintenance window can be moved to
  * `maintenanceType`: The type of maintenance that will be performed 
    * `SCHEDULED`: Maintenance will get seven days notice
    * `UNSCHEDULED`: Maintenance represents critical updates for which less notice is given than for scheduled maintenance events
  * `canReschedule`: Whether you can manually start maintenance during the notification period for this VM. 
    * `TRUE`: You can manually start maintenance during the notification period.
    * `FALSE`: You can't manually start maintenance on this VM. This is typically observed during the period in which the VM is actively undergoing maintenance.
  * `maintenanceStatus`: The current maintenance operation's status 
    * `ONGOING`: The maintenance operation is underway
    * `PENDING`: The maintenance operation has not yet started, but is scheduled



If there is no maintenance notification, the response looks similar to the following:
    
    
    { "error": "no notifications have been received yet, try again later" }
    

### Maintenance status behaviors

When managing maintenance events, check the values for `canReschedule` and `maintenanceStatus`. When combined, these fields indicate which actions you can or can't take with regards to manually starting a maintenance event:

  * **`canReschedule=True` and `maintenanceStatus=Pending`**: you can manually start the maintenance event for the instance before the scheduled start time.
  * **`canReschedule=False` and `maintenanceStatus=Ongoing`**: the maintenance is underway and can't be rescheduled.
  * **`canReschedule=False` and `maintenanceStatus=Pending`**: your instance doesn't support manually-triggered maintenance events.



## View maintenance notifications

You can view maintenance notifications by:

  * Calling the Cloud TPU API using the Google Cloud CLI
  * Querying the metadata server on your VM
  * Checking Cloud Logging



### Check TPUs for a maintenance notification

### gcloud

Use the [`gcloud alpha compute tpus tpu-vm describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/describe) command to view maintenance notifications:
    
    
    gcloud alpha compute tpus tpu-vm describe TPU_NAME \
        --zone=ZONE

If there is an upcoming maintenance event, the response will contain a section like the following:
    
    
    upcomingMaintenance:
        canReschedule: true
        latestWindowStartTime: "2025-12-01T19:00:00Z"
        maintenanceStatus: PENDING
        type: SCHEDULED
        windowEndTime: "2025-12-01T22:00:00Z"
        windowStartTime: "2025-12-01T19:00:00Z"

In this response:

  * The maintenance is scheduled for the date and time shown in `windowStartTime`.
  * `canReschedule` is set to `true` and `maintenanceStatus` is set to `PENDING`. These settings indicate that you can manually start the scheduled maintenance event before the date shown in `latestWindowStartTime`.



### Metadata server

From a TPU VM, query the metadata server to see the next maintenance event:
    
    
    curl http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance?alt=json -H "Metadata-Flavor: Google"

If there is an upcoming maintenance event, the response will contain a section similar to the following:
    
    
    Upcoming maintenance: {
        "can_reschedule" : "true",
        "latest_window_start_time" : "2024-06-12T16:00:01+00:00",
        "maintenance_status" : "PENDING",
        "type" : "SCHEDULED",
        "window_end_time" : "2024-06-12T20:00:00+00:00",
        "window_start_time" : "2024-06-12T16:00:00+00:00"
    }

You can query the metadata server from any TPU VM in the slice because the upcoming maintenance event notification is the same for all VMs in a slice.

For more information about VM metadata, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) in the Compute Engine documentation.

### Check Cloud Logging for a maintenance notification

When a notification is scheduled on your Cloud TPU, Cloud Logging will contain a system event log for the event, with the `methodName`: `compute.instance.upcomingMaintenance`. To view logs for upcoming maintenance events:

  1. In the Google Cloud console navigation menu, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Use the following search query to view any TPUs that have an upcoming maintenance event scheduled:

`"compute.instances.upcomingMaintenance"`

Cloud TPU logs upcoming maintenance events in Cloud Logging by the individual VM instance, for example, `t1v-n-5bdca789-w-0`.




#### Examples of maintenance notification logs

A maintenance event notification appears in Logs Explorer with values similar to the following:

  * `methodName`: `"compute.instances.upcomingMaintenance"`
  * `metadata`: 
    * `maintenanceStatus`: `"PENDING"`
    * `windowStartTime`: `"2024-07-23T20:00:00Z"`



The following is an example of a complete log entry for an upcoming maintenance event:
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "message": "Maintenance is scheduled for this instance. Review the maintenance schedule by describing the VM with gcloud CLI or querying the http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance metadata key."
        },
        "serviceName": "compute.googleapis.com",
        "methodName": "compute.instances.upcomingMaintenance",
        "resourceName": "projects/cloud-tpu-multipod-dev/zones/europe-west4-b/instances/t1v-n-9472280f-w-0",
        "request": {
          "@type": "type.googleapis.com/compute.instances.upcomingMaintenance"
        },
        "metadata": {
          "type": "SCHEDULED",
          "windowStartTime": "2024-11-15T04:00:00Z",
          "canReschedule": true,
          "latestWindowStartTime": "2024-11-15T04:00:01Z",
          "windowEndTime": "2024-11-15T08:00:00Z",
          "maintenanceStatus": "PENDING"
      },
      "logName": "projects/cloud-tpu-multipod-dev/logs/cloudaudit.googleapis.com%2Fsystem_event",
      "operation": {
        "id": "systemevent-1731038451389-6265ecbfcd453-5127b81e-f40b8149",
        "producer": "compute.instances.upcomingMaintenance",
        "first": true,
        "last": true
      },
      "receiveTimestamp": "2024-11-08T04:00:54.457835088Z"
    }
    

When the maintenance event starts, a new informational event appears in the logs with values similar to the following:

  * `methodName`: `"compute.instances.upcomingMaintenance"`
  * `metadata`: 
    * `maintenanceStatus`: `"ONGOING"`
    * `windowStartTime`: `"2024-07-23T20:00:00Z"`



When the maintenance event ends, a new informational event appears in the audit logs with values similar to the following:

  * `methodName`: `"compute.instances.upcomingMaintenance"`
  * `status: { message: "Maintenance window has completed for this instance. All maintenance notifications on the instance have been removed." }`



## What's next

  * [Prepare for maintenance events](https://docs.cloud.google.com/tpu/docs/maintenance-events)
  * [Manually start a host maintenance event](https://docs.cloud.google.com/tpu/docs/manually-start-maintenance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
