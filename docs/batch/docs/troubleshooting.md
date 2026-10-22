---
url: https://docs.cloud.google.com/batch/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:42.996454+00:00
---

# Troubleshooting  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Batch.

If you're trying to troubleshoot a job that you don't have an error message for, then, before reviewing this document, we recommend that you check for error messages as follows:

  1. Check if the job's history contains any error messages by [viewing status events](https://docs.cloud.google.com/batch/docs/view-status-events).
  2. If the job's status events don't contain any error messages, then check the job's logs for errors by [viewing the job's logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs) and specifying the following query:
         
         labels.job_uid="JOB_UID" AND severity>="ERROR"
         

Replace `JOB_UID` with the unique ID (UID) of the job. To get a job's UID, [describe the job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs).




For more information about troubleshooting a job, also see the following documents:

  * [Known issues](https://docs.cloud.google.com/batch/docs/known-issues)
  * [Analyze a job using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs)
  * [View audit logs](https://docs.cloud.google.com/batch/docs/audit-logging)



## Job creation errors

If you can't create a job, it might be due to one of the errors in this section.

### Insufficient quota

#### Issue

One of the following issues occurs when you try to create a job:

  * When the job is in the [`QUEUED` state](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#State), the following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus):
        
        Quota checking process decides to delay scheduling for the job JOB_UID due to inadequate quotas [Quota: QUOTA_NAME, limit: QUOTA_LIMIT, usage: QUOTA_CURRENT_USAGE, wanted: WANTED_QUOTA.].
        

This issue indicates that the job has been delayed because the current usage (`QUOTA_USAGE`) and limit (`QUOTA_LIMIT`) of `QUOTA_NAME` quota prevented the job's requested usage (`WANT_QUOTA`).

  * When the job is in [`QUEUED`, `SCHEDULED`, or `FAILED` states](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#State), one of the following issues appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus):
        
        RESOURCE_NAME creation failed:
        Quota QUOTA_NAME exceeded. Limit: QUOTA_LIMIT in region REGION
        
        
        RESOURCE_NAME creation failed:
        Quota QUOTA_NAME exceeded. Limit: QUOTA_LIMIT in zone ZONE
        

This issue indicates that creating a resource failed because the request exceeded your `QUOTA_NAME` quota, which has a limit of `QUOTA_LIMIT` in the specified location.




#### Solution

To resolve the issue, do the following:

  * If the job was delayed, try to wait for more quota to be released.

  * If the job failed due to insufficient quota or if these delays persist, try to prevent insufficient quota by doing any of the following:

    * Create jobs that use less of that quota or a different quota. For example, specify a different location or resource type for the job, or split your quota usage across additional projects.

    * Request a higher quota limit for your project from Google Cloud.




For more information, see [Batch quotas and limits](https://docs.cloud.google.com/batch/quotas) and [Work with quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

### Insufficient permissions to act as the service account

#### Issue

The following issue occurs when you try to create a job:

  * If the job does not use an instance template, the issue appears as the following:
        
        caller does not have access to act as the specified service account: SERVICE_ACCOUNT_NAME
        

  * If the job uses an instance template, the issue appears as the following:
        
        Error: code - CODE_SERVICE_ACCOUNT_MISMATCH, description - The service account specified in the instance template INSTANCE_TEMPLATE_SERVICE_ACCOUNT doesn't match the service account specified in the job JOB_SERVICE_ACCOUNT for JOB_UID, project PROJECT_NUMBER
        




This issue usually occurs because the user creating the job does not have sufficient permissions to act as the service account used by the job, which is controlled by the [`iam.serviceAccounts.actAs` permission](https://docs.cloud.google.com/iam/docs/service-accounts-actas).

#### Solution

To resolve the issue, do the following:

  1. If the job uses an instance template, verify that the service account specified in the instance template matches the service account specified in the job's definition.
  2. Make sure that the user who is creating the job has been granted Service Account User role (`roles/iam.serviceAccountUser`) on the service account specified for the job. For more information, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  3. Recreate the job.



### Invalid allowed location

#### Issue

The following issue occurs when you try to create a job:
    
    
    allowed locations must be in the same region as the resource. Resource region: JOB_LOCATION, allowed locations: LIST_OF_ALLOWED_LOCATIONS"
    

This issue occurs because you specified one or more values for the `allowedLocations[]` field that are outside of the region that you specified for the job's location.

#### Solution

To resolve the issue, recreate the job and update the value of the `allowedLocations[]` field to only contain a region or zones that are located within the region that you specified for the job's location.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations) and the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations).

### Repeated networks

#### Issue

The following issue occurs when you try to create a job:
    
    
    Networks must be distinct for NICs in the same InstanceTemplate
    

This issue occurs because you specified the network for a job more than once.

#### Solution

To resolve the issue, recreate the job and specify the network by using _one_ of the following options:

  * **VM instance template:** If you want to [use a VM instance template while creating this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), you must specify the network in the VM instance template.
  * **[`network` and `subnetwork` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface):** These fields can be used in the request body when you create a job using the Batch API or in the JSON configuration file when you create a job using the gcloud CLI.
  * **[`--network` and `--subnetwork` flags](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):** These flags can be used with the `gcloud batch jobs submit` command when you create a job using the gcloud CLI.



For more information, see [Specify the network for a job](https://docs.cloud.google.com/batch/docs/specify-job-network).

### Invalid network for VPC Service Controls

#### Issue

The following issue occurs when you try to create a job:
    
    
    no_external_ip_address field is invalid. VPC Service Controls is enabled for the project, so external ip address must be disabled for the job. Please set no_external_ip_address field to be true
    

#### Solution

This issue occurs because you are attempting to create and run a job with VMs that have external IP addresses in a VPC Service Controls service perimeter.

To resolve the issue, [create a job that blocks external access for all VMs](https://docs.cloud.google.com/batch/docs/job-without-external-access).

For more information about how to configure networking for a job in a VPC Service Controls service perimeter, see [Use VPC Service Controls with Batch](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls).

## Job issues and failure errors

If you have issues with a job that is not running correctly or failed for unclear reasons, it might be due to one of the errors in this section or one of the exit codes in the following Task failure exit codes section.

### No logs in Cloud Logging

#### Issue

You need to debug a job, but no logs appear for the job in Cloud Logging.

This issue often occurs for the following reasons:

  * **The Cloud Logging API is not enabled for your project.** Even if you correctly configure everything else for a job's logs, it won't produce logs if the service is not enabled for your project.
  * **The job's service account does not have permission to write logs.** A job can't produce logs without sufficient permissions.
  * **The job was not configured to produce logs.** To produce logs in Cloud Logging, a job needs to have Cloud Logging enabled. The job's runnables should also be configured to write any information that you want to appear in logs to the standard output (stdout) and standard error (stderr) streams. For more information, see [Analyze a job by using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs).
  * **Tasks did not run.** Logs cannot be produced until tasks have been assigned resources and start running.
  * **Cloud Logging was configured to automatically exclude the job's logs.** Logs from Batch jobs can't appear if you have configured [exclusion filters for Cloud Logging](https://docs.cloud.google.com/logging/docs/exclusions#viewing-exclusion-filters) that cause logs from Batch jobs to be excluded.



#### Solution

To resolve this issue, do the following:

  1. Make sure that the logs weren't automatically excluded from Cloud Logging by disabling any current [exclusion filters for Cloud Logging](https://docs.cloud.google.com/logging/docs/exclusions#viewing-exclusion-filters).
  2. [Make sure that the Cloud Logging API is enabled for your project](https://docs.cloud.google.com/logging/docs/api/enable-api#enable-api).
  3. Make sure the service account for the job has the **Logs Writer** (`roles/logging.logWriter`) IAM role. For more information, see [Enable Batch for a project](https://docs.cloud.google.com/batch/docs/get-started#project-prerequisites).
  4. [View the details of the job using the gcloud CLI or Batch API](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs). The job details can help you understand why the job did not produce logs and might provide information that you hoped to get from logs. For example, do the following: 
     1. To verify that logging is enabled, review the job's [`logsPolicy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#logspolicy).
     2. To verify that the job finished running successfully, review the job's [`status` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus).



After you've made any changes, recreate the job and wait for the job to finish running before checking for logs.

### No service agent reporting

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job that is not running properly or failed before VMs were created:
    
    
    No VM has agent reporting correctly within time window NUMBER_OF_SECONDS seconds, VM state for instance VM_NAME is TIMESTAMP,agent,start
    

The issue indicates that none of a job's VMs are reporting to the [Batch service agent](https://docs.cloud.google.com/batch/docs/get-started#batch-service-agent).

This issue often occurs for the following reasons:

  * **The job's VMs do not have sufficient permissions.** A job's VMs require specific permissions to report their state to the Batch service agent. You can provide these permissions for a job's VMs by granting the Batch Agent Reporter role (`roles/batch.agentReporter`) to the job's service account.
  * **The job's VMs have network issues.** A job's VMs require network access to communicate with the Batch service agent.
  * **The job's VMs are using an outdated Batch VM OS image or using a VM OS image with outdated Batch service agent software.** The job's VMs require software in its VM OS image that provides the current dependencies for reporting to the Batch service agent.



#### Solution

To resolve the issue, do the following:

  1. Verify that the job's VMs have the permissions required to report their state to the Batch service agent.

     1. To identify the job's service account, [view the details of the job using the gcloud CLI or Batch API](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs). If no service account is listed, the job uses the Compute Engine default service account by default.
     2. Confirm that the job's service account has permissions for the Batch Agent Reporter role (`roles/batch.agentReporter`). For more information, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) and [Restricting service account usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts).

For example, to grant the Compute Engine default service account the required permissions, use the following command:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
              --role roles/batch.agentReporter \
              --member serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com
            

        * Replace PROJECT_NUMBER with your [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
        * Replace PROJECT_ID with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  2. Verify that the job's VMs have proper network access. For more information, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview) and [Troubleshoot common networking issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking).

  3. If you specified the VM OS image for the job, verify that the VM OS image is currently supported.

     1. If you enabled Cloud Logging for the job, you can identify this issue by checking for any of the following agent logs (`batch_agent_logs`). For more information, see [Analyze a job using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs).

        * Log for outdated Batch service agent software error:
              
              rpc error: code = FailedPrecondition, desc = Invalid resource state for BATCH_AGENT_VERSION: outdated Batch agent version used.
              

The BATCH_AGENT_VERSION is the version of software for communicating with the Batch service agent that the job uses—for example, `cloud-batch-agent_20221103.00_p00`.

        * Log for outdated Batch VM OS image error:
              
              rpc error: code = FailedPrecondition, desc = Invalid resource state for BATCH_VM_OS_IMAGE_NAME: outdated Batch image version.
              

The BATCH_VM_OS_IMAGE_NAME is the specific version of a VM OS image from Batch that the job uses—for example, `batch-cos-stable-official-20260730-00-p01`.

     2. You can resolve this issue by using a newer VM OS image. If the job uses a custom image, recreate the custom image based on one of the latest version of a supported public image.

For more information, see [Supported VM OS images](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview#supported_vm_os_images) and [View VM OS images](https://docs.cloud.google.com/batch/docs/view-os-images).

  4. Recreate the job.




### Missing resource metrics in Cloud Monitoring

#### Issue

You want to [view resource metrics for a job](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics), but some or all of the expected metrics are missing.

This issue often occurs for the following reasons:

  * **The API wasn't enabled for your project.** Even if you correctly configure everything else in your project, resource metrics might not appear until the Cloud Monitoring API is enabled. For the Ops Agent, you must also enable the Cloud Logging API.
  * **You don't have sufficient permissions to view the metrics.** You can't view metrics without sufficient permissions.
  * **The job's VMs didn't run.** Metrics can't be produced for a job until at least one of the job's VMs is running.
  * **The job's configuration or permissions didn't support Ops Agent metrics.** Some resource metrics can be provided only by the Ops Agent. To support Ops Agent metrics, a job must meet the requirements for the Ops Agent, install the Ops Agent, and use a service account that can write metrics to Monitoring.
  * **You need to use a different method or filter to view the metrics.** Some methods for viewing metrics don't display metrics for VMs after the VMs are deleted. Additionally, metrics won't appear if they are omitted by filters or the displayed time period. Furthermore, metric graphs have adjustable resolutions that can cause small amounts of data to be too thin to display.
  * **The metrics were deleted.** You cannot view metrics after they are deleted, which happens automatically after the Monitoring retention periods.



#### Solution

If only Ops Agent metrics are missing, first try to resolve the issue by do the following:

  1. Verify the job's configuration by doing the following: 
     1. To see the job's complete configuration information, [view the details of the job using the gcloud CLI or Batch API](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs). Use the output for the remaining steps.
     2. Ensure that the job's service account has the [permissions to write Ops Agent metrics](https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent#job-service-account-iam).
     3. Ensure that the job meets all the [Ops Agent requirements](https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent#ops-agent-requirements).
     4. Ensure that the job correctly installs the Ops Agent. Although it's possible to install the Ops Agent manually in a runnable, the recommended method is to automatically install the Ops Agent by setting the [`installOpsAgent` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate.FIELDS.install_ops_agent) to `true`.
  2. If the issue still persists, see [Troubleshoot the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshooting) in the Google Cloud Observability documentation.



Otherwise, resolve the issue by doing the following:

  1. Ensure that the Monitoring API is enabled for your project: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)

  2. Ensure that job's VMs started running and that the run time is still within the [Monitoring retention periods](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy). You can see the job's run time by [viewing the details of the job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs).
  3. Verify that there aren't any issues with the methods you are using to view metrics by doing the following: 
     1. Unless you want to see metrics for only running resources, ensure that you are viewing metrics by using the Metrics Explorer or a custom dashboard made from Metrics Explorer charts. Other methods, such as Compute Engine dashboards, don't display metrics for resources that have been deleted.
     2. Ensure that the [display period](https://docs.cloud.google.com/monitoring/charts/working-with-charts#display-period) includes the job's run time. For graphs, also ensure that the [graph resolution](https://docs.cloud.google.com/monitoring/charts/working-with-charts#zooming) is appropriate for your data.
     3. Ensure that you don't have any [filters](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option) that are hiding the data.
  4. If the issue still persists, see the [Troubleshoot Cloud Monitoring](https://docs.cloud.google.com/monitoring/support/troubleshooting) pages in the Google Cloud Observability documentation.



### Constraint violated for VM external IP addresses

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a failed job:
    
    
    Instance VM_NAME creation failed: Constraint constraints/compute.vmExternalIpAccess violated for project PROJECT_NUMBER.
    Add instance VM_NAME to the constraint to use external IP with it.
    

This issue occurs because your project, folder, or organization has set the [`compute.vmExternalIpAccess` organizational policy constraint](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip) so that only allowlisted VMs can use external IP addresses.

#### Solution

To resolve the issue, recreate the job and do _one_ of the following:

  * Use a project that is [exempt from the constraint](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#RestoreDefault).
  * [Create a job that blocks external access for all VMs](https://docs.cloud.google.com/batch/docs/job-without-external-access).



### Constraint violated for trusted images

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a failed job:
    
    
    Instance VM_NAME creation failed: Constraint constraints/compute.trustedImageProjects violated for project PROJECT_ID. Use of images from project batch-custom-image is prohibited.
    

#### Solution

This issue occurs because your project has set the trusted images (`compute.trustedImageProjects`) policy constraint so that images from Batch, which are in the `batch-custom-image` images project, are not allowed.

To resolve the issue, do at least one of the following:

  * Recreate the job to [specify a VM OS image](https://docs.cloud.google.com/batch/docs/specify-vm-os-image) that is already allowed by the trusted images policy constraint.
  * Ask your administrator to modify the trusted image policy constraint to allow VM OS images from the `batch-custom-image` images project. For instructions, see [Control access to VM OS images for Batch](https://docs.cloud.google.com/batch/docs/control-access-vm-os-images).



### Failed to install `linux-headers-` packages

#### Issue

The following issue or a similar issue mentioning `linux-headers-` appears when you [view the logs for the job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs):
    
    
    Failed with exception: Command '['apt', 'install', '-y', 'linux-headers-VERSION', 'software-properties-common', 'pciutils', 'gce', 'make', 'dkms']' returned non-zero exit status 100.
    

#### Solution

This issue occurs due to a known issue. For more information about this issue and how to resolve it, see [Jobs might fail when specifying Compute Engine (or custom) VM OS images with outdated kernels](https://docs.cloud.google.com/batch/docs/known-issues#jobs-fail-specify-compute-images-outdated-kernels).

### Job failed while using an instance template

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a failed job that uses an instance template:
    
    
    INVALID_FIELD_VALUE,BACKEND_ERROR
    

This issue occurs due to unclear problems with the job's instance template.

#### Solution

To debug the issue further, do the following:

  1. [Create a MIG](https://docs.cloud.google.com/compute/docs/quickstart-mig) using the instance template and observe if errors occur with more details.
  2. Optional: To try to find more information, see the [long running operation](https://docs.cloud.google.com/apis/design/design_patterns#long_running_operations) that is creating the MIG in the Google Cloud console.

[Go to Compute Engine Operations](https://console.cloud.google.com/compute/operations)




## Task failure exit codes

When a specific task in a job fails, the task returns a nonzero [exit code](https://en.wikipedia.org/wiki/Exit_status). Depending on how you configure the [`ignoreExitStatus` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#runnable), a failed task might or might not cause a job to fail.

In addition to any exit codes that you define in a runnable, a Batch has several reserved exit codes, including the following exit codes.

### VM preemption (50001)

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job:
    
    
    Task state is updated from PRE-STATE to FAILED on zones/ZONE/instances/INSTANCE_ID due to Spot Preemption with exit code 50001.
    

This issue occurs when a [Spot VM](https://docs.cloud.google.com/compute/docs/instances/spot) for the job is preempted during run time.

#### Solution

To resolve the issue, do one of the following:

  * Retry the task either by using [automated task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) or manually re-running the job.
  * To guarantee there is no preemption, use VMs with the standard provisioning model instead.



### VM reporting timeout (50002)

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job:
    
    
    Task state is updated from PRE-STATE to FAILED on zones/ZONE/instances/INSTANCE_ID due to Batch no longer receives VM updates with exit code 50002.
    

This issue occurs when there is a timeout in the backend that caused Batch to no longer receive updates from a VM for the job. Unfortunately, many hardware failures or software failures can cause a VM to be unresponsive—for example, a VM might crash due to a temporary host event or [insufficient resources](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

#### Solution

To resolve this issue, do the following:

  1. In case the issue is temporary and resolves itself, retry the task either by using [automated task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) or manually re-running the job.
  2. If the issue persists, identify and resolve what is causing the VM to be unresponsive by doing one or more of the following:

     * **Recommended:** Get support through [Google Cloud Support](https://docs.cloud.google.com/support) or the [Batch label on Cloud Forums](https://www.googlecloudcommunity.com/gc/forums/filteredbylabelpage/board-id/cloud-infrastructure/label-name/batch).

     * Try to identify and resolve the issue yourself. For example, if you are familiar with Compute Engine, you can try to troubleshoot the job's VMs by doing the following:

       1. To identify the names of your job's VMs, do the following:

          1. [View logs for the job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs).
          2. [Filter logs](https://docs.cloud.google.com/logging/docs/view/building-queries#search-text) for entries that contain phrase `report agent state:`.
          3. Review the logs to determine the VM for each attempt of each task. Each log is similar to the following, in which there is one `instance:` phrase and one or more `task_id:` phrases.
                 
                 report agent state: ... instance:"INSTANCE_NAME" ... task_id:"task/JOB_UID-group0-TASK_INDEX/TASK_RETRIES/0 ..."
                 

This log includes the following values:

             * `INSTANCE_NAME`: The name of the VM.
             * `JOB_UID`: The unique ID (UID) of the job.
             * `TASK_INDEX`: The index of the task.
             * `TASK_RETRIES`: The attempt of the task that ran on this VM, which is formatted as the number of retries. For example, this value is `0` for the first attempt of a task. Each task is only attempted once unless you enable [automated task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).
       2. Troubleshoot your job's VMs using the Compute Engine documentation. For example, see [Troubleshooting VM shutdowns and reboots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reboots) and [Troubleshooting VM startup](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-startup).




### VM rebooted during execution (50003)

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job:
    
    
    Task state is updated from PRE-STATE to FAILED on zones/ZONE/instances/INSTANCE_ID due to VM is rebooted during task execution with exit code 50003.
    

This issue occurs when a VM for a job unexpectedly reboots during run time.

#### Solution

To resolve this issue, retry the task either by using [automated task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) or manually re-running the job.

### VM and task are unresponsive (50004)

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job:
    
    
    Task state is updated from PRE-STATE to FAILED on zones/ZONE/instances/INSTANCE_ID due to tasks cannot be canceled with exit code 50004.
    

This issue occurs when a task reaches the unresponsive time limit and cannot be cancelled.

#### Solution

To resolve this issue, retry the task either by using [automated task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) or manually re-running the job.

### Task runs over the maximum runtime (50005)

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job:
    
    
    Task state is updated from PRE-STATE to FAILED on zones/ZONE/instances/INSTANCE_ID due to task runs over the maximum runtime with exit code 50005.
    

This issue occurs in the following cases:

  * A task's run time exceeds the time limit specified in the [`maxRunDuration` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.max_run_duration)
  * A runnable's run time exceeds the time limit specified in the [`timeout` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#runnable.FIELDS.timeout)



To identify specifically which time limit was exceeded, [view logs for the job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs) and find a log that mentions the `50005` exit code. This `textPayload` field of this log indicates where and when the time limit was exceeded.

**Important:** Due to a known issue, the logs generated by Batch for exceeded timeout don't indicate whether the task's timeout or the runnable's timeout was exceeded. For a workaround that explains how to identify which timeout was exceeded, see the [known issue](https://docs.cloud.google.com/batch/docs/known-issues#runnable-timeout).

#### Solution

To resolve the issue, attempt to verify the total run time required by the task or runnable that exceeded the time limit. Then, do one of the following:

  * If you only occasionally expect this error, such as for a task or runnable with an inconsistent run time, you can try to recreate the job and configure it to [automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) to try to increase the success rate.

  * Otherwise, if the task or runnable consistently and intentionally needs more time to finish running than the current timeout allows, [set a longer timeout](https://docs.cloud.google.com/batch/docs/set-timeouts).




### VM recreated during execution (50006)

#### Issue

The following issue appears in the [`statusEvents` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobstatus) for a job:
    
    
    Task state is updated from PRE-STATE to FAILED on zones/ZONE/instances/INSTANCE_ID due to VM is recreated during task execution with exit code 50006.
    

This issue occurs when a VM for a job is unexpectedly recreated during run time.

#### Solution

To resolve this issue, retry the task either by using [automated task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) or manually re-running the job.

## What's next

  * [Get support for Batch](https://docs.cloud.google.com/batch/docs/get-started#get-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
