---
url: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-google-api-source/
title: Quickstart: Publish events from a Google source \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:47.853318+00:00
---

# Quickstart: Publish events from a Google source  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-google-api-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish events from a Google source

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

Eventarc Advanced lets you route events from Google Cloud services across your architecture. This helps you trigger automated downstream processing whenever resource changes occur.

In this quickstart, you use the gcloud CLI to set up message routing with an Eventarc Advanced bus and enrollment:

  * A _bus_ acts as a central router, receiving messages from event sources or published by providers.

  * An _enrollment_ routes messages received by the bus to one or more destinations through a processing _pipeline_.




During the process, you:

  1. Deploy an event receiver service to Cloud Run.
  2. Create an Eventarc Advanced bus.
  3. Enable events from Google sources.
  4. Create an Eventarc Advanced enrollment.
  5. Publish an event message to the bus by creating a workflow.
  6. View the event data in the Cloud Run logs.



For more information, see [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources).

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

  7. Enable the Artifact Registry, Cloud Build, Cloud Run, Eventarc, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com eventarcpublishing.googleapis.com run.googleapis.com workflows.googleapis.com

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

  13. Enable the Artifact Registry, Cloud Build, Cloud Run, Eventarc, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com eventarcpublishing.googleapis.com run.googleapis.com workflows.googleapis.com

  14. Update `gcloud` components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login

  16. Set the configuration variable used in this quickstart: 
         
         REGION=REGION

