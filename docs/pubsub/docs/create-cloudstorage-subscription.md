---
url: https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription/
title: Create Cloud Storage subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:46.624592+00:00
---

# Create Cloud Storage subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create Cloud Storage subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a Cloud Storage subscription. You can use the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API to create a Cloud Storage subscription.

## Before you begin

Before reading this document, ensure that you're familiar with the following:

  * How a [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/cloudstorage) works.
  * How [Cloud Storage](https://docs.cloud.google.com/storage/docs) works and how to create and manage [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * How to configure a [dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) to handle message failures.



## Required roles and permissions

To get the permissions that you need to create a Cloud Storage subscription, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a Cloud Storage subscription. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Cloud Storage subscription:

  * `pubsub.subscriptions.create` on the project
  * `pubsub.topics.attachSubscription` on the topic



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Cross-project subscriptions

If you create a subscription in one project for a topic in another project, you must have `pubsub.subscriptions.create` permission on the project in which you are creating the subscription, and `pubsub.topics.attachSubscription` permission on the topic.

## Grant IAM roles to the service account

Pub/Sub uses an Identity and Access Management (IAM) service account to access Google Cloud resources. By default, it uses the Pub/Sub service agent (`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`).

To enable Pub/Sub to write to Cloud Storage, the service account requires the following roles:

  * **Storage Object Creator** (`roles/storage.objectCreator`)
  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)



You can give the service account permissions either for the project or the Cloud Storage bucket, as follows:

### Project

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Select **Include Google-provided role grants**.

  3. Find the row for the **Cloud Pub/Sub** service account and click mode_edit **Edit principal**.

  4. Click **Add another role** and select the **Storage Object Creator** role. Repeat this step for the **Storage Legacy Bucket Reader** role.




For more information, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).

###  Cloud Storage bucket 

  1. In the Google Cloud console, go to **Buckets**.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the Cloud Storage bucket to which you want to grant permission.

  3. In the **Bucket details** page, click the **Permissions** tab.

  4. In the **Permissions** pane, click the **View by principals** tab.

  5. Click **Grant access**.

  6. In the **New principals** field, enter the service account identifier, in the following format:

`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`.

  7. In the **Assign roles** list, select **Storage Object Creator**.

  8. Click add **Add another role** and select **Storage Legacy Bucket Reader**.

  9. Click **Save**. The principal is granted the roles on the resource.




### Use a custom service account

By granting the **Storage Object Creator** and **Storage Legacy Bucket Reader** roles to the **Cloud Pub/Sub** service account, any user who has permission to create a subscription in your project can write to the Cloud Storage bucket. If you want to provide more granular permissions, configure a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) instead.

The following permissions are required to configure a user-managed service account to write to Cloud Storage:

  * The user-managed service account must have the **Storage Object Creator** and **Storage Legacy Bucket Reader** roles.

  * The **Cloud Pub/Sub** service account must have the `iam.serviceAccounts.getAccessToken` permission on the user-managed service account.

  * The user creating the subscription must have the `iam.serviceAccounts.actAs` permission on the user-managed service account.




When you create the subscription, specify the user-managed service account as the subscription service account.

## Cloud Storage subscription properties

Cloud Storage subscriptions support all of the [common subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties). The following sections describe properties that are specific to Cloud Storage subscriptions.

### Bucket name

A Cloud Storage bucket must already exist before you create a Cloud Storage subscription.

