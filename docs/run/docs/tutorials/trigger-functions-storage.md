---
url: https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage/
title: Trigger functions from Cloud Storage using Eventarc \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:08.697236+00:00
---

# Trigger functions from Cloud Storage using Eventarc  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Trigger functions from Cloud Storage using Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy an event-driven function in Cloud Run, and use Eventarc to trigger the function in response to Cloud Storage events using the Google Cloud CLI.

By specifying filters for an Eventarc trigger, you can configure the routing of events, including the event source and the event target. For the example in this tutorial, an update to a Cloud Storage bucket triggers the event, and a request is sent to your function in the form of an of HTTP request.

## Objectives

In this tutorial, you will:

  1. Create a Cloud Storage bucket to be the event source.
  2. Deploy an event-driven function.
  3. Create an Eventarc trigger.
  4. Trigger the function by uploading a file to Cloud Storage.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Eventarc](https://docs.cloud.google.com/eventarc)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

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

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. If you are not using Cloud Shell, update the Google Cloud CLI components and log in using your account: 
         
         gcloud components update
         gcloud auth login

  13. Enable the APIs: 
         
         gcloud services enable artifactregistry.googleapis.com \
             cloudbuild.googleapis.com \
             eventarc.googleapis.com \
             run.googleapis.com \
             storage.googleapis.com

  14. Set the configuration variables to use in this tutorial: 
         
         export REGION=us-central1
         gcloud config set run/region ${REGION}
         gcloud config set run/platform managed
         gcloud config set eventarc/location ${REGION}

  15. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).




### Set required roles

You or your administrator must grant the deployer account, the trigger identity, and optionally, the Pub/Sub service agent and the Cloud Storage service agent the following IAM roles.

#### Required roles for the deployer account

  1. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).




#### Required roles for the trigger identity

  1. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. By default, Cloud Run services are only callable by Project Owners, Project Editors, and Cloud Run Admins and Invokers. You can [control access on a per-service basis](https://docs.cloud.google.com/run/docs/securing/managing-access#control-service-or-job-access); however, for testing purposes, grant the [Cloud Run Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`run.invoker`) on the Google Cloud project to the Compute Engine service account. This grants the role on all Cloud Run services and jobs in a project. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/run.invoker

Note that if you create a trigger for an authenticated Cloud Run service without granting the Cloud Run Invoker role, the trigger is created successfully and is active. However, the trigger will not work as expected and a message similar to the following appears in the logs:

`The request was not authenticated. Either allow public access or set the proper Authorization header.`
  3. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the Compute Engine default service account so that the Eventarc trigger can receive events from event providers. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/eventarc.eventReceiver




#### Optional role for the Cloud Storage service agent

  * Before creating a trigger for direct events from Cloud Storage, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) to the Cloud Storage service agent: 
        
        SERVICE_ACCOUNT="$(gcloud storage service-agent --project=PROJECT_ID)"
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:${SERVICE_ACCOUNT}" \
            --role='roles/pubsub.publisher'




#### Optional role for the Pub/Sub service agent

  * If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
            --role=roles/iam.serviceAccountTokenCreator




## Create a Cloud Storage bucket

Create a Cloud Storage bucket to use as the event source:
    
    
    gcloud storage buckets create -l us-central1 gs://PROJECT_ID-bucket/

