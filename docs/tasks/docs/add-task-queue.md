---
url: https://docs.cloud.google.com/tasks/docs/add-task-queue/
title: Quickstart: Add an HTTP target task to a Cloud Tasks queue \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:37.746175+00:00
---

# Quickstart: Add an HTTP target task to a Cloud Tasks queue  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/add-task-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add an HTTP target task to a Cloud Tasks queue

Cloud Tasks lets you dispatch asynchronous tasks to HTTP targets while controlling execution rates and retry behavior. In this quickstart, you use the Cloud Tasks API to create a queue and add an [HTTP target task](https://docs.cloud.google.com/tasks/docs/dual-overview#http) to that queue.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
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

  7. Enable the Cloud Tasks API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudtasks.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/cloudtasks.admin, roles/logging.viewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud Tasks API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudtasks.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/cloudtasks.admin, roles/logging.viewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Create a Cloud Tasks queue

Use the [`gcloud tasks queues create`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/create) command to create your queue.

**Caution:** Using Cloud Tasks `gcloud` queue management methods carries some risk if used together with methods based on uploading `queue.yaml/queue.xml`. For more information, see [Use Queue Management or queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml).

  1. In your terminal, create a queue that logs all operations.
         
         gcloud tasks queues create QUEUE_NAME \
             --log-sampling-ratio=1.0 \
             --location=REGION
         

Replace the following:

     * `QUEUE_NAME`: a name for your Cloud Tasks queue
     * `REGION`: the [supported region](https://docs.cloud.google.com/tasks/docs/locations) you deployed your service or app in
  2. Wait for the queue to initialize and then verify that it was created successfully.
         
         gcloud tasks queues describe QUEUE_NAME \
             --location=REGION
         

The output should be similar to the following:
         
         name: projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_NAME
          rateLimits:
            maxBurstSize: 100
            maxConcurrentDispatches: 1000
            maxDispatchesPerSecond: 500.0
          retryConfig:
            maxAttempts: 100
            maxBackoff: 3600s
            maxDoublings: 16
            minBackoff: 0.100s
          state: RUNNING
         




## Add a task to the Cloud Tasks queue

Use the [`gcloud tasks create-http-task`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/create-http-task) command to create a task that targets an HTTP endpoint and add the task to your queue.

  1. Create a task, add it to the queue you created, and deliver that task to an HTTP endpoint.
         
         gcloud tasks create-http-task \
             --queue=QUEUE_NAME \
             --url=URL_PATH \
             --method=GET \
             --location=REGION \
             --project=PROJECT_ID
         

Replace `URL_PATH` with the full URL path that the request will be sent to. The path must begin with either `http://` or `https://`—for example: `https://www.example.com`.

**Note:** To target a Cloud Run service or function, use its [default `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url).
  2. Verify that the task was executed successfully by reading the logs.
         
         gcloud logging read 'resource.type="cloud_tasks_queue" resource.labels.queue_id="QUEUE_NAME" severity>=DEFAULT' --limit=3
         

The logs should look similar to the following:
         
         jsonPayload:
         '@type': type.googleapis.com/google.cloud.tasks.logging.v1.TaskActivityLog
         task: projects/PROJECT_ID/locations/REGION/queues/QUEUE_NAME/tasks/TASK_ID
         taskCreationLog:
            scheduleTime: '2024-07-04T19:00:27.801837Z'
            status: OK
            targetAddress: GET https://www.example.com/
            targetType: HTTP
         ...
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

Alternatively, you can delete the Cloud Tasks queue:
    
    
    gcloud tasks queues delete QUEUE_NAME \
        --location=REGION
    

## What's next

  * [Manage queues and tasks](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks)
  * [Create Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues)
  * [RPC API reference](https://docs.cloud.google.com/tasks/docs/reference/rpc)
  * [REST API reference](https://docs.cloud.google.com/tasks/docs/reference/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
