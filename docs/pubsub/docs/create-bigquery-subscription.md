---
url: https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription/
title: Create BigQuery subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:57.835791+00:00
---

# Create BigQuery subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create BigQuery subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a BigQuery subscription. You can use the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API to create a BigQuery subscription.

## Before you begin

Before reading this document, ensure that you're familiar with the following:

  * How [subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview) work.

  * The workflow for [BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/bigquery).

  * How to configure a [dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) to handle message failures.




In addition to your familiarity with Pub/Sub and BigQuery, ensure that you meet the following prerequisites before you create a BigQuery subscription:

  * A BigQuery table exists. Alternatively, you can create one when you create the BigQuery subscription as described in the later sections of this document.

  * Compatibility between the schema of the Pub/Sub topic and the BigQuery table. If you add a non-compatible BigQuery table, you get a compatibility-related error message. For more information, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).




## Required roles and permissions

To get the permissions that you need to create a BigQuery subscription, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a BigQuery subscription. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a BigQuery subscription:

  * `pubsub.subscriptions.create` on the project
  * `pubsub.topics.attachSubscription` on the topic



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Cross-project subscriptions

If you create a subscription in one project for a topic in another project, you must have `pubsub.subscriptions.create` permission on the project in which you are creating the subscription, and `pubsub.topics.attachSubscription` permission on the topic.

## Grant IAM roles to the service account

Pub/Sub uses an Identity and Access Management (IAM) service account to access Google Cloud resources. By default, it uses the Pub/Sub service agent (`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`).

To enable Pub/Sub to write to a BigQuery table, the service account requires the **BigQuery Data Editor** (`roles/bigquery.dataEditor`) role. You can give the service account permissions either for the project or the table, as follows:

### Project

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants**.

  3. Find the row for the **Cloud Pub/Sub** service account and click mode_edit **Edit principal**.

  4. Click **Add another role** and select the **BigQuery Data Editor** role.




For more information, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).

### Table

  1. In the Google Cloud console, go to **BigQuery Studio**.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

  2. In the Explorer pane search box labeled **Filter by name and labels** , type the name of the table and press **Enter**.

  3. In the search results, click the name of the table to which you want to grant permission.

  4. In the **Details** tab, click person_add **Share** > **Manage permissions**.

  5. Click person_add **Add principal** , then enter the service account identifier, in the following format:

`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`.

  6. In the **Assign roles** list, select **BigQuery Data Editor**.

  7. Click **Save**. The principal is granted the role on the resource.




### Use a custom service account

By granting the **BigQuery Data Editor** role to the **Cloud Pub/Sub** service account, any user who has permission to create a subscription in your project can write to the BigQuery table. If you want to provide more granular permissions, configure a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) instead.

The following permissions are required to configure a user-managed service account to write to BigQuery:

  * The user-managed service account must have the **BigQuery Data Editor** role.

  * The **Cloud Pub/Sub** service account must have the `iam.serviceAccounts.getAccessToken` permission on the user-managed service account.

  * The user creating the subscription must have the `iam.serviceAccounts.actAs` permission on the user-managed service account.




When you create the subscription, specify the user-managed service account as the subscription service account.

## BigQuery subscription properties

BigQuery subscriptions support all of the [common subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties). The following sections describe properties that are specific to BigQuery subscriptions.

### Use topic schema

This option lets Pub/Sub use the [schema of the Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/schemas) to which the subscription is attached. In addition, Pub/Sub writes the fields in messages to the corresponding columns in the BigQuery table.

