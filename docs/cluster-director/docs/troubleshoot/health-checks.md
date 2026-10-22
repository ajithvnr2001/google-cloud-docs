---
url: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks/
title: Troubleshoot GPU health check failures \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:02.841728+00:00
---

# Troubleshoot GPU health check failures  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Troubleshoot GPU health check failures Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to troubleshoot a compute node after it fails a health check for its attached GPUs.

To prevent your jobs from failing or producing incorrect results, [Slurm runs two automated checks in your cluster](https://docs.cloud.google.com/cluster-director/docs/orchestration#capabilities). If one of these checks fails, then you can do the following:

  * **Prolog health check** : if the prolog health check fails and Slurm drains your node, then you can troubleshoot the issue to return the node to service.

**Important:** If the prolog health check failed due to a false positive, or if your workload can tolerate the hardware issue that the health check detected, then you can [bypass the prolog health check for a specific job](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#bypass-checks).
  * **Background health check** : if the background health check detects an issue, then you can troubleshoot the issue and determine whether to keep running your jobs on the node or reschedule the jobs on a different node.




## Troubleshoot a GPU health check failure

To troubleshoot a compute node's health check failure and return the node to service if Slurm drained it, complete the following steps:

  1. Identify the cause of the failure

  2. Resolve the error

  3. Run a manual health check

  4. Undrain the node




### Identify the cause of the failure

To identify whether the prolog health check or the background health check detected an issue with your GPUs, review the compute node's log files by using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** pane, enter one of the following queries. If you can't see the **Query** pane, then click the **Show query** toggle to the on position.

     * To view the logs for the prolog health check, enter the following query:
           
           SEARCH("/var/log/slurm/chs_health_check.log")
           labels."compute.googleapis.com/resource_name"="NODE_NAME"
           

     * To view the logs for the background health check, enter the following query:
           
           log_name="projects/PROJECT_ID/logs/syslog"
           SEARCH("dcgm-health-check")
           labels."compute.googleapis.com/resource_name"="NODE_NAME"
           

Replace the following:

     * `PROJECT_ID`: the ID of the project where your cluster exists.

     * `NODE_NAME`: the name of the compute node.

  3. To run the query, click **Run query**. The **Query results** pane displays error messages from [`nvidia-smi`](https://docs.nvidia.com/deploy/nvidia-smi/index.html) and [DCGM diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html).

  4. Optional: To find more details about the issue, check the NVIDIA driver resource manager (NVRM) for specific Xid errors as follows:

     1. In the **Query** pane, clear the query editor. Then, to filter for NVRM Xid errors for your node, enter the following query:
            
            resource.type="gce_instance"
            SEARCH("NVRM: Xid")
            labels."compute.googleapis.com/resource_name"="NODE_NAME"
            

     2. To run the query, click **Run query**. The **Query results** pane displays low-level GPU driver events and Xid error codes. To determine the steps to fix the issue, compare the Xid error codes with the troubleshooting guidance in the [NVIDIA Xid errors catalog](https://docs.nvidia.com/deploy/xid-errors/analyzing-xid-catalog.html).




### Resolve the error

After you identify the cause of the health check failure in the previous section, choose one of the following resolution methods based on the error:

  * Resolve a hardware error

  * Resolve a temporary issue




If you can't resolve the error, then contact your account team or [support](https://cloud.google.com/support).

#### Resolve a hardware error

If the log files show a [Xid error](https://docs.nvidia.com/deploy/xid-errors/introduction.html) that requires recreating the node, then recreate the node by completing the following steps:

**Caution:** Recreating a node permanently deletes the node and its attached disks. Before you proceed, back up any data that you want to preserve. For backup options, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. Recreate the node:
         
         sudo scontrol update nodename=NODE_NAME state=POWER_DOWN_ASAP reason="Recreate a faulty compute node."
         




#### Resolve a temporary issue

If the health check failure indicates a temporary issue, such as a transient power spike or cosmic ray-induced bit flip, then do the following:

  1. If you haven't already, then [connect to the compute node](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#compute).

  2. Stop all tasks that use the node's GPUs:
         
         sudo systemctl stop nvidia-persistenced.service nvidia-dcgm.service google-cloud-ops-agent-opentelemetry-collector.service
         

  3. Reset the GPUs:
         
         sudo nvidia-smi -r
         

  4. Restart the tasks:
         
         sudo systemctl start nvidia-persistenced.service nvidia-dcgm.service google-cloud-ops-agent-opentelemetry-collector.service
         




### Run a manual health check

After you attempt to fix a health check failure, as described in the previous section, run a manual health check to verify the compute node's status. If the prolog health check or background health check scripts run without errors, then you've resolved the issue. Manually running these checks before a critical job starts running helps to minimize the chance of errors.

To manually run a health check on a compute node, complete the following steps:

  1. If you haven't already, then [connect to the compute node](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#compute).

  2. To run a manual health check, run one of the following scripts:

     * Run the prolog health check script:
           
           sudo /slurm/custom_scripts/prolog.d/990_chs_gpu_health_check_hcs.sh
           

     * Run the background health check script:
           
           sudo /slurm/custom_scripts/health_check_program.d/health_check_program.sh
           




### Undrain the node

If you resolved the issue that the prolog health check detected, and you want to return the compute node to service and let it accept new jobs, then undrain the node:

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. Undrain the node:
         
         sudo scontrol update nodename=NODE_NAME state=RESUME
         




Before starting new jobs on the node, Slurm runs the prolog health check. The background health check keeps running every two minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
