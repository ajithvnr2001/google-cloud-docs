---
url: https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers/
title: Create triggers from Pub/Sub events \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:36.733689+00:00
---

# Create triggers from Pub/Sub events  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Create triggers from Pub/Sub events Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Run, you can trigger services in response to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) messages using Eventarc. When you specify a Pub/Sub trigger for your service, you also specify a Pub/Sub topic. As a result of this trigger, your service is called whenever you publish a message to the specified topic.

The [Google Events](https://github.com/googleapis/google-cloudevents) repository contains additional resources for working with event data.

## Before you begin

  1. Make sure you have set up a new project for Cloud Run as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.

  2. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, Eventarc, Cloud Logging, and Pub/Sub APIs:

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,run.googleapis.com,eventarc.googleapis.com,logging.googleapis.com,pubsub.googleapis.com)

  3. [Grant the required IAM roles and permissions](https://docs.cloud.google.com/eventarc/docs/roles-permissions).




#### Required roles for the deployer account

To get the permissions that you need to trigger from Pub/Sub events, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)
  * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).

## Create a trigger for services

After deploying a service, you can configure a trigger using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

  1. Deploy your Cloud Run service using [containers](https://docs.cloud.google.com/run/docs/deploying) or from [source](https://docs.cloud.google.com/run/docs/deploying-source-code).

  2. In the Google Cloud console, go to **Cloud Run** :

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  3. From the list of services, click an existing service.

  4. On the Service details page, navigate to the **Triggers** tab.

  5. Click add **Add trigger** , and select **Pub/Sub trigger**.

  6. In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. In the **Trigger name** field, enter a name for the trigger, or use the default name.

     2. Select a **Trigger type** from the list to specify one of the following trigger types:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Pub/Sub** from the **Event provider** list, to select a product that provides the type of event for triggering your service. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **google.cloud.pubsub.topic.v1.messagePublished** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. From the **Select a Cloud Pub/Sub topic** topic field, choose a topic for the trigger to monitor. Messages you publish to this topic trigger calls to your function. 

     6. If the **Region** field is enabled, select a [location](https://docs.cloud.google.com/eventarc/docs/overview#trigger-location) for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your service in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     7. In the **Service account** field, select a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your service. Your Eventarc trigger's service account must have the permission to invoke your service. By default, Cloud Run uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

     8. Optionally, specify the **Service URL path** to send the incoming request to. This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, and `route/subroute`.

     9. Optionally, to enable retries if the delivery attempt fails, select the **Enable retry on failure** checkbox; otherwise, the default behavior is a single delivery attempt with no retries. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).

     10. Once you've completed the required fields, click **Save trigger**.

  7. After creating the trigger, verify its health by ensuring that there is a checkmark _check_circle_ on the **Triggers** tab.

**Note:** Although a trigger is created immediately, it can take up to two minutes for a trigger to propagate and filter events.



###  gcloud 

  1. Deploy your Cloud Run service using [containers](https://docs.cloud.google.com/run/docs/deploying) or from [source](https://docs.cloud.google.com/run/docs/deploying-source-code).

  2. Run the following command to create a trigger that filters and routes events:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=LOCATION \
             --destination-run-service=DESTINATION_RUN_SERVICE  \
             --destination-run-region=DESTINATION_RUN_REGION \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --transport-topic=projects/PROJECT_ID/topics/TOPIC_ID \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `DESTINATION_RUN_SERVICE`: the name of the Cloud Run service that receives the events for the trigger. The service can be in any of the Cloud Run supported locations and doesn't need to be in the same location as the trigger. However, the service must be in the same project as the trigger and will receive events as HTTP POST requests sent to its root URL path (`/`), whenever the event is generated. 
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run service can be found. If not specified, it is assumed that the service is in the same region as the trigger. 
     * The `--event-filters="type=google.cloud.pubsub.topic.v1.messagePublished"` flag is required and can't be changed. For a different event type, you must create a new trigger.
     * `TOPIC_ID`: the ID of the existing Pub/Sub topic. The topic must be in the same project as the trigger.
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 



###  Terraform 

To create an Eventarc trigger for a Cloud Run service, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

## Create a trigger for functions

After deploying a function, you can configure a trigger using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

When you use the Google Cloud console to create a function, you can also add a trigger to your function. Follow these steps to create a trigger for your function:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Write a function** , and enter the function details. For more information about configuring functions during deployment, see [Deploy functions](https://docs.cloud.google.com/run/docs/deploy-functions#console).

  3. In the **Trigger** section, click **Add trigger**.

  4. Select **Pub/Sub trigger**.

  5. In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. Enter a name for the trigger in the **Trigger name** field, or use the default name.

     2. Select a **Trigger type** from the list:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Pub/Sub** from the **Event provider** list, to select a product that provides the type of event for triggering your function. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **google.cloud.pubsub.topic.v1.messagePublished** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. From the **Select a Cloud Pub/Sub topic** topic field, choose a topic for the trigger to monitor. Messages you publish to this topic trigger calls to your function. 

     6. If the **Region** field is enabled, select a [location](https://docs.cloud.google.com/eventarc/docs/overview#trigger-location) for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     7. In the **Service account** field, select a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

     8. Optionally, specify the **Service URL path** to send the incoming request to. This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, and `route/subroute`.

     9. Optionally, to enable retries if the delivery attempt fails, select the **Enable retry on failure** checkbox; otherwise, the default behavior is a single delivery attempt with no retries. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).

  6. Once you've completed the required fields, click **Save trigger**.

  7. Click **Create**.

  8. In the **Source** tab, edit the source code if needed, then select **Save and redeploy**.




###  gcloud 

When you create a function using the gcloud CLI, you must first [deploy](https://docs.cloud.google.com/run/docs/deploy-functions) your function, and then create a trigger. Follow these steps to create a trigger for your function:

  1. Run the following command in the directory that contains the sample code to deploy your function:
         
         gcloud run deploy FUNCTION \
             --source . \
             --function FUNCTION_ENTRYPOINT \
             --base-image BASE_IMAGE_ID \
             --region REGION
         

Replace the following:

     * `FUNCTION`: the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

     * `FUNCTION_ENTRYPOINT`: the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

     * `BASE_IMAGE_ID`: the base image environment for your function. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

     * `REGION`: the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

  2. Run the following command to create a trigger that filters and routes events:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=LOCATION \
             --destination-run-service=FUNCTION  \
             --destination-run-region=DESTINATION_RUN_REGION \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --transport-topic=projects/PROJECT_ID/topics/TOPIC_ID \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `FUNCTION`: the name of the deployed Cloud Run function that receives the events for the trigger. 
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run function can be found. If not specified, it is assumed that the function is in the same region as the trigger. 
     * The `--event-filters="type=google.cloud.pubsub.topic.v1.messagePublished"` flag is required and can't be changed. For a different event type, you must create a new trigger.
     * `TOPIC_ID`: the ID of the existing Pub/Sub topic. The topic must be in the same project as the trigger.
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 



###  Terraform 

To create an Eventarc trigger for a Cloud Run function, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

## Next steps

  * Learn how to [trigger with events](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events).
  * Learn how to [trigger services from Pub/Sub](https://docs.cloud.google.com/run/docs/tutorials/pubsub).
  * Learn how to [configure retries](https://docs.cloud.google.com/run/docs/tips/function-retries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