**Caution:** Deleting a schema or a schema revision is permanent. Any messages that validated against a deleted schema revision at the time of publish cannot be written to BigQuery using a BigQuery subscription with **Use topic schema** enabled. Instead of deleting a schema or revision, consider [rolling back a schema](https://docs.cloud.google.com/pubsub/docs/roll-back-schemas).

When you use this option, remember to check the following additional requirements:

  * The fields in the topic schema and the BigQuery schema must have the same names and their types must be compatible with each other.

  * Any optional field in the topic schema must also be optional in the BigQuery schema.

  * Required fields in the topic schema don't need to be required in the BigQuery schema.

  * If there are BigQuery fields that are not present in the topic schema, these BigQuery fields must be in mode `NULLABLE`.

  * If the topic schema has additional fields that are not present in the BigQuery schema and these fields can be dropped, select the option **Drop unknown fields**.

  * You can select only one of the subscription properties, **Use topic schema** or **Use table schema**.




If you don't select the **Use topic schema** or **Use table schema** option, ensure that the BigQuery table has a column called `data` of type `BYTES`, `STRING`, or `JSON`. Pub/Sub writes the message to this BigQuery column.

You might not see changes to the Pub/Sub topics schema or BigQuery table schema take effect immediately with messages written to the BigQuery table. For example, if the **Drop unknown fields** option is enabled and a field is present in the Pub/Sub schema, but not the BigQuery schema, messages written to the BigQuery table might still not contain the field after adding it to the BigQuery schema. Eventually, the schemas synchronize and subsequent messages include the field.

When you use the **Use topic schema** option for your BigQuery subscription, you can also take advantage of BigQuery change data capture (CDC). CDC updates your BigQuery tables by processing and applying changes to existing rows.

To learn more about this feature, see [Stream table updates with change data capture](https://docs.cloud.google.com/bigquery/docs/change-data-capture).

To learn how to use this feature with BigQuery subscriptions, see [BigQuery change data capture](https://docs.cloud.google.com/pubsub/docs/bigquery#change_data_capture).

### Use table schema

This option lets Pub/Sub use the schema of the BigQuery table to write the fields of a JSON message to the corresponding columns. When you use this option, remember to check the following additional requirements:

  * The names of each column in the BigQuery table must only contain letters (a-z, A-Z), numbers (0-9), or underscores (_).

  * Published messages must be in JSON format.

If a BigQuery table column has the `JSON` data type, the corresponding field in your Pub/Sub message must be valid, JSON in an escaped string. For example, for a column named `myData`, the message field must be `"myData": "{\"key\":\"value\"}"`. BigQuery rejects messages that don't contain valid JSON.

  * The following JSON conversions are supported:

**JSON Type** | **BigQuery Data Type**  
---|---  
`string` | `NUMERIC`, `BIGNUMERIC`, `DATE`, `TIME`, `DATETIME`, or `TIMESTAMP`  
`number` | `NUMERIC`, `BIGNUMERIC`, `DATE`, `TIME`, `DATETIME`, or `TIMESTAMP`  
    * When using `number` to `DATE`, `DATETIME`, `TIME`, or `TIMESTAMP` conversions, the number must adhere to the [supported representations](https://docs.cloud.google.com/pubsub/docs/bigquery#date_time_int).
    * When using `number` to `NUMERIC` or `BIGNUMERIC` conversion, the precision and range of values is limited to those accepted by the [IEEE 754 standard for floating-point arithmetic](https://ieeexplore.ieee.org/document/8766229). If you require high precision or a wider range of values, use `string` to `NUMERIC` or `BIGNUMERIC` conversions instead.
    * When using `string` to `NUMERIC` or `BIGNUMERIC` conversions, Pub/Sub assumes the string is a human readable number (e.g. `"123.124"`). If processing the string as a human readable number fails, Pub/Sub treats the string as bytes encoded with the [BigDecimalByteStringEncoder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigDecimalByteStringEncoder).
  * If the subscription's topic [has a schema associated with it](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic), then the message encoding property must be set to `JSON`.

  * If there are BigQuery fields that are not present in the messages, these BigQuery fields must be in mode `NULLABLE`.

  * If the messages have additional fields that are not present in the BigQuery schema and these fields can be dropped, select the option **Drop unknown fields**.

  * You can select only one of the subscription properties, **Use topic schema** or **Use table schema**.




If you don't select the **Use topic schema** or **Use table schema** option, ensure that the BigQuery table has a column called `data` of type `BYTES`, `STRING`, or `JSON`. Pub/Sub writes the message to this BigQuery column.

You might not see changes to the BigQuery table schema take effect immediately with messages written to the BigQuery table. For example, if the **Drop unknown fields** option is enabled and a field is present in the messages, but not in the BigQuery schema, messages written to the BigQuery table might still not contain the field after adding it to the BigQuery schema. Eventually, the schema synchronizes and subsequent messages include the field.

When you use the **Use table schema** option for your BigQuery subscription, you can also take advantage of BigQuery change data capture (CDC). CDC updates your BigQuery tables by processing and applying changes to existing rows.

To learn more about this feature, see [Stream table updates with change data capture](https://docs.cloud.google.com/bigquery/docs/change-data-capture).

To learn how to use this feature with BigQuery subscriptions, see [BigQuery change data capture](https://docs.cloud.google.com/pubsub/docs/bigquery#change_data_capture).

### Drop unknown fields

This option is used with the **Use topic schema** or **Use table schema** option. When enabled, this option lets Pub/Sub drop any field that is present in the topic schema or message but not in the BigQuery schema. The fields that are not part of the BigQuery schema are dropped when writing the message to the BigQuery table.

Without **Drop unknown fields** set, messages with extra fields are not written to BigQuery and remain in the subscription backlog unless you configure a [dead letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics).

The **Drop unknown fields** setting does not affect fields that are not defined in either the Pub/Sub topic schema or the BigQuery table schema. In this case, a valid Pub/Sub message is delivered to the subscription. However, because BigQuery does not have columns defined for these extra fields, these fields are dropped during the BigQuery writing process. To prevent this behavior, ensure that any field contained in the Pub/Sub message is also contained in the BigQuery table schema.

The behavior regarding extra fields can also depend on the specific schema type (Avro, Protocol Buffer) and encoding (JSON, Binary) used. For information about how these factors affect the handling of extra fields, see the documentation for your specific schema type and encoding.

### Write metadata

This option lets Pub/Sub write the metadata of each message to additional columns in the BigQuery table. Else, the metadata is not written to the BigQuery table.

If you select the **Write metadata** option, ensure that the BigQuery table has the fields described in the following table.

If you don't select the **Write metadata** option, then the destination BigQuery table only requires the `data` field unless `use_topic_schema` is true. If you select both the **Write metadata** and **Use topic schema** options, then the schema of the topic must not contain any fields with names that match those of the metadata parameters. This limitation includes camelcase versions of these snake case parameters.

Parameters  
---  
`subscription_name` |  STRING Name of a subscription.  
`message_id` |  STRING ID of a message  
`publish_time` |  TIMESTAMP The time of publishing a message.  
`data` |  BYTES, STRING, or JSON The message body. The `data` field is required for all destination BigQuery tables that don't select **Use topic schema** or **Use table schema**. If the field is of type JSON, then the message body must be valid JSON.  
`attributes` |  STRING or JSON A JSON object containing all message attributes. It also contains additional fields that are part of the Pub/Sub message including the ordering key, if present.  
  
### Service account

You have the following options to write messages to a BigQuery table:

  * Configure a [custom service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) so that only users who have the `iam.serviceAccounts.actAs` permission on the service account can create a subscription that writes to the table. An example role that includes the `iam.serviceAccounts.actAs` permission is the **Service Account User** (`roles/iam.serviceAccountUser`) role.

  * Use the default Pub/Sub service agent that lets any user with the ability to create subscriptions in the project to create a subscription that writes to the table. The Pub/Sub service agent is the default setting when you don't specify a custom service account.




## Create a BigQuery subscription

To create a subscription with BigQuery delivery, perform the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Create subscription** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription/create)

  2. For the **Subscription ID** field, enter a name. For information on how to name a subscription, see [Guidelines to name a topic or a subscription](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  3. In the **Select a Cloud Pub/Sub topic** box, type or select the topic to receive messages from.

  4. For **Delivery type** , select **Write to BigQuery**.

  5. Select the BigQuery table:

     1. For **Project** , select the Google Cloud project that contains the BigQuery table.

     2. For **Dataset** , select an existing dataset or click **Create new dataset** to create a new dataset. For information about creating a dataset, see [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets).

     3. In the **Table** field, enter the name of the table. To create a new table, click the link that takes you to the BigQuery **Create new table** page. The page opens in a separate tab. For information about creating a table, see [Create and use tables](https://docs.cloud.google.com/bigquery/docs/tables).

  6. For **Schema Configuration** , select one of the following options:

     * **Don't use a schema**. Pub/Sub writes the message bytes to a column named `data`.

     * **Use topic schema**. Pub/Sub uses the schema that is associated with the topic. For more information, see Use topic schema.

     * **Use table schema**. Pub/Sub uses the schema of the BigQuery table. For more information, see Use table schema.

  7. Optional. To write message metadata to the BigQuery table, select **Write metadata**. For more information, see Write metadata.

  8. Optional. To drop fields that are not present in the BigQuery table schema, select **Drop unknown fields**. For more information, see Drop unknown fields.

  9. Configure the [common subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties) as needed. We strongly recommend that you enable **Dead lettering** to handle message failures. For more information, see [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic).

  10. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a Pub/Sub subscription, use the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command:
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID \
             --topic=TOPIC_ID \
             --bigquery-table=PROJECT_ID.DATASET_ID.TABLE_ID
         

If you want to use a custom service account, provide it as an additional argument:
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID \
             --topic=TOPIC_ID \
             --bigquery-table=PROJECT_ID.DATASET_ID.TABLE_ID \
             --bigquery-service-account-email=SERVICE_ACCOUNT_NAME
         

Replace the following:

     * `SUBSCRIPTION_ID`: Specifies the ID of the subscription.
     * `TOPIC_ID`: Specifies the ID of the topic. The topic requires a schema.
     * `PROJECT_ID`: Specifies the ID of the project.
     * `DATASET_ID`: Specifies the ID of an existing dataset. To create a dataset, see [ Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset).
     * `TABLE_ID`: Specifies the ID of an existing table. The table requires a `data` field if your topic doesn't have a schema. To create a table, see [Create an empty table with a schema definition](https://docs.cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition).
     * `SERVICE_ACCOUNT_NAME`: Specifies the name of the service account to use to write to BigQuery.



###  C++ 

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id, std::string const& topic_id,
       std::string const& subscription_id, std::string const& table_id) {
      google::pubsub::v1::Subscription request;
      request.set_name(
          pubsub::Subscription(project_id, subscription_id).FullName());
      request.set_topic(pubsub::Topic(project_id, topic_id).FullName());
      request.mutable_bigquery_config()->set_table(table_id);
      auto sub = client.CreateSubscription(request);
      if (!sub) {
        if (sub.status().code() == google::cloud::StatusCode::kAlreadyExists) {
          std::cout << "The subscription already exists\n";
          return;
        }
        throw std::move(sub).status();
      }
    
      std::cout << "The subscription was successfully created: "
                << sub->DebugString() << "\n";
    }

###  C# 

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class CreateBigQuerySubscriptionSample
    {
        public Subscription CreateBigQuerySubscription(string projectId, string topicId, string subscriptionId, string bigqueryTableId)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
    
            var subscriptionRequest = new [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html)
            {
                SubscriptionName = subscriptionName,
                TopicAsTopicName = topicName,
                BigqueryConfig = new [BigQueryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.BigQueryConfig.html)
                {
                    Table = bigqueryTableId
                }
            };
            var subscription = subscriber.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(subscriptionRequest);
            return subscription;
        }
    }

###  Go 

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    // createBigQuerySubscription creates a Pub/Sub subscription that exports messages to BigQuery.
    func createBigQuerySubscription(w io.Writer, projectID, topic, subscription, table string) error {
    	// projectID := "my-project"
    	// topic := "projects/my-project-id/topics/my-topic"
    	// subscription := "projects/my-project/subscriptions/my-sub"
    	// table := "my-project-id.dataset_id.table_id"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub, err := client.SubscriptionAdminClient.CreateSubscription(ctx, &pubsubpb.Subscription{
    		Name:  subscription,
    		Topic: topic,
    		BigqueryConfig: &pubsubpb.BigQueryConfig{
    			Table:         table,
    			WriteMetadata: true,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create subscription: %w", err)
    	}
    	fmt.Fprintf(w, "Created BigQuery subscription: %v\n", sub)
    
    	return nil
    }
    

###  Java 

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.pubsub.v1.[BigQueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.BigQueryConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import java.io.IOException;
    
    public class CreateBigQuerySubscriptionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
        String bigqueryTableId = "your-project.your-dataset.your-table";
    
        createBigQuerySubscription(projectId, topicId, subscriptionId, bigqueryTableId);
      }
    
      public static void createBigQuerySubscription(
          String projectId, String topicId, String subscriptionId, String bigqueryTableId)
          throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
    
          [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(projectId, topicId);
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [BigQueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.BigQueryConfig.html) bigqueryConfig =
              [BigQueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.BigQueryConfig.html).newBuilder().setTable(bigqueryTableId).setWriteMetadata(true).build();
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
              subscriptionAdminClient.createSubscription(
                  [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html).newBuilder()
                      .setName(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                      .setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__)())
                      .[setBigqueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.Builder.html#com_google_pubsub_v1_Subscription_Builder_setBigqueryConfig_com_google_pubsub_v1_BigQueryConfig_)(bigqueryConfig)
                      .build());
    
          System.out.println("Created a BigQuery subscription: " + subscription.getAllFields());
        }
      }
    }

###  Node.js 

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const bigqueryTableId = 'YOUR_TABLE_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createBigQuerySubscription(
      topicNameOrId,
      subscriptionNameOrId,
      bigqueryTableId,
    ) {
      const options = {
        bigqueryConfig: {
          table: bigqueryTableId,
          writeMetadata: true,
        },
      };
    
      await pubSubClient
        .topic(topicNameOrId)
        .createSubscription(subscriptionNameOrId, options);
    
      console.log(`Subscription ${subscriptionNameOrId} created.`);
    }

###  Node.ts 

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const bigqueryTableId = 'YOUR_TABLE_ID';
    
    // Imports the Google Cloud client library
    import {PubSub, CreateSubscriptionOptions} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createBigQuerySubscription(
      topicNameOrId: string,
      subscriptionNameOrId: string,
      bigqueryTableId: string,
    ) {
      const options: CreateSubscriptionOptions = {
        bigqueryConfig: {
          table: bigqueryTableId,
          writeMetadata: true,
        },
      };
    
      await pubSubClient
        .topic(topicNameOrId)
        .createSubscription(subscriptionNameOrId, options);
    
      console.log(`Subscription ${subscriptionNameOrId} created.`);
    }

###  PHP 

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    use Google\Cloud\PubSub\V1\BigQueryConfig;
    
    /**
     * Creates a Pub/Sub BigQuery subscription.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $subscriptionName  The Pub/Sub subscription name.
     * @param string $table      The BigQuery table to which to write.
     */
    function create_bigquery_subscription($projectId, $topicName, $subscriptionName, $table)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $topic = $pubsub->topic($topicName);
        $subscription = $topic->subscription($subscriptionName);
        $config = new BigQueryConfig(['table' => $table]);
        $subscription->create([
            'bigqueryConfig' => $config
        ]);
    
        printf('Subscription created: %s' . PHP_EOL, $subscription->name());
    }

###  Python 

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # bigquery_table_id = "your-project.your-dataset.your-table"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    bigquery_config = pubsub_v1.types.[BigQueryConfig](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.BigQueryConfig.html)(
        table=bigquery_table_id, write_metadata=True
    )
    
    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "bigquery_config": bigquery_config,
            }
        )
    
    print(f"BigQuery subscription created: {subscription}.")
    print(f"Table for subscription is: {bigquery_table_id}")

###  Ruby 

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # bigquery_table_id = "my-project:dataset-id.table-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) project_id: project_id
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    subscription = subscription_admin.create_subscription \
      name: pubsub.subscription_path(subscription_id),
      topic: pubsub.topic_path(topic_id),
      bigquery_config: {
        table: bigquery_table_id,
        write_metadata: true
      }
    
    puts "BigQuery subscription created: #{subscription_id}."
    puts "Table for subscription is: #{bigquery_table_id}"

## Monitor a BigQuery subscription

Cloud Monitoring provides a number of metrics to [monitor subscriptions](https://docs.cloud.google.com/pubsub/docs/monitoring#maintain_a_healthy_subscription).

For a list of all the available metrics related to Pub/Sub and their descriptions, see the [Monitoring documentation for Pub/Sub](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub).

You can also monitor subscriptions from [within Pub/Sub](https://docs.cloud.google.com/pubsub/docs/monitor-subscription).

## What's next

  * Create or modify a subscription with [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).
  * Create or modify a subscription with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).
  * Troubleshoot a [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery-troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
