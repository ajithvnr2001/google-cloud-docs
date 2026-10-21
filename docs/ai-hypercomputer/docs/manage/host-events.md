---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events/
title: Manage host events across compute instances \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:43.855519+00:00
---

# Manage host events across compute instances  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Manage host events across compute instances Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus) [ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document explains how to monitor, plan for, and perform scheduled maintenance on [Clustered GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus) (A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs)) and [General GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) instances. When you proactively manage upcoming [maintenance host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) on your Compute Engine instances, you can minimize disruptions and maintain optimal performance.

For more options for maintaining your infrastructure, see the following:

  * To manage maintenance on your blocks of reservation-bound capacity, whether compute instances are running on them or not, see [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations).

  * To manage maintenance on a cluster in Cluster Director, see [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health).




## Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Required roles

To get the permissions that you need to manage host maintenance events across compute instances, ask your administrator to grant you the following IAM roles: 

  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project
  * For read-only access to System Event audit logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage host maintenance events across compute instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage host maintenance events across compute instances:

  * To view the details of an instance: `compute.instances.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

To optimize the maintenance of your compute instances, complete the following steps:

  1. **Understand and handle host maintenance**. Learn about the frequency and maintenance behavior of your instances based on their machine series, and learn how to prepare your workload to handle host maintenance. This information helps you minimize disruptions and prevent data loss.

  2. **Set up notification alerts**. Create log-based alerts to receive notifications when maintenance for your instances is scheduled, started, or completed. This approach helps you proactively plan your activities and avoid unexpected downtime.

  3. **Manage maintenance across instances**. View if maintenance is scheduled for your instances. If needed, you can manually start maintenance across your instances. This process helps you increase the resilience of your workloads to host events, prevent downtime, and maximize the availability of your applications.




## Understand and handle host maintenance

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the following:

  * Planned maintenance of Compute Engine infrastructure.
  * Unplanned, emergency maintenance to repair Compute Engine infrastructure after a host error or a faulty host report.



The following table describes the host maintenance features for accelerator-optimized machine types:

Machine type | Typical scheduled maintenance event frequency | Maintenance behavior | Advanced notification for scheduled maintenance | Advanced notifications for emergency maintenance | On-demand maintenance | Simulate maintenance  
---|---|---|---|---|---|---  
A4X Max and A4X | Minimum of 90 days | Terminates with [ Local SSD data persistence](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence) | 90 days | If you [ enable emergency notifications](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications), then 7 days. Otherwise, a few hours.  | Yes | No  
A4 | Minimum of 90 days | Terminates with [ Local SSD data persistence](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence) | 90 days | If you [ enable emergency notifications](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications), then 7 days. Otherwise, a few hours.  | Yes | No  
A3 Ultra | Minimum of 90 days | Terminates with [ Local SSD data persistence](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence) | 90 days | If you [ enable emergency notifications](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications), then 7 days. Otherwise, a few hours.  | Yes | No  
A3 Mega and A3 High (8 GPUs) | Minimum of 90 days | Terminates with [ Local SSD data persistence](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence) | 90 days | If you [ enable emergency notifications](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications), then 7 days. Otherwise, a few hours.  | Yes | Yes  
A3 Edge | Minimum of 30 days | Terminate and restart | 7 days | If you [ enable emergency notifications](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications), then 7 days. Otherwise, a few hours.  | Yes | Yes  
  
The following notes apply to the preceding table:

  * **Typical scheduled maintenance event frequency** : 

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.




To help prevent losing data or progress, configure your workloads to handle host maintenance. For example, use the following techniques to save your temporary data and progress before your workload is stopped:

  * [Migrate your temporary data off of Local SSD disks](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance#migrate-temp-data-ssds)

  * [Use training check points](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#use-training-checkpoints-to-save-the-current-state-of-your-experiment)




## Set up notification alerts for compute instances

You can get notified about scheduled, started, or completed maintenance events for your instances by [creating log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

To create an alert for the maintenance events of your instances, complete the following procedure. Repeat this procedure for each alert that you want to create.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Click the **Show query** toggle to the on position.

  3. In the **Query** pane, build one of the following queries. These queries filter log entries to identify specific maintenance events. If you want to use multiple queries, repeat this procedure to create a unique alert for each query.

     * To receive alerts when maintenance for an instance is scheduled:
           
           protoPayload.methodName="compute.instances.upcomingMaintenance" severity>=DEFAULT
           protoPayload.status.message =~ "scheduled"
           

     * To receive alerts when the maintenance window for an instance has opened:
           
           protoPayload.methodName="compute.instances.upcomingMaintenance" severity>=DEFAULT
           protoPayload.status.message =~ "ongoing"
           

     * To receive alerts when maintenance for an instance has started:
           
           protoPayload.methodName="compute.instance.terminateOnHostMaintenance" severity>=DEFAULT
           

     * To receive alerts when maintenance for an instance has completed:
           
           protoPayload.methodName="compute.instances.upcomingMaintenance" severity>=DEFAULT
           protoPayload.status.message =~ "completed"
           

  4. To validate the query, click **Run query**. If the query is valid, then the **Query results** pane displays log entries that match the query.

  5. In the **Query** results toolbar, click the **Actions** list, and then select add_alert **Create log alert**. The **Create logs-based alert policy** pane appears.

  6. In the **Alert details** section, do the following:

     1. In the **Alert Policy Name** field, enter a name for the policy.

     2. In the **Policy severity level** list, select **Warning** (or a higher severity).

     3. Click **Next**.

  7. In the **Choose logs to include in the alert** section, click **Next**.

  8. In the **Set notification frequency and autoclose duration** section, specify the following:

     1. In the **Time between notifications** list, select how often you want to be notified.

     2. In the **Incident autoclose duration** list, select after how long Cloud Logging stops sending notifications and automatically closes the incident.

     3. Click **Next**.

  9. In the **Who should be notified?** section, specify a [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options) for Logging to send notifications to.

  10. Click **Save**.




To view examples of maintenance event notifications in the Logs Explorer, see [Examples of maintenance notifications](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#examples_of_maintenance_notifications) in the Compute Engine documentation.

## Manage maintenance across compute instances

You can view and control maintenance for your instances by doing one or more of the following:

  * To check the state and scheduled time of upcoming maintenance for your instances, view the maintenance state of instances.

  * To immediately start maintenance on your instances, rather than waiting for their scheduled maintenance time, manually start maintenance on instances.


**Note:** A3 Edge does not report a `physicalHost` ID. To identify instance groupings for A3 Edge, you must use [compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

### View the maintenance state of compute instances

You can view the state and scheduled time of upcoming maintenance for your instances by checking the value of the `upcomingMaintenance` field in the instance's metadata. If an instance doesn't contain the `upcomingMaintenance` field, then no host maintenance event is scheduled for the instance. For more information about the fields in `upcomingMaintenance`, see [Maintenance status definitions](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#maintenance-status-definitions) in the Compute Engine documentation.

Additionally, if maintenance is scheduled for an instance, the `upcomingGroupMaintenance` field contains the `maintenanceReasons` field. This field describes why maintenance was scheduled for your instance, as described in the following table:

Maintenance type | Maintenance reason | Compute instance state  
---|---|---  
Planned maintenance after faulty host report | `FAILURE_GPU_CUSTOMER_REPORTED` | Applies only to instances that are running on the host that you reported as faulty.  
Planned maintenance for regular maintenance | 

  * **`PLANNED_UPDATE`** : planned infrastructure maintenance
  * **`PLANNED_NETWORK_UPDATE`** : planned network maintenance

| Applies to running, stopped, or suspended instances.  
Unplanned, emergency maintenance | 

  * **`FAILURE_DISK`** : unplanned maintenance scheduled due to an error with a disk attached to an instance. 
  * **`FAILURE_GPU`** : unplanned maintenance scheduled due to a GPU-related error.
  * **`FAILURE_GPU_TEMPERATURE`** : unplanned maintenance scheduled due to a GPU-related error after the GPU reached a high temperature.
  * **`FAILURE_GPU_XID`** : unplanned maintenance after you received an [ Xid message](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#xid_messages) due to a GPU-related error.
  * **`FAILURE_INFRA`** : unplanned maintenance scheduled due to an error with the infrastructure.
  * **`FAILURE_INTERFACE`** : unplanned maintenance scheduled due to an error with the NIC.
  * **`FAILURE_MEMORY`** : unplanned maintenance scheduled due to an error with an instance's memory. 
  * **`FAILURE_NETWORK`** : unplanned maintenance scheduled due to an error with the network.
  * **`FAILURE_NVLINK`** : unplanned maintenance scheduled due to an error with the NVLink.

| Applies only to running instances.  
  
To view the `maintenanceReasons` field in an instance, you must use the gcloud CLI or REST API. To view the maintenance state for multiple compute instances simultaneously, you must use the Google Cloud console or REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Maintenance status** column, Compute Engine displays the maintenance state of your instances. If you don't see this column in the **VM instances** table, then click view_column **Column display options** , select the **Maintenance status** checkbox, and then click **OK**.




###  gcloud 

To view the maintenance state of an instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with the `--flatten=resourceStatus.upcomingMaintenance` flag:
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --flatten=resourceStatus.upcomingMaintenance \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the instance name.

  * `ZONE`: the zone where the instance exists.




The output is similar to one of the following:

  * If a host maintenance event is scheduled for your instance, then the output is similar to the following:
        
        ---
        canReschedule: true
        latestWindowStartTime: '2025-11-01T19:00:00Z'
        maintenanceReasons:
        - 'PLANNED_UPDATE'
        - 'PLANNED_NETWORK_UPDATE'
        maintenanceStatus: 'PENDING'
        type: 'SCHEDULED'
        windowEndTime: '2025-11-01T22:00:00Z'
        windowStartTime: '2025-11-01T19:00:00Z'
        

  * If a host maintenance event isn't scheduled for your instance, then the output is similar to the following:
        
        ---
        null
        




###  REST 

To view the maintenance state of your instances, make one of the following `GET` requests. When you make a request, you must include the `fields` query parameter to only show the name, machine type, and upcoming maintenance for an instance. You must also include the `filter` query parameter to only filter instances by a specific machine type.

  * To view instances across all zones: [`instances.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/instances?fields=items.name,items.machineType,items.upcomingMaintenance&filter=machineType%3AMACHINE_TYPE
        

  * To view instances in a specific zone: [`instances.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances?fields=items.name,items.machineType,items.upcomingMaintenance&filter=machineType%3AMACHINE_TYPE
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where you created instances.

  * `ZONE`: the zone where the instances exist.

  * `MACHINE_TYPE`: the machine type that you want to filter the instances by.




If a host maintenance event is scheduled for an instance, then the instance contains the `upcomingMaintenance` field:
    
    
    {
      "items": [
        {
          "name": "vm-01",
          "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
          "resourceStatus": {
            "upcomingMaintenance": {
              "canReschedule": true,
              "latestWindowStartTime": "2024-11-01T19:00:00Z",
              "maintenanceStatus": "PENDING",
              "maintenanceReasons": [
                "PLANNED_UPDATE",
                "PLANNED_NETWORK_UPDATE"
              ],
              "type": "SCHEDULED",
              "windowEndTime": "2024-11-01T22:00:00Z",
              "windowStartTime": "2024-11-01T19:00:00Z"
            }
          }
        },
        ...
      ]
    }
    

Optionally, to further narrow down a list of instances, set the `filter` query parameter to a different [filter expression](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#body.QUERY_PARAMETERS.filter).

###  Metadata server 

To view the maintenance state of an instance, do the following:

  1. If you haven't already, then connect to your [Linux](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) or [Windows instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. To view the upcoming maintenance schedule, query the `upcoming-maintenance` endpoint:
         
         curl http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance?alt=json -H "Metadata-Flavor: Google"
         

If a host maintenance event is scheduled for your instance, then the output is similar to the following:
         
         "Upcoming maintenance": {
           "can_reschedule": "true",
           "latest_window_start_time": "2024-12-01T19:00:01Z",
           "maintenance_reasons": [
             "PLANNED_UPDATE",
             "PLANNED_NETWORK_UPDATE"
           ],
           "maintenance_status": "PENDING",
           "type": "SCHEDULED",
           "window_end_time": "2024-12-01T21:00:01Z",
           "window_start_time": "2024-12-01T19:00:01Z"
         }
         

If a host maintenance event isn't scheduled, then the output is similar to the following:
         
         { }
         

  3. To view the current maintenance state of a VM, query the `maintenance-event` endpoint:
         
         curl http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event -H "Metadata-Flavor: Google"
         

For more information about the output of these queries, see [Review the outputs](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice#review_the_outputs).




### Manually start maintenance on compute instances

You can manually start maintenance for your instances instead of waiting for the scheduled time.

Depending on the maintenance state of an instance, the following occurs:

Maintenance state | Description | What you see  
---|---|---  
Scheduled | Compute Engine has scheduled maintenance for the instance. You can manually start maintenance before the scheduled time. | 

  * In the Google Cloud console, the maintenance state shows as **Ready to run - will run on DATE**.
  * In the gcloud CLI or REST API, Compute Engine sets the `maintenanceStatus` field to `PENDING`.

  
In progress | Maintenance is underway. You can't reschedule it. | 

  * In the Google Cloud console, the maintenance state shows as **Running**.
  * In the gcloud CLI or REST API, Compute Engine sets the `maintenanceStatus` field to `ONGOING`.

  
Complete | Maintenance is finished. Compute Engine has removed all maintenance notifications from the instance. | 

  * In the Google Cloud console, the maintenance state shows as **Up-to-date**.
  * In the gcloud CLI or REST API, Compute Engine sets the `maintenanceStatus` field to `COMPLETE`.

  
  
You can manually start maintenance for multiple instances simultaneously or for individual instances. For multiple instances, use the Google Cloud console or, for instances located in the same zone, the gcloud CLI. For individual instances, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the rows for the instances where you want to start maintenance.

  3. Click add **Run maintenance**.

  4. To confirm, click **Run maintenance**.




###  gcloud 

To manually start maintenance for one or more instances within the same zone, use the [`gcloud compute instances perform-maintenance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/perform-maintenance):
    
    
    gcloud compute instances perform-maintenance INSTANCE_NAMES \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of instance names separated by spaces; for example, `vm-01 vm-02 vm-03`.

  * `ZONE`: the zone where the instances exist.




###  REST 

To manually start maintenance for an instance, make a `POST` request to the [`instances.performMaintenance` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/performMaintenance):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/performMaintenance
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created the instance.

  * `ZONE`: the zone where the instance exists.

  * `INSTANCE_NAME`: the instance name.




## What's next

  * To test your workload after a host event, see [Benchmarking recipes](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview).

  * To learn more about monitoring VMs, see [Monitor VMs and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
