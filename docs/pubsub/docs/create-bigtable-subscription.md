---
url: https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription/
title: Create Bigtable subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:03.990673+00:00
---

# Create Bigtable subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create Bigtable subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create a Bigtable subscription in Pub/Sub. Bigtable subscriptions let you write Pub/Sub messages directly to a [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) table.

For more information about this subscription type, see [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions).

## Before you begin

  * The Bigtable table where you want to write Pub/Sub messages must already exist. For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

  * The table must have a column family named `data`. You can add the column family when you create the table.

  * If you want to write message metadata to the table, the table must also have a column family named `pubsub_metadata`.




## Required roles and permissions

To get the permissions that you need to create a Bigtable subscription, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a Bigtable subscription. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Bigtable subscription:

  * `pubsub.subscriptions.create` on the project
  * `pubsub.topics.attachSubscription` on the topic



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Cross-project subscriptions

If you create a subscription in one project for a topic in another project, you must have `pubsub.subscriptions.create` permission on the project in which you are creating the subscription, and `pubsub.topics.attachSubscription` permission on the topic.

## Grant IAM roles to the service account

Pub/Sub uses an Identity and Access Management (IAM) service account to access Google Cloud resources. To enable Pub/Sub to write to Bigtable, you must grant the **Bigtable User** (`roles/bigtable.user`) role to this service account.

By default, Pub/Sub uses the Pub/Sub service agent  
(`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`). You can also specify a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) when you create the Bigtable subscription.

### Use the Pub/Sub service agent

To grant the required role to the Pub/Sub service agent, perform the following steps. You can grant the role on the project or on the Bigtable instance that contains the table.

### Project

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants**.

  3. Find the row for **Cloud Pub/Sub Service Account** (Principal `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`) and click mode_edit **Edit principal**.

  4. Click **Add another role** and select the **Bigtable user** role.




For more information, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).

### Instance

  1. In the Google Cloud console, go to the **Bigtable** > **Instances** page.

[Go to Instances](https://console.cloud.google.com/bigtable/instances)

  2. In the **Instances** page, select the checkbox next to the name of the instance.

  3. If the info panel isn't visible, click **Show info panel**.

  4. Click person_add **Add principal** , then enter the service account identifier, in the following format:

`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`.

  5. In the **Assign roles** list, select **Bigtable User**.

  6. Click **Save**. The principal is granted the role on the resource.




Also ensure that the Pub/Sub service account has the Pub/Sub service agent role. This allows Pub/Sub to use your Bigtable instance project's Admin API quota. 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants**.

  3. Find the row for **Cloud Pub/Sub Service Account** (Principal `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`) and click mode_edit **Edit principal**.

  4. In the **Assign roles** section, if the **Cloud Pub/Sub Service Agent** role isn't already present, add it by clicking **Add another role**.




### Use a custom service account

If you grant the **Bigtable User** role to the Pub/Sub service agent, then any user with permission to create a subscription in your project can write to the Bigtable table. If you want to provide more granular permissions, configure a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) instead.

The following permissions are required to configure a user-managed service account to write to Bigtable:

  * The user-managed service account must have the **Bigtable User** role.

  * The **Cloud Pub/Sub** service account must have the `iam.serviceAccounts.getAccessToken` permission on the user-managed service account.

  * The user creating the subscription must have the `iam.serviceAccounts.actAs` permission on the user-managed service account.




When you create the subscription, specify the user-managed service account. For more information, see Create a Bigtable subscription.

## Bigtable table writes

This section describes how a Bigtable subscription writes Pub/Sub messages to a table.

### Message data

A Bigtable subscription writes the Pub/Sub message data to a column family named `data`.

  * Each row contains the data from one message.

  * The row key is a concatenation of the subscription ID, a message ID salt prefix, and the message ID, in the following format:

