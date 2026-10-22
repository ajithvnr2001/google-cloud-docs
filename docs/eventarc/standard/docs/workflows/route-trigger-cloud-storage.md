---
url: https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage/
title: Route Cloud Storage events to Workflows \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:54.701512+00:00
---

# Route Cloud Storage events to Workflows  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Route Cloud Storage events to Workflows Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

An Eventarc trigger declares your interest in a certain event or set of events. You can configure event routing by specifying filters for the trigger, including the event source, and the target workflow.

Events are delivered in the CloudEvents format through an HTTP request. The Workflows service converts the event to a JSON object (following the [CloudEvents specification](https://docs.cloud.google.com/eventarc/docs/cloudevents-json)) and passes the event into the workflow execution as a [workflow runtime argument](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments). Make sure that the event size does not exceed the [resource limit](https://docs.cloud.google.com/workflows/quotas#resource_limits). Events larger than the maximum Workflows arguments size won't trigger workflow executions.

These instructions show you how to configure event routing so that an execution of your workflow is triggered in response to a direct Cloud Storage event. This applies to a **Cloud Storage** event provider. For more details, see the list of [supported direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). **Note:** If both direct and audit log events are supported for a Google provider, we recommend that you create a trigger that filters for the direct event. Direct events offer a number of advantages over audit log events. For more information, see [Event routes](https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options).

## Prepare to create a trigger

Before creating an Eventarc trigger for a target workflow, complete the following tasks.

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Eventarc, Eventarc Publishing, Workflows, and Workflow Executions APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com,workflows.googleapis.com,workflowexecutions.googleapis.com)

  3. If applicable, enable the API related to the direct events. For example, for Cloud Storage events, enable the Cloud Storage API. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for a target workflow.

     1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for event trigger`.

     4. Click **Create and continue**.

     5. To provide appropriate access, in the **Select a role** list, select the required Identity and Access Management (IAM) roles to grant to your service account. For more information, see [Roles and permissions for Workflows targets](https://docs.cloud.google.com/eventarc/standard/docs/workflows/roles-permissions).

For additional roles, click add **Add another role** and add each additional role.

     6. Click **Continue**.

     7. To finish creating the account, click **Done**. 

  5. Grant the Pub/Sub Publisher role to the Cloud Storage service agent. Typically, this is `service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`. You can [retrieve the email address for the Cloud Storage service agent](https://docs.cloud.google.com/storage/docs/getting-service-agent#console).

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

  2. Enable the Eventarc, Eventarc Publishing, Workflows, and Workflow Executions APIs:
         
         gcloud services enable eventarc.googleapis.com \
             eventarcpublishing.googleapis.com \
             workflows.googleapis.com \
             workflowexecutions.googleapis.com

  3. If applicable, enable the API related to the direct events. For example, for Cloud Storage events, enable `storage.googleapis.com`. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for a target workflow.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account. It must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you cannot change its name.

     2. Grant the required Identity and Access Management (IAM) roles or permissions. For more information, see [Roles and permissions for Workflows targets](https://docs.cloud.google.com/eventarc/standard/docs/workflows/roles-permissions). 

  5. If you are creating a trigger for a direct Cloud Storage event, grant the `pubsub.publisher` role to the Cloud Storage service account:
         
         SERVICE_ACCOUNT="$(gcloud storage service-agent --project=PROJECT_ID)"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:${SERVICE_ACCOUNT}" \
             --role="roles/pubsub.publisher"
         




## Create a trigger

You can create an Eventarc trigger with a deployed workflow as the event receiver by using the Google Cloud CLI (`gcloud` or Terraform), or through the Google Cloud console.

**Note:** Filtering is done through an exact match and does not support wildcards or regular expressions.

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**. 
  3. Type a **Trigger name**. 

This is the ID of the trigger and it must start with a letter. It can contain up to 63 lowercase letters, numbers, or hyphens.

  4. For the **Trigger type** , select **Google sources**. 
  5. In the **Event provider** list, select **Cloud Storage**. 

Note that the event provider name used in the associated [Google Cloud documentation](https://docs.cloud.google.com/docs) might not have a prefix of _Cloud_ or _Google Cloud_. For example, on the console, _Memorystore for Redis_ is referred to as **Google Cloud Memorystore for Redis**.

  6. In the **Event type** list, from the _Direct_ events, select an event type: 
     * **google.cloud.storage.object.v1.archived** : event is sent when a live version of an object becomes a noncurrent version. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).
     * **google.cloud.storage.object.v1.delete** : event is sent when an object is soft deleted. For more information, see [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).
     * **google.cloud.storage.object.v1.finalized** : event is sent when a new object is created (or an existing object is overwritten, and a new generation of that object is created) in the bucket. 
     * **google.cloud.storage.object.v1.metadataUpdated** : event is sent when the [metadata](/storage/docs/metadata) of an existing object changes. 
  7. In the **Event data content type** list, select the encoding of the event payload. 

For direct events from Cloud Storage, this must be **application/json**.

  8. Specify or browse for the globally unique identifier of the Cloud Storage **Bucket**. 

The Cloud Storage bucket must reside in the same Google Cloud project and [region or multi-region](https://docs.cloud.google.com/eventarc/docs/locations) as the Eventarc trigger.

  9. Select a **Region**. 

Cloud Storage triggers for Eventarc are available in [single-region, dual-region, and multi-region locations](https://docs.cloud.google.com/eventarc/docs/locations#gcs-triggers). Note that the Cloud Storage bucket must reside in the same Google Cloud project and region or multi-region as the Eventarc trigger.

**Important:** Because Eventarc Standard uses Pub/Sub as its transport layer, Cloud Storage triggers can fail if a Cloud Storage event originates from a region not permitted by your Pub/Sub message storage policy, and if in-transit operations are enforced (`"enforceInTransit": true`). When you create a Cloud Storage trigger in a [multi-region](https://docs.cloud.google.com/eventarc/docs/locations#gcs-triggers) location, ensure your message storage policy allows all source regions within that multi-region. For more information, see [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). 

Events are delivered using [Pub/Sub notifications from Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications). Setting up too many notifications registered against the same bucket might exhaust the notification limit for the bucket as indicated by the error `Cloud Storage bucket ...: Pub/Sub notification limit reached`. The bucket can have up to 10 notification configurations set to trigger for a specific event. See more quotas and limitations in the [Cloud Storage quotas and limits page](https://docs.cloud.google.com/storage/quotas#buckets) .

  10. Select the **Service account** that will invoke your service or workflow. 

Or, you can create a new service account.

This specifies the Identity and Access Management (IAM) service account email associated with the trigger and to which you previously granted [specific roles](https://docs.cloud.google.com/eventarc/standard/docs/access-control) required by Eventarc. 

  11. In the **Event destination** list, select **Workflows**. 
  12. Select a workflow.  


This is the name of the workflow to pass events to. Events for a workflow execution are transformed and passed to the workflow as runtime arguments.

For more information, see [ Create a trigger for Workflows](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers). 

  13. Optionally, to add a label, you can click add **Add label**. Labels are key-value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
  14. Click **Create**. 

After a trigger is created, the event source filters can't be modified. Instead, create a new trigger and delete the old one. For more information, see [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers). 




###  gcloud 
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-workflow=DESTINATION_WORKFLOW  \
        --destination-workflow-location=DESTINATION_WORKFLOW_LOCATION \
        --event-filters="type=EVENT_FILTER_TYPE" \
        --event-filters="bucket=BUCKET" \
        --service-account="SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier. 
  * `LOCATION`: the location of the Eventarc trigger and available in single-region, dual-region, and multi-region locations; you cannot create a `global` Eventarc trigger. Note that the Cloud Storage bucket must reside in the same Google Cloud project and region as the Eventarc trigger. For more information, see [Eventarc Locations](https://docs.cloud.google.com/eventarc/docs/locations#cloud-storage). **Important:** Because Eventarc Standard uses Pub/Sub as its transport layer, Cloud Storage triggers can fail if a Cloud Storage event originates from a region not permitted by your Pub/Sub message storage policy, and if in-transit operations are enforced (`"enforceInTransit": true`). When you create a Cloud Storage trigger in a [multi-region](https://docs.cloud.google.com/eventarc/docs/locations#gcs-triggers) location, ensure your message storage policy allows all source regions within that multi-region. For more information, see [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). 
  * `DESTINATION_WORKFLOW`: the ID of the deployed workflow that receives the events from the trigger. The workflow can be in any of the Workflows supported [locations](https://docs.cloud.google.com/workflows/docs/locations) and does not need to be in the same location as the trigger. However, the workflow must be in the same project as the trigger. 
  * `DESTINATION_WORKFLOW_LOCATION` (optional): the location in which the destination workflow is deployed. If not specified, it is assumed that the workflow is in the same location as the trigger. 
  * `EVENT_FILTER_TYPE`: the identifier of the Cloud Storage event and can be one of the following: 
    * `google.cloud.storage.object.v1.finalized`: Event is sent when a new object is created (or an existing object is overwritten, and a new generation of that object is created) in the bucket 
    * `google.cloud.storage.object.v1.archived`: event is sent when a live version of an object becomes a noncurrent version. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).
    * `google.cloud.storage.object.v1.deleted`: event is sent when an object is soft deleted. For more information, see [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).
    * `google.cloud.storage.object.v1.metadataUpdated`: Event is sent when the [metadata](https://docs.cloud.google.com/storage/docs/metadata) of an existing object changes. 
  * `BUCKET`: the globally unique identifier of the Cloud Storage bucket. 
  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
  * `PROJECT_ID`: your Google Cloud project ID 



Notes:

  * For direct events from Cloud Storage, the encoding of the event payload is `application/json`.
  * These flags are required: 
    * `--event-filters="type=EVENT_FILTER_TYPE"`
    * `--event-filters="bucket=BUCKET"`
  * After a trigger is created, `EVENT_FILTER_TYPE` can't be changed. For a different event type, you must create a new trigger. 
  * The `--service-account` flag is used to specify the Identity and Access Management (IAM) service account email associated with the trigger. 
  * Events are delivered using [Pub/Sub notifications from Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications). Setting up too many notifications registered against the same bucket might exhaust the notification limit for the bucket as indicated by the error `Cloud Storage bucket ...: Pub/Sub notification limit reached`. The bucket can have up to 10 notification configurations set to trigger for a specific event. See more quotas and limitations in the [Cloud Storage quotas and limits page](https://docs.cloud.google.com/storage/quotas#buckets). 
  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported. 
  * The Cloud Storage bucket must reside in the same Google Cloud project and [region or multi-region](https://docs.cloud.google.com/eventarc/docs/locations) as the Eventarc trigger. 
  * By default, Pub/Sub subscriptions created for Eventarc persist regardless of activity and do not expire. To change the inactivity duration, see [Subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties). 



Example:
    
    
    gcloud eventarc triggers create helloworld-trigger \
        --location=us-central1 \
        --destination-workflow=my-workflow \
        --destination-workflow-location=europe-west4 \
        --event-filters="type=google.cloud.storage.object.v1.finalized" \
        --event-filters="bucket=my-project-bucket" \
        --service-account="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

This command creates a trigger called `helloworld-trigger` for the Cloud Storage bucket `my-project-bucket` and the event identified as `google.cloud.storage.object.v1.finalized`.

###  Terraform 

You can create a trigger for a workflow using Terraform. For details, see [Trigger a workflow using Eventarc and Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform). 

**Note:** Although your trigger is created immediately, it can take up to two minutes for a trigger to propagate and filter events.

## List a trigger

You can confirm the creation of a trigger by listing Eventarc triggers using the Google Cloud CLI or through the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

This page lists your triggers in all locations, and includes details such as names, regions, event providers, destinations, and more.

  2. To filter your triggers:

     1. Click filter_list **Filter** or the **Filter triggers** field.
  3. In the **Properties** list, select an option to filter the triggers by.



You can select a single property or use the logical operator `OR` to add more properties.

* To sort your triggers, beside any supported column heading, click arrow_upward **Sort**.

###  gcloud 

Run the following command to list your triggers:
    
    
    gcloud eventarc triggers list --location=-

This command lists your triggers in all locations, and includes details such as names, types, destinations, and statuses.

## What's next

  * [Trigger a workflow using Eventarc and Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform)

  * [Trigger Workflows with events from Cloud Storage](https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-storage)

  * [Trigger Workflows with Pub/Sub messages](https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-pubsub)

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
