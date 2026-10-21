---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/workflows-autoscaling/
title: Scale Cloud Run worker pools with Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:51.570526+00:00
---

# Scale Cloud Run worker pools with Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/workflows-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Scale Cloud Run worker pools with Workflows Stay organized with collections  Save and categorize content based on your preferences. 

After you've created a Cloud Run worker pool, you can use [Workflows](https://docs.cloud.google.com/workflows/docs/overview) to automate its scaling. This lets you adjust the instance count based on external events, custom logic, or schedules. 

## Before you begin

The following list describes the requirements when using Workflows to deploy and execute a Cloud Run worker pools workflow:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Run Admin API and Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,workflows.googleapis.com)




### Required roles

To get the permissions that you need to deploy and execute Cloud Run worker pools with Workflows, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the Cloud Run worker pool
  * [Workflows Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.editor) (`roles/workflows.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



To allow Workflows to update the Cloud Run worker pool, the service account that is used to deploy your workflow must have the following role:

  * [Cloud Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a Cloud Run worker pool

[Create a Cloud Run worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools#worker-pool) if you haven't done so already. You will reference the name of the Cloud Run worker pool when executing your workflow later on.

## Create, deploy, and execute the workflow

The following workflow updates the instance count of your Cloud Run worker pool.

  1. In your home directory, create a new YAML file for your workflow, such as `update-cr-worker-pool.yaml`, and copy and paste the following content into your file:
         
         main:
           params: [args]
           steps:
             - init:
                 assign:
                   - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                   - region: ${args.region}
                   - workerPoolName: ${args.workerPool}
                   - instanceCount: ${args.instanceCount}
                   - workerPoolUrl: ${"https://run.googleapis.com/v2/projects/" + project + "/locations/" + region + "/workerPools/" + workerPoolName}
             - updateWorkerPool:
                 call: http.patch
                 args:
                   url: ${workerPoolUrl}
                   query:
                     updateMask: "scaling.manualInstanceCount"
                   auth:
                     type: OAuth2
                   body:
                     scaling:
                       manualInstanceCount: ${int(instanceCount)}
                 result: updateResult
             - returnOutput:
                 return: ${updateResult.body}
         

  2. Deploy the workflow and associate it with a specified service account:
         
         gcloud workflows deploy WORKFLOW_NAME \
             --source=WORKFLOW_NAME.yaml \
             --location=REGION \
             --service-account=SERVICE_ACCOUNT

Replace the following:

     * WORKFLOW_NAME: the name of your workflow, such as `update-worker-pool`. The workflow name should match the name of the YAML file you created earlier.
     * REGION: the region your Cloud Run worker pool is deployed in, for example `europe-west1`.
     * SERVICE_ACCOUNT: the service account email that has been granted the required roles, for example: 
       * `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`
       * `PROJECT_NUMBER-compute@developer.gserviceaccount.com`
  3. Execute the workflow with the details of your worker pool and the instance count:
         
         gcloud workflows execute WORKFLOW_NAME \
             --location=REGION \
             --data='{"region":"REGION", "workerPool":"WORKER_POOL_NAME", "instanceCount":INSTANCE_COUNT}'

Replace the following:

     * WORKFLOW_NAME: the name of your workflow.
     * REGION: the region your Cloud Run worker pool is deployed in, for example `europe-west1`.
     * WORKER_POOL_NAME: the name of your worker pool.
     * INSTANCE_COUNT: the modified number of instances for the worker pool, for example `3`.



## Verify the updates

After you've executed the workflow, you can view the updates in the following places in the Google Cloud console:

  * To view the execution status and results, go to the Workflows details page and select your workflow:

[Go to Workflows](https://console.cloud.google.com/workflows)

Verify that the `manualInstanceCount` field has changed in the most recent execution of the workflow.

  * To verify the update was successful in Cloud Run, go to the worker pools page:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

Verify that the manual scaling count for your worker pool has changed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
