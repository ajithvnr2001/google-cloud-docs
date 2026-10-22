---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-pub-sub-gcloud/
title: Quickstart: Receive events using Pub/Sub messages (Google Cloud CLI) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:48.756574+00:00
---

# Quickstart: Receive events using Pub/Sub messages (Google Cloud CLI)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-pub-sub-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Receive events using Pub/Sub messages (gcloud CLI)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This quickstart shows you how to deploy an _unauthenticated_ Cloud Run service that receives events using Pub/Sub.

**Note:** All Cloud Run services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request. For projects with [ domain restricted sharing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), use an authenticated Cloud Run target service rather than one that allows [public access](https://docs.cloud.google.com/run/docs/authenticating/public). 

In this quickstart, you:

  1. Deploy an event receiver service to Cloud Run.

  2. Create an Eventarc trigger.

  3. Publish a message to a Pub/Sub topic to generate an event, and view it in the Cloud Run logs.




## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

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

  7. Enable the Cloud Run, Cloud Logging, Pub/Sub, and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable run.googleapis.com logging.googleapis.com pubsub.googleapis.com eventarc.googleapis.com

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

  13. Enable the Cloud Run, Cloud Logging, Pub/Sub, and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable run.googleapis.com logging.googleapis.com pubsub.googleapis.com eventarc.googleapis.com

  14. Update Google Cloud CLI components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login

  16. Set the configuration variables used in this quickstart: 
         
         gcloud config set run/region us-central1
         gcloud config set run/platform managed
         gcloud config set eventarc/location us-central1

  17. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  18. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
    
    gcloud projects describe PROJECT_ID --format='value(projectNumber)'




## Deploy an event receiver to Cloud Run

Deploy a Cloud Run service that will receive and log events using a prebuilt image, `us-docker.pkg.dev/cloudrun/container/hello`:
    
    
    gcloud run deploy helloworld-events-pubsub-quickstart \
        --image=us-docker.pkg.dev/cloudrun/container/hello \
        --allow-unauthenticated
    

When you see the service URL, the deployment is complete.

## Create an Eventarc trigger

The event trigger sends messages to the event receiver service deployed on Cloud Run when a message is published to the Pub/Sub topic.

  1. Create a trigger to listen for Pub/Sub messages:

### New Pub/Sub topic
         
         gcloud eventarc triggers create events-pubsub-trigger \
             --destination-run-service=helloworld-events-pubsub-quickstart \
             --destination-run-region=us-central1 \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished"
         

This creates a new Pub/Sub topic and a trigger for it called `events-pubsub-trigger`.

### Existing Pub/Sub topic
         
         gcloud eventarc triggers create events-pubsub-trigger \
             --destination-run-service=helloworld-events-pubsub-quickstart \
             --destination-run-region=us-central1 \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --transport-topic=projects/PROJECT_ID/topics/TOPIC_ID
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID
     * `TOPIC_ID`: the ID of the existing Pub/Sub topic

This creates a trigger called `events-pubsub-trigger` for the existing Pub/Sub topic.

Note that when creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).

  2. Confirm that the trigger was successfully created:
         
         gcloud eventarc triggers list --location=us-central1
         

The `events-pubsub-trigger` is listed with a destination that is the Cloud Run service, `helloworld-events-pubsub-quickstart`.


**Note:** Although your trigger is created immediately, it can take up to two minutes for triggers to be fully functional.

## Generate and view a Pub/Sub topic event

You can generate an Eventarc event by publishing a message to a Pub/Sub topic.

  1. Find and set the Pub/Sub topic as an environment variable:
         
         export RUN_TOPIC=$(gcloud eventarc triggers describe events-pubsub-trigger \
             --format='value(transport.pubsub.topic)')
         

  2. Publish a message to the Pub/Sub topic to generate an event:
         
         gcloud pubsub topics publish $RUN_TOPIC --message "Hello World!"
         

The event is routed to the Cloud Run service, which logs the event message.

  3. To view the event-related log entries created by your service, run the following command:
         
         gcloud logging read 'jsonPayload.message: "Received event of type google.cloud.pubsub.topic.v1.messagePublished"'
         

  4. Look for a log entry similar to:
         
         jsonPayload:
         ...
         message: 'Received event of type google.cloud.pubsub.topic.v1.messagePublished.
             Event data: Hello World!'
         

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command. The trigger can take up to two minutes after creation to start filtering events.



Congratulations! You have successfully deployed an event receiver service to Cloud Run, created an Eventarc trigger, generated an event from Pub/Sub, and viewed it in the Cloud Run logs.

## Clean up

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created.

You can:

  1. [Delete the Cloud Run service](https://docs.cloud.google.com/run/docs/managing/services#delete).

  2. [Delete the Eventarc trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#deleting_triggers).

This also deletes the associated Pub/Sub topic.




Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

## What's next

  * [Receive Pub/Sub events using an authenticated Cloud Run service](https://docs.cloud.google.com/eventarc/standard/docs/run/pubsub-authenticated)
  * [Build containers for Cloud Run](https://docs.cloud.google.com/run/docs/building/containers)
  * [Develop services for Cloud Run](https://docs.cloud.google.com/run/docs/developing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
