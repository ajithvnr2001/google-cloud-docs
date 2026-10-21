---
url: https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event/
title: Monitor and plan for a host maintenance event \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:53:56.925777+00:00
---

# Monitor and plan for a host maintenance event  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor and plan for a host maintenance event Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Each virtual machine (VM) instance or bare metal instance uses a [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) to determine the behavior of the instance during a maintenance operation. Some instances offer the additional option of viewing the maintenance schedule ahead of time.

This page explains how to monitor and plan for a [host maintenance event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) on Compute Engine instances. 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create instances and manage instance maintenance, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * For read-only access to System Event audit logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create instances and manage instance maintenance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create instances and manage instance maintenance:

  * To get information about an instance, including metadata: `compute.instances.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

You can view notifications for an instance's upcoming maintenance event only if the instance uses a machine type from one of the following machine families:

  * **Accelerator-optimized machine families** :

    * GPUs: 

      * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)

      * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)

      * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)

      * [A3](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms)

      * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms)

      * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)

      * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)

      * [N1 machine types with NVIDIA T4 GPUs](https://docs.cloud.google.com/compute/docs/gpus#t4-gpus)

      * [N1 machine types with NVIDIA P4 GPUs](https://docs.cloud.google.com/compute/docs/gpus#p4-gpus)

      * [N1 machine types with NVIDIA V100 GPUs](https://docs.cloud.google.com/compute/docs/gpus#v100-gpus)

    * TPUs:

      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x)

      * [TPU v6e](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e)

      * [TPU v5p](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v5p)

  * **General-purpose machine families** :

    * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)

    * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)

    * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)

    * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series)

    * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)

  * **Network-optimized machine families** :

    * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)

    * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)

  * **Memory-optimized machine families** :

    * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_machine_types)

    * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_machine_types)

    * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types) and [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)

    * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types)

    * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types)

    * [M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types)

  * **Storage-optimized machine families** :

    * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
    * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)
    * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
  * **Compute-optimized machine families** :

    * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines)

    * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines)




## Overview of maintenance notifications

Google sends notifications for upcoming host maintenance through several methods. When the maintenance window opens, Google Cloud automatically performs maintenance on your instance. By monitoring your instance's upcoming maintenance windows, you can proactively prepare your workloads to handle upcoming maintenance with minimal disruption.

**Note:** Notification periods such as the 7-day advance notice for performance-sensitive machine families apply to scheduled maintenance. Unscheduled or emergency maintenance events, such as those required to address critical security vulnerabilities or imminent hardware failures, can occur with shorter or no advance notice.

Compute instances that support maintenance event notifications have the following characteristics:

  * **Fewer maintenance events** : In general, instances with recurrent maintenance intervals should see fewer maintenance events.
  * **Longer maintenance notification** : Get notified of maintenance events well in advance for planning purposes.
  * **Monitoring and planning** : Use Cloud Logging to track your maintenance schedule. Use incidents and alerts to stay informed.
  * **On-demand maintenance control** : Start maintenance during the notification period to update your instances when it fits your schedule.

**Note:** On-demand maintenance is only available for specific compute machine types. See [Manually start a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) for details.

The information about an upcoming notification event is presented in a manner similar to the following:
    
    
    upcomingMaintenance:{
        "canReschedule":True
        "latestWindowStartTime": "2024-12-01T19:00:01Z"
        "machineType":"x4-960-16t-metal"
        "maintenanceStatus":"PENDING"
        "type":"SCHEDULED"
        "windowEndTime": "2024-12-01T22:00:00Z"
        "windowStartTime": "2024-12-01T19:00:00Z"
    }
    

If there is no upcoming maintenance event, instead you see a message similar to the following:
    
    
    { "error": "no notifications have been received yet, try again later" }
    

## Maintenance status definitions

The following status definitions explain the responses to queries about host maintenance for an instance. They provide information related to the maintenance event. The Google Cloud CLI, REST, and the [metadata server](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata) use these same responses:

  * **canReschedule** : whether the maintenance can be started manually during the notification period for this instance. 
    * `TRUE`: customer-triggered maintenance can be performed during the notification period.
    * `FALSE`: customer-triggered maintenance can't be performed on this instance. This often occurs during the period in which the instance is undergoing maintenance or if the instance type doesn't support on-demand maintenance.
  * **latestWindowStartTime** : the latest time the maintenance window can be moved to.
  * **machineType** : the machine type of the instance, for example `x4-960-16t-metal` or `c4-highmem-192`.
  * **maintenanceReason** : the reason for an emergent maintenance event. Examples include: 
    * `FAILURE_GPU_TEMPERATURE`: maintenance due to high GPU temperature.
    * `FAILURE_MEMORY`: maintenance due to memory errors.
    * `FAILURE_NETWORK`: maintenance due to network errors.
    * `FAILURE_DISK`: maintenance due to disk errors.
  * **maintenanceStatus** : the current status of the maintenance event. 
    * `ONGOING`: the maintenance operation is underway.
    * `PENDING`: the maintenance operation is scheduled, but has not yet started.
  * **type** : the type of maintenance to be performed. 
    * `NONE`: No maintenance is scheduled for this instance.
    * `SCHEDULED`: For disruptive maintenance, Compute Engine provides a minimum of 7 days notice for most instances; X4 instances get approximately 60 days advanced notice.
    * `UNSCHEDULED`: Because the maintenance represents critical or urgent updates, Compute Engine tries to provide as much advanced notice as possible, but it is usually much less than for scheduled maintenance events.
  * **windowEndTime** : the end of the time window in which maintenance occurs.
  * **windowStartTime** : the start of the time window in which maintenance occurs.



### Maintenance status behaviors

When managing maintenance events, check the values for `canReschedule` and `maintenanceStatus`. When combined, these fields indicate what actions you can or can't take with regards to rescheduling a maintenance event: 

  * `canReschedule=True` and `maintenanceStatus=Pending`— you can manually start the maintenance event for the instance before the scheduled start time.
  * `canReschedule=False` and `maintenanceStatus=Ongoing`—the maintenance is underway and can't be rescheduled.
  * `canReschedule=False` and `maintenanceStatus=Pending`—your instance doesn't support manually-triggered maintenance events.



## View maintenance notifications

You can find maintenance notifications by querying your compute instances, the metadata server, or by using Cloud Logging.

You can also view emergent maintenance events using the same methods. However, notifications for emergent maintenance events include a `type` field with a value of `UNSCHEDULED`, and you can only view this field with Cloud Logging.

### Check instances for a maintenance event notification

Use the Google Cloud CLI, REST, or query the metadata server to see if there is an upcoming host maintenance event for your instance.

###  gcloud 

To see the upcoming maintenance window for an instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe).
    
    
    gcloud compute instances describe INSTANCE_NAME \
       --zone=ZONE_NAME --format="yaml(resourceStatus.upcomingMaintenance)"
    

Replace the following:

  * `INSTANCE_NAME`: The name of the compute instance.
  * `ZONE_NAME`: The zone where the instance resides.



If there is an upcoming maintenance event, then the response contains a section similar to the following:
    
    
      resourceStatus:
        upcomingMaintenance:
          canReschedule: true
          latestWindowStartTime: '2025-01-15T12:00:01Z'
          machineType: x4-960-16t-metal
          maintenanceStatus: PENDING
          type: SCHEDULED
          windowEndTime: '2025-01-15T16:00:00Z'
          windowStartTime: '2025-01-15T12:00:00Z'
    

In this response:

  * The maintenance is scheduled for the date and time shown in `windowStartTime`.
  * `canReschedule` is set to `true` and `maintenanceStatus` is set to `PENDING`. These settings indicate you can manually start the scheduled maintenance event before the date shown in `latestWindowStartTime`.



If the command returns `null`, this indicates that a maintenance event isn't scheduled and you should check again at a later date or time.

###  REST 

To see if there is upcoming maintenance for an instance, construct a `GET` request using the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_NAME`: The name of the project that contains the compute instance.
  * `ZONE`: The zone where the instance is located.
  * `INSTANCE_NAME`: The name of the instance.



