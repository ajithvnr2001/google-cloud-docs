---
url: https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs/
title: Schedule patch jobs \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:19.074596+00:00
---

# Schedule patch jobs  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Schedule patch jobs Stay organized with collections  Save and categorize content based on your preferences. 

In addition to [running patch jobs on demand](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#run-patch-job), you might want to have patch jobs that run automatically based on a set schedule by creating a patch deployment.

Each patch deployment can have either a one-time schedule, which runs a patch job at one specific date and time, or a recurring schedule, which runs a patch job at a specified interval.

[Instance filters](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#instance-filters) allow you to simultaneously patch many instances at the same time. These filters are applied to each individual patch job at the time it runs. This ensures that changes in your project are captured on a real-time basis. For example, say a patch deployment is created to apply patches to all instances in zone `asia-souteast1-b` starting two weeks from now. At the time of creating the patch, you had 20 instances in the zone but then 40 new instances are added to the zone a few days later. Because the filter is applied at the time the patch starts, all 60 instances are updated. This lets you add and remove instances without the need to update the patch deployment schedule.

**Note:** You can patch a maximum of 500 VMs in a single patch deployment.

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




You can schedule your patch jobs using either the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest).

## Permissions

Owners of a project have full access to create and manage patch deployments. For all other users, you need to grant permissions. You can grant one of the following granular roles:

  * `roles/osconfig.patchDeploymentAdmin`: Contains permissions to create, delete, get, and list patch deployments.
  * `roles/osconfig.patchDeploymentViewer`: Contains permissions for read-only access to get and list patch deployments.



For example, to grant a user administrator access to patch deployments, run the following command:
    
    
    gcloud projects add-iam-policy-binding project-id \
        --member user:user-id@gmail.com \
        --role roles/osconfig.patchDeploymentAdmin
    

Replace the following:

  * `project-id`: The project ID.
  * `user-id`: The user's Google Workspace username.



## Creating a patch deployment

When you create a patch deployment, the name of the patch deployment must meet the following naming requirements:

  * Each name must be unique within a project
  * Contain only lowercase letters, numbers, and hyphens
  * Start with a letter
  * End with a number or a letter
  * Be between 1 and 63 characters



In the Google Cloud CLI and REST, the name of the patch deployment is referred to as the `patch-deployment-id`.

After you have started a patch deployment, you can monitor your patches using the [Patch dashboard](https://docs.cloud.google.com/compute/vm-manager/docs/patch#dashboard). It takes approximately 30 minutes after a patch job starts before the data is populated on the dashboard.

**Note:** Targeting all VMs in a single patch deployment might cause a reduction in system availability. We recommend that you keep this in consideration when planning your maintenance window or that you use instance filters and patch VMs in small batches.

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Click **New patch deployment**.
  3. In the **Target VMs** section, select the zone that contains the VMs that you want to patch. You can also choose to select all zones.

**Note:** In the Google Cloud console, you can only filter by name prefix or label. If you need to apply other types of instance filters use either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest).

For example, to patch specific VMs in the zones you selected, enter the name and label filters similar to the following:

     * Name prefix: `test-`
     * Labels: `env=dev` and `app=web`
  4. In the **Patch configuration** section, configure the patch.

     1. Specify a **Name** for your patch.
     2. Select the required updates for your operating system. For more information, see [what is included in an OS patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch#whats-in-a-patch).
  5. In the **Scheduling** section, complete the following:

     * Select a schedule. You can schedule a one-time patch job or recurring patch jobs.
     * (Optional) Set a [duration or maintenance window](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#maintenance-window).
  6. In the **Rollout options** section, configure the [patch rollout options](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#rollout-options):

     * Select whether to patch one zone at a time or to patch zones concurrently.
     * Set a disruption budget. A disruption budget is the number or percentage of VMs in a zone that you want to be disrupted at one time by the patching process.
  7. (Optional) In the **Advanced options** section, you can complete the following tasks:

     * Select a reboot option.
     * Upload pre-patch and post-patch scripts. For more information about pre-patch and post-patch scripts, see [Specifying pre-patch and post-patch scripts](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#add-scripts).
  8. Click **Deploy**.




###  gcloud 

Use the [`os-config patch-deployments create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create) command to create a patch deployment.
    
    
    gcloud compute os-config patch-deployments create patch-deployment-id \
        --file patch-deployment-file

Replace the following:

  * `patch-deployment-id`: The name of your patch deployment.
  * `patch-deployment-file`: The path to the YAML or JSON file that contains the configurations for the patch deployment.



**Example patch deployment YAML files**

The following sample YAML file can be used to create a recurring schedule for all instances in the zones `us-west2-b` and `us-west2-c`. The recurring schedule has the following specifications:

  * Start date is January 09, 2019 at 7:30 PM
  * End date is January 09, 2020 at 7:30 PM
  * The time zone to use is "America/Los_Angeles"
  * Runs every week on a Tuesday


    
    
    instanceFilter:
      zones:
      - us-west2-b
      - us-west2-c
    recurringSchedule:
      frequency: WEEKLY
      weekly:
        dayOfWeek: TUESDAY
      timeOfDay:
        hours: 19
        minutes: 30
      timeZone:
        id: America/Los_Angeles
      startTime: '2019-09-01T12:00:00Z'
      endTime: '2020-09-01T12:00:00Z'
    

###  REST 

In the API, create a `POST` request to create a new patch deployment. You must explicitly define all of the required configuration fields as described in the [`patchDeployments.create`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/create) API documentation. For example, a patch deployment with the minimal required fields (instance filter and schedule) looks like the following. Replace `project-id` with your project ID.
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
      "instanceFilter": instance-filter
    
      // Add one of the following parameters:
      "recurringSchedule": schedule
      "oneTimeSchedule": schedule
    }
    

Replace the following:

  * `project-id`: Your project ID.
  * `instance-filter`: The filter parameters that you want. For more information about instance filters, see [instance filters](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#instance-filters).
  * `schedule`: Provide either the `oneTimeSchedule` or `recurringSchedule` parameter that details scheduling parameters such as date, time and frequency to run the patch job.



**Examples**

**Example 1** : Create a one-time schedule to run a patch job on January 10, 2020 at 12am UTC on all instances in zones `us-west2-b` and `us-west2-c`.
    
    
    {
     "instanceFilter":{
       "zones":[
         "us-west2-b",
         "us-west2-c"
       ]
     },
     "oneTimeSchedule": {
       "executeTime": "2020-01-10T00:00:00Z"
     }
    }
    

**Example 2** : Create a recurring schedule for all instances in the zones `us-west2-b` and `us-west2-c`. The recurring schedule has the following specifications:

  * Start date is January 09, 2019 at 7:30 PM
  * End date is January 09, 2020 at 7:30 PM
  * The time zone to use is "America/Los_Angeles"
  * Runs every week on a Tuesday


    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchDeployments
    {
      "instanceFilter":{
        "zones":[
          "us-west2-b",
          "us-west2-c"
        ]
      },
      "recurringSchedule":{
        "frequency":"WEEKLY",
        "weekly":{
          "dayOfWeek":"TUESDAY"
        },
        "timeOfDay":{
          "hours":19,
          "minutes":30
        },
        "timeZone":{
          "id":"America/Los_Angeles"
        },
        "startTime":"2019-09-01T12:00:00Z",
        "endTime":"2020-09-01T12:00:00Z"
      }
    }
    

## List patch deployments

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Select the **Scheduled deployments** tab.



###  gcloud 

Use the [`os-config patch-deployments list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/list) command to list patch deployments.
    
    
    gcloud compute os-config patch-deployments list

This command returns all patch deployments. The output resembles the following:
    
    
    NAME              LAST_RUN                  NEXT_RUN              FREQUENCY
    first-deployment  2019-12-18T00:07:00.738Z  ---                   Once: Scheduled for 2019-12-18T00:07:00.000Z
    my-deployment1    2020-01-05T14:00:00.228Z  2020-01-12T14:00:00Z  Recurring - Weekly
    my-deployment2    ---                       2020-01-15T05:30:00Z  Recurring - Monthly on specific date(s)
    

You can use more flags to limit and format your search. For example, to list the first 10 patch deployments in pages of 2, run the following command. Replace `project-id` with your project ID.
    
    
    gcloud compute os-config patch-deployments list --limit 10 --page-size 2

###  REST 

In the API, create a `GET` request to the [`patchDeployments.list`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/list) method. Replace `project-id` with your project ID.
    
    
    GET https://osconfig.googleapis.com/v1/projects/project-id/patchDeployments
    

## Describe a patch deployment

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Select the **Scheduled deployments** tab.
  3. Click the name of the deployment that you want to review.



###  gcloud 

Use the [`os-config patch-deployments describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/describe) command to describe a patch deployment. Replace `patch-deployment-id` with the name for your patch deployment.
    
    
    gcloud compute os-config patch-deployments describe patch-deployment-id

###  REST 

In the API, create a `GET` request to the [`patchDeployments.get`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/get) method.
    
    
    GET https://osconfig.googleapis.com/v1/projects/project-id/patchDeployments/patch-deployment-id
    

Replace the following:

  * `project-id`: Your project ID.
  * `patch-deployment-id`: Your patch deployment name.



## Delete a patch deployment

###  console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Select the **Scheduled deployments** tab.
  3. Click the name of the deployment that you want to delete.
  4. Click **Delete this schedule**.



###  gcloud 

Use the [`os-config patch-deployments delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/delete) command to delete a patch deployment. Replace `patch-deployment-id` with the name for your patch deployment.
    
    
    gcloud compute os-config patch-deployments delete patch-deployment-id

###  REST 

In the API, create a `DELETE` request to the [`patchDeployments.delete`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/delete) method.
    
    
    DELETE https://osconfig.googleapis.com/v1/projects/project-id/patchDeployments/patch-deployment-id
    

Replace the following:

  * `project-id`: Your project ID.
  * `patch-deployment-id`: Your patch deployment name.



## What's next?

  * Learn more about [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch).
  * [Create a patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Manage your patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