**Note:** The Cloud Storage bucket must reside in the same Google Cloud project and [region or multi-region](https://docs.cloud.google.com/eventarc/docs/locations) as the Eventarc trigger.

## Write an event-driven function

To write an event-driven function, follow these steps:

###  Node.js 

  1. Create a new directory named `helloGCS` and change directory into it:
         
         mkdir helloGCS
            cd helloGCS
         

  2. Create a `package.json` file in the `helloGCS` directory to specify Node.js dependencies:
         
         {
           "name": "nodejs-docs-samples-functions-v2-storage",
           "version": "0.0.1",
           "private": true,
           "license": "Apache-2.0",
           "author": "Google LLC",
           "repository": {
             "type": "git",
             "url": "https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git"
           },
           "engines": {
             "node": ">=20.0.0"
           },
           "scripts": {
             "test": "c8 mocha -p -j 2 test/*.test.js --timeout=60000"
           },
           "dependencies": {
             "@google-cloud/functions-framework": "^5.0.0"
           },
           "devDependencies": {
             "c8": "^12.0.0",
             "mocha": "^10.0.0",
             "sinon": "^18.0.0",
             "supertest": "^7.0.0"
           }
         }
         

  3. Create an `index.js` file in the `helloGCS` directory with the following Node.js sample:
         
         const functions = require('@google-cloud/functions-framework');
         
         // Register a CloudEvent callback with the Functions Framework that will
         // be triggered by Cloud Storage.
         functions.cloudEvent('helloGCS', cloudEvent => {
           console.log(`Event ID: ${cloudEvent.id}`);
           console.log(`Event Type: ${cloudEvent.type}`);
         
           const file = cloudEvent.data;
           console.log(`Bucket: ${file.bucket}`);
           console.log(`File: ${file.name}`);
           console.log(`Metageneration: ${file.metageneration}`);
           console.log(`Created: ${file.timeCreated}`);
           console.log(`Updated: ${file.updated}`);
         });




###  Python 

  1. Create a new directory named `helloGCS` and change directory into it:
         
         mkdir helloGCS
            cd helloGCS
         

  2. Create a `requirements.txt` file in the `helloGCS` directory, to specify Python dependencies:
         
         functions-framework==3.9.2
         cloudevents==1.11.0

This adds packages needed by the sample.

  3. Create a `main.py` file in the `helloGCS` directory with the following Python sample:
         
         from cloudevents.http import CloudEvent
         
         import functions_framework
         
         
         # Triggered by a change in a storage bucket
         @functions_framework.cloud_event
         def hello_gcs(cloud_event: CloudEvent) -> tuple:
             """This function is triggered by a change in a storage bucket.
         
             Args:
                 cloud_event: The CloudEvent that triggered this function.
             Returns:
                 The event ID, event type, bucket, name, metageneration, and timeCreated.
             """
             data = cloud_event.data
         
             event_id = cloud_event["id"]
             event_type = cloud_event["type"]
         
             bucket = data["bucket"]
             name = data["name"]
             metageneration = data["metageneration"]
             timeCreated = data["timeCreated"]
             updated = data["updated"]
         
             print(f"Event ID: {event_id}")
             print(f"Event type: {event_type}")
             print(f"Bucket: {bucket}")
             print(f"File: {name}")
             print(f"Metageneration: {metageneration}")
             print(f"Created: {timeCreated}")
             print(f"Updated: {updated}")
         
             return event_id, event_type, bucket, name, metageneration, timeCreated, updated
         
         




## Deploy an event-driven function

Deploy the function named `helloworld-events` by running the following command in the directory that contains the sample code:

###  Node.js 
    
    
    gcloud run deploy helloworld-events \
          --source . \
          --function helloGCS \
          --base-image BASE_IMAGE \
          --region us-central1
    

Replace BASE_IMAGE with the base image environment for your function, for example, `nodejs24`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

###  Python 
    
    
    gcloud run deploy helloworld-events \
          --source . \
          --function hello_gcs \
          --base-image BASE_IMAGE \
          --region us-central1
    

Replace BASE_IMAGE with the base image environment for your function, for example, `python314`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

When the deployment is complete, the Google Cloud CLI displays a URL where your service is running.

## Create an Eventarc trigger

The Eventarc trigger sends events from the Cloud Storage bucket to your `helloworld-events` Cloud Run service.

  1. Create a trigger that filters Cloud Storage events:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=${REGION} \
             --destination-run-service=helloworld-events  \
             --destination-run-region=${REGION} \
             --event-filters="type=google.cloud.storage.object.v1.finalized" \
             --event-filters="bucket=PROJECT_ID-bucket" \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace:

     * TRIGGER_NAME with the name for your trigger.
     * PROJECT_ID with your Google Cloud project ID.
     * PROJECT_NUMBER with your Google Cloud project number.

Note that when creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).

  2. Confirm that the trigger was successfully created. Note that although your trigger is created immediately, it can take up to two minutes for a trigger to be fully functional.
         
         gcloud eventarc triggers list --location=${REGION}

The output should be similar to the following:
         
         NAME: helloworld-events
         TYPE: google.cloud.storage.object.v1.finalized
         DESTINATION: Cloud Run service: helloworld-events
         ACTIVE: Yes
         LOCATION: us-central1
         




## Generate and view an event

Upload a text file to the Cloud Storage bucket to generate an event which is routed to the function. The Cloud Run function logs the event in the service logs.

  1. Upload a text file to Cloud Storage, to generate an event:
         
         echo "Hello World" > random.txt
          gcloud storage cp random.txt gs://PROJECT_ID-bucket/random.txt
         

The upload generates an event and the Cloud Run function logs the event's message.

  2. To view the log entry:

     1. Filter the log entries and return the output in JSON format:
            
            gcloud logging read "resource.labels.service_name=helloworld-events AND textPayload:random.txt" --format=json
            

     2. Look for a log entry similar to:
            
            [
              {
               ....
                "resource": {
                  "labels": {
                    ....
                    "location": "us-central1",
                    .....
                    "service_name": "helloworld-events"
                  },
                },
                "textPayload": "File: random.txt",
                 .....
              }
            ]
            

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command. The trigger can take up to two minutes after being created to start filtering events.

Logs might take a few moments to appear. If you don't see them immediately, check again after a minute.




After you see the log entry, this confirms that you have successfully deployed an event-driven function that was triggered when a text file was uploaded to Cloud Storage.

**Success:** You deployed an event-driven function in Cloud Run and used Eventarc to trigger the function in response to Cloud Storage events.

## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and want to keep it without the changes added in this tutorial, delete the resources created for the tutorial.

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

  1. Delete the Cloud Run service you deployed in this tutorial:
         
         gcloud run services delete SERVICE_NAME

Where `SERVICE_NAME` is your chosen service name.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove any gcloud CLI default configurations you added during the tutorial setup.

For example:

`gcloud config unset run/region`

or

`gcloud config unset project`

  3. Delete other Google Cloud resources created in this tutorial:

     * Delete the Eventarc trigger: 
           
           gcloud eventarc triggers delete TRIGGER_NAME
           

Replace `TRIGGER_NAME` with the name of your trigger.



## What's next

  * [Create Eventarc triggers for other event types](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events)
  * [Manage functions](https://docs.cloud.google.com/run/docs/managing/services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