The messages are sent as batches and stored in the Cloud Storage bucket. A single batch or file is stored as an [object](https://docs.cloud.google.com/storage/docs/objects) in the bucket.

The Cloud Storage bucket must have [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) disabled.

To create a Cloud Storage bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

### Filename prefix, suffix, and datetime

The output Cloud Storage files generated by the Cloud Storage subscription are stored as objects in the Cloud Storage bucket. The name of the object stored in the Cloud Storage bucket is of the following format: `<file-prefix><UTC-date-time>_<uuid><file-suffix>`.

The following list includes details of the file format and the fields that you can customize:

  * `<file-prefix>` is the custom filename prefix. This is an optional field.

  * `<UTC-date-time>` is a customizable auto-generated string based on the time the object is created.

  * `<uuid>` is an auto-generated random string for the object.

  * `<file-suffix>` is the custom filename suffix. This is an optional field. The filename suffix cannot end in "/".

  * You can change the filename prefix and suffix:

    * For example, if the value of the filename prefix is `prod_` and the value of the filename suffix is `_archive`, a sample object name is `prod_2023-09-25T04:10:00+00:00_uN1QuE_archive`.

    * If you don't specify the filename prefix and suffix, the object name stored in the Cloud Storage bucket is of the format: `<UTC-date-time>_<uuid>`.

    * Cloud Storage object naming requirements also apply to the filename prefix and suffix. For more information, see [About Cloud Storage objects](https://docs.cloud.google.com/storage/docs/objects#naming).

  * You can change how the date and time are displayed in the filename:

    * Required datetime matchers that you can use only once: year (`YYYY` or `YY`), month (`MM`), day (`DD`), hour (`hh`), minute (`mm`), second (`ss`). For example, `YY-YYYY` or `MMM` is invalid.

    * Optional matchers that you can use only once: datetime separator (`T`) and timezone offset (`Z` or `+00:00`).

    * Optional elements that you can use multiple times: hyphen (`-`), underscore (`_`), colon (`:`), and forward slash (`/`).

    * For example, if the value of the filename datetime format is `YYYY-MM-DD/hh_mm_ssZ`, a sample object name is `prod_2023-09-25/04_10_00Z_uNiQuE_archive`.

    * If the filename datetime format ends in a character which is not a matcher, that character will replace the separator between `<UTC-date-time>` and `<uuid>`. For example, if the value of the filename datetime format is `YYYY-MM-DDThh_mm_ss-`, a sample object name is `prod_2023-09-25T04_10_00-uNiQuE_archive`.




### File batching

Cloud Storage subscriptions let you decide when you want to create a new output file that is stored as an object in the Cloud Storage bucket. Pub/Sub writes an output file when one of the specified batching conditions are met. The following are the Cloud Storage batching conditions:

  * **Storage batch max duration.** This is a required setting. Pub/Sub writes a new output file if the specified value for max duration is exceeded. The duration is measured from when Pub/Sub begins writing to a new file to the time the file is finalized. For example, if you set the max duration to 5 minutes, Pub/Sub finalizes the file at most 5 minutes after Pub/Sub began writing to the file. A new file can be created before the max duration has passed. If you don't specify the value, a default value of 5 minutes is applied. The following are the applicable values for max duration:

    * Minimum value = 1 minute
    * Default value = 5 minutes
    * Maximum value = 10 minutes
  * **Storage batch max bytes.** This is an optional setting. The Cloud Storage subscription writes a new output file if the specified value of max bytes is exceeded. The following are the applicable values for max bytes:

    * Minimum value = 1 KB
    * Maximum value = 10 GiB
  * **Storage batch max messages.** This is an optional setting. The Cloud Storage subscription writes a new output file if the specified number of max messages is exceeded. The following are the applicable values for max messages:

    * Minimum value = 1000



For example, you can configure max duration as 6 minutes and max bytes as 2 GB. If at the 4th minute, the output file reaches a file size of 2 GB, Pub/Sub finalizes the previous file and starts writing to a new file.

A Cloud Storage subscription might write to multiple files in a Cloud Storage bucket simultaneously. If you have configured your subscription to create a new file every 6th minute, you might observe multiple Cloud Storage files being created every 6 minutes.

In some situations, Pub/Sub might start writing to a new file earlier than the time configured by the file batching conditions. A file might also exceed the Max bytes value if the subscription receives messages larger than the Max bytes value.

### File format

When you create a Cloud Storage subscription, you can specify the format of the output files that are to be stored in a Cloud Storage bucket as **Text** or **Avro**.

  * **Text** : The messages are stored as plain text. A newline character separates a message from the previous message in the file. Only message payloads are stored, not attributes or other metadata.

  * **Avro** : The messages are stored in [Apache Avro binary](https://avro.apache.org/docs/1.11.1/specification/#binary-encoding) format. When you select **Avro** , you can enable the following additional properties:

    * **Write metadata** : This option lets you store the message metadata along with the message. Metadata such as `subscription_name`, `message_id`, `publish_time`, and `attributes` fields are written to top-level fields in the output Avro object while all other message properties other than data (for example, an ordering_key, if present) are added as entries in the `attributes` map.

If **write metadata** is disabled, only the message payload is written to the output Avro object. Here is the Avro schema for the output messages with **write metadata** disabled:
          
          {
            "type": "record",
            "namespace": "com.google.pubsub",
            "name": "PubsubMessage",
            "fields": [
              { "name": "data", "type": "bytes" }
            ]
          }
          

Here is the Avro schema for the output messages with **write metadata** enabled:
          
          {
            "type": "record",
            "namespace": "com.google.pubsub",
            "name": "PubsubMessageWithMetadata",
            "fields": [
              { "name": "subscription_name", "type": "string" },
              { "name": "message_id", "type": "string"  },
              { "name": "publish_time", "type": {
                  "type": "long",
                  "logicalType": "timestamp-micros"
                }
              },
              { "name": "attributes", "type": { "type": "map", "values": "string" } },
              { "name": "data", "type": "bytes" }
            ]
          }
          

    * **Use topic schema** : This option lets Pub/Sub use the [schema of the Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/schemas) to which the subscription is attached when writing Avro files.

When you use this option, remember to check the following additional requirements:

      * The topic schema must be in [Apache Avro format](https://docs.cloud.google.com/pubsub/docs/schemas#avro-format).

      * If both **use topic schema** and **write metadata** are enabled, the topic schema must have a [Record](https://avro.apache.org/docs/1.11.1/specification/#schema-record) object at its root. Pub/Sub will expand the Record's list of fields to include the metadata fields. As a result, the Record cannot contain any fields with the same name as the metadata fields (`subscription_name`, `message_id`, `publish_time`, or `attributes`).


**Note:** For users interested in writing files in Parquet format, the best way to stream Pub/Sub data into Parquet files is by using a BigQuery subscription with [BigQuery tables for Apache Iceberg](https://docs.cloud.google.com/bigquery/docs/iceberg-tables). For more information, see [BigQuery subscriptions with Iceberg tables](https://docs.cloud.google.com/pubsub/docs/bigquery#iceberg_tables).

### Service account

You have the following options to write messages to a Cloud Storage bucket:

  * Configure a [custom service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) so that only users who have the `iam.serviceAccounts.actAs` permission on the service account can create a subscription that writes to the bucket. An example role that includes the `iam.serviceAccounts.actAs` permission is the **Service Account User** (`roles/iam.serviceAccountUser`) role.

  * Use the default Pub/Sub service agent that lets any user with the ability to create subscriptions in the project to create a subscription that writes to the bucket. The Pub/Sub service agent is the default setting when you don't specify a custom service account.




## Create a Cloud Storage subscription

### Console

  1. In the Google Cloud console, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click **Create subscription**.

  3. For the **Subscription ID** field, enter a name.

For information about how to name a subscription, see [Guidelines to name a topic or a subscription](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. Choose or create a topic from the drop-down menu.

The subscription receives messages from the topic.

For information about how to create a topic, see [Create and manage topics](https://docs.cloud.google.com/pubsub/docs/create-topic).

  5. Select **Delivery type** as **Write to Cloud Storage**.

  6. For the Cloud Storage bucket, click **Browse**.

     * You can select an existing bucket from any appropriate project.

     * You can also click the create icon and follow the instructions on the screen to create a new bucket.

After you create the bucket, select the bucket for the Cloud Storage subscription.

For more information about how to create a bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

When you specify the bucket, Pub/Sub checks for the appropriate permissions on the bucket for the Pub/Sub service agent. If there are permissions issues, you see a message similar to the following: `Unable to verify if the Pub/Sub service agent has write permissions on this bucket. You may be lacking permissions to view or set permissions`.

  7. If you get permission issues, click **Set Permission** and follow the on-screen instructions. 

Alternatively, follow the instructions in Assign Cloud Storage roles to the Pub/Sub service agent.

  8. For **File format** , select **Text** or **Avro**.

If you select **Avro** , you can also optionally specify if you want to store the message metadata in the output. 

For more information about the two options including the message metadata option for the Avro format, see File format.

  9. Optional: You can specify the **File name prefix, suffix, and datetime** for all your files that are to be written to the Cloud Storage bucket. A file is stored as an [object](https://docs.cloud.google.com/storage/docs/objects) in the bucket.

For more information about how to set the file prefix, suffix, and datetime, see Filename prefix, suffix, and datetime. 

  10. For **File batching** , specify a maximum time to elapse before creating a new file.

You can also optionally set the maximum file size or maximum number of messages for the files.

For more information about both file batching options, see File batching.

  11. We strongly recommend that you enable **Dead lettering** to handle message failures.

For more information, see [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic).

  12. You can keep the other settings as their defaults and click **Create**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a Cloud Storage subscription, run the [`gcloud pubsub subscriptions create` command](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create). 
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID \
             --topic=TOPIC_ID \
             --cloud-storage-bucket=BUCKET_NAME \
             --cloud-storage-file-prefix=CLOUD_STORAGE_FILE_PREFIX \
             --cloud-storage-file-suffix=CLOUD_STORAGE_FILE_SUFFIX \
             --cloud-storage-file-datetime-format=CLOUD_STORAGE_FILE_DATETIME_FORMAT \
             --cloud-storage-max-duration=CLOUD_STORAGE_MAX_DURATION \
             --cloud-storage-max-bytes=CLOUD_STORAGE_MAX_BYTES \
             --cloud-storage-max-messages=CLOUD_STORAGE_MAX_MESSAGES \
             --cloud-storage-output-format=CLOUD_STORAGE_OUTPUT_FORMAT \
             --cloud-storage-write-metadata
             --cloud-storage-use-topic-schema

If you want to use a custom service account, provide it as an additional argument:
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID \
             --topic=TOPIC_ID \
             --cloud-storage-bucket=BUCKET_NAME \
             --cloud-storage-file-prefix=CLOUD_STORAGE_FILE_PREFIX \
             --cloud-storage-file-suffix=CLOUD_STORAGE_FILE_SUFFIX \
             --cloud-storage-file-datetime-format=CLOUD_STORAGE_FILE_DATETIME_FORMAT \
             --cloud-storage-max-duration=CLOUD_STORAGE_MAX_DURATION \
             --cloud-storage-max-bytes=CLOUD_STORAGE_MAX_BYTES \
             --cloud-storage-max-messages=CLOUD_STORAGE_MAX_MESSAGES \
             --cloud-storage-output-format=CLOUD_STORAGE_OUTPUT_FORMAT \
             --cloud-storage-write-metadata
             --cloud-storage-use-topic-schema
             --cloud-storage-service-account-email=SERVICE_ACCOUNT_NAME
             

In the command, only `SUBSCRIPTION_ID`, the `--topic` flag, and the `--cloud-storage-bucket` flag are required. The remaining flags are optional and can be omitted. 

Replace the following:

     * `SUBSCRIPTION_ID`: The name or ID of your new Cloud Storage subscription.
     * `TOPIC_ID`: The name or ID of your topic.
     * `BUCKET_NAME`: Specifies the name of an existing bucket. For example, `prod_bucket`. The bucket name must not include the project ID. To create a bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).
     * `CLOUD_STORAGE_FILE_PREFIX`: Specifies the prefix for the Cloud Storage filename. For example, `log_events_`.
     * `CLOUD_STORAGE_FILE_SUFFIX`: Specifies the suffix for the Cloud Storage filename. For example, `.txt`.
     * `CLOUD_STORAGE_FILE_DATETIME_FORMAT`: Specifies the datetime format for the Cloud Storage filename. For example, `YYYY-MM-DD/hh_mm_ssZ`.
     * `CLOUD_STORAGE_MAX_DURATION`: The maximum duration that can elapse before a new Cloud Storage file is created. The value must be between 1m and 10m. For example, `5m`.
     * `CLOUD_STORAGE_MAX_BYTES`: The maximum bytes that can be written to a Cloud Storage file before a new file is created. The value must be between 1KB to 10GB. For example, `20MB`.
     * `CLOUD_STORAGE_MAX_MESSAGES`: The maximum number of messages that can be written to a Cloud Storage file before a new file is created. The value must be greater than or equal to 1000. For example, `100000`.
     * `CLOUD_STORAGE_OUTPUT_FORMAT`: The output format for data written to Cloud Storage. Values are as follows: 
       * `text`: Messages are written as raw text, separated by a newline. 
       * `avro`: Messages are written as an Avro binary. `--cloud-storage-write-metadata` and `--cloud-storage-use-topic-schema` only affect subscriptions with output format `avro`.
     * SERVICE_ACCOUNT_NAME: Specifies the name of the service account to use to write to Cloud Storage. 



### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id, std::string const& topic_id,
       std::string const& subscription_id, std::string const& bucket) {
      google::pubsub::v1::Subscription request;
      request.set_name(
          pubsub::Subscription(project_id, subscription_id).FullName());
      request.set_topic(pubsub::Topic(project_id, topic_id).FullName());
      request.mutable_cloud_storage_config()->set_bucket(bucket);
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

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateCloudStorageSubscriptionSample
    {
        public Subscription CreateCloudStorageSubscription(string projectId, string topicId, string subscriptionId,
            string bucket, string filenamePrefix, string filenameSuffix, TimeSpan maxDuration)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
    
            var subscriptionRequest = new [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html)
            {
                SubscriptionName = subscriptionName,
                TopicAsTopicName = topicName,
                CloudStorageConfig = new [CloudStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CloudStorageConfig.html)
                {
                    Bucket = bucket,
                    FilenamePrefix = filenamePrefix,
                    FilenameSuffix = filenameSuffix,
                    MaxDuration = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(maxDuration)
                }
            };
            var subscription = subscriber.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(subscriptionRequest);
            return subscription;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    // createCloudStorageSubscription creates a Pub/Sub subscription that exports messages to Cloud Storage.
    func createCloudStorageSubscription(w io.Writer, projectID, topic, subscription, bucket string) error {
    	// projectID := "my-project-id"
    	// topic := "projects/my-project-id/topics/my-topic"
    	// subscription := "projects/my-project/subscriptions/my-sub"
    	// bucket := "my-bucket" // bucket must not have the gs:// prefix
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub, err := client.SubscriptionAdminClient.CreateSubscription(ctx, &pubsubpb.Subscription{
    		Name:  subscription,
    		Topic: topic,
    		CloudStorageConfig: &pubsubpb.CloudStorageConfig{
    			Bucket:         bucket,
    			FilenamePrefix: "log_events_",
    			FilenameSuffix: ".avro",
    			OutputFormat: &pubsubpb.CloudStorageConfig_AvroConfig_{
    				AvroConfig: &pubsubpb.CloudStorageConfig_AvroConfig{
    					WriteMetadata: true,
    				},
    			},
    			MaxDuration: durationpb.New(1 * time.Minute),
    			MaxBytes:    1e8,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create cloud storage sub: %w", err)
    	}
    	fmt.Fprintf(w, "Created Cloud Storage subscription: %v\n", sub)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.pubsub.v1.[CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import java.io.IOException;
    
    public class CreateCloudStorageSubscriptionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
        String bucket = "your-bucket";
        String filenamePrefix = "log_events_";
        String filenameSuffix = ".text";
        [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) maxDuration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(300).build();
    
        createCloudStorageSubscription(
            projectId, topicId, subscriptionId, bucket, filenamePrefix, filenameSuffix, maxDuration);
      }
    
      public static void createCloudStorageSubscription(
          String projectId,
          String topicId,
          String subscriptionId,
          String bucket,
          String filenamePrefix,
          String filenameSuffix,
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) maxDuration)
          throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
    
          [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(projectId, topicId);
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.html) cloudStorageConfig =
              [CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.html).newBuilder()
                  .setBucket(bucket)
                  .[setFilenamePrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.Builder.html#com_google_pubsub_v1_CloudStorageConfig_Builder_setFilenamePrefix_java_lang_String_)(filenamePrefix)
                  .[setFilenameSuffix](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.Builder.html#com_google_pubsub_v1_CloudStorageConfig_Builder_setFilenameSuffix_java_lang_String_)(filenameSuffix)
                  .[setMaxDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.Builder.html#com_google_pubsub_v1_CloudStorageConfig_Builder_setMaxDuration_com_google_protobuf_Duration_)(maxDuration)
                  .build();
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
              subscriptionAdminClient.createSubscription(
                  [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html).newBuilder()
                      .setName(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                      .setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__)())
                      .[setCloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.Builder.html#com_google_pubsub_v1_Subscription_Builder_setCloudStorageConfig_com_google_pubsub_v1_CloudStorageConfig_)(cloudStorageConfig)
                      .build());
    
          System.out.println("Created a CloudStorage subscription: " + subscription.getAllFields());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicName = 'YOUR_TOPIC_NAME';
    // const subscriptionName = 'YOUR_SUBSCRIPTION_NAME';
    // const bucket = 'YOUR_BUCKET_ID';
    // const filenamePrefix = 'YOUR_FILENAME_PREFIX';
    // const filenameSuffix = 'YOUR_FILENAME_SUFFIX';
    // const maxDuration = 60;
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createCloudStorageSubscription(
      topicName,
      subscriptionName,
      bucket,
      filenamePrefix,
      filenameSuffix,
      maxDuration,
    ) {
      const options = {
        cloudStorageConfig: {
          bucket,
          filenamePrefix,
          filenameSuffix,
          maxDuration: {
            seconds: maxDuration,
          },
        },
      };
    
      await pubSubClient
        .topic(topicName)
        .createSubscription(subscriptionName, options);
    
      console.log(
        `Created subscription ${subscriptionName} with a cloud storage configuration.`,
      );
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicName = 'YOUR_TOPIC_NAME';
    // const subscriptionName = 'YOUR_SUBSCRIPTION_NAME';
    // const bucket = 'YOUR_BUCKET_ID';
    // const filenamePrefix = 'YOUR_FILENAME_PREFIX';
    // const filenameSuffix = 'YOUR_FILENAME_SUFFIX';
    // const maxDuration = 60;
    
    // Imports the Google Cloud client library
    import {CreateSubscriptionOptions, PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createCloudStorageSubscription(
      topicName: string,
      subscriptionName: string,
      bucket: string,
      filenamePrefix: string,
      filenameSuffix: string,
      maxDuration: number,
    ) {
      const options: CreateSubscriptionOptions = {
        cloudStorageConfig: {
          bucket,
          filenamePrefix,
          filenameSuffix,
          maxDuration: {
            seconds: maxDuration,
          },
        },
      };
    
      await pubSubClient
        .topic(topicName)
        .createSubscription(subscriptionName, options);
    
      console.log(
        `Created subscription ${subscriptionName} with a cloud storage configuration.`,
      );
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Creates a Pub/Sub GCS subscription.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $subscriptionName  The Pub/Sub subscription name.
     * @param string $bucket The Cloud Storage bucket name without any prefix like "gs://".
     */
    function create_cloud_storage_subscription($projectId, $topicName, $subscriptionName, $bucket)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $topic = $pubsub->topic($topicName);
        $subscription = $topic->subscription($subscriptionName);
        $config = ['bucket' => $bucket];
        $subscription->create([
            'cloudStorageConfig' => $config
        ]);
    
        printf('Subscription created: %s' . PHP_EOL, $subscription->name());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/pubsub/docs/authentication#client-libs). 
    
    
    from google.cloud import pubsub_v1
    from google.protobuf import duration_pb2
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # bucket = "my-bucket"
    
    filename_prefix = "log_events_"
    filename_suffix = ".avro"
    # Either CloudStorageConfig.AvroConfig or CloudStorageConfig.TextConfig
    # defaults to TextConfig
    avro_config = pubsub_v1.types.[CloudStorageConfig](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.CloudStorageConfig.html).[AvroConfig](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.CloudStorageConfig.AvroConfig.html)(write_metadata=True)
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    max_duration = duration_pb2.[Duration](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Duration.html)()
    max_duration.FromSeconds(300)
    
    cloudstorage_config = pubsub_v1.types.[CloudStorageConfig](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.CloudStorageConfig.html)(
        bucket=bucket,
        filename_prefix=filename_prefix,
        filename_suffix=filename_suffix,
        avro_config=avro_config,
        # Min 1 minutes, max 10 minutes
        max_duration=max_duration,
        # Min 1 KB, max 10 GiB
        max_bytes=10000000,
    )
    
    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "cloud_storage_config": cloudstorage_config,
            }
        )
    
    print(f"CloudStorage subscription created: {subscription}.")
    print(f"Bucket for subscription is: {bucket}")
    print(f"Prefix is: {filename_prefix}")
    print(f"Suffix is: {filename_suffix}")

## Monitor a Cloud Storage subscription

Cloud Monitoring provides a number of metrics to [monitor subscriptions](https://docs.cloud.google.com/pubsub/docs/monitoring#maintain_a_healthy_subscription).

For a list of all the available metrics related to Pub/Sub and their descriptions, see the [Monitoring documentation for Pub/Sub](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub).

You can also monitor subscriptions from [within Pub/Sub](https://docs.cloud.google.com/pubsub/docs/monitor-subscription).

## What's next

  * Troubleshoot a [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/cloudstorage-troubleshooting).

  * Read about [Cloud Storage](https://docs.cloud.google.com/storage/docs).

  * Review pricing for Pub/Sub, including [Cloud Storage subscription](https://cloud.google.com/pubsub/pricing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
