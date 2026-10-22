---
url: https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent/
title: Collect additional resource metrics using the Ops Agent \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:32.176937+00:00
---

# Collect additional resource metrics using the Ops Agent  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Collect additional resource metrics using the Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create and run a Batch job that automatically installs the Ops Agent. Install the Ops Agent to provide additional metrics in Cloud Monitoring about the performance of a job's resources. To learn more about using resource performance metrics for a job, see [Monitor and optimize job resources by viewing metrics](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

**Note:** The Ops Agent feature is not part of Batch and has its own pricing. For more information, see [Ops Agent pricing](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#pricing) in the Google Cloud Observability documentation.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. If your project hasn't already, enable the Cloud Monitoring and Cloud Logging APIs: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,logging.googleapis.com)

  3. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * To create a job: 
       * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
       * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/get-started#job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * To view logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  4. Unless you are using the default configuration for [the job's service account](https://docs.cloud.google.com/batch/docs/get-started#job-service-account), ensure that it has the necessary permissions.

To ensure that the job's service account has the necessary permissions to write Ops Agent metrics to Monitoring, ask your administrator to grant the following IAM roles to the job's service account: 

**Important:** You must grant these roles to the job's service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 
     * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on the project
     * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project

  5. Ensure that your planned job configuration meets the Ops Agent requirements. 



### Ops Agent requirements

To create and run a job that uses the Ops Agent, your job must comply with all the following requirements:

  * Ensure that the job's VMs use an [operating system (OS) that the Ops Agent supports](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems). For more information about the VM OS image for a job, see [Overview of the OS environment for a job's VMs](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).

  * If your job uses a non-default networking configuration or uses VPC Service Controls, ensure that the job meets the [access requirements](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#access) for the Ops Agent. For more information, see [VMs without remote package access](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#remote_package_access) in the Google Cloud Observability documentation.

  * Ensure that the job doesn't install a legacy Cloud Logging agent or Cloud Monitoring agent—for example, through a custom image or instance template.




For more information about the features and requirements of the Ops Agent, see [Ops Agent overview](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) in the Google Cloud Observability documentation.

## Create a job that automatically installs the Ops Agent

Use the Google Cloud CLI or REST API to [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that includes the [`installOpsAgent` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate.FIELDS.install_ops_agent) set to `true` in the `allocationPolicy.instances` field in the main body in the JSON file:
    
    
    "allocationPolicy": {
      "instances": [
        {
          "installOpsAgent": true
        }
      ]
    }
    

For example, a job that automatically installs the Ops Agent can have a JSON configuration file that is similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello World! This is task $BATCH_TASK_INDEX."
                }
              }
            ]
          },
          "taskCount": 3,
        }
      ],
      "allocationPolicy": {
        "instances": [
          {
            **"installOpsAgent" : true**
          }
        ]
      },
      "logsPolicy": {
          "destination": "CLOUD_LOGGING"
      }
    }
    

After the job's VMs start running, you can see the Ops Agent metrics the same as any other resource metric. For more information, see [Monitor and optimize job resources by viewing metrics](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
