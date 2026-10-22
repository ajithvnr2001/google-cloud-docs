---
url: https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic/
title: Create a Cloud Storage import topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:36.957768+00:00
---

# Create a Cloud Storage import topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create a Cloud Storage import topic Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Storage import topic lets you continuously ingest data from Cloud Storage into Pub/Sub. Then you can stream the data into any of the destinations that Pub/Sub supports. Pub/Sub automatically detects new objects added to the Cloud Storage bucket and ingests them.

Cloud Storage is a service for storing your objects in Google Cloud. An _object_ is an immutable piece of data consisting of a file of any format. You store objects in containers called _buckets_. Buckets can also contain managed folders, which you use to provide expanded access to groups of objects with a shared name prefix.

For more information about Cloud Storage, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/introduction).

For more information about import topics, see [About import topics](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#import-topic-overview).

## Before you begin

  * [Learn more about the Pub/Sub publish process](https://docs.cloud.google.com/pubsub/docs/publish-message-overview).

  * A Cloud Storage bucket must already exist before you create a Cloud Storage import topic. If you are using the console to create the import topic, the workflow lets you create a Cloud Storage bucket. For other configuration methods, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

  * If applicable, ensure that the message storage policy of the Pub/Sub topic overlaps with the region where your Cloud Storage bucket is located. For more information, see Message storage policy is compliant with the bucket location.

  * Some Google Cloud services have Google Cloud-managed service accounts that lets the services access your resources. These service accounts are known as service agents. Pub/Sub creates and maintains a service account for each project in the format `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`. Configure the required roles and permissions on the Pub/Sub service account to manage Cloud Storage import topics including the following:

    * Grant the [Pub/Sub publisher role (`roles/pubsub.publisher`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher) to the Pub/Sub service account. This service account is going to publish to the import topic. To grant this role, you require a user account with the [Pub/Sub Admin role (`roles/pubsub.admin`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.admin). For more information, see Add the Pub/Sub publisher role to the Pub/Sub service account.

    * Grant Cloud Storage permissions to the Pub/Sub service account. To grant these permissions, you require a user account with the [Storage Admin role (`roles/storage.admin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles). For more information, see Assign Cloud Storage roles to the Pub/Sub service account.




### Required roles and permissions

To get the permissions that you need to create and manage a Cloud Storage import topic, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your topic or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage a Cloud Storage import topic. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage a Cloud Storage import topic:

  * Create an import topic: `pubsub.topics.create`
  * Delete an import topic: `pubsub.topics.delete`
  * Get an import topic: `pubsub.topics.get`
  * List an import topic: `pubsub.topics.list`
  * Publish to an import topic: `pubsub.topics.publish`
  * Update an import topic: `pubsub.topics.update`
  * Get the IAM policy for an import topic: `pubsub.topics.getIamPolicy`
  * Configure the [IAM policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy) for an import topic: `pubsub.topics.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and the individual resource level.

## Message storage policy is compliant with the bucket location

**Note:** This section only applies if you have a message storage policy for Pub/Sub. To check if your topic has a message storage policy and, if required, to update the message storage policy, see [Update message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction#update_message_storage_policies).

The message storage policy of the Pub/Sub topic must overlap with the regions where your Cloud Storage bucket is located. This policy dictates where Pub/Sub is allowed to store your message data.

  * For buckets with location type as region: The policy must include that specific region. For example, if your bucket is in the `us-central1` region, the message storage policy must also include `us-central1`.

  * For buckets with location type as dual-region or multi-region: The policy must include at least one region within the dual-region or multi-region location. For example, if your bucket is in the `US multi-region`, the message storage policy could include `us-central1`, `us-east1`, or any other region within the `US multi-region`.

If the policy doesn't include the bucket's region, topic creation fails. For example, if your bucket is in `europe-west1` and your message storage policy only includes `asia-east1`, you'll receive an error.

If the message storage policy includes only one region that overlaps with the bucket's location, multi-region redundancy might be compromised. This is because if that single region becomes unavailable, your data might not be accessible. To ensure full redundancy, it's recommended to include at least two regions within the message storage policy that are part of the bucket's multi-region or dual-region location.




For more information about the bucket locations, see [the documentation](https://docs.cloud.google.com/storage/docs/locations).

## Enable publishing

To enable publishing, you must assign the Pub/Sub publisher role to the Pub/Sub service account so that Pub/Sub is able to publish to the Cloud Storage import topic.

### Enable publishing to all Cloud Storage import topics

Choose this option when you don't have a Cloud Storage import topic available in your project.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **Include Google-provided role grants** checkbox.

  3. Look for the Pub/Sub service account that has the format:

`service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`

  4. For this service account, click the **Edit Principal** button.

  5. If required, click **Add another role**.

  6. Search and select the **Pub/Sub publisher role** (`roles/pubsub.publisher`).

  7. Click **Save**.




### Enable publishing to a single Cloud Storage import topic

If you want to grant Pub/Sub the permission to publish to a specific Cloud Storage import topic that already exists, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/add-iam-policy-binding) command:
         
         gcloud pubsub topics add-iam-policy-binding TOPIC_ID\
            --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com"\
            --role="roles/pubsub.publisher"

Replace the following:

     * TOPIC_ID is the ID or name of the Cloud Storage import topic.

     * PROJECT_NUMBER is the project number. To view the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




## Assign Cloud Storage roles to the Pub/Sub service account

To create a Cloud Storage import topic, the Pub/Sub service account must have permission to read from the specific Cloud Storage bucket. The following permissions are required:

  * `storage.objects.list`
  * `storage.objects.get`
  * `storage.buckets.get`



To assign these permissions to the Pub/Sub service account, choose one of the following procedures:

  * Grant permissions at the bucket level. On the specific Cloud Storage bucket, grant the Storage Legacy Object Reader (`roles/storage.legacyObjectReader`) role and the Storage Legacy Bucket Reader (`roles/storage.legacyBucketReader`) roles to the Pub/Sub service account.

  * If you must grant roles at the project level, you might instead grant the Storage Admin (`roles/storage.admin`) role on the project containing the Cloud Storage bucket. Grant this role to the Pub/Sub service account.




### Bucket permissions

Perform the following steps to grant the Storage Legacy Object Reader (`roles/storage.legacyObjectReader`) role and the Storage Legacy Bucket Reader (`roles/storage.legacyBucketReader`) roles to the Pub/Sub service account at the bucket level:

  1. In the Google Cloud console, go to the **Cloud Storage** page.

[Go to Cloud Storage](https://console.cloud.google.com/storage/browser)

  2. Click the Cloud Storage bucket from which you would like to read messages and import to the Cloud Storage import topic.

The **Bucket details** page opens.

  3. In the **Bucket details** page, click the **Permissions** tab.

  4. In the **Permissions** > **View by Principals** tab, click **Grant access**.

The **Grant access** page opens.

  5. In the **Add Principals** section, enter the name of your Pub/Sub service account.

The format of the service account is `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`. For example, for a project with **PROJECT_NUMBER** =`112233445566`, the service account is of the format `service-112233445566@gcp-sa-pubsub.iam.gserviceaccount.com`.

  6. In the **Assign roles** > **Select a role** drop-down, enter `Object Reader` and select the **Storage Legacy Object Reader** role.

  7. Click **Add another role**.

  8. In the **Select a role** drop-down, enter `Bucket Reader`, and select the **Storage Legacy Bucket Reader** role.

  9. Click **Save**.




### Project permissions

Perform the following steps to grant the Storage Admin (`roles/storage.admin`) role at the project level:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the **Permissions** > **View by Principals** tab, click **Grant access**.

The **Grant access** page opens.

  3. In the **Add Principals** section, enter the name of your Pub/Sub service account.

The format of the service account is `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`. For example, for a project with **PROJECT_NUMBER** =`112233445566`, the service account is of the format `service-112233445566@gcp-sa-pubsub.iam.gserviceaccount.com`.

  4. In the **Assign roles** > **Select a role** drop-down, enter `Storage Admin` and select the **Storage Admin** role.

  5. Click **Save**.




For more information about Cloud Storage IAM, see [Cloud Storage Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

## Properties of Cloud Storage import topics

For more information about the common properties across all topics, see [Properties of a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#properties_of_a_topic).

### Bucket name

This is the name of the Cloud Storage bucket from which Pub/Sub reads the data that is published to a Cloud Storage import topic.

### Input format

When you create a Cloud Storage import topic, you can specify the format of the objects to be ingested as **Text** , **Avro** , or **Pub/Sub Avro**.

  * **Text**. Objects are assumed to hold data with plain text. This input format attempts to ingest all objects in the bucket as long as the object meets the minimum object creation time and matches the glob pattern criteria.

**Delimiter**. You can also specify a delimiter by which objects are split into messages. If unset, this defaults to the newline character (`\n`). The delimiter must only be a single character.

  * **Avro**. Objects are in the [Apache Avro binary](https://avro.apache.org/docs/1.11.1/specification/#binary-encoding) format. Any object that is not in a valid Apache Avro format is not ingested. Here are the limitations regarding Avro:

    * Avro versions 1.1.0 and 1.2.0 are not supported.
    * The maximum size of an Avro block is 16 MB.
  * **Pub/Sub Avro**. Objects are in the Apache Avro binary format with a schema matching that of an object written to Cloud Storage using a Pub/Sub [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/cloudstorage) with the [Avro file format](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription#file_format). Here are some important guidelines for Pub/Sub Avro:

    * The data field of the Avro record is used to populate the data field of the generated Pub/Sub message.

    * If the [**write_metadata option**](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription#file_format) is specified for the Cloud Storage subscription, any values in the attributes field are populated as the attributes of the generated Pub/Sub message.

    * If an [**ordering key**](https://docs.cloud.google.com/pubsub/docs/ordering) is specified in the original message written to Cloud Storage, this field is populated as an attribute with the name `original_message_ordering_key` in the generated Pub/Sub message.




### Minimum object creation time

You can optionally specify a minimum object creation time when creating a Cloud Storage import topic. Only objects that were created at or after this timestamp are ingested. This timestamp must be provided in a format like `YYYY-MM-DDThh:mm:ssZ`. Any date, past or future, from `0001-01-01T00:00:00Z` to `9999-12-31T23:59:59Z` inclusive, is valid.

### Match glob pattern

You can optionally specify a match glob pattern when creating a Cloud Storage import topic. Only objects with names that match this pattern are ingested. For example, to ingest all object with suffix `.txt`, you can specify the glob pattern as `**.txt`.

For information about supported syntax for glob patterns, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob).

## Use Cloud Storage import topics

You can create a new import topic or edit an existing topic.

### Considerations

**Caution:** If you already have data in the Cloud Storage bucket, first [create a standard topic and the required subscriptions](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic_2) without enabling the ingestion settings. Then, [convert the topic to a Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/change-topic-type#convert-standard-to-import). This method ensures that all messages are received by the subscriptions.

  * Creating the topic and subscription separately, even if done in rapid succession, can lead to data loss. There's a short window where the topic exists without a subscription. If any data is sent to the topic during this time, it is lost. By creating the topic first, creating the subscription, and then converting the topic to an import topic, you guarantee that no messages are missed during the import process.



### Create a Cloud Storage import topic

To create a Cloud Storage import topic, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click **Create topic**.

The topic details page opens.

  3. In the **Topic ID** field, enter an ID for your Cloud Storage import topic.

For more information about naming topics, see the [naming guidelines](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. Select **Add a default subscription**.

  5. Select **Enable ingestion**.

  6. For ingestion source, select **Google Cloud Storage**.

  7. For the Cloud Storage bucket, click **Browse**.

The **Select bucket** page opens. Select one of the following options:

     * Select an existing bucket from any appropriate project.

     * Click the create icon and follow the instructions on the screen to create a new bucket. After you create the bucket, select the bucket for the Cloud Storage import topic.

  8. When you specify the bucket, Pub/Sub checks for the appropriate permissions on the bucket for the Pub/Sub service account. If there are permissions issues, you see a message similar to the following:

`Unable to verify if the Pub/Sub service agent has write permissions on this bucket. You may be lacking permissions to view or set permissions.`

If you get permission issues, click **Set permissions**. For more information, see Grant Cloud Storage permissions to the Pub/Sub service account.

  9. For **Object format** , select **Text** , **Avro** , or **Pub/Sub Avro**.

If you select **Text** , you can optionally specify a **Delimiter** with which to split objects into messages.

For more information about these options, see Input format.

  10. Optional. You can specify a **Minimum object creation time** for your topic. If set, only objects created after the minimum object creation time are ingested.

For more information see Minimum object creation time.

  11. You must specify a **Glob pattern**. To ingest all objects in the bucket, use `**` as the glob pattern. If set, only objects that match the given pattern are ingested.

For more information, see Match a glob pattern.

  12. Retain the other default settings.

  13. Click **Create topic**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
         
         gcloud pubsub topics create TOPIC_ID \
             --cloud-storage-ingestion-bucket=BUCKET_NAME \
             --cloud-storage-ingestion-input-format=INPUT_FORMAT \
             --cloud-storage-ingestion-text-delimiter=TEXT_DELIMITER \
             --cloud-storage-ingestion-minimum-object-create-time=MINIMUM_OBJECT_CREATE_TIME \
             --cloud-storage-ingestion-match-glob=MATCH_GLOB
         

In the command, only `TOPIC_ID`, the `--cloud-storage-ingestion-bucket` flag, and the `--cloud-storage-ingestion-input-format` flag are required. The remaining flags are optional and can be omitted.

Replace the following:

     * `TOPIC_ID`: The name or ID of your topic.
     * `BUCKET_NAME`: Specifies the name of an existing bucket. For example, `prod_bucket`. The bucket name must not include the project ID. To create a bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).
     * `INPUT_FORMAT`: Specifies the format of the objects that is ingested. This can be `text`, `avro`, or `pubsub_avro`. For more information about these options, see Input format.
     * `TEXT_DELIMITER`: Specifies the delimiter with which to split text objects into Pub/Sub messages. This should be a single character and should only be set when `INPUT_FORMAT` is `text`. It defaults to the newline character (`\n`).

When using gcloud CLI to specify the delimiter, pay close attention to the handling of special characters like newline `\n`. Use the format `'\n'` to ensure the delimiter is correctly interpreted. Simply using `\n` without quotes or escaping results in a delimiter of `"n"`.

     * `MINIMUM_OBJECT_CREATE_TIME`: Specifies the minimum time at which an object was created in order for it to be ingested. This should be in UTC in the format `YYYY-MM-DDThh:mm:ssZ`. For example, `2024-10-14T08:30:30Z`.

Any date, past or future, from `0001-01-01T00:00:00Z` to `9999-12-31T23:59:59Z` inclusive, is valid.

     * `MATCH_GLOB`: Specifies the glob pattern to match in order for an object to be ingested. When you are using gcloud CLI, a match glob with `*` characters must have the `*` character formatted as escaped in the form `\*\*.txt` or the whole match glob must be in quotes `"**.txt"` or `'**.txt'`. For information about supported syntax for glob patterns, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob).




### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string bucket, std::string const& input_format,
       std::string text_delimiter, std::string match_glob,
       std::string const& minimum_object_create_time) {
      google::pubsub::v1::Topic request;
      request.set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto& cloud_storage = *request.mutable_ingestion_data_source_settings()
                                 ->mutable_cloud_storage();
      cloud_storage.set_bucket(std::move(bucket));
      if (input_format == "text") {
        cloud_storage.mutable_text_format()->set_delimiter(
            std::move(text_delimiter));
      } else if (input_format == "avro") {
        cloud_storage.mutable_avro_format();
      } else if (input_format == "pubsub_avro") {
        cloud_storage.mutable_pubsub_avro_format();
      } else {
        std::cout << "input_format must be in ('text', 'avro', 'pubsub_avro'); "
                     "got value: "
                  << input_format << std::endl;
        return;
      }
    
      if (!match_glob.empty()) {
        cloud_storage.set_match_glob(std::move(match_glob));
      }
    
      if (!minimum_object_create_time.empty()) {
        google::protobuf::Timestamp timestamp;
        if (!google::protobuf::util::TimeUtil::FromString(
                minimum_object_create_time,
                cloud_storage.mutable_minimum_object_create_time())) {
          std::cout << "Invalid minimum object create time: "
                    << minimum_object_create_time << std::endl;
        }
      }
    
      auto topic = client.CreateTopic(request);
      // Note that kAlreadyExists is a possible error when the library retries.
      if (topic.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The topic already exists\n";
        return;
      }
      if (!topic) throw std::move(topic).status();
    
      std::cout << "The topic was successfully created: " << topic->DebugString()
                << "\n";
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    func createTopicWithCloudStorageIngestion(w io.Writer, projectID, topicID, bucket, matchGlob, minimumObjectCreateTime, delimiter string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// bucket := "my-bucket"
    	// matchGlob := "**.txt"
    	// minimumObjectCreateTime := "2006-01-02T15:04:05Z"
    	// delimiter := ","
    
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	minCreateTime, err := time.Parse(time.RFC3339, minimumObjectCreateTime)
    	if err != nil {
    		return err
    	}
    
    	topicpb := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    		IngestionDataSourceSettings: &pubsubpb.IngestionDataSourceSettings{
    			Source: &pubsubpb.IngestionDataSourceSettings_CloudStorage_{
    				CloudStorage: &pubsubpb.IngestionDataSourceSettings_CloudStorage{
    					Bucket: bucket,
    					// Alternatively, can be Avro or PubSubAvro formats. See
    					InputFormat: &pubsubpb.IngestionDataSourceSettings_CloudStorage_TextFormat_{
    						TextFormat: &pubsubpb.IngestionDataSourceSettings_CloudStorage_TextFormat{
    							Delimiter: &delimiter,
    						},
    					},
    					MatchGlob:               matchGlob,
    					MinimumObjectCreateTime: timestamppb.New(minCreateTime),
    				},
    			},
    		},
    	}
    	t, err := client.TopicAdminClient.CreateTopic(ctx, topicpb)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Cloud storage topic created: %v\n", t)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.protobuf.util.[Timestamps](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Timestamps.html);
    import com.google.pubsub.v1.[IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.text.ParseException;
    
    public class CreateTopicWithCloudStorageIngestionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Cloud Storage ingestion settings.
        // bucket and inputFormat are required arguments.
        String bucket = "your-bucket";
        String inputFormat = "text";
        String textDelimiter = "\n";
        String matchGlob = "**.txt";
        String minimumObjectCreateTime = "YYYY-MM-DDThh:mm:ssZ";
    
        createTopicWithCloudStorageIngestionExample(
            projectId, topicId, bucket, inputFormat, textDelimiter, matchGlob, minimumObjectCreateTime);
      }
    
      public static void createTopicWithCloudStorageIngestionExample(
          String projectId,
          String topicId,
          String bucket,
          String inputFormat,
          String textDelimiter,
          String matchGlob,
          String minimumObjectCreateTime)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[CloudStorage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.html).Builder cloudStorageBuilder =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).CloudStorage.newBuilder().setBucket(bucket);
          switch (inputFormat) {
            case "text":
              cloudStorageBuilder.[setTextFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_Builder_setTextFormat_com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_TextFormat_)(
                  [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).CloudStorage.TextFormat.newBuilder()
                      .[setDelimiter](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.TextFormat.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_TextFormat_Builder_setDelimiter_java_lang_String_)(textDelimiter)
                      .build());
              break;
            case "avro":
              cloudStorageBuilder.[setAvroFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_Builder_setAvroFormat_com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_AvroFormat_)(
                  [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).CloudStorage.AvroFormat.getDefaultInstance());
              break;
            case "pubsub_avro":
              cloudStorageBuilder.[setPubsubAvroFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_Builder_setPubsubAvroFormat_com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat_)(
                  [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).CloudStorage.PubSubAvroFormat.getDefaultInstance());
              break;
            default:
              throw new IllegalArgumentException(
                  "inputFormat must be in ('text', 'avro', 'pubsub_avro'); got value: " + inputFormat);
          }
    
          if (matchGlob != null && !matchGlob.isEmpty()) {
            cloudStorageBuilder.[setMatchGlob](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_Builder_setMatchGlob_java_lang_String_)(matchGlob);
          }
    
          if (minimumObjectCreateTime != null && !minimumObjectCreateTime.isEmpty()) {
            try {
              cloudStorageBuilder.[setMinimumObjectCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.CloudStorage.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_Builder_setMinimumObjectCreateTime_com_google_protobuf_Timestamp_)([Timestamps](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Timestamps.html).parse(minimumObjectCreateTime));
            } catch (ParseException e) {
              System.err.println("Unable to parse timestamp: " + minimumObjectCreateTime);
            }
          }
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder()
                  .[setCloudStorage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setCloudStorage_com_google_pubsub_v1_IngestionDataSourceSettings_CloudStorage_)(cloudStorageBuilder.build())
                  .build();
    
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                      .build());
    
          System.out.println(
              "Created topic with Cloud Storage ingestion settings: " + topic.getAllFields());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const bucket = 'YOUR_BUCKET_NAME';
    // const inputFormat = 'text';
    // const textDelimiter = '\n';
    // const matchGlob = '**.txt';
    // const minimumObjectCreateTime = 'YYYY-MM-DDThh:mm:ssZ;
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopicWithCloudStorageIngestion(
      topicNameOrId,
      bucket,
      inputFormat,
      textDelimiter,
      matchGlob,
      minimumObjectCreateTime,
    ) {
      const minimumDate = Date.parse(minimumObjectCreateTime);
      const topicMetadata = {
        name: topicNameOrId,
        ingestionDataSourceSettings: {
          cloudStorage: {
            bucket,
            minimumObjectCreateTime: {
              seconds: minimumDate / 1000,
              nanos: (minimumDate % 1000) * 1000,
            },
            matchGlob,
          },
        },
      };
    
      // Make a format appropriately.
      switch (inputFormat) {
        case 'text':
          topicMetadata.ingestionDataSourceSettings.cloudStorage.textFormat = {
            delimiter: textDelimiter,
          };
          break;
        case 'avro':
          topicMetadata.ingestionDataSourceSettings.cloudStorage.avroFormat = {};
          break;
        case 'pubsub_avro':
          topicMetadata.ingestionDataSourceSettings.cloudStorage.pubsubAvroFormat =
            {};
          break;
        default:
          console.error('inputFormat must be in ("text", "avro", "pubsub_avro")');
          return;
      }
    
      // Creates a new topic with Cloud Storage ingestion.
      await pubSubClient.createTopic(topicMetadata);
      console.log(`Topic ${topicNameOrId} created with Cloud Storage ingestion.`);
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const bucket = 'YOUR_BUCKET_NAME';
    // const inputFormat = 'text';
    // const textDelimiter = '\n';
    // const matchGlob = '**.txt';
    // const minimumObjectCreateTime = 'YYYY-MM-DDThh:mm:ssZ;
    
    // Imports the Google Cloud client library
    import {PubSub, TopicMetadata} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopicWithCloudStorageIngestion(
      topicNameOrId: string,
      bucket: string,
      inputFormat: string,
      textDelimiter: string,
      matchGlob: string,
      minimumObjectCreateTime: string,
    ) {
      const minimumDate = Date.parse(minimumObjectCreateTime);
      const topicMetadata: TopicMetadata = {
        name: topicNameOrId,
        ingestionDataSourceSettings: {
          cloudStorage: {
            bucket,
            minimumObjectCreateTime: {
              seconds: minimumDate / 1000,
              nanos: (minimumDate % 1000) * 1000,
            },
            matchGlob,
          },
        },
      };
    
      // Make a format appropriately.
      switch (inputFormat) {
        case 'text':
          topicMetadata.ingestionDataSourceSettings!.cloudStorage!.textFormat = {
            delimiter: textDelimiter,
          };
          break;
        case 'avro':
          topicMetadata.ingestionDataSourceSettings!.cloudStorage!.avroFormat = {};
          break;
        case 'pubsub_avro':
          topicMetadata.ingestionDataSourceSettings!.cloudStorage!.pubsubAvroFormat =
            {};
          break;
        default:
          console.error('inputFormat must be in ("text", "avro", "pubsub_avro")');
          return;
      }
    
      // Creates a new topic with Cloud Storage ingestion.
      await pubSubClient.createTopic(topicMetadata);
      console.log(`Topic ${topicNameOrId} created with Cloud Storage ingestion.`);
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    from google.protobuf import timestamp_pb2
    from google.pubsub_v1.types import [Topic](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Topic.html)
    from google.pubsub_v1.types import [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html)
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # bucket = "your-bucket"
    # input_format = "text"  (can be one of "text", "avro", "pubsub_avro")
    # text_delimiter = "\n"
    # match_glob = "**.txt"
    # minimum_object_create_time = "YYYY-MM-DDThh:mm:ssZ"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    cloud_storage_settings = [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html).[CloudStorage](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.html)(
        bucket=bucket,
    )
    if input_format == "text":
        cloud_storage_settings.text_format = (
            [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html).[CloudStorage](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.html).[TextFormat](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.TextFormat.html)(
                delimiter=text_delimiter
            )
        )
    elif input_format == "avro":
        cloud_storage_settings.avro_format = (
            [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html).[CloudStorage](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.html).[AvroFormat](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.AvroFormat.html)()
        )
    elif input_format == "pubsub_avro":
        cloud_storage_settings.pubsub_avro_format = (
            [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html).[CloudStorage](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.html).[PubSubAvroFormat](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.PubSubAvroFormat.html)()
        )
    else:
        print(
            "Invalid input_format: "
            + input_format
            + "; must be in ('text', 'avro', 'pubsub_avro')"
        )
        return
    
    if match_glob:
        cloud_storage_settings.match_glob = match_glob
    
    if minimum_object_create_time:
        try:
            minimum_object_create_time_timestamp = timestamp_pb2.[Timestamp](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Timestamp.html)()
            minimum_object_create_time_timestamp.FromJsonString(
                minimum_object_create_time
            )
            cloud_storage_settings.minimum_object_create_time = (
                minimum_object_create_time_timestamp
            )
        except ValueError:
            print("Invalid minimum_object_create_time: " + minimum_object_create_time)
            return
    
    request = Topic(
        name=topic_path,
        ingestion_data_source_settings=IngestionDataSourceSettings(
            cloud_storage=cloud_storage_settings,
        ),
    )
    
    topic = publisher.create_topic(request=request)
    
    print(f"Created topic: {topic.name} with Cloud Storage Ingestion Settings")

If you run into issues, see [Troubleshooting a Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/cloud-storage-import-topic-troubleshooting).

### Edit a Cloud Storage import topic

You can edit a Cloud Storage import topic to update its properties.

For example, to restart ingestion, you can change the bucket or update the minimum object creation time.

To edit a Cloud Storage import topic, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the Cloud Storage import topic.

  3. In the topic details page, click **Edit**.

  4. Update the fields that you want to change.

  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To avoid losing your settings for the import topic, make sure to include all of them every time you update the topic. If you leave something out, Pub/Sub resets the setting to its original default value.

Run the [`gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update) command with all the flags mentioned in the following sample:
         
         gcloud pubsub topics update TOPIC_ID \
             --cloud-storage-ingestion-bucket=BUCKET_NAME\
             --cloud-storage-ingestion-input-format=INPUT_FORMAT\
             --cloud-storage-ingestion-text-delimiter=TEXT_DELIMITER\
             --cloud-storage-ingestion-minimum-object-create-time=MINIMUM_OBJECT_CREATE_TIME\
             --cloud-storage-ingestion-match-glob=MATCH_GLOB

Replace the following:

     * TOPIC_ID is the topic ID or name. This field cannot be updated.

     * BUCKET_NAME: Specifies the name of an existing bucket. For example, `prod_bucket`. The bucket name must not include the project ID. To create a bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

     * INPUT_FORMAT: Specifies the format of the objects that is ingested. This can be `text`, `avro`, or `pubsub_avro`. See  Input format for more information on these options.

     * TEXT_DELIMITER: Specifies the delimiter with which to split text objects into Pub/Sub messages. This should be a single character and should only be set when `INPUT_FORMAT` is `text`. It defaults to the newline character (`\n`).

When using gcloud CLI to specify the delimiter, pay close attention to the handling of special characters like newline `\n`. Use the format `'\n'` to ensure the delimiter is correctly interpreted. Simply using `\n` without quotes or escaping results in a delimiter of `"n"`.

     * MINIMUM_OBJECT_CREATE_TIME: Specifies the minimum time at which an object was created in order for it to be ingested. This should be in UTC in the format `YYYY-MM-DDThh:mm:ssZ`. For example, `2024-10-14T08:30:30Z`.

Any date, past or future, from `0001-01-01T00:00:00Z` to `9999-12-31T23:59:59Z` inclusive, is valid.

     * MATCH_GLOB: Specifies the glob pattern to match in order for an object to be ingested. When you are using gcloud CLI, a match glob with `*` characters must have the `*` character formatted as escaped in the form `\*\*.txt` or the whole match glob must be in quotes `"**.txt"` or `'**.txt'`. For information about supported syntax for glob patterns, see the [ Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob).




## Quotas and limits for Cloud Storage import topics

The publisher throughput for import topics is bound by the publish quota of the topic. For more information, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).

## What's next

  * [Monitor an import topic](https://docs.cloud.google.com/pubsub/docs/monitor-topic#metrics-monitor-topic).

  * [Enable platform logs](https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub) for a Cloud Storage import topic.

  * Choose the [type of subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) for your topic.

  * Learn how to [publish a message to a topic](https://docs.cloud.google.com/pubsub/docs/publisher).

  * [Troubleshoot a Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/cloud-storage-import-topic-troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
