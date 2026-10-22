---
url: https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-firestore/
title: Route Cloud Firestore events to Workflows \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:57.811995+00:00
---

# Route Cloud Firestore events to Workflows  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Route Cloud Firestore events to Workflows Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

An Eventarc trigger declares your interest in a certain event or set of events. You can configure event routing by specifying filters for the trigger, including the event source, and the target workflow.

Events are delivered in the CloudEvents format through an HTTP request. The Workflows service converts the event to a JSON object (following the [CloudEvents specification](https://docs.cloud.google.com/eventarc/docs/cloudevents-json)) and passes the event into the workflow execution as a [workflow runtime argument](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments). Make sure that the event size does not exceed the [resource limit](https://docs.cloud.google.com/workflows/quotas#resource_limits). Events larger than the maximum Workflows arguments size won't trigger workflow executions.

Cloud Firestore supports [Auth Context](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/authcontext.md) as an extension attribute to the CloudEvents format. When you create a trigger, you can apply this event type attribute to filter events with authentication information.

These instructions show you how to configure event routing so that an execution of your workflow is triggered in response to a direct Cloud Firestore event. For more details, see the list of [supported direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-firestore-preview).

**Note:** If both direct and audit log events are supported for a Google provider, we recommend that you create a trigger that filters for the direct event. Direct events offer a number of advantages over audit log events. For more information, see [Event routes](https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options).

## Prepare to create a trigger

Before creating an Eventarc trigger for a target workflow, complete the following tasks.

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Eventarc, Eventarc Publishing, Workflows, and Workflow Executions APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com,workflows.googleapis.com,workflowexecutions.googleapis.com)

  3. If applicable, enable the API related to the direct events. For example, for Cloud Firestore events, enable the Cloud Firestore API. 

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




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the Eventarc, Eventarc Publishing, Workflows, and Workflow Executions APIs:
         
         gcloud services enable eventarc.googleapis.com \
             eventarcpublishing.googleapis.com \
             workflows.googleapis.com \
             workflowexecutions.googleapis.com

  3. If applicable, enable the API related to the direct events. For example, for Cloud Firestore events, enable `firestore.googleapis.com`. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for a target workflow.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account. It must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you cannot change its name.

     2. Grant the required Identity and Access Management (IAM) roles or permissions. For more information, see [Roles and permissions for Workflows targets](https://docs.cloud.google.com/eventarc/standard/docs/workflows/roles-permissions). 




## Create a trigger

You can create an Eventarc trigger with a deployed workflow as the event receiver by using the Google Cloud CLI (`gcloud` or Terraform), or through the Google Cloud console.

**Note:** Filtering is done through an exact match and does not support wildcards or regular expressions. However, you can use the `--event-filters-path-pattern` flag in the following gcloud CLI command, or define a path pattern through the console. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns). 

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**. 
  3. Type a **Trigger name**. 

This is the ID of the trigger and it must start with a letter. It can contain up to 63 lowercase letters, numbers, or hyphens.

  4. For the **Trigger type** , select **Google sources**. 
  5. In the **Event provider** list, select **Cloud Firestore**. 

Note that the event provider name used in the associated [Google Cloud documentation](https://docs.cloud.google.com/docs) might not have a prefix of _Cloud_ or _Google Cloud_. For example, on the console, _Memorystore for Redis_ is referred to as **Google Cloud Memorystore for Redis**.

  6. In the **Event type** list, from the _Direct_ events, select an event type. 
  7. In the **Event data content type** list, select the encoding of the event payload. 

For direct events from Cloud Firestore, this must be **application/protobuf** and the event data is a byte array. For more information about the protobuf messages for Cloud Firestore events, see [Common events](https://docs.cloud.google.com/eventarc/docs/cloudevents-json#common-events). Note that you can use a Workflows standard library function to [encode bytes to Base64 text](https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/encode). For more information, see [Returning bytes](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes#bytes). 

  8. In the **Region** list, select the same region as the Google Cloud service that is generating events. 

For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  9. If applicable to the event provider, click **Add filter** and specify the following: 
     1. In the **Attribute 1** field, depending on the direct event you chose, select a [resource ID](https://docs.cloud.google.com/apis/design/resource_names) that can act as an event filter.
     2. Select an operator: 
        * **Equal**
        * **Path pattern** : applicable to `document` (Native mode) and `entity` (Datastore mode) resources. Use wildcards to respond to changes that match a pattern. A wildcard `*` matches a single segment and a multi-segment wildcard `**` matches zero or more segments in the pattern. Don't specify a leading slash—for example: `users/*` or `users/{userId}` | Matches all documents in the `/users` collection. Does not match documents in sub-collections like `/users/marie/messages/33e2IxYBD9enzS50SJ68`  
---|---  
`users/**` | Matches all documents in the `/users` collection and documents in subcollections like `/users/marie/messages/33e2IxYBD9enzS50SJ68`  
  
For more information, see[ Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).

     3. In the **Attribute value 1** field, depending on the operator that you chose, type the exact value or apply a path pattern.
     4. If more attribute filters are applicable, click **Add filter** and specify the appropriate values.
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

You can create a trigger by running a `gcloud eventarc triggers create` command along with required and optional flags.

The flags differ depending on whether you are running Firestore in Native mode or in Datastore mode. For more information, see [Choosing between Native mode and Datastore mode](https://docs.cloud.google.com/datastore/docs/firestore-or-datastore).

#### Native mode
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-workflow=DESTINATION_WORKFLOW  \
        --destination-workflow-location=DESTINATION_WORKFLOW_LOCATION \
        --event-filters="type=EVENT_FILTER_TYPE" \
        --event-filters="database=DATABASE" \
        --event-filters="namespace=NAMESPACE" \
        --event-filters-path-pattern="document=DOCUMENT" \
        --event-data-content-type="EVENT_DATA_CONTENT_TYPE" \
        --service-account="SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

#### Datastore mode
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-workflow=DESTINATION_WORKFLOW  \
        --destination-workflow-location=DESTINATION_WORKFLOW_LOCATION \
        --event-filters="type=EVENT_FILTER_TYPE" \
        --event-filters="database=DATABASE" \
        --event-filters="namespace=NAMESPACE" \
        --event-filters-path-pattern="entity=ENTITY" \
        --event-data-content-type="EVENT_DATA_CONTENT_TYPE" \
        --service-account="SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier. 


  * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example `gcloud config set eventarc/location us-central1`.

Cloud Firestore triggers for Eventarc are only available in certain locations and the trigger must be in the same location as the Cloud Firestore database. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations) and [Cloud Firestore locations](https://firebase.google.com/docs/firestore/locations). 

  * `DESTINATION_WORKFLOW`: the ID of the deployed workflow that receives the events from the trigger. The workflow can be in any of the Workflows supported [locations](https://docs.cloud.google.com/workflows/docs/locations) and does not need to be in the same location as the trigger. However, the workflow must be in the same project as the trigger. 
  * `DESTINATION_WORKFLOW_LOCATION` (optional): the location in which the destination workflow is deployed. If not specified, it is assumed that the workflow is in the same location as the trigger. 
  * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. For a list of supported event types, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). 

Cloud Firestore supports the following event types in **Native mode only**.

    * `google.cloud.firestore.document.v1.created`: event is sent when a document is written to for the first time
    * `google.cloud.firestore.document.v1.created.withAuthContext`: event with authentication information attributes is sent when a document is written to for the first time
    * `google.cloud.firestore.document.v1.updated`: event is sent when a document already exists and has any value changed
    * `google.cloud.firestore.document.v1.updated.withAuthContext`: event with authentication information attributes is sent when a document already exists and has any value changed
    * `google.cloud.firestore.document.v1.deleted`: event is sent when a document is deleted
    * `google.cloud.firestore.document.v1.deleted.withAuthContext`: event with authentication information attributes is sent when a document is deleted
    * `google.cloud.firestore.document.v1.written`: event is sent when a document is created, updated, or deleted
    * `google.cloud.firestore.document.v1.written.withAuthContext`: event with authentication information attributes is sent when a document is created, updated, or deleted.

Cloud Firestore supports the following event types in **Datastore mode only**. Data objects in Firestore in Datastore mode are known as _entities_.

    * `google.cloud.datastore.entity.v1.created`: event is sent when an entity is written to for the first time
    * `google.cloud.datastore.entity.v1.created.withAuthContext`: event with authentication information attributes is sent when an entity is written to for the first time
    * `google.cloud.datastore.entity.v1.updated`: event is sent when an entity already exists and has any value changed
    * `google.cloud.datastore.entity.v1.updated.withAuthContext`: event with authentication information attributes is sent when an entity already exists and has any value changed
    * `google.cloud.datastore.entity.v1.deleted`: event is sent when an entity is deleted
    * `google.cloud.datastore.entity.v1.deleted.withAuthContext`: event with authentication information attributes is sent when an entity is deleted
    * `google.cloud.datastore.entity.v1.written`: event is sent when an entity is created, updated, or deleted
    * `google.cloud.datastore.entity.v1.written.withAuthContext`: event with authentication information attributes is sent when an entity is created, updated, or deleted


  * `DATABASE`: the Firestore database. For the default database name, use `(default)`.
  * `NAMESPACE` (optional): the Firestore database namespace. For the default namespace in Datastore mode, use `(default)`. If not specified, a wildcard match (`*`) to any occurrences is made.
  * `DOCUMENT` (optional): applicable to database instances running in **Native mode only**. The database path from which you want to receive events from when data is created, updated, or deleted in that path. Don't specify a leading slash. The operator can be one of the following: 
    * Equal; for example, `--event-filters="document=DOCUMENT"`
    * Path pattern; for example, `--event-filters-path-pattern="document=DOCUMENT"`. 

Use wildcards to respond to changes in documents that match a pattern. A wildcard `*` matches a single segment and a multi-segment wildcard `**` matches zero or more segments in the pattern—for example:

`users/*` or `users/{userId}` | Matches all documents in the `/users` collection. Doesn't match documents in sub-collections like `/users/marie/messages/33e2IxYBD9enzS50SJ68`  
---|---  
`users/**` | Matches all documents in the `/users` collection and documents in subcollections like `/users/marie/messages/33e2IxYBD9enzS50SJ68`  
For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns). 
  * `ENTITY` (optional): applicable to database instances running in **Datastore mode only**. The database path from which you want to receive events from when data is created, updated, or deleted in that path. Don't specify a leading slash. The operator can be one of the following: 
    * Equal; for example, `--event-filters="document=ENTITY"`
    * Path pattern; for example, `--event-filters-path-pattern="ENTITY=ENTITY"`

For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).

Note that you might need to escape characters in kind IDs and entity IDs. Escaping a character lets the event filter correctly interpret the ID. For more information, see [Character escaping](https://docs.cloud.google.com/datastore/docs/extend-with-functions-2nd-gen#character_escaping).



  * `EVENT_DATA_CONTENT_TYPE`: the [encoding of the event payload](https://docs.cloud.google.com/eventarc/standard/docs/overview#event-format). For direct events from Firestore, this must be `application/protobuf` and the event data is a byte array. For more information about the protobuf messages for Cloud Firestore events, see [Common events](https://docs.cloud.google.com/eventarc/docs/cloudevents-json#common-events). Note that you can use a Workflows standard library function to [encode bytes to Base64 text](https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/encode). For more information, see [Returning bytes](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes#bytes). 
  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
  * `PROJECT_ID`: your Google Cloud project ID 



Notes:

  * For direct events from Cloud Firestore, the encoding of the event payload is `application/protobuf`. 
  * The `--event-filters="type=EVENT_FILTER_TYPE"` flag is required. If no other event filter is set, events for all resources are matched. 
  * `EVENT_FILTER_TYPE` cannot be changed after creation. To change `EVENT_FILTER_TYPE`, create a new trigger and delete the old one. 
  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported; however, when using the `--event-filters-path-pattern` flag, you can define a resource [path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns). 
  * The `--service-account` flag is used to specify the Identity and Access Management (IAM) service account email associated with the trigger. 



Example:
    
    
    gcloud eventarc triggers create helloworld-trigger \
        --location=us-east1 \
        --destination-workflow=my-workflow \
        --destination-workflow-location=us-east1 \
        --event-filters="type=google.cloud.firestore.document.v1.updated" \
        --event-filters="database=my-database" \
        --event-filters-path-pattern="document=users/my-document-*" \
        --event-data-content-type="application/protobuf" \
        --service-account="${TRIGGER_SA}@${PROJECT_ID}.iam.gserviceaccount.com"

This command creates a trigger called `helloworld-trigger` for the event identified as `google.cloud.firestore.document.v1.updated` in the `my-database` database instance running in Native mode, and filters events for `document` paths that match `users/my-document-`.

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

  * [Learn more about using Eventarc and Cloud Firestore](https://docs.cloud.google.com/firestore/docs/eventarc).
  * [Trigger a workflow using Eventarc and Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).
  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview).
  * [Learn how to manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