If there is an upcoming maintenance event, then the response contains a section similar to the following:
    
    
      upcomingMaintenance:{
        "canReschedule":True
        "latestWindowStartTime": "2023-12-01T19:00:01Z"
        "machineType": "x4-960-16t-metal"
        "maintenanceStatus":"PENDING"
        "type":"SCHEDULED"
        "windowEndTime": "2023-12-01T22:00:00Z"
        "windowStartTime": "2023-12-01T19:00:00Z"
      }
    

In this response:

  * The maintenance is scheduled for the date and time shown in `windowStartTime`.
  * `canReschedule` is set to `True` and `maintenanceStatus` is set to `PENDING`. These settings indicate you can manually start the scheduled maintenance event before the date shown in `latestWindowStartTime`.



If the query returns `NONE` with an HTTP code of `200`, this indicates that a maintenance event isn't scheduled and you should check again at a later date or time.

###  Metadata server 

From the Guest OS, query the metadata server to see the next maintenance event.
    
    
    $ curl http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance?alt=json -H "Metadata-Flavor: Google"
    

If the query returns `NONE` with an HTTP code of `200`, this indicates that a maintenance event isn't scheduled and you should check again at a later date or time.

### Check Cloud Logging for a maintenance event notification

Compute Engine creates system events in the [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) for an instance for maintenance events. You can view these events before, during, and after a maintenance event using [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) and [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

###  Console 

To query the audit logs for maintenance notifications for an instance, complete the following steps:

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the instance for which you want to view maintenance notifications.

The **Instance details** page opens.

  3. In the **Logs** section, click the link labeled **Logging**.

The **Logs Explorer query editor** page opens. In the **Query** pane, the `resource.type` and instance ID are already populated for your instance.

  4. In the **Query** pane, add the following line to the query:
         
         operation.producer="compute.instances.upcomingMaintenance" OR
         "compute.instances.terminateOnHostMaintenance" OR
         "compute.instances.migrateOnHostMaintenance"
         

  5. Click **Run query**. The matching maintenance notification events appear in the query results pane.

In the query results pane you can click **Edit time** to expand the search timeframe, or to narrow the results to specific dates or times.

  6. Click a log entry to view the maintenance notification details.

     1. For upcoming maintenance notifications, expand the heading `metadata` to view information such as the current status, type, and scheduled maintenance window start and end times.
     2. Expand the heading `status` to view the descriptive message for the notification.



#### Examples of maintenance notifications

A maintenance event notification for an instance appears in the Logs Explorer with values similar to the following:

  * `methodName`: `"compute.instances.upcomingMaintenance"`
  * `metadata`: 
    * `maintenanceStatus`: `"PENDING"`
    * `machineType`: `"x4-960-16t-metal"`
    * `windowStartTime`: `"2024-07-23T20:00:00Z"`



When the maintenance event starts, a new informational event appears in the logs with values similar to the following:

  * `methodName`: `"compute.instances.upcomingMaintenance"`
  * `metadata`: 
    * `maintenanceStatus`: `"ONGOING"`
    * `machineType`: `"x4-960-16t-metal"`
    * `windowStartTime`: `"2024-07-23T20:00:00Z"`



During the maintenance event, depending on the host maintenance policy configuration for the instance, one of the following system events is logged to the audit logs:

  * For instances configured to use live migration during maintenance events, a system event with `methodName: "compute.instances.migrateOnHostMaintenance"`.
  * For instances configured to terminate during maintenance events, a system event with `methodName: "compute.instances.terminateOnHostMaintenance"`.



When the maintenance event ends, a new informational event appears in the audit logs with values similar to the following:

  * `methodName`: `"compute.instances.upcomingMaintenance"`
  * `status: {` `message: "Maintenance window has completed for this instance. All` `maintenance notifications on the instance have been removed."` `}`



## Configure alerts for host maintenance notifications

You can set up a log-based [alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) to search for specific maintenance notification events and send alerts using a [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options).

###  Console 

To create an alert for a maintenance event for your instance, complete the following steps:

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the instance for which you want to create a maintenance event alert.

The **Instance details** page opens.

  3. In the **Logs** section, click the link labeled **Logging**.

The **Logs Explorer query editor** page opens. In the **Query** pane, the `resource.type` and instance ID are already populated for your instance.

  4. In the **Query** pane, add the following line to the query:
         
         operation.producer="compute.instances.upcomingMaintenance"
         

To filter host maintenance events for a machine type instead of a specific instance, edit the query as follows:

     1. Remove the line that specifies the instance ID.
     2. Add the following line to the query:
            
            protoPayload.metadata.machineType:"MACHINE_TYPE"

Replace `MACHINE_TYPE` with the machine type for which you want to filter the host maintenance events.

  5. Click **Run query**. The matching maintenance notification events appear in the query results pane.

  6. In the query results pane, click **Edit time**.

     1. On the left-hand side of the edit window, in the **Relative time** field, enter `1d` to view the log entries for the past week.
     2. Click **Apply**.
  7. In the header of the **Query results** pane, click _add_alert_ **Create alert**. If your viewing window is narrow, the **Create alert** option might appear on the **Actions** menu instead.

  8. In the **Create logs-based alert policy** pane, in the **Alert details** section, do the following:

     1. Enter a name for the alert policy, for example `Upcoming maintenance for my-c3d-vm@us-central1-b`.
     2. From the **Policy severity level** menu, select **No severity**.

     3. In the **Documentation** field, you can enter a description for your alerting policy. You can also include information that might help the recipient of a notification diagnose the problem. The following string summarizes the reason for the notification:
            
            Log-based alerting policy in project ${project} to monitor upcoming
            maintenance notifications. See also "Host maintenance alerts" and
            "onHostMaintenance actions" alerting policies.
            

For information about how you can format and tailor the content of this field, see [Using Markdown and variables in documentation templates](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

     4. To advance to the next step, click **Next**.

  9. In the **Choose logs to include in the alert** section, check the query and results by clicking **Preview logs**.

The query you built in the **Query** pane is also displayed on this pane. We recommend building the query in the Logs Explorer **Query** pane first.

You can edit the query in this pane, if necessary. If you edit the query, then check the results by clicking **Preview logs**.

  10. Click **Next**.

  11. In the **Set notification frequency and autoclose duration** pane, do the following:

     1. Select the minimum time between notifications. This value lets you control the number of notifications you get from Monitoring if this condition is met multiple times. For this example, select **1 day** from the options.

     2. For the **Incident autoclose duration** , use the maximum value of 7 days.

     3. Click **Next**.

  12. If you already have an email notification channel configured, then you can select it from the list. If not, click **Manage notification channels** and add an email channel. For information about creating notification channels, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  13. Click **Save**.

Your log-based alerting policy is now ready to test as described in [Test the example log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-test.)




To learn more, read [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) and [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

## What's next

  * Learn how to [Set a host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).
  * Learn how to [Get live migration notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice).
  * Learn how to manually [Trigger a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)
  * Learn how to manage [log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-edit) using the Google Cloud console for Monitoring or by using the Monitoring API.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
