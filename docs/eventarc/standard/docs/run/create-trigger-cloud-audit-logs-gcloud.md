---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-cloud-audit-logs-gcloud/
title: Quickstart: Receive events using Cloud Audit Logs (Google Cloud CLI) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:07.169088+00:00
---

# Quickstart: Receive events using Cloud Audit Logs (Google Cloud CLI)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-cloud-audit-logs-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Receive events using Cloud Audit Logs (gcloud CLI)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This quickstart shows you how to receive events from Cloud Storage in an _unauthenticated_ Cloud Run service using Eventarc.

**Note:** All Cloud Run services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request. For projects with [ domain restricted sharing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), use an authenticated Cloud Run target service rather than one that allows [public access](https://docs.cloud.google.com/run/docs/authenticating/public). 

You can complete this quickstart using the Google Cloud CLI. For instructions using the console, see [Create a trigger using the Google Cloud console](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs#console_1).

In this quickstart, you:

  1. Create a Cloud Storage bucket to be the event source.

  2. Deploy an event receiver service to Cloud Run.

  3. Create an event trigger.

  4. Generate an event by uploading a file to the Cloud Storage bucket, and view it in the Cloud Run logs.




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

  7. Enable the Artifact Registry, Cloud Build, Cloud Run, Eventarc, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com run.googleapis.com eventarc.googleapis.com pubsub.googleapis.com

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

  13. Enable the Artifact Registry, Cloud Build, Cloud Run, Eventarc, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com run.googleapis.com eventarc.googleapis.com pubsub.googleapis.com

  14. Update `gcloud` components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login

  16. Set the configuration variables used in this quickstart: 
         
         export REGION=us-central1
         gcloud config set run/region ${REGION}
         gcloud config set run/platform managed
         gcloud config set eventarc/location ${REGION}

  17. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).

#### Required permissions

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
     * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  18. Enable Cloud Audit Logs **Admin Read** , **Data Read** , and **Data Write** Log Types in Google Cloud Storage. 

Note that at the project level, you need the `[roles/owner](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles)` Identity and Access Management role to configure Data Access audit logs for your Google Cloud resources.

     1. Read your project's IAM policy and store it in a file: 
            
            gcloud projects get-iam-policy PROJECT_ID > /tmp/policy.yaml

     2. Edit your policy in `/tmp/policy.yaml`, adding or changing _only_ the Data Access audit logs configuration. **Caution:** You must preserve the `bindings:` and `etag:` sections without changes. Failure to do so might cause your project to become unusable.
            
            auditConfigs:
            - auditLogConfigs:
            - logType: ADMIN_READ
            - logType: DATA_WRITE
            - logType: DATA_READ
            service: storage.googleapis.com

     3. Write your new IAM policy: 
            
            gcloud projects set-iam-policy PROJECT_ID /tmp/policy.yaml

If the preceding command reports a conflict with another change, then repeat these steps, starting with reading the project's IAM policy. 
  19. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  20. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the Compute Engine default service account so that the Eventarc trigger can receive events from event providers. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/eventarc.eventReceiver

  21. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator

  22. [Download and install](https://git-scm.com/downloads) the Git source code management tool. 



## Create an Artifact Registry standard repository

Create an Artifact Registry standard repository to store your container image: 
    
    
    gcloud artifacts repositories create REPOSITORY \
        --repository-format=docker \
        --location=$REGION

Replace `REPOSITORY` with a unique name for the repository.

## Create a Cloud Storage bucket

This quickstart uses Cloud Storage as the event source. To create a storage bucket:
    
    
    gcloud storage buckets create gs://events-quickstart-PROJECT_ID/ --location=${REGION}

After the event source is created, you can deploy the event receiver service on Cloud Run.

## Deploy the event receiver service to Cloud Run

Deploy a Cloud Run service that receives and logs events. To deploy the sample event receiver service:

  1. Clone the GitHub repository:

### Go
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git
         cd golang-samples/eventarc/audit_storage
         

### Java
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git
         cd java-docs-samples/eventarc/audit-storage
         

### .NET
         
         git clone https://github.com/GoogleCloudPlatform/dotnet-docs-samples.git
         cd dotnet-docs-samples/eventarc/audit-storage
         

### Node.js
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git
         cd nodejs-docs-samples/eventarc/audit-storage
         

### Python
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         cd python-docs-samples/eventarc/audit-storage
         

  2. Build the container and upload it to Cloud Build:
         
         gcloud builds submit --tag $REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/helloworld-events:v1

  3. Deploy the container image to Cloud Run:
         
         gcloud run deploy helloworld-events \
             --image $REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/helloworld-events:v1 \
             --allow-unauthenticated

When the deployment succeeds, the command line displays the service URL.

Now that you have deployed your event receiver service called `helloworld-events` to Cloud Run, you can set up your trigger.




## Create an Eventarc trigger

The Eventarc trigger will send events from the Cloud Storage bucket to the `helloworld-events` Cloud Run service.

  1. Create a trigger that filters Cloud Storage events and that uses the Google Cloud project Compute Engine default service account:
         
         gcloud eventarc triggers create events-quickstart-trigger \
             --destination-run-service=helloworld-events \
             --destination-run-region=${REGION} \
             --event-filters="type=google.cloud.audit.log.v1.written" \
             --event-filters="serviceName=storage.googleapis.com" \
             --event-filters="methodName=storage.objects.create" \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com

This creates a trigger called `events-quickstart-trigger`.

Note that when creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).

  2. To confirm `events-quickstart-trigger` was successfully created, run:
         
         gcloud eventarc triggers list --location=${REGION}

The `events-quickstart-trigger` is listed with a destination that is the Cloud Run service, `helloworld-events`.


**Note:** Although your trigger is created immediately, it can take up to two minutes for triggers to be fully functional.

## Generate and view an event

  1. To generate an event, upload a text file to Cloud Storage:
         
         echo "Hello World" > random.txt
          gcloud storage cp random.txt gs://events-quickstart-PROJECT_ID/random.txt
         

The upload generates an event and the Cloud Run service logs the event's message.

  2. To view the event-related log entries created by your service, run the following command:
         
         gcloud logging read 'textPayload: "Detected change in Cloud Storage bucket"'
         

  3. Look for a log entry similar to:
         
         Detected change in Cloud Storage bucket: storage.googleapis.com/projects/_/buckets/BUCKET_NAME/objects/random.txt
         

where `BUCKET_NAME` is the name of the Cloud Storage bucket.

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command. The trigger can take up to two minutes after creation to start filtering events.



You have successfully deployed an event receiver service to Cloud Run, created an Eventarc trigger, generated an event from Cloud Storage, and viewed it in the Cloud Run logs.

## Clean up

While Cloud Run does not charge when the service is not in use, you might still be charged for [storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing), [storing files in your Cloud Storage bucket](https://cloud.google.com/storage/pricing), and [Eventarc resources](https://cloud.google.com/eventarc/pricing). 

You can:

  1. [Delete your container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

  2. [Delete your storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).

  3. [Delete the Eventarc trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#deleting_triggers).




Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Receive a Cloud Audit Logs event for production workloads](https://docs.cloud.google.com/eventarc/standard/docs/run/cal)
  * [Build containers](https://docs.cloud.google.com/run/docs/building/containers)
  * [Determine event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal)
  * [Develop Cloud Run services](https://docs.cloud.google.com/run/docs/developing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
