---
url: https://docs.cloud.google.com/tasks/docs/add-task-queue-app-eng/
title: Quickstart: Add an App Engine task to a Cloud Tasks queue \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:51.701323+00:00
---

# Quickstart: Add an App Engine task to a Cloud Tasks queue  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/add-task-queue-app-eng/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add an App Engine task to a Cloud Tasks queue

Cloud Tasks lets you dispatch asynchronous tasks to App Engine services to process background workloads. In this quickstart, you use the Cloud Tasks API to create and add an [App Engine task](https://docs.cloud.google.com/tasks/docs/dual-overview#appe) to a Cloud Tasks queue.

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

  7. Enable the Cloud Resource Manager and Cloud Tasks API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com tasks.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud Resource Manager and Cloud Tasks API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com tasks.googleapis.com

  15. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  16. The [App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts#default_service_account) is automatically created when you use App Engine. You can use this service account when trying out this quickstart. However, depending on your organization policy configuration, the default service account might not automatically be granted the `Editor` role on your project. If that is the case, you must [grant the service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) the following roles: 
     1. Artifact Registry Administrator (`roles/artifactregistry.admin`)
     2. Artifact Registry Create-on-Push Writer (`roles/artifactregistry.createOnPushWriter`)
     3. Compute Admin (`roles/compute.admin`)
     4. Logs Writer (`roles/logging.logWriter`)
     5. Storage Object Viewer (`roles/storage.objectViewer`)



## Add an App Engine application

When you target an App Engine task, and before you can deploy an app to the App Engine standard environment, you must add an [App Engine application](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing) to your project.

  1. In the Google Cloud console, go to the **App Engine** page.

[Go to App Engine](https://console.cloud.google.com/appengine/start)

  2. In the **Welcome to App Engine** dialog, do one of the following:

     * If you have already created an App Engine application and there is a **Your App Engine application has been created** message displayed, you can then skip the remaining steps in this section and proceed with the steps in the Install and deploy the sample section. 

or

     * If you haven't created an App Engine application yet, then click **Create application** and continue with the remaining steps in this section.

  3. Select a [region](https://docs.cloud.google.com/appengine/docs/locations) for your application and make a note of it.

Note that `europe-west` and `us-central` are called, respectively, `europe-west1` and `us-central1` in Cloud Tasks commands.

  4. Don't select a service account; the default App Engine service account is used.

  5. Click **Next**.

The application is configured and created. This can take a couple of minutes.

  6. Don't download the Cloud SDK; instead, click **I'll do this later**.

You should see a **Your App Engine application has been created** message.




## Install and deploy the sample

The Node.js sample used in this quickstart consists of two files: `createTask.js` is run locally as a command-line tool to create and add tasks to the Tasks queue; `server.js` is deployed on App Engine as a worker service to process the task.

  1. In your terminal, clone the sample application repository to your local machine.
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git
         

  2. Navigate to the directory that contains the sample code.
         
         cd nodejs-docs-samples/cloud-tasks/snippets
         

  3. Install all dependencies using a Node.js package manager.

You can use NPM:
         
         npm install
         

Or, you can use Yarn:
         
         yarn install
         

  4. Deploy the worker service (`server.js`) to the App Engine standard environment.
         
         gcloud app deploy app.yaml
         

  5. Make sure that the app containing the service is running.
         
         gcloud app browse
         

  6. In your browser, go to the provided link. For example:
         
         https://PROJECT_ID.uc.r.appspot.com/
         

You should see `Hello, World!` displayed.




## Create a Cloud Tasks queue

Use the [`gcloud tasks queues create`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/create) command to create your queue in the environment you've prepared.

**Caution:** Using Cloud Tasks `gcloud` queue management methods carries some risk if used together with methods based on uploading `queue.yaml/queue.xml`. For more information, see [Use Queue Management or queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml).

  1. In your terminal, create a queue that logs all operations.
         
         gcloud tasks queues create QUEUE_NAME \
             --log-sampling-ratio=1.0 \
             --location=REGION
         

Replace the following:

     * `QUEUE_NAME`: a name for your Cloud Tasks queue
     * `REGION`: the region you deployed your app in
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

Create a task, add it to the queue you created, and deliver that task to the worker service.

  1. Set the following environment variables. The client uses this information to create the request.
         
         export PROJECT_ID=PROJECT_ID
         export LOCATION_ID=REGION
         export QUEUE_ID=QUEUE_NAME
         

  2. Create a task with a payload of `hello` and add that task to your queue. The payload can be any data from the request that the worker service needs to process the task.
         
         node createTask.js $PROJECT_ID $QUEUE_ID $LOCATION_ID hello
         

  3. Verify that the task was executed by displaying the logs of the worker service.
         
         gcloud app logs read
         

The logs should look similar to the following:
         
         2024-06-20 15:00:00 default[20240620t143852]  "POST /log_payload HTTP/1.1" 200
         2024-06-20 15:00:00 default[20240620t143852]  App listening on port 8081
         2024-06-20 15:00:00 default[20240620t143852]  Press Ctrl+C to quit.
         2024-06-20 15:00:00 default[20240620t143852]  Received task with payload: hello
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

Alternatively, you can delete the resources you created:

  1. Delete the Cloud Tasks queue:
         
         gcloud tasks queues delete QUEUE_NAME \
             --location=REGION
         

  2. [Disable the App Engine application](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing#disabling_an_application).




## What's next

  * [Manage queues and tasks](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks)
  * [Create Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues)
  * [RPC API reference](https://docs.cloud.google.com/tasks/docs/reference/rpc)
  * [REST API reference](https://docs.cloud.google.com/tasks/docs/reference/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
