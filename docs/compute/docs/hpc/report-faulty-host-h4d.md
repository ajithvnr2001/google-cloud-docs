---
url: https://docs.cloud.google.com/compute/docs/hpc/report-faulty-host-h4d/
title: Report faulty host \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:19.233538+00:00
---

# Report faulty host  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/report-faulty-host-h4d/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Report faulty host Stay organized with collections  Save and categorize content based on your preferences. 

If you notice issues on a reserved H4D VM that you can't resolve otherwise— such as persistent errors with the RDMA device— then we recommend that you report its host as faulty. When you report a host as faulty, Compute Engine reports the host as faulty and then automatically repairs the VM by running host maintenance. For H4D VMs, Compute Engine attempts to migrate the VM to a different host when maintenance starts, which can help minimize the downtime for your workload.

This document explains how to report and repair faulty hosts for virtual machine (VM) instances that are part of VM-based clusters. For Google Kubernetes Engine (GKE) clusters, see [Report faulty hosts through GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters#report-faulty-hosts-how-to).

## Limitations

When you report a faulty host, the following limitations apply:

  * You can only report a faulty host if the VM that runs on the host meets all of the following conditions:

    * The VM is running.

    * The VM uses an H4D machine type.

    * The VM uses the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#reservation-bound).

**Note:** If a running H4D VM uses a different provisioning model, but you still want to report its host as faulty, then contact your account team.
  * Google Cloud makes best-effort attempts to fulfill all your report faulty host requests. However, due to capacity constraints or rate limits, a request might not always be fulfilled.




## Before you begin

**Caution:** Reporting a faulty host is a disruptive action that stops your VM. Before you report a host, thoroughly investigate your environment to identify the root cause of the issue. Then, only report the host as faulty if you have no alternatives to resolve your issue.

  * Select the tab for how you plan to use the samples on this page:

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

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the VM or the project
  * To view the state of a faulty host report operation by using Cloud Logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to report a faulty host. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to report a faulty host:

  * To create a faulty host report: `compute.instances.update` on the VM 
  * To view a list of operations by using Logging: `logging.operations.list` on the project 
  * To view the details of an operation by using Logging: `logging.operations.get` on the project 
  * To view a list of operations in Compute Engine: `compute.zoneOperations.list` on the project 
  * To view the details of an operation in Compute Engine: `compute.zoneOperations.describe` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Understand the faulty host report process

After you report a faulty host for a H4D VM, the time when the H4D VM restarts varies based on the [reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode) of the reservation you used to create the VM. To verify the reservation operational mode for a reservation, [view the **reservationOperationalMode** field](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#view-reservation) in the reservation.

| Managed mode (`HIGHLY_AVAILABLE_CAPACITY`)  
---|---  
Supported machine types | H4D  
Faulty host report API rate limiting | Calls to the API may be rate-limited.  
Faulty host report process |  When you report a faulty host for a H4D VM that runs in managed mode, the following occurs:

  1. **Report the faulty host** : The VM remains in the `RUNNING` state throughout the reporting operation, which usually takes 10-12 minutes to complete. To review the operation state, see Review report faulty host operations in this document. 
  2. **Start repairing the host** : After the report faulty host operation completes, the host repair operation starts within a minute. When the repair host operation starts, the VM stops and its state changes depending on the [automatic restart (`automaticRestart`) setting](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) that is specified for the VM:
     * If automatic restart is enabled for the VM, the VM state changes to `REPAIRING`. The VM automatically restarts when its host is healthy unless you stop the VM before then.
     * If automatic restart is disabled for the VM, the VM state changes to `TERMINATED`. You need to manually restart the VM after its host is healthy.
Repairing the faulty host can take 3-14 days, or even longer at times.
  3. **Migrate and restart the VM** : After the host repair operation _starts_ (usually 10-12 minutes), Compute Engine attempts to reserve one more host to replace your reported faulty host in your reserved capacity. If Compute Engine finds a healthy host—if it successfully replaces the faulty host or otherwise finds a matching healthy host in your reserved capacity—then Compute Engine migrates the VM to that host. Then, restarting the VM happens through one of the following: 
     * If the VM is in the `REPAIRING` state and resources are available before or when the repair completes, then Compute Engine automatically restarts the VM on a healthy host.
     * Otherwise, if the VM is in the `TERMINATED` state or if resources aren't available before or when the repair completes, then the VM state stays in or changes to `TERMINATED`. You must [manually restart the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run. However, restarting the VM might fail if resources aren't available when you restart the VM; for example, this can happen if other VMs are already using the repaired host.

  
  
## Report a faulty host

To report a faulty host, complete the following steps:

  1. **Review the host on which your VM runs**.

For instructions, see [View H4D cluster topology](https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology).

  2. Optional: **Back up Local SSD data**. When the VM stops, Compute Engine automatically discards the data of any Local SSD disks that are attached to the VM. You can't recover Local SSD data after Compute Engine discards it.

For instructions on how to preserve Local SSD data, see [Local SSD data backup](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_backup).

  3. **Report the faulty host**. To report a faulty host, select one of the following options. The host repair operation starts immediately, within a minute after the report faulty host operation completes. If the VM becomes unresponsive after you start the faulty host report operation, then, after you wait for at least 15 minutes, we recommend that you restart the VM.

###  gcloud 

To report a faulty host, use the following [`gcloud compute instances report-host-as-faulty` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty):
         
         gcloud compute instances report-host-as-faulty VM_NAME \
             --async \
             --disruption-schedule=IMMEDIATE \
             --fault-reasons=behavior=FAULT_REASON,description=DESCRIPTION \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM.

     * `FAULT_REASON`: a list of host issues that your VM encountered, separated by commas—for example, `ISSUE_1,ISSUE_2`. You can specify the following values:

       * **`PERFORMANCE`** : you see performance degradation of the CPU or Cloud RDMA network operation, IRDMA network interface failures, or that the IRDMA network device isn't present.

       * **`SILENT_DATA_CORRUPTION`** : you see data corruption in your VM, but the VM keeps running. Silent data corruption can be due to issues like vCPU defects, software bugs, or kernel issues.

       * **`BEHAVIOR_UNSPECIFIED`** : you aren't sure about what issue is affecting your VM or the issue isn't covered by the other options.

     * `DESCRIPTION`: a description of the issue that is affecting your VM, such as XID information or suspected performance problems.

     * `ZONE`: the zone where the VM exists.

###  REST 

To report a faulty host, make the following `POST` request to the [`instances.reportHostAsFaulty` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/reportHostAsFaulty).

When you report a faulty host, you can specify multiple fault reasons at once. For example, to specify two fault reasons, make a request as follows:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/reportHostAsFaulty
    
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

     * `PROJECT_ID`: the ID of the project where the VM exists.

     * `ZONE`: the zone where the VM exists.

     * `VM_NAME`: the name of the VM.

     * `FAULT_REASON_1` and `FAULT_REASON_2`: each host issue that your VM encountered. You can specify the following values:

       * **`PERFORMANCE`** : you see performance degradation of the CPU or RDMA network operation, RDMA device failures, or that the RDMA device is not present.

       * **`SILENT_DATA_CORRUPTION`** : you see data corruption in your VM, but the VM keeps running. Silent data corruption can be due to issues like vCPUs defects, software bugs, or kernel issues.

       * **`BEHAVIOR_UNSPECIFIED`** : you aren't sure about what the issue to your VM is.

     * `DESCRIPTION_1` and `DESCRIPTION_2`: a description for each host issue that you specified, such as XID information or suspected performance problems.




## Review report faulty host operations

After you report a faulty host, Compute Engine starts a series of operations to mark the host as faulty and prepares the host for repair. Specifically, during a report faulty host operation, the following process happens:

  1. **Mark the host as faulty**. Compute Engine creates the report faulty host operation. The report faulty host operation then creates a sequence of sub-operations. These sub-operations mark the underlying host as faulty.

  2. **Prepare the host for repairs**. After all sub-operations complete, the report faulty host operation starts. Compute Engine stops the VM and starts the repair faulty host operation. Based on the reservation operational mode that is specified in the reservation that the VM uses, and if healthy hosts are available, Compute Engine either keeps the VM stopped or attempts to automatically migrate and restart the VM.

  3. **Report completion and repair the host**. Compute Engine completes the report faulty host operation, and the host repair operation runs.




To track the status of the report faulty host (`compute.instances.reportHostAsFaulty`) operations in your project, select one of the following options. For more information about other operations that you can use to track repairs, migration, and automatic restart, see [Maintenance and restart behaviors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) and [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) in the Compute Engine documentation.

###  Console (VM operations) 

  1. In the Google Cloud console, go to the **Operations** page.

[Go to Operations](https://console.cloud.google.com/compute/operations)

  2. In the table that appears, locate the VM that you reported.

  3. In the row that contains the VM, in the **Status** column, you can see the status of the report faulty host operation. When the operation completes, the value is **Done**.

  4. Optional: To verify if Compute Engine has restarted the VM, [view the details of the VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).




###  Console (VM logs) 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Verify that the **Show query** toggle is set to the on position.

  3. In the query editor, enter the following query:
         
         resource.type="gce_instance" AND protoPayload.methodName=~"compute\.instances\.reportHostAsFaulty"
         

  4. Click **Run query**. The **Query results** pane displays the query results.




###  gcloud 

  1. To view the status of the report faulty host operations in your project, use the [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) with the `--filter` flag set to `operationType:compute.instances.reportHostAsFaulty`:
         
         gcloud compute operations list --filter="operationType:compute.instances.reportHostAsFaulty"
         

  2. If you want to view the details of a specific faulty host operation, then use the [`gcloud compute operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe):
         
         gcloud compute operations describe OPERATION_NAME \
             --zone="ZONE"
         

Replace the following:

     * `OPERATION_NAME`: the name of the operation.

     * `ZONE`: the zone where the operation exists.




###  REST 

To view the status of the report faulty host operations in your project, make a `GET` request to the [`zoneOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list). In the request URL, include the `filter` query parameter set to `items.operationType:compute.instances.reportHostAsFaulty`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations&filter=items.operationType:compute.instances.reportHostAsFaulty
    

Replace the following:

  * `PROJECT_ID`: the name of the operation.

  * `ZONE`: the zone where the operations exist.




## What's next?

  * If you encounter issues when reporting a faulty host, then see [Troubleshoot faulty host API](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
