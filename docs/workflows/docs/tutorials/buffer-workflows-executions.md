---
url: https://docs.cloud.google.com/workflows/docs/tutorials/buffer-workflows-executions/
title: Use a Cloud Tasks queue to buffer your workflow executions \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:55.464725+00:00
---

# Use a Cloud Tasks queue to buffer your workflow executions  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/buffer-workflows-executions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Use a Cloud Tasks queue to buffer your workflow executions Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create a Cloud Tasks queue that can regulate the rate of workflow executions.

There is a [maximum number](https://docs.cloud.google.com/workflows/quotas#quotas) of active workflow executions that can happen concurrently. Once this quota is exhausted, and if [execution backlogging](https://docs.cloud.google.com/workflows/docs/executing-workflow#manage_execution_backlogging) is disabled, or if the quota for backlogged executions is reached, any new executions fail with an HTTP `429 Too many requests` status code. By enabling a Cloud Tasks queue to execute child workflows at a rate that you define, you can avoid Workflows quota-related issues and achieve a better execution rate.

Note that Cloud Tasks is designed to provide "at least once" delivery; however, Workflows doesn't ensure exactly-once processing of duplicate requests from Cloud Tasks.

In the following diagram, a parent workflow invokes child workflows that are regulated by a Cloud Tasks queue that has a dispatch rate applied.

![Parent workflow invoking iterations of a child workflow through
Cloud Tasks Queue](https://docs.cloud.google.com/static/workflows/images/workflows-tasks.svg)

## Objectives

In this tutorial you will:

  1. Create a Cloud Tasks queue that acts as an intermediary between the parent and child workflows.
  2. Create and deploy a child workflow that receives data from the parent workflow.
  3. Create and deploy the parent workflow that executes the child workflow through the Cloud Tasks queue.
  4. Run the parent workflow without a dispatch rate limit, which invokes executions of the child workflow.
  5. Apply a dispatch limit to the Cloud Tasks queue and run the parent workflow.
  6. Observe that the child workflows are executed at the rate defined through the Cloud Tasks queue.



You can run the following commands in the Google Cloud console or by using the Google Cloud CLI in either your terminal or Cloud Shell.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Tasks](https://docs.cloud.google.com/tasks)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

###  Console 

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Tasks, Compute Engine, and Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudtasks.googleapis.com,compute.googleapis.com,workflows.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Tasks, Compute Engine, and Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudtasks.googleapis.com,compute.googleapis.com,workflows.googleapis.com)

  8. In the Google Cloud console, go to the **IAM** page to set permissions for the Compute Engine default service account. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will associate it with the workflows in this tutorial for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  9. Select the Compute Engine default service account and in that row, click edit **Edit principal**.
  10. In the dialog box that appears, click add **Add another role** and add the following roles: 
     1. In the **Select a role** list, select **Workflows** > **Workflows Invoker** so that the account has permission to trigger your workflow execution.
     2. In the **Select a role** list, select **Cloud Tasks** > **Cloud Tasks Enqueuer** so that the account has permission to create tasks.
  11. Click **Save**.



###  gcloud 

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Tasks, Compute Engine, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudtasks.googleapis.com compute.googleapis.com workflows.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Tasks, Compute Engine, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudtasks.googleapis.com compute.googleapis.com workflows.googleapis.com

  14. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will associate it with the workflows in this tutorial for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  15. Grant the [Workflows Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.invoker) (`roles/workflows.invoker`) on the project to the Compute Engine default service account so that the account has permission to trigger your workflow execution. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/workflows.invoker

Replace the following:

     * `PROJECT_ID`: the Google Cloud project ID
     * `PROJECT_NUMBER`: the Google Cloud project number 

  16. Grant the [Cloud Tasks Enqueuer role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.enqueuer) (`roles/cloudtasks.enqueuer`) on the project to the Compute Engine default service account so that the account has permission to create tasks. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/cloudtasks.enqueuer




## Create a Cloud Tasks queue

Create a Cloud Tasks queue that you can use in the parent workflow and that lets you regulate the rate of workflow executions.

### Console

  1. In the Google Cloud console, go to the **Cloud Tasks** page:

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click add **Create push queue**.

  3. Enter the **Queue name** , `queue-workflow-child`.

  4. In the **Region** list, select **us-central1 (Iowa)**.

  5. Click **Create**.




### gcloud
    
    
    QUEUE=queue-workflow-child
    LOCATION=us-central1
    gcloud tasks queues create $QUEUE --location=$LOCATION

## Create and deploy a child workflow

A child workflow can receive and process data from a parent workflow. Create and deploy a child workflow that does the following:

  * Receives an `iteration` as an argument
  * Sleeps for 10 seconds to simulate some processing
  * Returns a string upon successful execution




### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter the name, `workflow-child`, for the new workflow.

  4. In the **Region** list, select **us-central1 (Iowa)**.

  5. In the **Service account** list, select the **Compute Engine default service account**.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
           params: [args]
           steps:
             - init:
                 assign:
                   - iteration : ${args.iteration}
             - wait:
                 call: sys.sleep
                 args:
                     seconds: 10
             - return_message:
                 return: ${"Hello world"+iteration}

  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch workflow-child.yaml

  2. Open your source code file in a text editor and copy the following workflow to the file.
         
         main:
           params: [args]
           steps:
             - init:
                 assign:
                   - iteration : ${args.iteration}
             - wait:
                 call: sys.sleep
                 args:
                     seconds: 10
             - return_message:
                 return: ${"Hello world"+iteration}

  3. Deploy the workflow:
         
         gcloud workflows deploy workflow-child \
             --source=workflow-child.yaml \
             --location=us-central1 \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com




## Create and deploy the parent workflow

The parent workflow executes multiple branches of the child workflow using a `for` loop.

  1. Copy the source code that defines the parent workflow:
         
         main:
           steps:
             - init:
                 assign:
                   - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                   - project_number: ${sys.get_env("GOOGLE_CLOUD_PROJECT_NUMBER")}
                   - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
                   - workflow_child_name: "workflow-child"
                   - queue_name: "queue-workflow-child"
             - enqueue_tasks_to_execute_child_workflow:
                 for:
                   value: iteration
                   range: [1, 100]
                   steps:
                       - iterate:
                           assign:
                             - data:
                                 iteration: ${iteration}
                             - exec:
                                 # Encode object to JSON string in expression for workflow argument
                                 argument: ${json.encode_to_string(data)}
                       - create_task_to_execute_child_workflow:
                           call: googleapis.cloudtasks.v2.projects.locations.queues.tasks.create
                           args:
                               parent: ${"projects/" + project_id + "/locations/" + location + "/queues/" + queue_name}
                               body:
                                 task:
                                   httpRequest:
                                     body: ${base64.encode(json.encode(exec))}
                                     url: ${"https://workflowexecutions.googleapis.com/v1/projects/" + project_id + "/locations/" + location + "/workflows/" + workflow_child_name + "/executions"}
                                     oauthToken:
                                       serviceAccountEmail: ${project_number + "-compute@developer.gserviceaccount.com"}

The workflow consists of the following parts:

     * A map that is used to assign constants referring to the child workflow and the Cloud Tasks queue name. For more information, see [Maps](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps).

     * A `for` loop that is executed to invoke the child workflow, iteratively. For more information, see [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration).

     * A workflow step that creates and adds a large number of tasks to the Cloud Tasks queue to execute the child workflow. For more information, see [Cloud Tasks API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/Overview).

  2. Deploy the workflow:

### Console

     1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

     2. Click add **Create**.

     3. Enter the name, `workflow-parent`, for the new workflow.

     4. In the **Region** list, select **us-central1 (Iowa)**.

     5. In the **Service account** list, select the **Compute Engine default service account**.

     6. Click **Next**.

     7. In the workflow editor, paste the definition for the parent workflow.

     8. Click **Deploy**.

### gcloud

     1. Create a source code file for your workflow:
            
            touch workflow-parent.yaml

     2. Open your source code file in a text editor and paste the definition for the parent workflow.

     3. Deploy the workflow:
            
            gcloud workflows deploy workflow-parent \
                --source=workflow-parent.yaml \
                --location=us-central1 \
                --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com




## Execute the parent workflow without rate limits

Execute the parent workflow to invoke the child workflows through the Cloud Tasks queue. The executions should take about 10 seconds to complete.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click the **workflow-parent** workflow to go to its details page.

  3. On the **Workflow details** page, click _play_arrow_ **Execute**.

  4. Click **Execute** again.

  5. As the parent workflow is running, return to the **Workflows** page, and click the **workflow-child** workflow to go to its details page.

  6. Click the **Executions** tab.

You should see executions of the child workflow, running around the same time, similar to the following:

![Details of the child workflow executions running around the
same time.](https://docs.cloud.google.com/static/workflows/images/workflow-execution-no-rate-limits.png)



### gcloud

  1. Execute the workflow:
         
         gcloud workflows run workflow-parent \
              --location=us-central1

  2. To verify that a workflow execution was triggered, list the last four executions:
         
         gcloud workflows executions list workflow-child --limit=4

Since the number of executions (100 ) is below the Workflows concurrency limit, the results should be similar to the following. Quota issues might arise if you submit thousands of executions at the same time. 
         
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/1570d06e-d133-4536-a859-b7b6a1a85524
         STATE: ACTIVE
         START_TIME: 2023-07-27T00:56:15.093934448Z
         END_TIME:
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/82724960-7d92-4961-aa2c-a0f0be46212c
         STATE: ACTIVE
         START_TIME: 2023-07-27T00:56:14.903007626Z
         END_TIME:
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/598126fb-37f9-45bc-91d8-aea7d795d702
         STATE: ACTIVE
         START_TIME: 2023-07-27T00:56:14.698260524Z
         END_TIME:
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/d2e9960b-f93f-4df4-a594-3e7e5c2be53f
         STATE: ACTIVE
         START_TIME: 2023-07-27T00:56:14.503818840Z
         END_TIME: 




You have created and deployed a workflow that invokes 100 iterations of the child workflow.

## Execute the parent workflow with rate limits

Apply a rate limit of one dispatch per second to the Cloud Tasks queue and then execute the parent workflow.

### Console

  1. In the Google Cloud console, go to the **Cloud Tasks** page:

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click **queue-workflow-child** , the Cloud Tasks queue you created, and click **Edit queue**.

  3. In the **Rate limits for task dispatches** section, for the **Max dispatches** field, type **1**.

  4. Click **Save**.

  5. Go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  6. Click the **workflow-parent** workflow to go to its details page.

  7. On the **Workflow details** page, click _play_arrow_ **Execute**.

  8. Click **Execute** again.

  9. As the parent workflow is running, return to the **Workflows** page, and click the **workflow-child** workflow to go to its details page.

  10. Click the **Executions** tab.

You should see executions of the child workflow, running at one request per second, similar to the following:

![Details of the child workflow executing at request per second.](https://docs.cloud.google.com/static/workflows/images/workflow-execution-with-rate-limits.png)



### gcloud

  1. Update the Cloud Tasks queue to apply a rate limit of one dispatch per second:
         
         gcloud tasks queues update $QUEUE \
             --max-dispatches-per-second=1 \
             --location=us-central1

  2. Execute the workflow:
         
         gcloud workflows run workflow-parent \
            --location=us-central1

  3. To verify that a workflow execution was triggered, list the last four executions:
         
         gcloud workflows executions list workflow-child --limit=4

The results should be similar to the following, with one workflow executed per second: 
         
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/becf4957-9fb2-40d9-835d-0ff2dd0c1249
         STATE: ACTIVE
         START_TIME: 2023-07-27T01:07:24.446361457Z
         END_TIME:
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/6c1e7c4b-7ac6-4121-b351-1e2d56d10903
         STATE: ACTIVE
         START_TIME: 2023-07-27T01:07:23.448213989Z
         END_TIME:
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/f2ba5027-af40-4cd3-8cd0-b8033bcc6211
         STATE: ACTIVE
         START_TIME: 2023-07-27T01:07:22.431485914Z
         END_TIME:
         NAME: projects/620278351741/locations/us-central1/workflows/workflow-child/executions/ecc61ee5-fe87-49eb-8803-89dba929f6c8
         STATE: ACTIVE
         START_TIME: 2023-07-27T01:07:21.443466369Z
         END_TIME: 




You have successfully deployed a workflow that invokes 100 iterations of the child workflow with a dispatch rate of one execution per second.

## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

Delete the workflows and Cloud Tasks resources created in this tutorial:

### Console

  * To delete the workflows, follow these steps:

    1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

    2. From the list of workflows, click a workflow to go to its **Workflow details** page.

    3. Click delete**Delete**.

    4. Type the name of the workflow and then click **Confirm**.

  * To delete the Cloud Tasks queue, follow these steps:

    1. In the Google Cloud console, go to the **Cloud Tasks** page:

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

    2. Select the name of the queue you want to delete and click **Delete queue**.

    3. Confirm the action.




### gcloud

  * To delete the workflows, run these commands: 
        
        gcloud workflows delete workflow-child
        gcloud workflows delete workflow-parent

  * To delete the Cloud Tasks queue, run this command: 
        
        gcloud tasks queues delete queue-workflow-child




## What's next

  * To learn more about how to use Cloud Tasks to queue a workflow and execute it asynchronously, see [Queue workflow executions using Cloud Tasks](https://docs.cloud.google.com/workflows/docs/create-http-task).
  * To learn more about the Workflows syntax, see the [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
