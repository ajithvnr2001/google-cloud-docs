---
url: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-bigquery-table/
title: Quickstart: Publish events to a BigQuery table \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:05.376878+00:00
---

# Quickstart: Publish events to a BigQuery table  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-bigquery-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish events to a BigQuery table

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

This quickstart shows you how to publish and receive event messages by creating an Eventarc Advanced bus and enrollment in your Google Cloud project.

  * A _bus_ acts as a central router, receiving messages from event sources or published by providers.

  * An _enrollment_ routes messages received by the bus to one or more destinations through a processing _pipeline_.




In this quickstart, you:

  1. Create a BigQuery table.

  2. Create an Eventarc Advanced bus.

  3. Create an Eventarc Advanced enrollment.

  4. Publish an event message to the bus.

  5. View the event data in the BigQuery table.




You can complete this quickstart using the gcloud CLI and the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool).

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

  7. Enable the BigQuery and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigquery.googleapis.com eventarc.googleapis.com eventarcpublishing.googleapis.com

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

  13. Enable the BigQuery and Eventarc APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigquery.googleapis.com eventarc.googleapis.com eventarcpublishing.googleapis.com

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

     * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
     * [Eventarc Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.developer) (`roles/eventarc.developer`)
     * [Eventarc Message Bus Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusAdmin) (`roles/eventarc.messageBusAdmin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  18. To give Eventarc Advanced the necessary permissions to update BigQuery table properties, ask your administrator to grant the [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) IAM role on your Google Cloud project to a service account: 
     1. Create a service account. For testing purposes, you will attach this service account to an Eventarc Advanced pipeline to represent the identity of the pipeline. 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for your service account. 
     2. Grant the `roles/bigquery.dataEditor` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
                --role=roles/bigquery.dataEditor




## Create a BigQuery table

Create a [BigQuery table](https://docs.cloud.google.com/bigquery/docs/tables-intro) as your event destination. Other event destinations are supported such as a Pub/Sub topic, Workflows, or another HTTP endpoint. For more information, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/advanced/docs/event-providers-targets).

Before creating a BigQuery table, create a [dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) which acts as a top-level container for the table, and a table [schema](https://docs.cloud.google.com/bigquery/docs/schemas).

  1. To create a new dataset, use the [bq mk](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#mk-dataset) command with the `--dataset` flag.
         
         bq --location=$REGION mk --dataset DATASET_ID

Replace `DATASET_ID` with a unique name for the BigQuery dataset—for example, `my_dataset`.

  2. In your terminal, create a new file called `my-schema.json`.

  3. Copy and paste the following schema into the new file, and then save the file.
         
         [
             {
                 "name": "name",
                 "type": "STRING",
                 "mode": "REQUIRED"
             },
             {
                 "name": "age",
                 "type": "INTEGER",
                 "mode": "NULLABLE"
             }
         ]

  4. To create a table, use the [bq mk](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#mk-table) command with the `--table` flag.
         
         bq mk --table PROJECT_ID:DATASET_ID.TABLE_ID my-schema.json

Replace `TABLE_ID` with a unique name for the BigQuery table—for example, `my-table`.




## Create an Eventarc Advanced bus

A bus receives event messages from a message source or published by a provider and acts as a message router.

For more information, see [Create a bus to route messages](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus).

**Note:** You can create one bus per Google Cloud project per [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

Create an Eventarc Advanced bus in your project by using the [`gcloud eventarc message-buses create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/create) command:
    
    
    gcloud eventarc message-buses create BUS_NAME \
        --location=$REGION

Replace `BUS_NAME` with the ID of your bus or a fully qualified name—for example, `my-bus`.

## Create an Eventarc Advanced enrollment

An enrollment determines which messages are routed to a destination and it also specifies the pipeline that is used to configure a destination for the event messages. In this case, the target destination is a [BigQuery API endpoint](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll).

For more information, see [Create an enrollment to receive events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment).

**Note:** Creating a pipeline might take more than 10 minutes.

When using the gcloud CLI, you first create a pipeline, and then create an enrollment:

  1. Create a pipeline by using the [`gcloud eventarc pipelines create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/create) command:
         
         gcloud eventarc pipelines create PIPELINE_NAME \
             --destinations=http_endpoint_uri='https://bigquery.googleapis.com/bigquery/v2/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID/insertAll',http_endpoint_message_binding_template='{"headers": headers.merge({"content-type":"application/json"}), "body": {"rows":[{"json":message.data}]}}',oauth_token_authentication_service_account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --input-payload-format-json= \
             --location=$REGION

Replace the `PIPELINE_NAME` with the ID of the pipeline or a fully qualified name—for example, `my-pipeline`.

Note the following:

     * The `http_endpoint_message_binding_template` key transforms the event into the format expected by the API. When defining a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding), you must configure an input format to access the payload.
     * The `oauth_token_authentication_service_account` key specifies a service account email. This email is used to generate an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) which should generally be used only when calling Google APIs hosted on `*.googleapis.com`.
     * The `input-payload-format-json` flag specifies that the pipeline's input payload format is JSON; any messages not matching this format are treated as [persistent errors](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events#persistent).
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

To directly publish a message to your bus, you can use the [`gcloud eventarc message-buses publish`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/publish) command or send a request to the [Eventarc Publishing REST API](https://docs.cloud.google.com/eventarc/docs/reference/publishing/rest). For more information, see [Publish events directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format).

The message must be in a CloudEvents format which is a specification for describing event data in a common way. The `data` element is the payload of your event and it must ultimately match the schema of your BigQuery table. Any well-formed JSON can go in this field. For more information about CloudEvents context attributes, see [Event format](https://docs.cloud.google.com/eventarc/advanced/docs/event-format).

The following are examples of directly publishing an event to an Eventarc Advanced bus:

### Example 1

You can publish an event to a bus using the gcloud CLI and an `--event-data` and other event attribute flags:
    
    
    gcloud eventarc message-buses publish BUS_NAME \
        --event-data='{"name": "my-name", "age": "20"}' \
        --event-id=hello-world-id-1234 \
        --event-source=hello-world-source \
        --event-type=hello-world-type \
        --event-attributes="datacontenttype=application/json" \
        --location=$REGION
    

### Example 2

You can publish an event to a bus as a JSON message using the gcloud CLI and a `--json-message` flag:
    
    
    gcloud eventarc message-buses publish BUS_NAME \
        --location=$REGION \
        --json-message='{"id": "hello-world-id-1234", "type":
     "hello-world-type", "source":
     "hello-world-source", "specversion": "1.0", "data":
     {"name": "my-name", "age": "20"}}'
    

After publishing an event, you should receive an "Event published successfully" message.

## View the event data in the BigQuery table

After publishing an event to your Eventarc Advanced bus, you can use the [bq query](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query) command to confirm that a new row was added to your BigQuery table.
    
    
    bq query \
        --use_legacy_sql=false \
        'SELECT
          *
        FROM
          `PROJECT_ID.DATASET_ID.TABLE_ID`
        LIMIT
          10;'

You have successfully created an Eventarc Advanced bus and enrollment, published an event message to the bus, and verified the expected outcome by querying the BigQuery table.

## Clean up

When you finish the tasks that are described in this quickstart, you can avoid continued billing by deleting the resources that you created:

  1. [Delete a BigQuery table](https://docs.cloud.google.com/bigquery/docs/managing-tables#deleting_tables).

  2. [Delete a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/managing-datasets#delete-datasets).

  3. Delete Eventarc Advanced resources:

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
