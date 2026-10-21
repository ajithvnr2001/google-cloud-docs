---
url: https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs/
title: Manage patch jobs \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:34:27.399109+00:00
---

# Manage patch jobs  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Manage patch jobs Stay organized with collections  Save and categorize content based on your preferences. 

After you [create a patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job), you can use the following procedures to review and manage your patches:

  * List patch jobs: View a list of all active and completed jobs.
  * List VM instance details: Review patch status for your VM instances.
  * Describe patch job: Get details about a specific patch job.
  * Cancel a patch job: Cancel a specific patch job.



You can manage your patch jobs using either the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest).

## Before you begin

  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
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




## Permissions

Owners of a project have full access to run and manage patch jobs. For all other users, you need to grant permissions. You can grant one of the following granular roles:

  * `roles/osconfig.patchJobExecutor`: Contains permissions to run, cancel, get, and list patch jobs. It also contains permissions to view instance details for a patch job.
  * `roles/osconfig.patchJobViewer`: Contains permissions for read-only access to get and list patch jobs. It also contains permissions to view instance details for a patch job.



## List patch jobs

View a list of all active and completed jobs.

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Select the **Patch Jobs** tab.



###  gcloud 

Use the [`os-config patch-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list) command to list patch jobs.
    
    
    gcloud compute os-config patch-jobs list

For the Google Cloud CLI, the default output returns the 10 most recent patch jobs whether they are completed or active. You can override this setting, by using the `--limit` flag.

The output resembles the following:
    
    
    ID                                          NAME    DESCRIPTION               CREATE_TIME               UPDATE_TIME               STATE                  TARGETED_INSTANCES
    23b0815e-1c94-4dc6-91b1-30a6da395cb9                                          2019-11-05T20:22:54.150Z  2019-11-06T19:40:08.641Z  COMPLETED_WITH_ERRORS  4
    4116ad72-bd57-4e48-94dc-7a577dc707b6                                          2019-08-23T20:36:03.068Z  2019-08-23T20:36:15.984Z  CANCELED               2
    06856cbe-9a7b-498e-9105-9ae4eb566511                                          2019-08-12T20:27:38.410Z  2019-08-12T20:28:37.583Z  SUCCEEDED              1
    04a15964-9eaa-4282-96f5-9cd535352cf6                                          2019-08-12T17:48:22.938Z  2019-08-12T17:48:42.274Z  SUCCEEDED              0
    21dc1e06-deee-4e3a-821e-8082a32abde5                testing patch job reboot  2019-07-24T22:45:07.451Z  2019-07-25T00:44:44.459Z  TIMED_OUT              1
    

You can use more flags to filter, order, and format your search. For example, to filter the above output to list only the URIs for the patch jobs that have a status of `SUCCEEDED` sorted by creation time and in ascending order, run the following command:
    
    
    gcloud compute os-config patch-jobs list \
       --filter="state=SUCCEEDED" \
       --sort-by="create_time" --uri
    

The output resembles the following:
    
    
    https://osconfig.googleapis.com/v1/projects/1234567/patchJobs/04a15964-9eaa-4282-96f5-9cd535352cf6
    https://osconfig.googleapis.com/v1/projects/1234567/patchJobs/06856cbe-9a7b-498e-9105-9ae4eb566511
    

For a full list of flags, review the [`os-config patch-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list) command.

###  REST 

In the API, create a `GET` request to the [`patchJobs.list`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/list) method. Replace `project-id` with your project ID.
    
    
    GET https://osconfig.googleapis.com/v1/projects/project-id/patchJobs
    

## List all VM instance details for a specific patch job

Review the patch job status for the full list of VM instances that use OS patch management.

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Select the **Patch Jobs** tab.
  3. Click the name of the patch job that you want to review.
  4. Scroll-down to **Updated VM instances**.



###  gcloud 

Use the [`os-config patch-jobs list-instance-details`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list-instance-details) command to list the details for all VMs in a specific patch job. Replace `patch-job-id` with the ID for your patch job.
    
    
    gcloud compute os-config patch-jobs list-instance-details patch-job-id

For example, to view the details for all instances that are a part of patch job `23b0815e-1c94-4dc6-91b1-30a6da395cb9`, run the following command:
    
    
    gcloud compute os-config patch-jobs list-instance-details 23b0815e-1c94-4dc6-91b1-30a6da395cb9

