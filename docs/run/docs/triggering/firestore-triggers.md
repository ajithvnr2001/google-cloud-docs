---
url: https://docs.cloud.google.com/run/docs/triggering/firestore-triggers/
title: Create triggers from Firestore events \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:28.651401+00:00
---

# Create triggers from Firestore events  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/firestore-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Create triggers from Firestore events Stay organized with collections  Save and categorize content based on your preferences. 

This guide covers the instructions for creating triggers for Cloud Run services and functions from Firestore events.

You can configure your Cloud Run services to be triggered by events in a Firestore database. When triggered, your service reads and updates a Firestore database in response to these events through the [Firestore APIs and client libraries](https://docs.cloud.google.com/firestore/docs/apis).

In a typical lifecycle, the following happens when a Cloud Run service is triggered by Firestore events:

  1. The service waits for changes to a particular document.

  2. When a change occurs, the service is triggered and performs its tasks.

  3. The service receives a data object with a snapshot of the affected document. For `write` or `update` events, the data object contains snapshots representing document state before and after the triggering event.




## Event types

Firestore supports `create`, `update`, `delete`, and `write` events. The `write` event encompasses all modifications to a document.

Event type | Trigger  
---|---  
`google.cloud.firestore.document.v1.created` (default) | Triggered when a document is written to for the first time.  
`google.cloud.firestore.document.v1.updated` | Triggered when a document already exists and has any value changed.  
`google.cloud.firestore.document.v1.deleted` | Triggered when a document with data is deleted.  
`google.cloud.firestore.document.v1.written` | Triggered when a document is created, updated or deleted.  
**Note:** You set triggers at the document level. It is not possible to create a trigger activated by changes to a specific field or collection.

Wildcards are written in triggers using curly braces, for example: `projects/YOUR_PROJECT_ID/databases/(default)/documents/collection/{document_wildcard}`

### Specify the document path

To trigger your service, specify a document path to listen to. The document path must be in the same Google Cloud project as the service.

Here are a few examples of valid document paths:

  * `users/marie`: valid trigger. Monitors a single document, `/users/marie`.

  * `users/{username}`: valid trigger. Monitors all user documents. Wildcards are used to monitor all documents in the collection.

  * `users/{username}/addresses`: _invalid_ trigger. Refers to the subcollection `addresses`, not a document.

  * `users/{username}/addresses/home`: valid trigger. Monitors the home address document for all users.

  * `users/{username}/addresses/{addressId}`: valid trigger. Monitors all address documents.

  * `users/{user=**}`: valid trigger. Monitors all user documents and any documents in subcollections under each user document such as `/users/userID/address/home` or `/users/userID/phone/work`.




#### Wildcards and parameters

If you don't know the specific document you want to monitor, use a `{wildcard}` instead of the document ID:

  * `users/{username}` listens for changes to all user documents.



In this example, when any field on any document in `users` is changed, it matches a wildcard called `{username}`.

If a document in `users` has [subcollections](https://docs.cloud.google.com/firestore/docs/concepts/structure-data#subcollections), and a field in one of those subcollections' documents is changed, the `{username}` wildcard is _not_ triggered. If your goal is to respond to events in subcollections also, use the multi-segment wildcard `{username=**}`.

Wildcard matches are extracted from document paths. You can define as many wildcards as you like to substitute explicit collection or document IDs. You can use up to _one_ multi-segment wildcard like `{username=**}`.

## Event structures

This trigger invokes your service with an event similar to: 
    
    
    {
        "oldValue": { // Update and Delete operations only
            A [Document](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents) object containing a pre-operation document snapshot
        },
        "updateMask": { // Update operations only
            A [DocumentMask](https://firebase.google.com/docs/firestore/reference/rest/v1/DocumentMask) object that lists changed fields.
        },
        "value": {
            // A [Document](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents) object containing a post-operation document snapshot
        }
    }

Each `Document` object contains one or more `Value` objects. See the [`Value` documentation](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/Value) for type references.

## Before you begin

  1. Make sure you have set up a new project for Cloud Run as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.
  2. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, Eventarc, Firestore Cloud Logging, and Pub/Sub APIs:

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,artifactregistry.googleapis.com,eventarc.googleapis.com,run.googleapis.com,logging.googleapis.com,pubsub.googleapis.com,firestore.googleapis.com)

  3. [Grant the required IAM roles and permissions](https://docs.cloud.google.com/eventarc/docs/roles-permissions).




#### Required roles for the deployer account

To get the permissions that you need to trigger from Firestore events, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)
  * [Datastore Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)
  * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).

## Set up your Firestore database

Before you deploy your service, you must create a Firestore database:

  1. Go to the [Firestore Data page](https://console.cloud.google.com/firestore/databases).

  2. Select **Create Database**.

  3. Click **Native Mode** , then select **Continue**.

  4. In the **Name your database** field, enter a _Database ID_ , such as `firestore-db`.

  5. In **Location type** , select **Region** and choose the region for where your database is to reside. This choice is permanent.

  6. Leave the **Secure rules** section as is.

  7. Click **Create database**.




The [Firestore data model](https://docs.cloud.google.com/firestore/docs/data-model) consists of collections that contain documents. A document contains a set of key-value pairs.

## Create triggers

Depending on the type of service you are deploying, you can either:

  * Create a trigger for services
  * Create a trigger for functions



### Create a trigger for services

After deploying a service, you can configure a trigger using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

  1. Deploy your Cloud Run service using [containers](https://docs.cloud.google.com/run/docs/deploying) or from [source](https://docs.cloud.google.com/run/docs/deploying-source-code).

  2. In the Google Cloud console, go to **Cloud Run** :

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  3. From the list of services, click an existing service.

  4. On the Service details page, navigate to the **Triggers** tab.

  5. Click add **Add trigger** , and select **Firestore trigger**.

  6. In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. In the **Trigger name** field, enter a name for the trigger, or use the default name.

     2. Select a **Trigger type** from the list to specify one of the following trigger types:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Firestore** from the **Event provider** list, to select a product that provides the type of event for triggering your service. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **type=google.cloud.firestore.document.v1.created** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. In the Filters section, select a database, operation and attribute values, or use the default selections. 

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
             --event-filters="type=EVENT_FILTER_TYPE" \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `DESTINATION_RUN_SERVICE`: the name of the Cloud Run service that receives the events for the trigger. The service can be in any of the Cloud Run supported locations and doesn't need to be in the same location as the trigger. However, the service must be in the same project as the trigger and will receive events as HTTP POST requests sent to its root URL path (`/`), whenever the event is generated. 
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run service can be found. If not specified, it is assumed that the service is in the same region as the trigger. 
     * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. For a list of supported event types, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). 
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * After a trigger is created, the event filter type can't be changed. For a different event type, you must create a new trigger. 
     * `--event-filters=type=google.cloud.firestore.document.v1.written` specifies that the function is triggered when a document is created, updated or deleted, per the [event type](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#event_types).
     * `--event-filters=database='(default)'` specifies the Firebase database. For the default database name, use `(default)`.
     * `--event-filters-path-pattern=document='users/{username}'` provides the path pattern of the documents that should be monitored for relevant changes. This path pattern states that all documents in the `users` collection should be monitored. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).
     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 



###  Terraform 

To create an Eventarc trigger for a Cloud Run service, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

### Create a trigger for functions

After deploying a function, you can configure a trigger using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

When you use the Google Cloud console to create a function, you can also add a trigger to your function. Follow these steps to create a trigger for your function:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Write a function** , and enter the function details. For more information about configuring functions during deployment, see [Deploy functions](https://docs.cloud.google.com/run/docs/deploy-functions#console).

  3. In the **Trigger** section, click **Add trigger**.

  4. Select **Firestore trigger**.

  5. In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. Enter a name for the trigger in the **Trigger name** field, or use the default name.

     2. Select a **Trigger type** from the list:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Firestore** from the **Event provider** list, to select a product that provides the type of event for triggering your function. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **type=google.cloud.firestore.document.v1.created** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. In the Filters section, select a database, operation and attribute values, or use the default selections. 

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
             --event-filters="type=EVENT_FILTER_TYPE" \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `FUNCTION`: the name of the deployed Cloud Run function that receives the events for the trigger. 
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run function can be found. If not specified, it is assumed that the function is in the same region as the trigger. 
     * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. For a list of supported event types, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). 
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * After a trigger is created, the event filter type can't be changed. For a different event type, you must create a new trigger. 
     * `--event-filters=type=google.cloud.firestore.document.v1.written` specifies that the function is triggered when a document is created, updated or deleted, per the [event type](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#event_types).
     * `--event-filters=database='(default)'` specifies the Firebase database. For the default database name, use `(default)`.
     * `--event-filters-path-pattern=document='users/{username}'` provides the path pattern of the documents that should be monitored for relevant changes. This path pattern states that all documents in the `users` collection should be monitored. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).
     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 



###  Terraform 

To create an Eventarc trigger for a Cloud Run function, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

See [Extend Firestore with event triggers using Cloud Run functions](https://docs.cloud.google.com/firestore/native/docs/extend-with-cloud-run-functions) for more information.

## What's next

  * See [examples of functions](https://docs.cloud.google.com/run/docs/triggering/trigger-functions-with-firestore-documents) that are triggered when you make changes to a document inside of a specified collection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
