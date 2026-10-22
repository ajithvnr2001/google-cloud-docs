---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host/
title: Report faulty host \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:00.839625+00:00
---

# Report faulty host  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Report faulty host Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

If you notice an issue on an A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instance that you can't resolve on your own, then you can report its host as faulty. An example of such an issue could be slower performance within a cluster, or consistently high GPU temperatures.

When you report a host as faulty, Compute Engine automatically repairs the compute instance by running host maintenance.

  * For A4 and A3 Ultra instances, Compute Engine attempts to migrate the instance to a different host when maintenance starts, if you have unused reserved capacity or capacity is available in the instance's zone. Reporting a host as faulty helps you minimize downtime for your workload.
  * For A3 Mega and A3 High instances, Compute Engine stops the instance, performs the necessary host repairs, and then restarts the instance on the same host.



If you observe GPU memory or Xid errors on a compute instance and want to verify whether manual recovery measures such as resetting the GPUs or rebooting the instance can resolve the issue before reporting the host as faulty, see [Review Xid messages](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#review-xid-messages).

This document explains how to report and repair faulty host instances that are part of a Slurm cluster or other compute instance-based clusters. To report faulty hosts in a Google Kubernetes Engine (GKE) cluster, see [Report faulty hosts through GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters#report-faulty-hosts-how-to).

**Note:** [General GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) don't support reporting faulty hosts. If you encounter hardware issues with a General GPU instance, use standard GKE node auto-repair or contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs/overview) instead.**Caution** : Reporting a faulty host is a disruptive action that stops your VM. Before you report a host, thoroughly investigate your environment to identify the root cause of the issue. Only report the host as faulty if you have no alternatives to resolve your issue. 

## Limitations

When you report a faulty host, the following limitations apply:

  * You can only report a faulty host if the compute instance that runs on the host meets all of the following conditions:

    * The compute instance is running.

    * The compute instance uses an A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machine type.

    * The compute instance uses the [reservation-bound provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound).

**Note:** If a running A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instance uses a different provisioning model, but you still want to report its host as faulty, then contact your account team.
  * If you delete a compute instance while the `reportHostAsFaulty` operation is in progress, then the `reportHostAsFaulty` operation fails.

  * Google Cloud makes best-effort attempts to fulfill all your report faulty host requests. However, due to capacity constraints or rate limits, a request might not always be fulfilled.




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

To get the permissions that you need to report a faulty host, ask your administrator to grant you the following IAM roles: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the compute instance or the project
  * To view the state of a faulty host report operation by using Cloud Logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to report a faulty host. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to report a faulty host:

  * To create a faulty host report: `compute.instances.update` on the compute instance 
  * To view a list of operations by using Logging: `logging.operations.list` on the project 
  * To view the details of an operation by using Logging: `logging.operations.get` on the project 
  * To view a list of operations in Compute Engine: `compute.zoneOperations.list` on the project 
  * To view the details of an operation in Compute Engine: `compute.zoneOperations.describe` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Understand the faulty host report process

After you report a faulty host for a compute instance, the time when the compute instance restarts varies based on the [](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode) reservation operational mode that is specified in the reservation that the compute instance uses. To verify the reservation operational mode for a reservation, [view the `reservationOperationalMode` field in the reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation). The following table summarizes the faulty host process for the two available reservation operational modes: _all capacity mode_ and _managed mode_.  | All capacity mode (`ALL_CAPACITY`) | Managed mode (`HIGHLY_AVAILABLE_CAPACITY`)  
---|---|---  
Supported machine types | A4X Max and A4X | A4, A3 Ultra, A3 Mega, and A3 High  
Faulty host report API rate limiting | No rate limits apply. | Calls to the API may be rate-limited.  
Faulty host report process |  When you report a faulty host for a compute instance that runs in the all capacity mode, the following occurs:

  1. **Report the faulty host** : The instance remains in the `RUNNING` state throughout the report faulty host operation, which usually takes 10-12 minutes to complete. To review the operation state, see Review report faulty host operations in this document. 
  2. **Repair the host** : After the report faulty host operation completes, the host repair operation starts within a minute. When the repair host operation starts, the instance stops and its state changes depending on the [automatic restart (`automaticRestart`) setting](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) that is specified for the instance:
     * If automatic restart is enabled for the instance, the instance state changes to `REPAIRING`. The instance automatically restarts when its host is healthy unless you stop the instance before then.
     * If automatic restart is disabled for the instance, the instance state changes to `TERMINATED`. You need to manually restart the instance after its host is healthy.
Repairing the faulty host can take 3-14 days, or even longer at times.
  3. **Restart the instance** : After the host repair operation _completes_ (usually 3-14 days), one of the following occurs:
     * If the instance is in the `REPAIRING` state and the resources are available when the repair completes, then Compute Engine automatically restarts the instance on the repaired host.
     * Otherwise, if the instance is in the `TERMINATED` state or if resources aren't available when the repair completes, then the instance state stays in or changes to `TERMINATED`. You must [manually restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run. However, restarting the instance might fail if resources aren't available when you restart the instance; for example, this can happen if other instances are already using the repaired host.

|  When you report a faulty host for a compute instance that runs in the managed mode, the following occurs:

  1. **Report the faulty host** : The instance remains in the `RUNNING` state throughout the report faulty host operation, which usually takes 10-12 minutes to complete. To review the operation state, see Review report faulty host operations in this document. 
  2. **Start repairing the host** : After the report faulty host operation completes, the host repair operation starts within a minute. When the repair host operation starts, the instance stops and its state changes depending on the [automatic restart (`automaticRestart`) setting](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) that is specified for the instance:
     * If automatic restart is enabled for the instance, the instance state changes to `REPAIRING`. The instance automatically restarts when its host is healthy unless you stop the instance before then.
     * If automatic restart is disabled for the instance, the instance state changes to `TERMINATED`. You need to manually restart the instance after its host is healthy.
Repairing the faulty host can take 3-14 days, or even longer at times.
  3. **Migrate and restart the instance** : After the host repair operation _starts_ (usually 10-12 minutes), Compute Engine attempts to reserve one more host to replace your reported faulty host in your reserved capacity. If Compute Engine finds a healthy host—if it successfully replaces the faulty host or otherwise finds a matching healthy host in your reserved capacity—then Compute Engine migrates the instance to that host. Then, restarting the instance happens through one of the following: 
     * If the instance is in the `REPAIRING` state and resources are available before or when the repair completes, then Compute Engine automatically restarts the instance on a healthy host.
     * Otherwise, if the instance is in the `TERMINATED` state or if resources aren't available before or when the repair completes, then the instance state stays in or changes to `TERMINATED`. You must [manually restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run. However, restarting the instance might fail if resources aren't available when you restart the instance; for example, this can happen if other instances are already using the repaired host.

  
  
## Troubleshoot issues before you report a faulty host

Before you report a faulty host, we recommend that you troubleshoot the issue to confirm if it's a hardware problem, rather than an issue with your workload or cluster configuration. This approach helps to prevent unnecessary downtime for your workloads.

### Check for GPU performance issues and stragglers

If you notice slow performance, use the [straggler detection service](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance) to identify VMs that might be performing slower than others in the cluster.

### Monitor GPU temperatures and thermal violations

If you see thermal violation warnings in your logs or reported by DCGM, review the following guidance:

  * **Warnings vs. Critical Errors** : Current DCGM diagnostics might report thermal violations as warnings with a severity of `monitor`. This means that the GPUs are still ready to execute workloads but should be monitored.
  * **False Positives** : NVIDIA is investigating an increase in the frequency of thermal violation reports on GPUs that don't show signs of actual thermal issues.
  * **Recommendation** : Before reporting a host as faulty due to thermal warnings, check if the actual GPU temperatures exceed safe thresholds and if the performance of your workload is affected. If temperatures remain stable and performance is normal, we recommend monitoring the GPU instead of reporting it as faulty.



For more information about GPU troubleshooting, see [Troubleshoot GPU VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus) in the Compute Engine documentation.

## Report a faulty host

To report a faulty host, complete the following steps:

  1. **Review the host on which your compute instance runs**.

For instructions, see [View topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology#view-topology).

  2. Optional: **Back up Local SSD data**. When the instance stops, Compute Engine automatically discards the data of any Local SSD disks that are attached to the instance. You can't recover Local SSD data after Compute Engine discards it.

For instructions on how to preserve Local SSD data, see [Local SSD data backup](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_backup).

  3. **Report the faulty host**. To report a faulty host, select one of the following options. The host repair operation starts immediately, within a minute after the report faulty host operation completes. If the instance becomes unresponsive after you start the faulty host report operation, then, after you wait for at least 15 minutes, we recommend that you restart the compute instance.

**Important:** After you report a host as faulty, don't send additional requests until the operation completes. Compute Engine rejects additional requests while the operation is in progress.

###  gcloud 

To report a faulty host, use the following [`gcloud compute instances report-host-as-faulty` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty):
         
         gcloud compute instances report-host-as-faulty INSTANCE_NAME \
             --async \
             --disruption-schedule=IMMEDIATE \
             --fault-reasons=behavior=FAULT_REASON,description=DESCRIPTION \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance.

     * `FAULT_REASON`: a list of host issues that your compute instance encountered, separated by commas—for example, `ISSUE_1,ISSUE_2`. You can specify the following values:

       * **`PERFORMANCE`** : that GPUs that are attached to the compute instance have performance issues compared to other GPUs in the cluster, you see no XID errors in the logs, and the Compute Engine detects no other usual failure patterns, such as silent data corruption.

       * **`SILENT_DATA_CORRUPTION`** : you see data corruption in your compute instance, but the compute instance keeps running. Silent data corruption can be due to issues like vCPUs defects, software bugs, or kernel issues.

       * **`UNRECOVERABLE_GPU_ERROR`** : you identified an unrecoverable GPU error with an XID.

       * **`BEHAVIOR_UNSPECIFIED`** : you aren't sure about what the issue to your compute instance is.

     * `DESCRIPTION`: a description of the issue that is affecting your compute instance, such as XID information or suspected performance problems.

     * `ZONE`: the zone where the compute instance exists.

###  REST 

To report a faulty host, make the following `POST` request to the [`instances.reportHostAsFaulty` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/reportHostAsFaulty).

When you report a faulty host, you can specify multiple fault reasons at once. For example, to specify two fault reasons, make a request as follows:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/reportHostAsFaulty
    
    {
      "disruptionSchedule": "IMMEDIATE",
      "faultReasons": [
        {
          "behavior": "FAULT_REASON_1",
          "description": "DESCRIPTION_1"
        },
        {
          "behavior": "FAULT_REASON_2",
          "description": "DESCRIPTION_2"
        }
      ]
    }
    

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compute instance exists.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of the compute instance.

     * `FAULT_REASON_1` and `FAULT_REASON_2`: each host issue that your compute instance encountered. You can specify the following values:

       * **`PERFORMANCE`** : that GPUs that are attached to the compute instance have performance issues compared to other GPUs in the cluster, you see no XID errors in the logs, and the Compute Engine detects no other usual failure patterns, such as silent data corruption.

       * **`SILENT_DATA_CORRUPTION`** : you see data corruption in your compute instance, but the compute instance keeps running. Silent data corruption can be due to issues like vCPUs defects, software bugs, or kernel issues.

       * **`UNRECOVERABLE_GPU_ERROR`** : you identified an unrecoverable GPU error with an XID.

       * **`BEHAVIOR_UNSPECIFIED`** : you aren't sure about what the issue to your compute instance is.

     * `DESCRIPTION_1` and `DESCRIPTION_2`: a description for each host issue that you specified, such as XID information or suspected performance problems.




## Review report faulty host operations

After you report a faulty host, Compute Engine starts a series of operations to mark the host as faulty and prepares the host for repair. Specifically, during a report faulty host operation, the following process happens:

  1. **Mark the host as faulty**. Compute Engine creates the report faulty host operation. The report faulty host operation then creates a sequence of sub-operations. These sub-operations mark the underlying host as faulty.

  2. **Prepare the host for repairs**. After all sub-operations complete, the report faulty host operation starts. Compute Engine stops the compute instance and starts the repair faulty host operation. Based on the reservation operational mode that is specified in the reservation that the compute instance uses, and if healthy hosts are available, Compute Engine either keeps the compute instance stopped or attempts to automatically migrate and restart the compute instance.

  3. **Report completion and repair the host**. Compute Engine completes the report faulty host operation, and the host repair operation runs.




To track the status of the report faulty host (`compute.instances.reportHostAsFaulty`) operations in your project, select one of the following options. For more information about other operations that you can use to track repairs, migration, and automatic restart, see [Maintenance and restart behaviors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) and [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) in the Compute Engine documentation.

###  Console (Instance operations) 

  1. In the Google Cloud console, go to the **Operations** page.

[Go to Operations](https://console.cloud.google.com/compute/operations)

  2. In the table that appears, locate the compute instance that you reported.

  3. In the row that contains the compute instance, in the **Status** column, you can see the status of the report faulty host operation. When the operation completes, the value is **Done**.

  4. Optional: To verify if Compute Engine has restarted the compute instance, [view the details of the instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).




###  Console (Compute instance logs) 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Verify that the **Show query** toggle is set to the on position.

  3. In the query editor, enter the following query:
         
         resource.type="gce_instance" AND protoPayload.methodName=~"compute\.instances\.reportHostAsFaulty"
         

  4. Click **Run query**. The **Query results** pane displays the query results.




###  gcloud 

  1. To view the status of the report faulty host operations in your project, use the [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) with the `--filter` flag set to `operationType:reportHostAsFaulty`:
         
         gcloud compute operations list --filter="operationType:reportHostAsFaulty"
         

  2. If you want to view the details of a specific faulty host operation, then use the [`gcloud compute operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe):
         
         gcloud compute operations describe OPERATION_NAME \
             --zone="ZONE"
         

Replace the following:

     * `OPERATION_NAME`: the name of the operation.

     * `ZONE`: the zone where the operation exists.




###  REST 

To view the status of the report faulty host operations in your project, make a `GET` request to the [`zoneOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list). In the request URL, include the `filter` query parameter set to `items.operationType:reportHostAsFaulty`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations&filter=items.operationType:reportHostAsFaulty
    

Replace the following:

  * `PROJECT_ID`: the name of the operation.

  * `ZONE`: the zone where the operations exist.




## What's next?

  * If you encounter issues when reporting a faulty host, then see [Troubleshoot faulty host API](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
