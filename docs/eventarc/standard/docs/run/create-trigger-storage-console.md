---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-storage-console/
title: Receive direct events from Cloud Storage (Google Cloud console) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:11.627837+00:00
---

# Receive direct events from Cloud Storage (Google Cloud console)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-storage-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Receive direct events from Cloud Storage (Google Cloud console)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This quickstart shows you how to receive direct events from Cloud Storage in a Cloud Run service that allows public access.

**Note:** All Cloud Run services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request. For projects with [ domain restricted sharing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), use an authenticated Cloud Run target service rather than one that allows [public access](https://docs.cloud.google.com/run/docs/authenticating/public). 

You can configure the triggering of notifications in response to various events inside a Cloud Storage bucket—object creation, deletion, archiving, and metadata updates. For more information, see [Create a trigger to route Cloud Storage events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-storage).

You can complete this quickstart using the Google Cloud console. For instructions using the Google Cloud CLI, see [Receive direct events from Cloud Storage (gcloud CLI)](https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-storage-gcloud).

In this quickstart, you: 

  1. Create a Cloud Storage bucket to be an event source.

  2. Deploy a sample service to Cloud Run to receive events.

  3. Create an Eventarc trigger to filter and route events.

  4. Generate an event by uploading a file to the Cloud Storage bucket, and view the event in the Cloud Run logs.




* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=eventarc--quickstart-console)

* * *

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud Build and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,eventarc.googleapis.com,eventarcpublishing.googleapis.com&redirect=https%3A//cloud.google.com/eventarc/docs/run/create-trigger-storage-console)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud Build and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,eventarc.googleapis.com,eventarcpublishing.googleapis.com&redirect=https%3A//cloud.google.com/eventarc/docs/run/create-trigger-storage-console)




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud Storage bucket

This quickstart uses Cloud Storage as the event source. 

  1. In the Google Cloud console, go to the **Cloud Storage** > **Overview** page.

[Go to Overview](https://console.cloud.google.com/storage/overview)

  2. Click add_box **Create bucket**.

  3. Enter a unique **Name** for your bucket.

For example, `hello-bucket`.

  4. Click **Continue**.

  5. For **Location type** , select **Region** , and then select **us-central1 (Iowa)**.

  6. Accept the other defaults.

  7. Click **Create**.




After the event source is created, you can deploy the event receiver service to Cloud Run. 

## Deploy the event receiver service to Cloud Run

Deploy a sample Cloud Run service that receives and logs events.

  1. In the Google Cloud console, go to the **Cloud Run** > **Services** page.

[Go to Services](https://console.cloud.google.com/run/services)

  2. Click add_box **Deploy container**.

  3. In the **Create service** form:

     1. Select **Deploy one revision from an existing container image**.

     2. Click **Test with a sample container**.

     3. In the **Region** list, for the location of your service, select **us-central1 (Iowa)**.

     4. For **Authentication** , select **Allow public access**.

     5. Accept the other defaults.

     6. To deploy the sample container image, click **Create**.




The deployment of the `hello` service can take up to two minutes to complete.

## Create an Eventarc trigger

The Eventarc trigger will send events from the Cloud Storage bucket to the sample Cloud Run service. 

  1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**.

  3. Type a **Trigger name**.

For example, `hello-trigger`.

  4. In the **Trigger type** list, select **Google sources**.

This filters events sent from Google Cloud providers (directly or through Cloud Audit Logs entries), or providers using Pub/Sub messages.

  5. In the **Event provider** list, select **Cloud Storage**.

  6. In the **Event type** list, select **Direct** > **google.cloud.storage.object.v1.finalized**.

  7. For **Bucket** , select the **hello-bucket** Cloud Storage bucket you created previously.

  8. If prompted, grant the following roles:

     * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the Pub/Sub service account
     * [Eventarc Event Receiver](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) to the default compute service account
     * [Pub/Sub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) to the Cloud Storage service account
  9. Use the **Default compute service account** as the service account that invokes your service.

  10. In the **Event destination** list, select **Cloud Run**.

  11. For the **Cloud Run service** , select the sample **hello** service you created previously.

  12. Accept the other defaults.

  13. Click **Create**.




It might take a few minutes before all necessary permissions are propagated to the Eventarc service agent. If you receive a `Permission denied while using the Eventarc Service Agent` error, wait a few minutes, and then try again. Once a trigger is created, it can take up to two minutes for a trigger to be fully functional.

## Generate and view an event

Generate an event and confirm that the Eventarc trigger is working as expected.

  1. To generate an event:

     1. Create a text file with the filename `random.txt` and the text "Hello World".

     2. In the Google Cloud console, go to the **Cloud Storage** > **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     3. Click the name of the storage bucket you created.

     4. In the **Objects** tab, click **Upload files** and upload the `random.txt` file.

The upload generates an event and the Cloud Run service logs the event's message.

  2. To view the log entry:

     1. In the Google Cloud console, go to the **Cloud Run** > **Services** page.

[Go to Services](https://console.cloud.google.com/run/services)

     2. Click the name of the service you created.

     3. To retrieve the log entries for all revisions of this service, in the **Service details** page, click the **Logs** tab. You can filter by log severity level.

     4. Look for a log entry similar to:
            
            Received event of type google.cloud.storage.object.v1.finalized. Event data: [...]




Congratulations! You have successfully deployed an event receiver service to Cloud Run, created an Eventarc trigger, generated an event from Cloud Storage, and viewed it in the Cloud Run logs.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

While Cloud Run does not charge when the service is not in use, you might still be charged for the following: 

  * [Storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
  * [Cloud Run resources](https://cloud.google.com/run/pricing)
  * [Storing files in your Cloud Storage bucket](https://cloud.google.com/storage/pricing)



You can [delete your image](https://docs.cloud.google.com/container-registry/docs/managing#deleting_images), [delete your storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets), and [delete your Cloud Run service](https://docs.cloud.google.com/run/docs/managing/services#delete).

To delete the Eventarc trigger:

  1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click the name of the trigger you created.

  3. On the **Triggers details** page, click delete **Delete**.




Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Receive a Cloud Audit Logs event for production workloads](https://docs.cloud.google.com/eventarc/standard/docs/run/cal).
  * [Execute a Cloud Run job in a workflow using an Eventarc trigger](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs).
  * [Developing your service](https://docs.cloud.google.com/run/docs/developing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
