---
url: https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts/
title: Report and repair faulty TPU hosts in All Capacity mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:26.366987+00:00
---

# Report and repair faulty TPU hosts in All Capacity mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Report and repair faulty TPU hosts in All Capacity mode

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to All Capacity mode TPUs.

If a TPU VM running in [All Capacity mode](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation) experiences an unresolvable hardware issue (such as high inter-chip interconnect (ICI) latency or high temperatures), you can report its host as faulty. Reporting a faulty host prompts Compute Engine to mark the host for automatic repair.

**Important:** The VM is not migrated to a new host; it stops during the repair and restarts on the same host after the repair is complete. The host repair process can take between 3 and 14 days, or longer.

## Limitations

When you report a faulty host, the following limitations apply:

  * **Repair duration:** Repairing the faulty host typically takes 3 to 14 days, during which the TPU VM remains stopped.
  * **Prerequisites:** You can only report a faulty host if the TPU VM that runs on the host meets all of the following conditions: 
    * The TPU VM is running.
    * The TPU VM is configured in All Capacity mode.
    * The TPU VM uses the [reservation-bound provisioning model](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation).
  * **Deletion constraint:** If you delete a TPU VM while the `reportHostAsFaulty` operation is in progress, then the operation fails.



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

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the TPU VM or the project
  * To view the state of a faulty host report operation by using Cloud Logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to report a faulty host. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to report a faulty host:

  * To create a faulty host report: `compute.instances.update` on the TPU VM 
  * To view a list of operations by using Logging: `logging.operations.list` on the project 
  * To view the details of an operation by using Logging: `logging.operations.get` on the project 
  * To view a list of operations in Compute Engine: `compute.zoneOperations.list` on the project 
  * To view the details of an operation in Compute Engine: `compute.zoneOperations.describe` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Understand the faulty host report process

After you report a faulty host for a TPU VM, the host repair process begins. The following details outline the scope, rate limits, and step-by-step process for All Capacity mode.

### Specifications

  * **Supported machine types:** TPU v6e and later.
  * **Rate limiting:** No rate limits apply to the report faulty host API.



### Process timeline

The following diagram illustrates the lifecycle of the host reporting and repair process:

When you report a faulty host, the following sequence occurs (corresponding to the numbered steps in the diagram):

  1. **Report the faulty host:** You initiate the report using the `gcloud` command or REST API. The TPU VM remains in the `RUNNING` state during this initial check, which typically takes 10–12 minutes. To track the status, see Review report faulty host operations.
  2. **Mark host as faulty:** Compute Engine confirms the request, creates the report operation, and marks the underlying physical host as faulty.
  3. **Stop the TPU VM:** Once the host is marked, the TPU VM is stopped, and its state changes to `REPAIRING`.
  4. **Begin repair:** The automatic host repair operation starts (usually within a minute after the VM stops).

**Warning:** Repairing the faulty host can take 3 to 14 days, or longer. The VM is not migrated to another host during this time and remains stopped.
  5. **Complete repair:** The hardware repair process finishes on the physical host.




## Report a faulty host

Report the faulty host. Select one of the following options.

###  gcloud 

Use the `report-host-as-faulty` command to report a faulty host using the `--fault-reasons` parameter to provide additional information about the problem.
    
    
    gcloud compute instances report-host-as-faulty TPU_NAME \
      --fault-reasons=behavior=FAULT_BEHAVIOR,description=DESCRIPTION \
      --disruption-schedule=DISRUPTION_SCHEDULE
    

###  REST 

To report a faulty host, make the following `POST` request to the [`instances.reportHostAsFaulty` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/reportHostAsFaulty).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/TPU_NAME/reportHostAsFaulty
    {
      "disruptionSchedule": "DISRUPTION_SCHEDULE",
      "faultReasons": [
        {
          "behavior": "FAULT_BEHAVIOR",
          "description": "DESCRIPTION"
        }
      ]
    }
    

Replace the following:

  * PROJECT_ID: The ID of the project where the TPU VM exists.
  * ZONE: The zone where the TPU VM exists.
  * TPU_NAME: The name of the TPU VM.
  * FAULT_BEHAVIOR: The type of fault observed. Use one of the following values: 
    * `PERFORMANCE`: The host is experiencing performance degradation, such as high inter-chip-interconnect (ICI) latency.
    * `SILENT_DATA_CORRUPTION`: The host is experiencing silent data corruption (SDC).
    * `BEHAVIOR_UNSPECIFIED`: Use this to report an issue that does not fit in the other behavior groups.
  * DESCRIPTION: A brief description of the issue, which is useful for debugging and tracking.
  * DISRUPTION_SCHEDULE: The timing of the host disruption for repair. Use one of the following values: 
    * `IMMEDIATE`: Stops the TPU VM and starts the host repair process immediately.
    * `FUTURE`: Schedules the host repair for a later time, allowing the VM to continue running temporarily if the workload can tolerate the fault.



## Review report faulty host operations

After you report a faulty host, Compute Engine starts a series of operations to mark the host as faulty and prepares the host for repair. Specifically, during a report faulty host operation, the following process happens:

  1. **Mark the host as faulty**. Compute Engine creates the report faulty host operation. The report faulty host operation then creates a sequence of sub-operations. These sub-operations mark the underlying host as faulty.

  2. **Prepare the host for repairs**. After all sub-operations complete, the report faulty host operation starts. Compute Engine stops the TPU VM and starts the repair faulty host operation.

  3. **Report completion and repair the host**. Compute Engine completes the report faulty host operation, and the host repair operation runs.




To track the status of report faulty host (`compute.instances.reportHostAsFaulty`) operations in your project, select one of the following options.

###  Console (Instance operations) 

  1. In the Google Cloud console, go to the **Operations** page.

[Go to Operations](https://console.cloud.google.com/compute/operations)

  2. In the table that appears, locate the row for the TPU VM you reported as faulty.

  3. The status of the report faulty host operation is displayed in the **Status** column of that row. When the operation completes, the value is **Done**.




###  Console (Logs Explorer) 

  1. Go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Verify that the **Show query** toggle is set to the on position.

  3. In the query editor, enter the following query:
         
         resource.type="gce_instance" AND protoPayload.methodName=~"compute\.instances\.reportHostAsFaulty"
         

  4. Click **Run query**. The **Query results** pane displays the query results.




###  gcloud 

  1. To view the status of the report faulty host operations in your project, use the [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) with the `--filter` flag set to `operationType:compute.instances.reportHostAsFaulty`:
         
         gcloud compute operations list --filter="operationType:compute.instances.reportHostAsFaulty"
         

  2. To view the details of a specific faulty host operation, use the [`gcloud compute operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe):
         
         gcloud compute operations describe OPERATION_NAME \
             --zone=ZONE
         




###  REST 

To view the status of the report faulty host operations in your project, make a `GET` request to the [`zoneOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list). In the request URL, include the `filter` query parameter set to `items.operationType:compute.instances.reportHostAsFaulty`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations?filter=items.operationType:compute.instances.reportHostAsFaulty
    

Replace the following:

  * PROJECT_ID: the ID of your project.
  * ZONE: the [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where the operations exist.



## What's next?

  * If you encounter issues when reporting a faulty host, then see [Troubleshoot faulty host API](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
