---
url: https://docs.cloud.google.com/scheduler/docs/start-and-stop-sql-server-instances-on-a-schedule/
title: Schedule a Cloud SQL instance to start or stop \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:47.456167+00:00
---

# Schedule a Cloud SQL instance to start or stop  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/start-and-stop-sql-server-instances-on-a-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Schedule a Cloud SQL instance to start or stop Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Scheduler to start and stop Cloud SQL instances on a regular schedule. For example, you might want your instances to run only during certain hours.

This tutorial demonstrates how to automatically start and stop a Cloud SQL for SQL Server instance by building an event-driven architecture using Google Cloud products.

**Note:** Google Cloud products are supported in specific [regions](https://cloud.google.com/about/locations#regional-products). For this application, no product needs to be deployed in the same region as any other. However, locating your products in the same region improves latency.

## Objectives

In this tutorial, you will create Cloud Scheduler jobs that schedule Cloud SQL instances with an `env=dev` resource label to run during specific hours. You will schedule only one instance. However, the architecture described in this tutorial can be used to stop and start multiple instances where the resource label is `env=dev`.

To accomplish this objective, complete the following steps:

  1. Create a [Cloud SQL for SQL Server instance](https://docs.cloud.google.com/sql/docs/sqlserver/features) and assign it a specific [resource label](https://docs.cloud.google.com/resource-manager/docs/labels-overview) (`env=dev`).
  2. Create two [Pub/Sub topics](https://docs.cloud.google.com/pubsub/docs/overview) to act as event sources for your Eventarc triggers, and as message brokers.
  3. Create and deploy two event-driven [Cloud Run functions](https://docs.cloud.google.com/run/docs/functions/overview) triggered through the Pub/Sub topics. When triggered, the functions search for Cloud SQL instances in your project that match the label provided in the Pub/Sub message payload (`env=dev`).
  4. Create and deploy two [Eventarc triggers](https://docs.cloud.google.com/eventarc/standard/docs/overview). Pub/Sub topic events are routed to your functions as HTTP requests, and the event message content is passed as input data to the functions.
  5. Create two [Cloud Scheduler cron jobs](https://docs.cloud.google.com/scheduler/docs/creating) to publish a message containing the target label to the Pub/Sub topics at specific times. Schedule the instances to start at 9:00 AM and stop at 5:00 PM, Monday through Friday.



The following diagram provides an overview of the event-driven architecture:

[ ![Starting and stopping Cloud SQL instances on a schedule](https://docs.cloud.google.com/static/scheduler/docs/images/start-stop-sql-server-instances.svg)](https://docs.cloud.google.com/static/scheduler/docs/images/start-stop-sql-server-instances.svg) Starting and stopping Cloud SQL instances on a schedule (click diagram to enlarge).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Cloud Run functions](https://cloud.google.com/run/pricing)

Cloud Run functions operate as Cloud Run services and are billed accordingly.

  * [ Cloud Scheduler](https://cloud.google.com/scheduler/pricing)
  * [ Cloud SQL for SQL Server](https://cloud.google.com/sql/pricing#sql-server-pricing-1)
  * [ Eventarc](https://cloud.google.com/eventarc/pricing)

Cloud Run uses Eventarc for event delivery. Pricing for Eventarc is not included in the Cloud Run pricing.

  * [ Pub/Sub](https://cloud.google.com/pubsub/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Build, Cloud Functions, Cloud Pub/Sub, Cloud Run Admin, Cloud Scheduler, Cloud SQL Admin, and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudbuild.googleapis.com cloudfunctions.googleapis.com pubsub.googleapis.com run.googleapis.com cloudscheduler.googleapis.com sqladmin.googleapis.com eventarc.googleapis.com

  9. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/cloudbuild.builds.builder, roles/cloudsql.editor, roles/run.invoker`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  14. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  15. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  16. Enable the Cloud Build, Cloud Functions, Cloud Pub/Sub, Cloud Run Admin, Cloud Scheduler, Cloud SQL Admin, and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudbuild.googleapis.com cloudfunctions.googleapis.com pubsub.googleapis.com run.googleapis.com cloudscheduler.googleapis.com sqladmin.googleapis.com eventarc.googleapis.com

  17. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/cloudbuild.builds.builder, roles/cloudsql.editor, roles/run.invoker`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 




## Create a Cloud SQL instance

To create a Cloud SQL for SQL Server instance with the resource label `env=dev`, use the [`gcloud beta sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create) command:
    
    
    gcloud beta sql instances create dev-instance \
        --database-version=SQLSERVER_2019_EXPRESS \
        --region=us-west1 \
        --tier=db-custom-2-3840 \
        --root-password=YourStrongPassword123! \
        --labels=env=dev

It might take a few minutes to create the instance. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

## Create Pub/Sub topics

To create the two Pub/Sub topics that act as event sources for your Eventarc triggers, use the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
    
    
    gcloud pubsub topics create start-instance-event
    gcloud pubsub topics create stop-instance-event

For more information, see [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).

## Create and deploy Cloud Run functions

Create and deploy two Cloud Run (Node.js) functions triggered by Eventarc through Pub/Sub topics. When triggered, the functions search for Cloud SQL instances in your project that match the label provided in the Pub/Sub message payload (`env=dev`):

  * The start function updates the `activationPolicy` of the instance to `ALWAYS`, which turns the instance on.
  * The stop function updates the `activationPolicy` to `NEVER`, which shuts the instance down.



For more information, see [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions) and [Cloud Run function triggers](https://docs.cloud.google.com/run/docs/function-triggers).

### Create the functions

Create event-driven Cloud Run functions that automatically unmarshal events conforming to the [CloudEvents](https://cloudevents.io/) specification. This industry-standard specification describes event data in a common way.

Your source code must define a function entry point, which is the code that runs when Cloud Run invokes your function. You specify this entry point when you deploy your function.

  1. Download the code.
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/main.zip) as a zip file and extract it. 

  2. Go to the correct directory.
         
         cd nodejs-docs-samples/functions/scheduleinstance/




### Deploy the event-driven functions

To deploy the functions on Cloud Run, use the [`gcloud run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) command.

  1. Deploy the function that starts the Cloud SQL instance:
         
         gcloud run deploy startinstance \
             --source . \
             --function startInstanceEvent \
             --base-image nodejs24 \
             --region=us-west1 \
             --build-service-account=projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

  2. If you are prompted to create a repository in the specified region, type `y`.

  3. At the `Allow unauthenticated invocations` prompt, type `n`.

  4. Deploy the function that shuts down the Cloud SQL instance:
         
         gcloud run deploy stopinstance \
             --source . \
             --function stopInstanceEvent \
             --base-image nodejs24 \
             --region=us-west1 \
             --build-service-account=projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

  5. If you are prompted to create a repository in the specified region, type `y`.

  6. At the `Allow unauthenticated invocations` prompt, type `n`.




When the deployment is complete, the Google Cloud CLI displays a URL where the service is running.

### Create Eventarc triggers

To create Eventarc triggers that route events from Pub/Sub, use the [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create) command. Every message published to the Pub/Sub topic triggers the corresponding function and the message content is passed as input data.

  1. Create a trigger that starts the Cloud SQL instance:
         
         gcloud eventarc triggers create start-instance-trigger \
             --location=us-west1 \
             --destination-run-service=startinstance \
             --destination-run-region=us-west1 \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --transport-topic=start-instance-event \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

  2. Create a trigger that stops the Cloud SQL instance:
         
         gcloud eventarc triggers create stop-instance-trigger \
             --location=us-west1 \
             --destination-run-service=stopinstance \
             --destination-run-region=us-west1 \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --transport-topic=stop-instance-event \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com




It can take up to 2 minutes for a new trigger to become active.

### Optional: Verify that the functions work

You can verify that your functions work by directly publishing messages to the Pub/Sub topics. It might take a few minutes to update the Cloud SQL instance.

  1. To stop instances with the label `env=dev`, use the [`gcloud pubsub topics publish`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish) command to publish a message to the stop topic:
         
         gcloud pubsub topics publish stop-instance-event --message='{"label":"env=dev"}'

  2. To confirm that the instance has stopped, check its activation policy by using the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe dev-instance --format="value(settings.activationPolicy)"

The output should be `NEVER`.

  3. To start instances with the label `env=dev`, publish a message to the start topic:
         
         gcloud pubsub topics publish start-instance-event --message='{"label":"env=dev"}'

  4. Confirm that the instance has started by checking its activation policy:
         
         gcloud sql instances describe dev-instance --format="value(settings.activationPolicy)"

The output should be `ALWAYS`.




## Create the Cloud Scheduler jobs

Create Cloud Scheduler jobs that publish messages to the Pub/Sub topics on a regular schedule.

  1. To create a job that runs at 9:00 AM, Monday to Friday, and which starts the instances, use the [`gcloud scheduler jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create) command:
         
         gcloud scheduler jobs create pubsub startup-dev-instances \
             --schedule '0 9 * * 1-5' \
             --topic start-instance-event \
             --message-body '{"label":"env=dev"}' \
             --time-zone 'America/Los_Angeles' \
             --location us-east1

  2. Create a job that runs at 5:00 PM, Monday to Friday, and which stops the instances:
         
         gcloud scheduler jobs create pubsub shutdown-dev-instances \
             --schedule '0 17 * * 1-5' \
             --topic stop-instance-event \
             --message-body '{"label":"env=dev"}' \
             --time-zone 'America/Los_Angeles' \
             --location us-east1




Due to some initial configuration, the first job created in a project can take a few minutes to run.

### Optional: Verify that the jobs work

You can manually run your Cloud Scheduler jobs to verify that they successfully trigger the start and stop functions. It might take a few minutes to update the Cloud SQL instance.

  1. To run the job and stop the Cloud SQL instance, use the [`gcloud scheduler jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run) command:
         
         gcloud scheduler jobs run shutdown-dev-instances --location="us-east1"

  2. Verify that the activation policy of `dev-instance` is `NEVER`:
         
         gcloud sql instances describe dev-instance --format="value(settings.activationPolicy)"

  3. Run the job to start the instance:
         
         gcloud scheduler jobs run startup-dev-instances --location="us-east1"

  4. Verify that the activation policy of `dev-instance` is `ALWAYS`:
         
         gcloud sql instances describe dev-instance --format="value(settings.activationPolicy)"




## Clean up

To avoid incurring charges for the resources used in this tutorial, clean up the resources by deleting them.

  1. Delete the Cloud Scheduler jobs: 
         
         gcloud scheduler jobs delete startup-dev-instances --location=us-east1 --quiet
         gcloud scheduler jobs delete shutdown-dev-instances --location=us-east1 --quiet

  2. Delete the Eventarc triggers: 
         
         gcloud eventarc triggers delete start-instance-trigger --location=us-west1 --quiet
         gcloud eventarc triggers delete stop-instance-trigger --location=us-west1 --quiet

  3. Delete the Cloud Run services: 
         
         gcloud run services delete startinstance --region=us-west1 --quiet
         gcloud run services delete stopinstance --region=us-west1 --quiet

  4. Delete the Pub/Sub topics: 
         
         gcloud pubsub topics delete start-instance-event
         gcloud pubsub topics delete stop-instance-event

  5. Delete the Cloud SQL instance: 
         
         gcloud sql instances delete dev-instance --quiet

  6. Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project. **Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