The output resembles the following:
    
    
    NAME                        ZONE           STATE      FAILURE_REASON
    instance-1                  us-central1-a  SUCCEEDED
    guest-policy-test-instance  us-east1-c     TIMED_OUT  Instance timed out while in state: APPLYING_PATCHES after PT1H2.225S
    my-centos                   us-west1-b     SUCCEEDED
    my-windows                  us-west1-b     FAILED     Error running pre-patch step: fork/exec /tmp/pre_patch_script.sh: no such file ..."
    

You can use more flags to filter, order, and format your search. For example, to list details for all inactive VMs sorted by instance name in descending order, run the following command. Replace `patch-job-id` with the ID for your patch job.
    
    
    gcloud compute os-config patch-jobs list-instance-details patch-job-id \
       --filter="state=INACTIVE" \
       --sort-by="~name"
    

For a full list of flags, review the [`os-config patch-jobs list-instance-details`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list-instance-details) command.

###  REST 

In the API, create a `GET` request to the [`patchJobs.instanceDetails`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails) method.
    
    
    GET https://osconfig.googleapis.com/v1/projects/project-id/patchJobs/patch-job-id/instanceDetails
    

Replace the following:

  * `project-id`: Your project ID.
  * `patch-job-id`: Your patch job ID.



## Describe patch jobs

Review detailed information for a patch job.

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Select the **Patch Jobs** tab.
  3. Click the name of the patch job that you want to review.
  4. Review the **Update info** section.



###  gcloud 

Use the [`os-config patch-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/describe) command to describe a patch job. Replace `patch-job-id` with the ID for your patch job.
    
    
    gcloud compute os-config patch-jobs describe patch-job-id

For example, to view information about patch job `23b0815e-1c94-4dc6-91b1-30a6da395cb9`, run the following command:
    
    
    gcloud compute os-config patch-jobs describe 23b0815e-1c94-4dc6-91b1-30a6da395cb9

The output resembles the following:
    
    
    createTime: '2019-11-05T20:22:54.150Z'
    errorMessage: Completed with 2 instance failure(s).
    filter: id=*
    instanceDetailsSummary:
      instancesFailed: '1'
      instancesSucceeded: '2'
      instancesTimedOut: '1'
    instanceFilter: {}
    name: projects/1234567/patchJobs/23b0815e-1c94-4dc6-91b1-30a6da395cb9
    patchConfig: {}
    percentComplete: 100.0
    state: COMPLETED_WITH_ERRORS
    updateTime: '2019-11-06T19:40:08.641Z'
    

###  REST 

In the API, create a `GET` request to the [`patchJobs.get`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/get) method.
    
    
    GET https://osconfig.googleapis.com/v1/projects/project-id/patchJobs/patch-job-id
    

Replace the following:

  * `project-id`: Your project ID.
  * `patch-job-id`: Your patch job ID.



## Cancel patch jobs

When cancelling a patch job, the OS Config agent finishes the sub-task that it is on but does not continue after that. Sub-task refers to a task performed by the agent that cannot be halted.

For example, if the patch job is canceled while the VM instance is rebooting, the reboot (and any potential post-reboot auto-patching) still runs to completion, but the agent does not initiate additional tasks for that patch job.

**Note:** You can only cancel active patch jobs.

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

     1. Select the **Patch Jobs** tab.
     2. Expand the more_vert**Actions** menu for the patch job that you want to cancel.
     3. Select **Cancel**.



###  gcloud 

Use the [`os-config patch-jobs cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/cancel) command to cancel a patch job. Replace `patch-job-id` with the ID for your patch job.
    
    
    gcloud compute os-config patch-jobs cancel patch-job-id

###  REST 

In the API, create a `POST` request to the [`patchJobs.cancel`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/cancel) method.
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs/patch-job-id:cancel
    

Replace the following:

  * `project-id`: Your project ID.
  * `patch-job-id`: Your patch job ID.



## What's next?

  * Learn more about [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch).
  * Learn more about [patch compliance status](https://docs.cloud.google.com/compute/vm-manager/docs/patch#patch_compliance_status).
  * [Create a patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Schedule patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
