---
url: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-cloud-run-job/
title: Quickstart: Publish events to a Cloud Run job \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:21.487959+00:00
---

# Quickstart: Publish events to a Cloud Run job  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-cloud-run-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish events to a Cloud Run job

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

This quickstart shows you how to publish and receive event messages by creating an Eventarc Advanced bus and enrollment in your Google Cloud project.

  * A _bus_ acts as a central router, receiving messages from event sources or published by providers.

  * An _enrollment_ routes messages received by the bus to one or more destinations through a processing _pipeline_.




In this quickstart, you:

  1. Deploy a Cloud Run job from source code.

  2. Create an Eventarc Advanced bus.

  3. Create an Eventarc Advanced enrollment.

  4. Publish an event message to the bus.

  5. Confirm that the Cloud Run job successfully executed.




You can complete this quickstart using the gcloud CLI.

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

  7. Enable the Artifact Registry, Cloud Build, Cloud Run and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com eventarcpublishing.googleapis.com run.googleapis.com 

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

  13. Enable the Artifact Registry, Cloud Build, Cloud Run and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com eventarcpublishing.googleapis.com run.googleapis.com 

  14. Update `gcloud` components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login

  16. Set the configuration variable used in this quickstart: 
         
         REGION=REGION

Replace `REGION` with a [supported location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) for the bus—for example, `us-central1`.

  17. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads).

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`)
     * [Eventarc Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.developer) (`roles/eventarc.developer`)
     * [Eventarc Message Bus Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusAdmin) (`roles/eventarc.messageBusAdmin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  18. To give Eventarc Advanced the necessary permissions to execute a Cloud Run job, ask your administrator to grant the [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`roles/run.invoker`) IAM role on your Google Cloud project to a service account: Note: To execute a job that overrides the job configuration (for example, by [ defining a message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding)), you must grant the **Cloud Run Developer** (`roles/run.developer`) or **Cloud Run Jobs Executor With Overrides** (`roles/run.jobsExecutorWithOverrides`) IAM role. For more information, see [Override job configuration for a specific execution](https://docs.cloud.google.com/run/docs/execute/jobs#override-job-configuration).
     1. Create a service account. For testing purposes, you will attach this service account to an Eventarc Advanced pipeline to represent the identity of the pipeline. 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for your service account. 
     2. Grant the `roles/run.invoker` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
                --role=roles/run.invoker




## Deploy a Cloud Run job from source code

Deploy a [Cloud Run job](https://docs.cloud.google.com/run/docs/create-jobs) as your event destination. Unlike a Cloud Run service, which listens for and serves requests, a Cloud Run job only runs its tasks and exits when finished. A job does not listen for or serve requests.

Other event destinations—such as a Pub/Sub topic, Workflows, or another HTTP endpoint—are supported. For more information, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/advanced/docs/event-providers-targets).

Create a job from Python source code by using the [gcloud run jobs deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/deploy) command. Your code is automatically packaged into a container image, uploaded to Artifact Registry, and then deployed to Cloud Run.

  1. Create a directory named `jobs` and navigate to it:
         
         mkdir jobs
         cd jobs
         

  2. Create a `main.py` file and copy the following sample code into it:
         
         import os
         
         TASK_INDEX = os.getenv("CLOUD_RUN_TASK_INDEX", 0)
         
         def main():
             """
             This job prints "Hello world"
             """
             print(f"Starting task #{TASK_INDEX}...")
             print("Hello world")
             print(f"Completed task #{TASK_INDEX}.")
         
         # Start script
         if __name__ == "__main__":
             main()
         

  3. Create a text file named `Procfile` with no file extension and copy the following text into it:
         
         web: python3 main.py
         

  4. Deploy the job:
         
         gcloud run jobs deploy JOB_NAME \
             --source . \
             --tasks 1 \
             --region=$REGION

Replace `JOB_NAME` with a unique name for the Cloud Run job—for example, `my-job`.




## Create an Eventarc Advanced bus

A bus receives event messages from a message source or published by a provider, and acts as a message router.

For more information, see [Create a bus to route messages](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus).

**Note:** You can create one bus per Google Cloud project per [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

Create an Eventarc Advanced bus in your project by using the [`gcloud eventarc message-buses create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/create) command:
    
    
    gcloud eventarc message-buses create BUS_NAME \
        --location=$REGION

Replace `BUS_NAME` with the ID of your bus or a fully qualified name—for example, `my-bus`.

## Create an Eventarc Advanced enrollment

An enrollment determines which messages are routed to a destination. It also specifies the pipeline used to configure the destination for the event messages. In this case, the target destination is a Cloud Run job.

For more information, see [Create an enrollment to receive events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment).

When using the gcloud CLI, you first create a pipeline, and then create an enrollment:

**Note:** Creating a pipeline might take more than 10 minutes.

  1. Create a pipeline by using the [`gcloud eventarc pipelines create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/create) command:
         
         gcloud eventarc pipelines create PIPELINE_NAME \
             --destinations=http_endpoint_uri='JOB_URI',http_endpoint_message_binding_template='{"body": ""}',oauth_token_authentication_service_account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --input-payload-format-json= \
             --location=$REGION

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name—for example, `my-pipeline`.
     * `JOB_URI`: the URI of the Cloud Run job in the following format:
           
           https://REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/PROJECT_NUMBER/jobs/JOB_NAME:run

You can retrieve your project number by running the following command:
           
           gcloud projects describe PROJECT_ID --format='value(projectNumber)'

Note the following:

     * The `http_endpoint_message_binding_template` key transforms the event into the format expected by the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/run). When defining a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding), you must configure an input format to access the payload—for example: `{"body": ""}`.
     * The `oauth_token_authentication_service_account` key specifies a service account email. This email is used to generate an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) typically used only when calling Google APIs hosted on `*.googleapis.com`.
  2. Create an enrollment by using the [`gcloud eventarc enrollments create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/create) command:
         
         gcloud eventarc enrollments create ENROLLMENT_NAME \
             --cel-match=MATCH_EXPRESSION \
             --destination-pipeline=PIPELINE_NAME \
             --message-bus=BUS_NAME \
             --message-bus-project=PROJECT_ID \
             --location=$REGION

Replace the following:

     * `ENROLLMENT_NAME`: the ID of the enrollment or a fully qualified name—for example, `my-enrollment`.
     * `MATCH_EXPRESSION`: the matching expression for this enrollment [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel)—for example:
           
           "message.type == 'hello-world-type'"
           




## Publish an event message to the bus

To directly publish a message to your bus, use the [`gcloud eventarc message-buses publish`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/publish) command or send a request to the [Eventarc Publishing REST API](https://docs.cloud.google.com/eventarc/docs/reference/publishing/rest). For more information, see [Publish events directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format).

The message must be in a CloudEvents format, a specification for describing event data in a common way. The `data` element is the payload of your event. Any well-formed JSON can go in this field. For more information about CloudEvents context attributes, see [Event format](https://docs.cloud.google.com/eventarc/advanced/docs/event-format).

The following are examples of directly publishing an event to an Eventarc Advanced bus:

### Example 1

Publish an event to a bus by using the gcloud CLI and an `--event-data` and other event attribute flags:
    
    
    gcloud eventarc message-buses publish BUS_NAME \
        --event-data='{"key": "hello-world-data"}' \
        --event-id=hello-world-id-1234 \
        --event-source=hello-world-source \
        --event-type=hello-world-type \
        --event-attributes="datacontenttype=application/json" \
        --location=$REGION
    

### Example 2

Publish an event to a bus as a JSON message by using the gcloud CLI and a `--json-message` flag:
    
    
    gcloud eventarc message-buses publish BUS_NAME \
        --location=$REGION \
        --json-message='{"id": "hello-world-id-1234", "type":
     "hello-world-type", "source":
     "hello-world-source", "specversion": "1.0", "data":
     {"key": "hello-world-data"}}'
    

After publishing an event, you should receive an "Event published successfully" message.

## Confirm that the Cloud Run job successfully executed

After publishing an event to your Eventarc Advanced bus, check the logs of your Cloud Run job to verify that the Cloud Run job successfully executed and that "Hello world" was printed. It might take a few minutes before the job runs and completes.

  1. Filter the log entries and return the output by using the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command:
         
         gcloud logging read 'textPayload: "Hello world"'
         

  2. Look for a log entry similar to the following:
         
         insertId: 693c8dd0000cb2976d7966b8
         ...
         labels:
             job_name: JOB_NAME
             location: REGION
             project_id: PROJECT_ID
         type: cloud_run_job
         textPayload: Hello world
         timestamp: '2025-12-12T21:49:04.832151Z'
         

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command.
  3. You can also confirm that the Cloud Run job executed successfully by using the [`gcloud run jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/describe) command:
         
         gcloud run jobs describe JOB_NAME \
             --region=$REGION
         

You should receive output similar to the following:
         
         ✔ Job JOB_NAME in region us-central1
         Executed 1 time
         ...
         




You have successfully created an Eventarc Advanced bus and enrollment, published an event message to the bus, and verified the expected outcome in the logs of the event receiver.

## Clean up

To help avoid continued billing after you finish this quickstart, delete the resources that you created: 

  1. [Delete a Cloud Run job](https://docs.cloud.google.com/run/docs/managing/jobs#delete).

  2. Delete Eventarc Advanced resources:

     1. [Delete an enrollment](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#delete-enrollment).

     2. [Delete a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#delete-pipeline).

     3. [Delete a bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus#delete-bus).




Alternatively, delete your Google Cloud project to help avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources)
  * [Publish events directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format)
  * [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events)
  * [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events)
  * [Troubleshoot issues](https://docs.cloud.google.com/eventarc/advanced/docs/troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
