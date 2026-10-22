---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/cal/
title: Receive a Cloud Audit Logs event \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:49.229159+00:00
---

# Receive a Cloud Audit Logs event  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/cal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Receive a Cloud Audit Logs event Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This tutorial shows you how to deploy an _authenticated_ Cloud Run service that receives events from Cloud Storage using Cloud Audit Logs. Use this tutorial to deploy production workloads. The Eventarc trigger filters events based on Cloud Audit Logs entries. For more information, see [Determine event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal).

**Note:** All Cloud Run services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request. For projects with [ domain restricted sharing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), use an authenticated Cloud Run target service rather than one that allows [public access](https://docs.cloud.google.com/run/docs/authenticating/public). 

You can complete this tutorial using either the Google Cloud console or the Google Cloud CLI.

## Objectives

In this tutorial, you will:

  1. Create a Cloud Storage bucket to be the event source.

  2. Deploy an event receiver service to Cloud Run.

  3. Create an Eventarc trigger.

  4. Generate an event by uploading a file to the Cloud Storage bucket, and view it in the Cloud Run logs.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Cloud Logging](https://docs.cloud.google.com/logging)
  * [Cloud Run](https://docs.cloud.google.com/run)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Eventarc](https://docs.cloud.google.com/eventarc)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

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

Complete the following steps using the Google Cloud console or the gcloud CLI:

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry, Cloud Build, Logging, Pub/Sub, Cloud Run, Cloud Storage, and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com,pubsub.googleapis.com,run.googleapis.com,storage.googleapis.com,andeventarc.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Artifact Registry, Cloud Build, Logging, Pub/Sub, Cloud Run, Cloud Storage, and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com,pubsub.googleapis.com,run.googleapis.com,storage.googleapis.com,andeventarc.googleapis.com&redirect=https%3A//console.cloud.google.com)

  8. To configure what data access is recorded in your audit logs, enable the **Admin Read** , **Data Read** , and **Data Write** log types for **Google Cloud Storage** : 

[Go to Audit Logs](https://console.cloud.google.com/iam-admin/audit)

  9. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts)

  10. Click **Create service account**. 
  11. Enter a service account name to display in the Google Cloud console. 

The Google Cloud console generates a service account ID based on this name. Edit the ID if necessary. You cannot change the ID later. 

  12. Optional: Enter a description of the service account. 
  13. If you don't want to set access controls now, click **Done** to finish creating the service account. 

To set access controls now, click **Create and continue** and continue to the next step. 

  14. Select the [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) and [ Eventarc Event Receiver](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) roles to grant on the project to the service account associated with your Eventarc trigger. 

For testing purposes, this grants the Cloud Run Invoker role on all Cloud Run services and jobs in the project; however, you can grant the role on the service. For more information, see [Grant Cloud Run service permissions](https://docs.cloud.google.com/eventarc/docs/roles-permissions#invoker-role). 

Note that if you create a trigger for an authenticated Cloud Run service without granting the Cloud Run Invoker role, the trigger is created successfully and is active. However, the trigger won't work as expected and a message similar to the following appears in the logs:

`The request was not authenticated. Either allow public access or set the proper Authorization header.`
  15. When you are done adding roles, click **Continue** and **Done** to finish creating the service account. 



### gcloud

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

  7. Enable the Artifact Registry, Cloud Build, Logging, Pub/Sub, Cloud Run, Cloud Storage, and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com 
               logging.googleapis.com  pubsub.googleapis.com  run.googleapis.com 
               storage.googleapis.com  and eventarc.googleapis.com

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

  13. Enable the Artifact Registry, Cloud Build, Logging, Pub/Sub, Cloud Run, Cloud Storage, and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com 
               logging.googleapis.com  pubsub.googleapis.com  run.googleapis.com 
               storage.googleapis.com  and eventarc.googleapis.com

  14. Update `gcloud` components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login
         

  16. Set the configuration variables used in this tutorial: 
         
         export REGION=us-central1
         gcloud config set run/region ${REGION}
         gcloud config set run/platform managed
         gcloud config set eventarc/location ${REGION}
         export SERVICE_NAME=helloworld-events

  17. To configure what data access is recorded in your audit logs, enable the `ADMIN_READ`, `DATA_READ`, and `DATA_WRITE` log types for the `storage.googleapis.com` service: 
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
  18. Create a service account for the project: 
         
         gcloud iam service-accounts create sample-service-account \
             --description="A sample service account" \
             --display-name="Sample service account"

After you create a service account, it can take up to seven minutes before you can use the service account. If you try to use a service account immediately after you create it, and you receive an error, wait at least 60 seconds and try again. 
  19. To confirm that `sample-service-account` has been created, run: 
         
         gcloud iam service-accounts list

The output should be similar to the following: 
         
         DISPLAY NAME                     EMAIL                                                               DISABLED
         Default compute service account  PROJECT_NUMBER-compute@developer.gserviceaccount.com                False
         Sample service account           sample-service-account@PROJECT_ID.iam.gserviceaccount.com           False

  20. Grant the [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`run.invoker`) and the [ Eventarc Event Receiver](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) roles on the project to the service account associated with your Eventarc trigger: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:sample-service-account@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/run.invoker"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:sample-service-account@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/eventarc.eventReceiver"

Replace `PROJECT_ID` with your Google Cloud project ID.

For testing purposes, this grants the Cloud Run Invoker role on all Cloud Run services and jobs in the project; however, you can grant the role on the service. For more information, see [Grant Cloud Run service permissions](https://docs.cloud.google.com/eventarc/docs/roles-permissions#invoker-role). 

Note that if you create a trigger for an authenticated Cloud Run service without granting the Cloud Run Invoker role, the trigger is created successfully and is active. However, the trigger won't work as expected and a message similar to the following appears in the logs:

`The request was not authenticated. Either allow public access or set the proper Authorization header.`
**Note:** If you enabled the Pub/Sub service account on or before April 8, 2021, grant the [ `iam.serviceAccountTokenCreator`](https://docs.cloud.google.com/pubsub/docs/push#setting_up_for_push_authentication) role to the Pub/Sub service account. 


## Create an Artifact Registry standard repository

Create an Artifact Registry standard repository to store your container image. 

### Console

  1. In the Google Cloud console, go to the **Repositories** page.  


[Go to Repositories](https://console.cloud.google.com/artifacts)

  2. Click add **Create repository**.
  3. Configure your repository: 
     1. Enter a unique **Name**.
     2. For **Format** , choose **Docker**.
     3. For **Mode** , choose **Standard**.
     4. For **Location type** , choose **Region**.
     5. In the **Region** list, select **us-central1 (Iowa)**.
  4. Accept the other defaults and click **Create**.



### gcloud
    
    
    gcloud artifacts repositories create REPOSITORY \
        --repository-format=docker \
        --location=$REGION

Replace `REPOSITORY` with a unique name for the Artifact Registry repository.

## Create a Cloud Storage bucket

This tutorial uses Cloud Storage as the event source. To create a storage bucket:

### Console

  1. In the Google Cloud console, go to the **Buckets** page.   


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add **Create bucket**.
  3. Enter your bucket information and click **Continue** to complete each step: 
     1. Enter a unique **Name**. For example, `eventarcbucket`.
     2. Select **Region** as the **Location Type**.
     3. Select **us-central1 (Iowa)** as the **Location**.
     4. Select **Standard** for **default storage class**.
     5. Select **Uniform** for **Access control**.
  4. Click **Create**.



### gcloud
    
    
    gcloud storage buckets create gs://events-tutorial-PROJECT_ID/ --location=$REGION

After the event source is created, you can deploy the event receiver service on Cloud Run. 

## Deploy the event receiver service to Cloud Run

Deploy a Cloud Run service that receives and logs events. To deploy the sample event receiver service:

### Console

  1. Clone the sample repository to your GitHub account:

### Go

     1. On GitHub, navigate to [GoogleCloudPlatform/golang-samples](https://github.com/GoogleCloudPlatform/golang-samples)
     2. Click **Fork**.
![Screenshot of the Fork button.](https://docs.cloud.google.com/static/run/docs/images/fork-repo.png)
     3. If prompted, select the location where you want to fork the repository.

### Java

     1. On GitHub, navigate to [GoogleCloudPlatform/java-docs-samples](https://github.com/GoogleCloudPlatform/java-docs-samples).
     2. Click **Fork**.
![Screenshot of the Fork button.](https://docs.cloud.google.com/static/run/docs/images/fork-repo.png)
     3. If prompted, select the location where you want to fork the repository.

### .NET

     1. On GitHub, navigate to [GoogleCloudPlatform/dotnet-docs-samples](https://github.com/GoogleCloudPlatform/dotnet-docs-samples).
     2. Click **Fork**.
![Screenshot of the Fork button.](https://docs.cloud.google.com/static/run/docs/images/fork-repo.png)
     3. If prompted, select the location where you want to fork the repository.

### Node.js

     1. On GitHub, navigate to [GoogleCloudPlatform/nodejs-docs-samples](https://github.com/GoogleCloudPlatform/nodejs-docs-samples).
     2. Click **Fork**.
![Screenshot of the Fork button.](https://docs.cloud.google.com/static/run/docs/images/fork-repo.png)
     3. If prompted, select the location where you want to fork the repository.

### Python

     1. On GitHub, navigate to [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples).
     2. Click **Fork**.
![Screenshot of the Fork button.](https://docs.cloud.google.com/static/run/docs/images/fork-repo.png)
     3. If prompted, select the location where you want to fork the repository.
  2. In the Google Cloud console, go to the **Services** page.

[Go to Services](https://console.cloud.google.com/run)

  3. Click add **Create service** to display the **Create service** form.
  4. Select **Continuously deploy from a repository**. 

Changes to your GitHub repository are automatically built into container images in Artifact Registry and deployed to Cloud Run.

  5. Click **Set up with Cloud Build** to open the **Set up with Cloud Build** form.
     1. If prompted, enable the **Cloud Build API** and **Artifact Analysis API**.
     2. Select **GitHub** as the **Repository Provider**. **Note:** If you are not yet authenticated, click **Authenticate** and follow the instructions to connect to your repository using the Cloud Build GitHub app. 
     3. If prompted, click **Install Google Cloud Build**.
     4. Select the GitHub repository you forked as the **Repository**.
     5. Click **Next**.
     6. In the **Branch** field, enter `^main$`.
     7. Select **Dockerfile** as the **Build Type** and provide the source location of the Dockerfile: 
        * `eventarc/audit-storage/Dockerfile`

or

        * `eventarc/audit_storage/Dockerfile`(Go)
     8. Click **Save**.
  6. In the **Create service** form, enter a service name. For example, `helloworld-events`.
  7. Select **us-central1(Iowa)** as the **Region** where you want your service located.
  8. Select any of the **Ingress** options based on the [ingress traffic](https://docs.cloud.google.com/run/docs/securing/ingress#settings) you want to allow on the Cloud Run service.
  9. Select **Require authentication**
  10. Click **Create**.



### gcloud

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
         
         gcloud builds submit --tag $REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/$SERVICE_NAME:v1
         

  3. Deploy the container image to Cloud Run: 
         
         gcloud run deploy $SERVICE_NAME \
             --image $REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/$SERVICE_NAME:v1
         

**Note:** Based on the required level of network access to the Cloud Run service, you can also set the [ingress flag](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--ingress). 

At the prompt to allow unauthenticated invocations, enter `n`.

When the deployment succeeds, the command line displays the service URL.




Now that you have deployed your event receiver service called `helloworld-events` to Cloud Run, you can set up your trigger. 

## Create an Eventarc trigger

The Eventarc trigger will send events from the Cloud Storage bucket to the `helloworld-events` Cloud Run service.

### Console

  1. In the Google Cloud console, go to the **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**.
  3. Type a **Trigger name**. 

This is the ID of the trigger and it must start with a letter. It can contain up to 63 lowercase letters, numbers, or hyphens.

  4. Select a **Trigger type** : 
     * **First-party** : Filters events sent from Google Cloud providers (directly or through Cloud Audit Logs entries) or providers using Pub/Sub messages.
     * **Third-party** : Filters events sent from third-party providers.
  5. In the **Event provider** list, select **Cloud Storage** as the source of events.
  6. In the **Event type** list, select **storage.objects.create**.
  7. In the **Region** list, select **us-central1** as the region to receive events from.
  8. Select the **Service account** you created. For example, `SERVICE_ACCOUNT_ID@PROJECT_ID`.iam.gserviceaccount.com.
  9. In the **Event destination** list, select **Cloud Run**.
  10. In the **Select a Cloud Run service** list, select **helloworld-events**.
  11. Click **Create**.
Note that you can also create an Eventarc trigger [ using the Cloud Run console page](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events#trigger-console). 


### gcloud

  1. Create a trigger that filters Cloud Storage events and that uses the service account you created: 
         
         gcloud eventarc triggers create events-tutorial-trigger \
             --destination-run-service=$SERVICE_NAME \
             --destination-run-region=$REGION \
             --event-filters="type=google.cloud.audit.log.v1.written" \
             --event-filters="serviceName=storage.googleapis.com" \
             --event-filters="methodName=storage.objects.create" \
             --service-account=sample-service-account@PROJECT_ID.iam.gserviceaccount.com

Replace `PROJECT_ID` with the Google Cloud project ID. 

Where:

     * `type`: specifies that audit logs are created when the trigger's filter criteria is met.
     * `serviceName`: the service that writes the audit log, which is Cloud Storage.
     * `methodName`: the operation that is being audited, which is `storage.objects.create`.
This creates a trigger called `events-tutorial-trigger`. 
  2. To confirm `events-tutorial-trigger` was successfully created, run: 
         
         gcloud eventarc triggers list --location=$REGION

The trigger, `events-tutorial-trigger`, is listed with a target of `helloworld-events`. 
**Note:** Although your trigger is created immediately, it can take up to two minutes for triggers to be fully functional. 

## Generate and view an event 

  1. To generate an event: 

### Console

     1. Create a text file with the filename `random.txt` and the text "Hello World".
     2. In the Google Cloud console, go to the **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     3. Select the storage bucket you created.
     4. In the **Objects** tab, click **Upload files** and upload the `random.txt` file.

### gcloud

Upload a text file to Cloud Storage:
    
    echo "Hello World" > random.txt
    gcloud storage cp random.txt gs://events-tutorial-PROJECT_ID/random.txt

  2. To view the log entry:

### Console

     1. In the Google Cloud console, go to the **Services** page. 

[Go to Services](https://console.cloud.google.com/run)

     2. From the list of services, click the name of the service you created to go to its **Service details** page.
     3. Click the **Logs** tab, to get the request and container logs for all revisions of this service. You can filter by log severity level.
     4. Look for a log entry similar to: 
            
            Detected change in Cloud Storage bucket: storage.googleapis.com/projects/_/buckets/BUCKET_NAME/objects/random.txt

where `BUCKET_NAME` is the name of the Cloud Storage bucket.

### gcloud

     1. gcloud logging read "resource.labels.service_name=helloworld-events AND textPayload:random.txt" --format=json

     2. Look for a log entry similar to: 
            
            Detected change in Cloud Storage bucket: storage.googleapis.com/projects/_/buckets/BUCKET_NAME/objects/random.txt

where `BUCKET_NAME` is the name of the Cloud Storage bucket. **Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command. The trigger can take up to two minutes after creation to start filtering events. 



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

  * [Build containers](https://docs.cloud.google.com/run/docs/building/containers)
  * [Create a trigger to route Cloud Audit Logs events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Develop Cloud Run services](https://docs.cloud.google.com/run/docs/developing)
  * [Receive Pub/Sub events using an authenticated Cloud Run service](https://docs.cloud.google.com/eventarc/standard/docs/run/pubsub-authenticated)
  * [Tutorial: Debug a Cloud Run service using Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/run/debugging-events-cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