`"projects/PROJECT_NUMBER/subscriptions/SUBSCRIPTION_ID#SALT_PREFIX#MESSAGE_ID"`

  * The message data is written to a single column in the `data` column family. The column has an empty-string (`""`) column qualifier.

  * Data is written as a [`BYTES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/data-types#bytes_type) type.

  * The cell's timestamp is the message's [publish time](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage).




### Message metadata

By default, the subscription doesn't write message metadata to the table. Optionally, you can enable writing metadata when you create a Bigtable subscription.

If writing metadata is enabled, the subscription writes the message metadata to a column family named `pubsub_metadata`. Before you create the subscription, ensure that your table has a column family with this name.

For each message, the subscription writes a new row with the following columns under the `pubsub_metadata` column family.

Column | Value | Data type  
---|---|---  
`subscription_name` | The name of the subscription | String  
`message_id` | The message ID | String  
`attributes` | A JSON object that contains the [message attributes](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes) | String  
  
## Create a Bigtable subscription

To create a Bigtable subscription, use the [`gcloud beta pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/create) command:
    
    
    gcloud beta pubsub subscriptions create SUBSCRIPTION_ID \
      --topic=TOPIC_ID \
      --bigtable-table=projects/PROJECT_ID/instances/INSTANCE_ID/tables/TABLE_ID
    

Replace the following:

  * `SUBSCRIPTION_ID`: A name for the subscription.
  * `TOPIC_ID`: The name or ID of the topic to read from.
  * `PROJECT_ID`: The project ID.
  * `INSTANCE_ID`: The ID of the Bigtable instance that contains the table.
  * `TABLE_ID`: The ID of the table to write to. The table must have a column family named `data`.



The following flags are optional:

  * `--bigtable-write-metadata`: Specifies whether to write message metadata. If you omit this flag, the subscription doesn't write metadata. For more information, see Message metadata.

  * `--bigtable-app-profile-id`=APP_PROFILE: Specifies an [app profile](https://docs.cloud.google.com/bigtable/docs/app-profiles) to use for Bigtable writes. The app profile must use [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). If this flag isn't specified, the subscription uses the default app profile.

  * `--bigtable-service-account-email`: Specifies a service account to use when writing to Bigtable. If not specified, the subscription uses the Pub/Sub service agent. For more information, see Use a custom service account.




## Example: Write from Pub/Sub to Bigtable

The following example shows how to create a Bigtable subscription, use the subscription to write Pub/Sub messages to a Bigtable table, and then query the table.

  1. Create a new Bigtable instance named `my-instance`.
         
         gcloud bigtable instances create my-instance --display-name="My instance" \
           --cluster-config=id=my-cluster-1,zone=ZONE,nodes=1
         

Replace ZONE with the [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs. Example: `us-central1-b`

  2. Create a Bigtable table named `table-1` with a column family named `data`.
         
         gcloud bigtable instances tables create table-1 \
           --instance=my-instance \
           --column-families=data
         

  3. Create a Pub/Sub topic named `topic-1`.
         
         gcloud pubsub topics create topic-1
         

  4. Create a Bigtable subscription that reads from the topic.
         
         gcloud beta pubsub subscriptions create bigtable-sub \
           --topic=topic-1 \
           --bigtable-table=projects/PROJECT_ID/instances/my-instance/tables/table-1
         

Replace PROJECT_ID with your Google Cloud project ID.

  5. Publish a message to the topic.
         
         gcloud pubsub topics publish topic-1 --message='{"name":"Alice"}'
         

If the message is successfully published, the output is the message ID:
         
         messageIds:
         - 'MESSAGE_ID'
         




The Bigtable subscription writes the message data to the `data` column family. To query the data, perform the following steps:

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Go to Instances](https://console.cloud.google.com/bigtable)

  2. Click the instance named `my-cluster-1`.

  3. In the navigation menu, click **Bigtable Studio**.

  4. In the [query editor](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#query-editor), run the following SQL query.
         
         SELECT _key, JSON_VALUE(CAST(data[''] AS STRING), '$.name') AS name FROM table-1;
         

The query result looks like the following:
         
         +-------------------+
         | _key      | name  |
         +-----------|-------+
         | "ROW_KEY" | Alice |
         +-------------------+
         

The message data is stored as a `BYTES` type. In this example, the data is a JSON string, so the query can use GoogleSQL [JSON functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions) to parse the data.




## Monitor a Bigtable subscription

Cloud Monitoring provides a number of metrics to [monitor subscriptions](https://docs.cloud.google.com/pubsub/docs/monitoring#maintain_a_healthy_subscription).

For a list of all the available metrics related to Pub/Sub and their descriptions, see the [Monitoring documentation for Pub/Sub](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub).

You can also monitor subscriptions from [within Pub/Sub](https://docs.cloud.google.com/pubsub/docs/monitor-subscription).

## What's next

  * Learn more about [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions).
  * [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber).
  * [Troubleshoot Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/troubleshoot-bigtable-subscriptions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