Replace `REGION` with a [supported location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) for the bus—for example, `us-central1`.

  17. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads).

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
     * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Eventarc Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.developer) (`roles/eventarc.developer`)
     * [Eventarc Message Bus Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusAdmin) (`roles/eventarc.messageBusAdmin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Workflows Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.editor) (`roles/workflows.editor`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  18. For testing purposes, create a service account, and grant it the roles necessary to complete this quickstart. 
     1. Create a service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for your service account. 
     2. Grant the roles necessary to build and deploy a container image, and to represent the identity of an Eventarc Advanced pipeline: 
        * [Artifact Registry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer): to upload Artifact Registry artifacts
        * [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter): to write logs to Cloud Logging
        * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin): to access Cloud Storage objects
        * [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker): to call Cloud Run
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
        --role=roles/artifactregistry.writer
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
        --role=roles/logging.logWriter
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
        --role=roles/storage.admin
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
        --role=roles/run.invoker

Note that you can configure who can access your Cloud Run service in either of the following ways:

     * Grant permission to select service accounts or groups to allow access to the service. All requests must have an HTTP Authorization header containing an OpenID Connect token signed by Google for one of the authorized service accounts. This is the way that access is configured in this quickstart.
     * Grant permission to [`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#all-users) to allow unauthenticated access.

For more information, see [Access control for Cloud Run](https://docs.cloud.google.com/run/docs/securing/security#access-control). 




## Deploy an event receiver service to Cloud Run

Deploy a [Cloud Run service](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) as an event destination that logs the contents of an event. Other event destinations are supported such as a Pub/Sub topic, Workflows, or an HTTP endpoint. For more information, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/advanced/docs/event-providers-targets).

  1. Create an [Artifact Registry standard repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) to store your container image.
         
         gcloud artifacts repositories create REPOSITORY \
             --repository-format=docker \
             --location=$REGION

Replace `REPOSITORY` with a unique name for the Artifact Registry repository—for example, `my-repo`.

  2. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/eventarc-samples.git

  3. Change to the directory that contains the Cloud Run sample code:
         
         cd eventarc-samples/eventarc-advanced-quickstart/

  4. Build a Docker container image and push the image to your repository:
         
         gcloud builds submit \
             --tag $REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/log-events:v1 \
             --service-account=projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --default-buckets-behavior=regional-user-owned-bucket

  5. Deploy the container image to Cloud Run:
         
         gcloud run deploy SERVICE_NAME \
             --image $REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/log-events:v1 \
             --platform managed \
             --ingress all \
             --no-allow-unauthenticated \
             --region=$REGION

Replace `SERVICE_NAME` with the name of your service—for example, `my-service`.

Note the following:

     * The `--platform` flag sets the target platform, in this case a fully managed version of Cloud Run.

     * The ingress setting of `all` allows all requests, including requests directly from the internet to the `run.app` URL. For more information, see [Restrict network ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress).

     * The `--no-allow-unauthenticated` flag configures the service to only allow authenticated invocations.

     * When you see the Cloud Run service URL, the deployment is complete.

  6. Copy and save the Cloud Run service URL as you will use it in a subsequent step.




## Create an Eventarc Advanced bus

A bus receives event messages from a message source or published by a provider and acts as a message router.

For more information, see [Create a bus to route messages](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus).

**Note:** You can create one bus per Google Cloud project per [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

Create an Eventarc Advanced bus in your project by using the [`gcloud eventarc message-buses create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/create) command:
    
    
    gcloud eventarc message-buses create BUS_NAME \
        --location=$REGION

Replace `BUS_NAME` with the ID of your bus or a fully qualified name—for example, `my-bus`.

## Enable events from Google sources

To publish events from Google sources, you must create a [`GoogleApiSource`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources#resource:-googleapisource) resource. This resource represents a subscription to Google API events for a particular Eventarc Advanced bus in a specific Google Cloud project and region.

Enable events from Google sources by using the [`gcloud eventarc google-api-sources create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/create) command:
    
    
    gcloud eventarc google-api-sources create GOOGLE_API_SOURCE_NAME \
        --destination-message-bus=BUS_NAME \
        --destination-message-bus-project=PROJECT_ID \
        --location=$REGION

Replace `GOOGLE_API_SOURCE_NAME` with the ID of your `GoogleApiSource` resource or a fully qualified name—for example, `my-google-api-source`.

All [supported Google event types](https://docs.cloud.google.com/eventarc/advanced/docs/event-types#advanced-events) sent directly from a Google source are now collected and published to your bus.

## Create an Eventarc Advanced enrollment

An enrollment determines which messages are routed to a destination and it also specifies the pipeline that is used to configure a destination for the event messages.

For more information, see [Create an enrollment to receive events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment).

**Note:** Creating a pipeline might take more than 10 minutes.

When using the gcloud CLI, you first create a pipeline, and then create an enrollment:

  1. Create a pipeline by using the [`gcloud eventarc pipelines create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/create) command:
         
         gcloud eventarc pipelines create PIPELINE_NAME \
             --destinations=http_endpoint_uri='CLOUD_RUN_SERVICE_URL',google_oidc_authentication_service_account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --location=$REGION

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name—for example, `my-pipeline`.
     * `CLOUD_RUN_SERVICE_URL`: the fully qualified URL of your Cloud Run service—for example, `https://SERVICE_NAME-abcdef-uc.a.run.app`. This is the destination for your event messages.

Note that the `google_oidc_authentication_service_account` key specifies a service account email which is used to generate an [OIDC token](https://developers.google.com/identity/protocols/OpenIDConnect).

  2. Create an enrollment by using the [`gcloud eventarc enrollments create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/create) command:
         
         gcloud eventarc enrollments create ENROLLMENT_NAME \
             --cel-match=MATCH_EXPRESSION \
             --destination-pipeline=PIPELINE_NAME \
             --message-bus=BUS_NAME \
             --message-bus-project=PROJECT_ID \
             --location=$REGION

Replace the following:

     * `ENROLLMENT_NAME`: the ID of the enrollment or a fully qualified name—for example, `my-enrollment`.
     * `MATCH_EXPRESSION`: the matching expression for this enrollment [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel)—for example, to publish event messages whenever a Workflows workflow is created, use the following expression:
           
           "message.type == 'google.cloud.workflows.workflow.v1.created'"
           




## Publish an event message to the bus by creating a workflow

[Workflows](https://docs.cloud.google.com/workflows/docs/overview) is a fully managed orchestration platform that executes services in an order that you define: a _workflow_. Create a workflow to generate a [supported event type](https://docs.cloud.google.com/eventarc/advanced/docs/event-types#advanced-events) from a Google source.

  1. In your home directory, create a new file called `myWorkflow.yaml`.

  2. Copy and paste the following workflow into the new file, then save it:
         
         - getCurrentTime:
             call: http.get
             args:
               url: https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam
             result: currentTime
         - readWikipedia:
             call: http.get
             args:
               url: https://en.wikipedia.org/w/api.php
               query:
                 action: opensearch
                 search: ${currentTime.body.dayOfWeek}
             result: wikiResult
         - returnResult:
             return: ${wikiResult.body[1]}
         

This workflow passes the current day of the week as a search term to the [Wikipedia API](https://wikipedia.org/w/api.php). A list of related Wikipedia articles is returned.

  3. Deploy the workflow and associate it with the specified service account by using the [`gcloud workflows deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy) command:
         
         gcloud workflows deploy myWorkflow --source=myWorkflow.yaml \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --location=$REGION




## View the event data in the Cloud Run logs

After publishing an event to your Eventarc Advanced bus, you can check the logs of your Cloud Run service to verify that the event was received as expected.

  1. Filter the log entries and return the output by using the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command:
         
         gcloud logging read 'textPayload: "google.cloud.workflows.workflow.v1.created"'
         

  2. Look for a log entry similar to the following:
         
         insertId: 689644c30004cde066603b3a
         labels:
           instanceId: 0069c7a98846e3b870396a63478212b9642512ef362b67c33090846e10498949c671ccfefbc66f4f093796406e9a714bebc6fbb82f321578134ef95e56f9e9986c3265d2820b56f7994617ba7172ab
         logName: projects/PROJECT_ID/logs/run.googleapis.com%2Fstderr
         receiveTimestamp: '2025-08-08T18:41:07.632226222Z'
         resource:
           labels:
           ...
           type: cloud_run_revision
         textPayload: 'Ce-Type: google.cloud.workflows.workflow.v1.created'
         timestamp: '2025-08-08T18:41:07.314848Z'
         

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command.



You have successfully created an Eventarc Advanced bus and enrollment, enabled the publishing of events from Google sources, created a workflow to generate a supported event type from a Google provider, and then verified the expected outcome in the logs of the event receiver service.

## Clean up

When you finish the tasks that are described in this quickstart, you can avoid continued billing by deleting the resources that you created:

  1. [Delete an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos).

  2. [Delete a Cloud Run service](https://docs.cloud.google.com/run/docs/managing/services#delete).

  3. [Delete a Workflows workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#delete-workflow).

  4. Delete Eventarc Advanced resources:

     1. [Delete an enrollment](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#delete-enrollment).

     2. [Delete a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#delete-pipeline).

     3. [Delete a bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus#delete-bus).




Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
