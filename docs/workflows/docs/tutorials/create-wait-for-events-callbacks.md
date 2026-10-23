---
url: https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks/
title: Wait for events using callbacks and Eventarc triggers \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:39.922057+00:00
---

# Wait for events using callbacks and Eventarc triggers  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Workflows ](https://docs.cloud.google.com/workflows)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Wait for events using callbacks and Eventarc triggers Stay organized with collections  Save and categorize content based on your preferences. 

Your workflow might need to wait for an external process. You can use [HTTP callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) to wait for another service to make a request to a callback endpoint; that request resumes the execution of the workflow. You can also [wait using polling](https://docs.cloud.google.com/workflows/docs/sleeping).

Instead of using polling, this tutorial demonstrates how you can wait for events or Pub/Sub messages using HTTP callbacks and Eventarc triggers. Although you can [trigger a workflow with events or Pub/Sub messages](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc), you might want to halt that execution to wait for another event before continuing. For example, an event triggers a workflow to initiate a process, but the workflow needs to wait for another event that signals that the process is complete. You can implement this by having one workflow call back another workflow.

## Objectives

In this tutorial, the following occurs:

  1. **A primary workflow that needs to wait on events** is deployed and executed. As it must wait for the events to occur, it stores its callback details in a Firestore database so that the secondary workflow can retrieve the details. The primary workflow then waits for the HTTP calls.

  2. **A secondary workflow is triggered by the events** and retrieves the callback details from the Firestore database when the events are generated. The secondary workflow then calls back the primary workflow which resumes its execution.




This is an overview of the entire process:

![Wait for events using callbacks and a primary and secondary workflow](https://docs.cloud.google.com/static/workflows/images/callback-events.svg)

#### Primary workflow:

  1. A `callback-event-sample` workflow creates callback endpoints for two event sources: a Pub/Sub topic and a Cloud Storage bucket.
  2. This workflow store both callback endpoints in a Firestore document.
  3. This workflow halts its execution and waits for HTTP requests to arrive at the callback endpoints.



#### Events:

  4. Events occur: a message is published to a Pub/Sub topic and a file is uploaded to a Cloud Storage bucket.



#### Secondary workflow:

  5. Eventarc route the events to the `callback-event-listener` workflow and triggers its execution.
  6. This workflow retrieves the appropriate callback endpoint URLs from the Firestore document.
  7. This workflow executes the callbacks to the appropriate endpoints in the sample workflow.



#### Primary workflow:

  8. The `callback-event-sample` workflow receives the events at the callback endpoints and resumes its execution.
  9. This workflow deletes the callback URLs from the Firestore document and completes its execution. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Eventarc](https://docs.cloud.google.com/eventarc)
  * [Firestore](https://docs.cloud.google.com/firestore)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

You can run the following commands in the Google Cloud console, or by using the Google Cloud CLI in either your terminal or Cloud Shell.

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Enable the App Engine, Eventarc, Firestore, Pub/Sub, and Workflows APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=appengine.googleapis.com,eventarc.googleapis.com,firestore.googleapis.com,pubsub.googleapis.com,workflows.googleapis.com)

  4. Create a service account for your workflow to use for authentication with other Google Cloud services and grant it the appropriate roles:

     1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. To go to the **Create service account** page, select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for tutorial`.

     4. Click **Create and continue**.

     5. In the **Select a role** list, filter for the following roles to grant to the user-managed service account you created in the previous step:

        * **Cloud Datastore User** : to access Firestore in Datastore mode (Datastore) data.
        * **Eventarc Event Receiver** : to receive events from event providers.
        * **Logs Writer** : to write logs.
        * **Workflows Invoker** : to execute workflows and manage the executions.

For additional roles, click add **Add another role** and add each additional role.

**Note:** The **Role** field affects which resources your service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs.
     6. Click **Continue**.

     7. To finish creating the account, click **Done**.

  5. To create an Eventarc trigger that routes events from Cloud Storage, grant the Pub/Sub Publisher role to the Cloud Storage service agent. Typically, this is `service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`. You can [retrieve the email address for the Cloud Storage service agent](https://docs.cloud.google.com/storage/docs/getting-service-agent#console).

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)

     2. In the row for the Cloud Storage service agent, click edit**Edit principal**. (If the service agent is not listed, proceed to the next step.) The **Edit access** pane opens.

        1. Click _add_**Add another role** and then search for the **Pub/Sub Publisher** role.
        2. Select the role.
        3. Click **Save**.
     3. If the service agent is not listed, click person_add**Grant access**. The **Grant access** pane opens.

        1. In the **New principals** field, enter the email address for the service agent.
        2. In the **Select a role** list, search for the **Pub/Sub Publisher** role.
        3. Select the role.
        4. Click **Save**.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Enable the App Engine, Eventarc, Firestore, Pub/Sub, and Workflows APIs.
         
         gcloud services enable \
             appengine.googleapis.com \
             eventarc.googleapis.com \
             firestore.googleapis.com \
             pubsub.googleapis.com \
             workflows.googleapis.com

  4. Create a service account for your workflow to use for authentication with other Google Cloud services and grant it the appropriate roles.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account.

     2. Grant roles to the user-managed service account you created in the previous step. Run the following command once for each of the following IAM roles:

        * `roles/datastore.user`: to access Firestore in Datastore mode (Datastore) data.
        * `roles/eventarc.eventReceiver`: to receive events from event providers.
        * `roles/logging.logWriter`: to write logs.
        * `roles/workflows.invoker`: to execute workflows and manage the executions.
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --role=ROLE

Replace the following:

        * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you created the service account
        * `ROLE`: the role to grant
**Note:** The `--role` flag affects which resources your service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs.
  5. To create an Eventarc trigger that routes events from Cloud Storage, grant the Pub/Sub Publisher role to the [Cloud Storage service agent](https://docs.cloud.google.com/storage/docs/getting-service-agent). Typically, this is `service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`. Use [`gcloud storage service-agent`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/service-agent) to first retrieve the Cloud Storage service agent.
         
         SERVICE_ACCOUNT_STORAGE="$(gcloud storage service-agent --project=PROJECT_ID)"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:$SERVICE_ACCOUNT_STORAGE \
             --role=roles/pubsub.publisher




## Create a Firestore database

Firestore stores your data in documents that contain fields mapping to values. These documents are stored in collections, which are containers for your documents that you can use to organize your data and build queries. [Learn more about Firestore](https://firebase.google.com/docs/firestore).

Note that each Google Cloud project is limited to one Firestore database. Complete the following steps if you need to create a new database.

###  Console 

  1. In the Google Cloud console, go to the Firestore **Get started** page.

[Go to Get started](https://console.cloud.google.com/firestore/welcome)

  2. Click **Select Native Mode**.

For guidance on selecting a database mode and for a feature-by-feature comparison, see [choosing between Native Mode and Datastore Mode](https://docs.cloud.google.com/datastore/docs/firestore-or-datastore).

  3. In the **Select a location** list, select **nam5 (United States)**.

The location applies to both the Firestore database and the App Engine application in your Google Cloud project. Once you create your database, you cannot change the location.

  4. Click **Create database**.




###  gcloud 

To create a Firestore database, you must first create an App Engine application and then run the [`gcloud firestore databases create`](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/databases/create) command:
    
    
    gcloud app create --region=us-central
    gcloud firestore databases create --region=us-central

You can ignore the `us-central is not a valid Firestore location` warning. App Engine and Firestore support the same locations, but the App Engine `us-central` (Iowa) region maps to the Firestore `nam5` (United States) multi-region.

## Create a Pub/Sub topic

This tutorial uses Pub/Sub as an event source. Create a Pub/Sub topic so that you can publish a message to it. [Learn more about creating and managing topics](https://docs.cloud.google.com/pubsub/docs/create-topic).

###  Console 

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click add_box **Create topic**.

  3. In the **Topic ID** field, enter `topic-callback`.

  4. Accept the other defaults.

  5. Click **Create topic**.




###  gcloud 

To create a topic, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
    
    
    gcloud pubsub topics create topic-callback

## Create a Cloud Storage bucket

This tutorial uses Cloud Storage as an event source. Create a Cloud Storage bucket so that you can upload a file to it. [Learn more about creating storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Cloud Storage](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.

  3. For the **Name** of your bucket, enter `PROJECT_ID-bucket-callback`.

The [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) is used in the `callback-event-sample` workflow to identify the bucket.

  4. Click **Continue**.

  5. For **Location type** , select **Region** , and then select **us-central1 (Iowa)**.

  6. Accept the other defaults.

  7. Click **Create**.




###  gcloud 

To create a bucket, run the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command:
    
    
    gcloud storage buckets create gs://PROJECT_ID-bucket-callback \
        --location=us-central1

The [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) is used in the `callback-event-sample` workflow to identify the bucket.

After the event sources are created, you can deploy the event receiver workflow.

## Deploy a workflow that listens for events

The `callback-event-listener` workflow is triggered when a message is published to a Pub/Sub topic or when a file is uploaded to a Cloud Storage bucket. The workflow receives the event, retrieves the appropriate callback details from the Firestore database, and then sends an HTTP request to the callback endpoint.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow: `callback-event-listener`.

  4. In the **Region** list, select **us-central1**.

  5. Select the **Service account** that you previously created.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
           params: [event]
           steps:
             - log_event:
                 call: sys.log
                 args:
                   text: ${event}
                   severity: INFO
             - init:
                 assign:
                   - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/callbacks/"}
                   - event_source_tokens: ${text.split(event.source, "/")}
                   - event_source_len: ${len(event_source_tokens)}
                   - event_source: ${event_source_tokens[event_source_len - 1]}
                   - doc_name: ${database_root + event_source}
             - get_document_for_event_source:
                 try:
                   call: googleapis.firestore.v1.projects.databases.documents.get
                   args:
                     name: ${doc_name}
                   result: document
                 except:
                     as: e
                     steps:
                         - known_errors:
                             switch:
                             - condition: ${e.code == 404}
                               return: ${"No callbacks for event source " + event_source}
                         - unhandled_exception:
                             raise: ${e}
             - process_callback_urls:
                 steps:
                   - check_fields_exist:
                       switch:
                       - condition: ${not("fields" in document)}
                         return: ${"No callbacks for event source " + event_source}
                       - condition: true
                         next: processFields
                   - processFields:
                       for:
                           value: key
                           in: ${keys(document.fields)}
                           steps:
                               - extract_callback_url:
                                   assign:
                                       - callback_url: ${document.fields[key]["stringValue"]}
                               - log_callback_url:
                                   call: sys.log
                                   args:
                                     text: ${"Calling back url " + callback_url}
                                     severity: INFO
                               - http_post:
                                   call: http.post
                                   args:
                                       url: ${callback_url}
                                       auth:
                                           type: OAuth2
                                       body:
                                           event: ${event}

  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch callback-event-listener.yaml

  2. In a text editor, copy the following workflow to your source code file:
         
         main:
           params: [event]
           steps:
             - log_event:
                 call: sys.log
                 args:
                   text: ${event}
                   severity: INFO
             - init:
                 assign:
                   - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/callbacks/"}
                   - event_source_tokens: ${text.split(event.source, "/")}
                   - event_source_len: ${len(event_source_tokens)}
                   - event_source: ${event_source_tokens[event_source_len - 1]}
                   - doc_name: ${database_root + event_source}
             - get_document_for_event_source:
                 try:
                   call: googleapis.firestore.v1.projects.databases.documents.get
                   args:
                     name: ${doc_name}
                   result: document
                 except:
                     as: e
                     steps:
                         - known_errors:
                             switch:
                             - condition: ${e.code == 404}
                               return: ${"No callbacks for event source " + event_source}
                         - unhandled_exception:
                             raise: ${e}
             - process_callback_urls:
                 steps:
                   - check_fields_exist:
                       switch:
                       - condition: ${not("fields" in document)}
                         return: ${"No callbacks for event source " + event_source}
                       - condition: true
                         next: processFields
                   - processFields:
                       for:
                           value: key
                           in: ${keys(document.fields)}
                           steps:
                               - extract_callback_url:
                                   assign:
                                       - callback_url: ${document.fields[key]["stringValue"]}
                               - log_callback_url:
                                   call: sys.log
                                   args:
                                     text: ${"Calling back url " + callback_url}
                                     severity: INFO
                               - http_post:
                                   call: http.post
                                   args:
                                       url: ${callback_url}
                                       auth:
                                           type: OAuth2
                                       body:
                                           event: ${event}

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy callback-event-listener \
             --source=callback-event-listener.yaml \
             --location=us-central1 \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account that you previously created.




## Deploy a workflow that waits for events

The `callback-event-sample` workflow stores its callback details in a Firestore database, halts its execution, and then waits for specific events to occur.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow: `callback-event-sample`.

  4. In the **Region** list, select **us-central1**.

  5. Select the **Service account** that you previously created.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
           steps:
             - init:
                 assign:
                   - pubsub_topic: topic-callback
                   - storage_bucket: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "-bucket-callback"}
             - await_pubsub_message:
                 call: await_callback_event
                 args:
                   event_source: ${pubsub_topic}
                 result: pubsub_event
             - await_storage_bucket:
                 call: await_callback_event
                 args:
                   event_source: ${storage_bucket}
                 result: storage_event
             - return_events:
                 return:
                     pubsub_event: ${pubsub_event}
                     storage_event: ${storage_event}
         
         await_callback_event:
             params: [event_source]
             steps:
                 - init:
                     assign:
                       - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/callbacks/"}
                       - doc_name: ${database_root + event_source}
                       - execution_id: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                       - firestore_key: ${"exec_" + text.split(execution_id, "-")[0]}
                 - create_callback:
                     call: events.create_callback_endpoint
                     args:
                       http_callback_method: POST
                     result: callback_details
                 - save_callback_url:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                       name: ${doc_name}
                       updateMask:
                         fieldPaths: ["${firestore_key}"]
                       body:
                         fields:
                           ${firestore_key}:
                             stringValue: ${callback_details.url}
                 - log_and_await_callback:
                     try:
                       steps:
                         - log_await_start:
                             call: sys.log
                             args:
                               severity: INFO
                               data: ${"Started waiting 1hr for an event from source " + event_source}
                         - await_callback:
                             call: events.await_callback
                             args:
                               callback: ${callback_details}
                               timeout: 3600
                             result: callback_request
                         - log_await_stop:
                             call: sys.log
                             args:
                               severity: INFO
                               data: ${"Stopped waiting for an event from source " + event_source}
                     except:
                         as: e
                         steps:
                             - log_error:
                                 call: sys.log
                                 args:
                                     severity: "ERROR"
                                     text: ${"Received error " + e.message}
                 - delete_callback_url:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                       name: ${doc_name}
                       updateMask:
                         fieldPaths: ["${firestore_key}"]
                 - check_null_event:
                     switch:
                       - condition: ${callback_request == null}
                         return: null
                 - log_await_result:
                     call: sys.log
                     args:
                       severity: INFO
                       data: ${callback_request.http_request.body.event}
                 - return_event:
                     return: ${callback_request.http_request.body.event}

  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch callback-event-sample.yaml

  2. In a text editor, copy the following workflow to your source code file:
         
         main:
           steps:
             - init:
                 assign:
                   - pubsub_topic: topic-callback
                   - storage_bucket: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "-bucket-callback"}
             - await_pubsub_message:
                 call: await_callback_event
                 args:
                   event_source: ${pubsub_topic}
                 result: pubsub_event
             - await_storage_bucket:
                 call: await_callback_event
                 args:
                   event_source: ${storage_bucket}
                 result: storage_event
             - return_events:
                 return:
                     pubsub_event: ${pubsub_event}
                     storage_event: ${storage_event}
         
         await_callback_event:
             params: [event_source]
             steps:
                 - init:
                     assign:
                       - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/callbacks/"}
                       - doc_name: ${database_root + event_source}
                       - execution_id: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                       - firestore_key: ${"exec_" + text.split(execution_id, "-")[0]}
                 - create_callback:
                     call: events.create_callback_endpoint
                     args:
                       http_callback_method: POST
                     result: callback_details
                 - save_callback_url:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                       name: ${doc_name}
                       updateMask:
                         fieldPaths: ["${firestore_key}"]
                       body:
                         fields:
                           ${firestore_key}:
                             stringValue: ${callback_details.url}
                 - log_and_await_callback:
                     try:
                       steps:
                         - log_await_start:
                             call: sys.log
                             args:
                               severity: INFO
                               data: ${"Started waiting 1hr for an event from source " + event_source}
                         - await_callback:
                             call: events.await_callback
                             args:
                               callback: ${callback_details}
                               timeout: 3600
                             result: callback_request
                         - log_await_stop:
                             call: sys.log
                             args:
                               severity: INFO
                               data: ${"Stopped waiting for an event from source " + event_source}
                     except:
                         as: e
                         steps:
                             - log_error:
                                 call: sys.log
                                 args:
                                     severity: "ERROR"
                                     text: ${"Received error " + e.message}
                 - delete_callback_url:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                       name: ${doc_name}
                       updateMask:
                         fieldPaths: ["${firestore_key}"]
                 - check_null_event:
                     switch:
                       - condition: ${callback_request == null}
                         return: null
                 - log_await_result:
                     call: sys.log
                     args:
                       severity: INFO
                       data: ${callback_request.http_request.body.event}
                 - return_event:
                     return: ${callback_request.http_request.body.event}

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy callback-event-sample \
             --source=callback-event-sample.yaml \
             --location=us-central1 \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account that you previously created.




## Create an Eventarc trigger to route Pub/Sub events

An Eventarc trigger allows you to route events by specifying filters for the trigger, including the event source, and the target workflow. Create an Eventarc trigger to execute the `callback-event-listener` workflow as the result of publishing a message to a Pub/Sub topic. [Learn more about triggering a workflow](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc).

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** page.

[Go to Eventarc](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**.

  3. Type a **Trigger name**.

For example, `trigger-pubsub-events-listener`.

  4. In the **Event provider** list, select **Cloud Pub/Sub**.

  5. In the **Event** list, under _Custom_ , select **google.cloud.pubsub.topic.v1.messagePublished**.

  6. In the **Select a Cloud Pub/Sub topic** list, select the topic that you previously created.

  7. In the **Region** list, select **us-central1 (Iowa)**.

  8. If prompted, grant the `iam.serviceAccountTokenCreator` role to the Pub/Sub service account.

  9. Select the **Service account** that you previously created.

  10. In the **Event destination** list, select **Workflows**.

  11. In the **Select a workflow** list, select the **callback-event-listener** workflow.

  12. Click **Create**.




###  gcloud 

To create a trigger, run the [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create) command:
    
    
    gcloud eventarc triggers create trigger-pubsub-events-listener \
        --location=us-central1 \
        --destination-workflow=callback-event-listener \
        --destination-workflow-location=us-central1 \
        --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
        --transport-topic=topic-callback \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Events are transformed and passed to the workflow execution as runtime arguments. Note that it can take up to 2 minutes for the new trigger to become active.

## Create an Eventarc trigger to route Cloud Storage events

An Eventarc trigger allows you to route events by specifying filters for the trigger, including the event source, and the target workflow. Create an Eventarc trigger to execute the `callback-event-listener` workflow as the result of uploading a file to a Cloud Storage bucket. [Learn more about triggering a workflow](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc).

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** page.

[Go to Eventarc](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**.

  3. Type a **Trigger name**.

For example, `trigger-storage-events-listener`.

  4. In the **Event provider** list, select **Cloud Storage**.

  5. In the **Event** list, under _Direct_ , select **google.cloud.storage.object.v1.finalized**.

  6. In the **Bucket** list, browse for the bucket that you previously created and select it.

  7. In the **Region** list, based on your Cloud Storage bucket, accept the default of **us-central1 (Iowa)**.

  8. If prompted, grant the `iam.serviceAccountTokenCreator` role to the Pub/Sub service account.

  9. Select the **Service account** that you previously created.

  10. In the **Event destination** list, select **Workflows**.

  11. In the **Select a workflow** list, select the **callback-event-listener** workflow.

  12. Click **Create**.




###  gcloud 

To create a trigger, run the [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create) command:
    
    
    gcloud eventarc triggers create trigger-storage-events-listener \
        --location=us-central1 \
        --destination-workflow=callback-event-listener \
        --destination-workflow-location=us-central1 \
        --event-filters="type=google.cloud.storage.object.v1.finalized" \
        --event-filters="bucket=PROJECT_ID-bucket-callback" \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Events are transformed and passed to the workflow execution as runtime arguments. Note that it can take up to 2 minutes for the new trigger to become active.

## Execute the primary workflow

Executing a workflow runs the current workflow definition associated with the workflow. Execute the `callback-event-sample` workflow. This is the primary workflow and it waits for specific events to occurs, only resuming its execution when the secondary workflow makes the appropriate callback requests.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click the **callback-event-sample** workflow to go to its details page.

  3. On the **Workflow Details** page, click _play_arrow_ **Execute**.

  4. Click **Execute** again.

The workflow execution starts. While the execution runs, you should see an **Execution state** of `Running` and a log entry similar to the following: `Started waiting 1hr for an event from source topic-callback`.




###  gcloud 

To execute a workflow, run the [`gcloud workflows run`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/run) command:
    
    
    gcloud workflows run callback-event-sample \
        --location=us-central1

The workflow execution starts. While the execution runs, you should see an execution state similar to the following:
    
    
    Waiting for execution [a848a164-268a-449c-b2fe-396f32f2ed66] to complete...working...
    

## Generate events and check the execution status

You can confirm that the results are as expected by generating events, viewing log entries, and checking the workflow execution status.

### Publish a message

Publish a message to the Pub/Sub topic that you previously created.

###  Console 

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click **topic-callback**.

  3. Click the **Messages** tab.

  4. Click **Publish message**.

  5. In the **Message body** field, enter `Hello World`.

  6. Click **Publish**.




###  gcloud 

To publish a message, use the [gcloud pubsub topics publish](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish) command:
    
    
    gcloud pubsub topics publish topic-callback \
        --message="Hello World"

### Upload an object

Upload a file to the Cloud Storage bucket that you previously created.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket that you previously created.

  3. In the **Objects** tab, do either of the following:

     * Drag and drop the desired file from your desktop or file manager to the main pane in the Google Cloud console.

     * Click **Upload files** , select the file that you want to upload, and then click **Open**.




###  gcloud 

To upload a file, run the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp OBJECT_LOCATION gs://PROJECT_ID-bucket-callback/

Replace `OBJECT_LOCATION` with the local path to your object. For example, `random.txt`.

### View log entries and execution status

Confirm that the `callback-event-sample` workflow completed successfully.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click the **callback-event-sample** workflow to go to its details page.

  3. On the **Workflow Details** page, to retrieve the details for a particular execution, click the appropriate execution ID.

The **Execution state** should be **Succeeded** and, in the Output pane, you should see the received Pub/Sub and Cloud Storage events.




###  gcloud 

  1. Filter the log entries and return the output in JSON format:
         
         gcloud logging read "resource.type=workflows.googleapis.com/Workflow AND textPayload:calling OR textPayload:waiting" \
             --format=json

  2. Look for log entries similar to:
         
         "textPayload": "Stopped waiting for an event from source..."
         "textPayload": "Calling back url https://workflowexecutions.googleapis.com/v1/projects/..."
         "textPayload": "Started waiting 1hr for an event from source..."
         

  3. Check the status of the last execution attempt:
         
         gcloud workflows executions wait-last

The result should be similar to the following:
         
         Using cached execution name: projects/1085953646031/locations/us-central1/workflows/callback-event-sample/executions/79929e4e-82c1-4da1-b068-f828034c01b7
         Waiting for execution [79929e4e-82c1-4da1-b068-f828034c01b7] to complete...done.
         [...]
         state: SUCCEEDED
         




## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

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



### Delete resources created in this tutorial

  1. [Delete data from Firestore](https://firebase.google.com/docs/firestore/manage-data/delete-data).

  2. [Delete a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic#delete_a_topic).

  3. [Delete a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).

  4. [Delete an Eventarc trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).

  5. [Delete a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#delete-workflow).




## What's next

  * Try the [Create a human-in-the-loop workflow using callbacks](https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore) tutorial.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
