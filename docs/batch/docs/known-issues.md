---
url: https://docs.cloud.google.com/batch/docs/known-issues/
title: Known issues \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:28.720094+00:00
---

# Known issues  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known issues that you might run into while using Batch.

If you need further help using Batch, see the [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting) documentation or [Get support](https://docs.cloud.google.com/batch/docs/get-started#get-support).

## Pub/Sub might not send notifications for intermediate states during quick changes

Pub/Sub might not send notifications for all intermediate states when a job or task changes very quickly. For example, suppose that a task quickly changes states from `ASSIGNED`, then `RUNNING`, and then `FAILED`. In that scenario, you might not get a notification that the task reached the `RUNNING` state.

To mitigate this issue, we recommend that, when you want to see the complete state history of a job or task, [view status events](https://docs.cloud.google.com/batch/docs/view-status-events) instead of Pub/Sub notifications.

For more information about Pub/Sub notifications, see [Monitor job status using Pub/Sub notifications and BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications).

## Timeouts logs don't indicate whether task's or runnable's timeout was exceeded

When a job fails due to exceeding a [timeout](https://docs.cloud.google.com/batch/docs/set-timeouts), the logs associated with the job don't indicate whether the failure was caused by the relevant task's timeout or the relevant runnable's timeout.

To work around this issue, set different timeout values for tasks and runnables. Then, you can identify whether a failure was caused by exceeding the timeout of the relevant task or runnable by using the following procedure:

  1. Identify the task, runnable, and time of an exceeded-timeout failure.

     1. [View logs for the job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs).

     2. Find a log that mentions the exceeded-timeout exit code, `50005`. This log has a `textPayload` that's similar to the following message:
            
            Task task/JOB_UID-group0-TASK_INDEX/0/0 runnable RUNNABLE_INDEX...exitCode 50005
            

From that log, record `TASK_INDEX` as the failed task, `RUNNABLE_INDEX` as the failed runnable, and the log's `timestamp` value as the time of the exceeded-timeout failure.

  2. Identify the start time of the failed task.

     1. [View the status events of the failed task](https://docs.cloud.google.com/batch/docs/view-status-events#view-task-status-events).

     2. Find the status event that mentions the following message:
            
            Task state is updated from ASSIGNED to RUNNING
            

From that status event, record the `eventTime` field as the start time of the failed task.

  3. Calculate failed task's total run time, \\({failedTaskRunTime}\\), by using the following formula:

\\[{failedTaskRunTime}={failureTime}-{failedTaskStartTime}\\]

Replace the following values:

     * \\({failureTime}\\): the time of the exceeded-timeout failure.
     * \\({failedTaskStartTime}\\): the start time of the failed task.
  4. Identify the exceeded timeout:

     * If \\({failedTaskRunTime}\\) matches the timeout that you configured for the failed task, then that failed task's timeout was exceeded and caused the failure.

     * Otherwise, the timeout that you configured for the failed runnable was exceeded and caused the failure.




## Jobs consuming reservations might be delayed or prevented

When you try to [create and run a job that consumes Compute Engine reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation), Batch might incorrectly delay or prevent the job from running. Specifically, Batch is requiring projects to have sufficient [Compute Engine resource quotas](https://docs.cloud.google.com/compute/resource-usage) even when those resource quotas are being used by unconsumed reservations.

Learn more about this issue as follows:

  1. If you want more information about how and when this issue impacts jobs, then see Identify and understand this issue.
  2. To learn how to prevent or resolve this issue, see Work around this issue.



### Identify and understand this issue

This issue isn't indicated by any specific error message. Instead, this issue can happen in the following circumstances:

  * **If your project reserves all of the resources that it has quota for, this issue prevents any jobs that specify those resources.**

For example, suppose that your project has the following:

    * A maximum quota for H100 GPUs of 16.
    * An unconsumed, single-project reservation for 2 `a3-highgpu-8g` VMs, which reserves 16 H100 GPUs total.

In this scenario, this issue prevents your project from scheduling and running any job that is correctly configured to consume any of the reserved H100 GPUs.

  * **If your project reserves some of the resources that it has quota for, this issue might prevent or delay jobs that specify those resources.**

For example, suppose your project has the following:

    * A maximum quota for H100 GPUs of 16.
    * An unconsumed, single-project reservation for 1 `a3-highgpu-8g` VM, which reserves 8 H100 GPUs total.
    * A `a3-highgpu-8g` VM that is configured to [not consume any reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption) and is occasionally deleted then recreated. (This VM uses 8 unreserved H100 GPUs when it exists.)

In this scenario, this issue only allows your project to schedule and start running any job that is correctly configured to consume any of the reserved H100 GPUs when the `a3-highgpu-8g` VM doesn't exist.




### Work around this issue

To work around this issue for a job, add a label with the name `goog-batch-skip-quota-check` and value `true` to the [job-level `labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#resource:-job). This label causes Batch to skip verifying your project's resource quotas before trying to create a job.

**Important:** It's not recommended to enable the `goog-batch-skip-quota-check` label for jobs that can't consume any reservations in your project. For example, avoid this workaround when your project doesn't have any Compute Engine reservations or when a job requires VMs that aren't compatible with those reservations. Otherwise, if jobs unnecessarily skip quota checks, you might see unnecessary [insufficient quota failures](https://docs.cloud.google.com/batch/docs/troubleshooting#insufficient-quota).

For example, to prevent or resolve this issue for a basic script job that can consume reservations, create and run a job with the following JSON configuration:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy": {
        "instances": [
          {
            VM_RESOURCES
          }
        ],
      },
      **"labels" : {
        "goog-batch-skip-quota-check": "true"
      },**
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace `VM_RESOURCES` with the VM resources that match the reservation that you want to the job to consume.

For more instructions, see [Create and run a job that can consume reserved VMs](https://docs.cloud.google.com/batch/docs/create-run-job-reservation#create-run-job-consume-reservation) and [Define custom labels for the job](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels#define-labels-job).

## Jobs might fail when specifying Compute Engine (or custom) VM OS images with outdated kernels

A job might fail if it specifies a Compute Engine VM OS image that doesn't have the latest kernel version. (This issue also impacts any custom images based on Compute Engine VM OS images.) Consider this issue if you have a job that fails unexpectedly and specifies a Compute Engine VM OS image or similar custom image. Although this issue can happen for any Compute Engine images (even the latest version) at any time, we've observed that it's mainly prevalent for Debian Compute Engine images.

Learn more about this issue as follows:

**Note:** If your job uses GPUs, also see Jobs using GPUs and VM OS images with outdated kernels fail only when automatically installing drivers.

  1. If you want more information about how and when this issue impacts jobs, then see Identify and understand this issue.
  2. To learn how to prevent or resolve this issue, see Work around this issue.



### Identify and understand this issue

This issue is caused by an outdated kernel version in the VM OS image that causes the VM to reboot. When a job specifies any VM OS image that isn't from Batch or based on a Batch image, Batch installs required packages on the job's VMs after they start. The required packages can vary for different jobs and change over time, and they might require your VM OS image to have the latest kernel version. This issue appears when updating the kernel version requires the VM to reboot, which causes the package installation and the job to fail.

This issue might happen at any time, even if you use the latest version of a Compute Engine image. If an OS has been updated recently, especially for unpredictable updates like hotfixes—urgent updates for vulnerabilities or critical issues—then Compute Engine VM OS images might not have been able to react to the changes yet. For example, we've observed that, for Debian OS, packages with `linux-headers-` prefixes can be unpredictably removed from the kernel by hotfixes.

To identify this issue, we recommend that you [view logs for the job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs) to check for installation errors related to your VM OS image. For example, if your job uses a Debian Compute Engine image or similar custom image, then we recommend that you check for [errors related to installing `linux-headers-` packages](https://docs.cloud.google.com/batch/docs/troubleshooting#failed-to-install-linux-headers) by specifying the following query:
    
    
    labels.job_uid="JOB_UID" AND severity="ERROR" AND textPayload:("failed" "apt" "install" "linux-headers-")
    

Replace `JOB_UID` with the unique ID (UID) of the job. To get a job's UID, [describe the job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs). If this query returns any results, then this issue might be impacting your job.

### Work around this issue

To prevent or resolve this issue, we recommend that you do the following:

  1. Whenever possible, use Batch images or custom images based on Batch images, which aren't affected by this issue.

  2. Try the latest version of your preferred Compute Engine image. Generally, newer versions of Compute Engine images are more likely to have the latest kernel version than earlier versions.

  3. Choose one of the following options:

     * Try a different OS or create a custom image. For example, if the latest version of Debian 12 doesn't work, you can try to [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-custom) from a Compute Engine VM that runs Debian 12 and that you've updated to use the latest kernel version.

     * If your job fails due to [errors related to installing `linux-headers-` packages](https://docs.cloud.google.com/batch/docs/troubleshooting#failed-to-install-linux-headers), then you can attempt to use the VM OS image with outdated `linux-headers-` packages. To allow outdated `linux-headers-` packages, add a label with the name `goog-batch-allow-insecure-linux-headers-installation` and value `true` to the [job-level `labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#resource:-job).

**Caution:** Enable the `goog-batch-allow-insecure-linux-headers-installation` label at your own risk. This label allows your job to attempt installing and using archived `linux-headers-` packages. Because the packages are outdated, they are potentially insecure and might expose your job to vulnerabilities or be missing critical updates.

For example, to allow outdated `linux-headers-` packages for a basic script job that specifies a VM OS image, create and run a job with the following JSON configuration:
           
           {
             "taskGroups": [
               {
                 "taskSpec": {
                   "runnables": [
                     {
                       "script": {
                         "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                       }
                     }
                   ]
                 },
                 "taskCount": 3
               }
             ],
             "allocationPolicy": {
               "instances": [
                 {
                   "policy": {
                     "bootDisk": {
                       "image": "VM_OS_IMAGE_URI"
                     }
                   }
                 }
               ]
             },
             **"labels" : {
               "goog-batch-allow-insecure-linux-headers-installation": "true"
             },**
             "logsPolicy": {
               "destination": "CLOUD_LOGGING"
             }
           }
           

Replace `VM_OS_IMAGE_URI` with the URI of the VM OS image that you want to use.

For more instructions, see [Define custom labels for the job](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels#define-labels-job) and [Specify the VM OS image for a job](https://docs.cloud.google.com/batch/docs/specify-vm-os-image).




For more information about VM OS images, see [Overview of the OS environment for a job's VMs](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).

## Jobs using GPUs and VM OS images with outdated kernels might fail only when automatically installing drivers

This issue is closely related to the previous issue, Jobs might fail when specifying Compute Engine (or custom) VM OS images with outdated kernels. Specifically, jobs that both specify a Compute Engine (or custom) VM OS image without the latest kernel and use GPUs might fail only if you try to install GPU drivers automatically. For these jobs, you might also resolve the failures just by installing GPU drivers manually.

For more information about this issue and how to resolve it, see Jobs might fail when specifying Compute Engine (or custom) VM OS images with outdated kernels. For more information about GPUs, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
