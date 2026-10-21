---
url: https://docs.cloud.google.com/pubsub/docs/change-topic-type/
title: Change topic type \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:59.947158+00:00
---

# Change topic type  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/change-topic-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Change topic type Stay organized with collections  Save and categorize content based on your preferences. 

You can convert an import topic to a standard one or conversely, a standard topic to an import one.

## Convert an import topic to a standard topic

To convert an import topic to a standard topic, clear the ingestion settings. Perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the import topic.

  3. In the topic details page, click **Edit**.

  4. Clear the option **Enable ingestion**.

  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update) command:
         
         gcloud pubsub topics update TOPIC_ID \
             --clear-ingestion-data-source-settings

Replace TOPIC_ID with the topic ID.




## Convert a standard topic to an Amazon Kinesis Data Streams import topic

To convert a standard topic to an Amazon Kinesis Data Streams import topic, first check that you meet all the [prerequisites](https://docs.cloud.google.com/pubsub/docs/create-import-topic#before-you-begin).

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the topic that you want to convert to an import topic.

  3. In the topic details page, click **Edit**.

  4. Select the option **Enable ingestion**.

  5. For ingestion source, select **Amazon Kinesis Data Streams**.

  6. Enter the following details:

     * **Kinesis Stream ARN** : The ARN for the Kinesis Data Stream that you are planning to ingest into Pub/Sub. The ARN format is as follows: `arn:${Partition}:kinesis:${Region}:${Account}:stream/${StreamName}`. 

     * **Kinesis Consumer ARN** : The ARN of the consumer resource that is registered to the AWS Kinesis Data Stream. The ARN format is as follows: `arn:${Partition}:kinesis:${Region}:${Account}:${StreamType}/${StreamName}/consumer/${ConsumerName}:${ConsumerCreationTimestamp}`. 

     * **AWS Role ARN** : The ARN of the AWS role. The ARN format of the role is as follows: `arn:aws:iam::${Account}:role/${RoleName}`. 

     * **Service account** : The service account that you created.

  7. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update) command with all the flags mentioned in the following sample:
         
         gcloud pubsub topics update TOPIC_ID   
           --kinesis-ingestion-stream-arn KINESIS_STREAM_ARN  
           --kinesis-ingestion-consumer-arn KINESIS_CONSUMER_ARN  
           --kinesis-ingestion-role-arn KINESIS_ROLE_ARN  
           --kinesis-ingestion-service-account PUBSUB_SERVICE_ACCOUNT

Replace the following:

     * TOPIC_ID is the topic ID or name. This field cannot be updated.

     * KINESIS_STREAM_ARN is the ARN for the Kinesis Data Streams that you are planning to ingest into Pub/Sub. The ARN format is as follows: `arn:${Partition}:kinesis:${Region}:${Account}:stream/${StreamName}`. 

     * KINESIS_CONSUMER_ARN is the ARN of the consumer resource that is registered to the AWS Kinesis Data Streams. The ARN format is as follows: `arn:${Partition}:kinesis:${Region}:${Account}:${StreamType}/${StreamName}/consumer/${ConsumerName}:${ConsumerCreationTimestamp}`. 

     * KINESIS_ROLE_ARN is the ARN of the AWS role. The ARN format of the role is as follows: `arn:aws:iam::${Account}:role/${RoleName}`.

     * PUBSUB_SERVICE_ACCOUNT is the service account that you created.




### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    func updateTopicType(w io.Writer, projectID, topic string) error {
    	// projectID := "my-project-id"
    	// topic := "projects/my-project-id/topics/my-topic"
    	streamARN := "stream-arn"
    	consumerARN := "consumer-arn"
    	awsRoleARN := "aws-role-arn"
    	gcpServiceAccount := "gcp-service-account"
    
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	pbTopic := &pubsubpb.Topic{
    		Name: topic,
    		IngestionDataSourceSettings: &pubsubpb.IngestionDataSourceSettings{
    			Source: &pubsubpb.IngestionDataSourceSettings_AwsKinesis_{
    				AwsKinesis: &pubsubpb.IngestionDataSourceSettings_AwsKinesis{
    					StreamArn:         streamARN,
    					ConsumerArn:       consumerARN,
    					AwsRoleArn:        awsRoleARN,
    					GcpServiceAccount: gcpServiceAccount,
    				},
    			},
    		},
    	}
    	updateReq := &pubsubpb.UpdateTopicRequest{
    		Topic: pbTopic,
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{"ingestion_data_source_settings"},
    		},
    	}
    	topicCfg, err := client.TopicAdminClient.UpdateTopic(ctx, updateReq)
    	if err != nil {
    		return fmt.Errorf("topic.Update: %w", err)
    	}
    	fmt.Fprintf(w, "Topic updated with kinesis source: %v\n", topicCfg)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.pubsub.v1.[IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import com.google.pubsub.v1.[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html);
    import java.io.IOException;
    
    public class UpdateTopicTypeExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Kinesis ingestion settings.
        String streamArn = "stream-arn";
        String consumerArn = "consumer-arn";
        String awsRoleArn = "aws-role-arn";
        String gcpServiceAccount = "gcp-service-account";
    
        UpdateTopicTypeExample.updateTopicTypeExample(
            projectId, topicId, streamArn, consumerArn, awsRoleArn, gcpServiceAccount);
      }
    
      public static void updateTopicTypeExample(
          String projectId,
          String topicId,
          String streamArn,
          String consumerArn,
          String awsRoleArn,
          String gcpServiceAccount)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[AwsKinesis](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.html) awsKinesis =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).AwsKinesis.newBuilder()
                  .setStreamArn(streamArn)
                  .[setConsumerArn](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_AwsKinesis_Builder_setConsumerArn_java_lang_String_)(consumerArn)
                  .setAwsRoleArn(awsRoleArn)
                  .setGcpServiceAccount(gcpServiceAccount)
                  .build();
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder().[setAwsKinesis](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setAwsKinesis_com_google_pubsub_v1_IngestionDataSourceSettings_AwsKinesis_)(awsKinesis).build();
    
          // Construct the topic with Kinesis ingestion settings.
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                  .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                  .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                  .build();
    
          // Construct a field mask to indicate which field to update in the topic.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("ingestion_data_source_settings").build();
    
          [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html) request =
              [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html).newBuilder().setTopic(topic).setUpdateMask(updateMask).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) response = topicAdminClient.updateTopic(request);
    
          System.out.println(
              "Updated topic with Kinesis ingestion settings: " + response.getAllFields());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const awsRoleArn = 'arn:aws:iam:...';
    // const gcpServiceAccount = 'ingestion-account@...';
    // const streamArn = 'arn:aws:kinesis:...';
    // const consumerArn = 'arn:aws:kinesis:...';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function updateTopicIngestionType(
      topicNameOrId,
      awsRoleArn,
      gcpServiceAccount,
      streamArn,
      consumerArn,
    ) {
      const metadata = {
        ingestionDataSourceSettings: {
          awsKinesis: {
            awsRoleArn,
            gcpServiceAccount,
            streamArn,
            consumerArn,
          },
        },
      };
    
      await pubSubClient.topic(topicNameOrId).setMetadata(metadata);
    
      console.log('Topic updated with Kinesis source successfully.');
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    from google.pubsub_v1.types import [Topic](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Topic.html)
    from google.pubsub_v1.types import [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html)
    from google.pubsub_v1.types import [UpdateTopicRequest](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.UpdateTopicRequest.html)
    from google.protobuf import field_mask_pb2
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # stream_arn = "your-stream-arn"
    # consumer_arn = "your-consumer-arn"
    # aws_role_arn = "your-aws-role-arn"
    # gcp_service_account = "your-gcp-service-account"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    update_request = UpdateTopicRequest(
        topic=Topic(
            name=topic_path,
            ingestion_data_source_settings=IngestionDataSourceSettings(
                aws_kinesis=[IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html).[AwsKinesis](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.AwsKinesis.html)(
                    stream_arn=stream_arn,
                    consumer_arn=consumer_arn,
                    aws_role_arn=aws_role_arn,
                    gcp_service_account=gcp_service_account,
                )
            ),
        ),
        update_mask=field_mask_pb2.[FieldMask](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.FieldMask.html)(paths=["ingestion_data_source_settings"]),
    )
    
    topic = publisher.update_topic(request=update_request)
    print(f"Updated topic: {topic.name} with AWS Kinesis Ingestion Settings")
    
    

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string stream_arn, std::string consumer_arn,
       std::string aws_role_arn, std::string gcp_service_account) {
      google::pubsub::v1::UpdateTopicRequest request;
    
      request.mutable_topic()->set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto* aws_kinesis = request.mutable_topic()
                              ->mutable_ingestion_data_source_settings()
                              ->mutable_aws_kinesis();
      aws_kinesis->set_stream_arn(stream_arn);
      aws_kinesis->set_consumer_arn(consumer_arn);
      aws_kinesis->set_aws_role_arn(aws_role_arn);
      aws_kinesis->set_gcp_service_account(gcp_service_account);
      *request.mutable_update_mask()->add_paths() =
          "ingestion_data_source_settings";
    
      auto topic = client.UpdateTopic(request);
      if (!topic) throw std::move(topic).status();
    
      std::cout << "The topic was successfully updated: " << topic->DebugString()
                << "\n";
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const awsRoleArn = 'arn:aws:iam:...';
    // const gcpServiceAccount = 'ingestion-account@...';
    // const streamArn = 'arn:aws:kinesis:...';
    // const consumerArn = 'arn:aws:kinesis:...';
    
    // Imports the Google Cloud client library
    import {PubSub, TopicMetadata} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function updateTopicIngestionType(
      topicNameOrId: string,
      awsRoleArn: string,
      gcpServiceAccount: string,
      streamArn: string,
      consumerArn: string,
    ) {
      const metadata: TopicMetadata = {
        ingestionDataSourceSettings: {
          awsKinesis: {
            awsRoleArn,
            gcpServiceAccount,
            streamArn,
            consumerArn,
          },
        },
      };
    
      await pubSubClient.topic(topicNameOrId).setMetadata(metadata);
    
      console.log('Topic updated with Kinesis source successfully.');
    }

For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html#arn-syntax-kinesis-streams) and [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html).

## Convert a standard topic to a Cloud Storage import topic

To convert a standard topic to a Cloud Storage import topic, first check that you meet all the [prerequisites](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#before_you_begin).

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the topic that you want to convert to a Cloud Storage import topic.

  3. In the topic details page, click **Edit**.

  4. Select the option **Enable ingestion**.

  5. For ingestion source, select **Google Cloud Storage**.

  6. For the Cloud Storage bucket, click **Browse**. 

The **Select bucket** page opens. Select one of the following options:

     * Select an existing bucket from any appropriate project.

     * Click the create icon and follow the instructions on the screen to create a new bucket. After you create the bucket, select the bucket for the Cloud Storage import topic.

  7. When you specify the bucket, Pub/Sub checks for the appropriate permissions on the bucket for the Pub/Sub service account. If there are permissions issues, you see an error message related to the permissions.

If you get permission issues, click **Set permissions**. For more information, see [ Grant Cloud Storage permissions to the Pub/Sub service account](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#assign_roles_cloudstorage).

  8. For **Object format** , select **Text** , **Avro** , or **Pub/Sub Avro**.

If you select **Text** , you can optionally specify a **Delimiter** with which to split objects into messages.

For more information about these options, see [Input format](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#input_format).

  9. Optional. You can specify a **Minimum object creation time** for your topic. If set, only objects created after the minimum object creation time are ingested. 

For more information, see [ Minimum object creation time](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#minimum_object_creation_time). 

  10. You must specify a **Glob pattern**. To ingest all objects in the bucket, use `**` as the glob pattern. Only objects that match the given pattern are ingested. 

For more information, see [ Match a glob pattern](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#match_glob_pattern).

  11. Retain the other default settings.
  12. Click **Update topic**.



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

     * INPUT_FORMAT: Specifies the format of the objects that are ingested. This can be `text`, `avro`, or `pubsub_avro`. For more information about these options, see [Input format](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#input_format).

     * TEXT_DELIMITER: Specifies the delimiter with which to split text objects into Pub/Sub messages. This must be a single character and must only be set when `INPUT_FORMAT` is `text`. It defaults to the newline character (`\n`).

When using gcloud CLI to specify the delimiter, pay close attention to the handling of special characters like newline `\n`. Use the format `'\n'` to ensure the delimiter is correctly interpreted. Simply using `\n` without quotes or escaping results in a delimiter of `"n"`.

     * MINIMUM_OBJECT_CREATE_TIME: Specifies the minimum time at which an object was created in order for it to be ingested. This should be in UTC in the format `YYYY-MM-DDThh:mm:ssZ`. For example, `2024-10-14T08:30:30Z`.

Any date, past or future, from `0001-01-01T00:00:00Z` to `9999-12-31T23:59:59Z` inclusive, is valid.

     * MATCH_GLOB: Specifies the glob pattern to match in order for an object to be ingested. When you are using gcloud CLI, a match glob with `*` characters must have the `*` character formatted as escaped in the form `\*\*.txt` or the whole match glob must be in quotes `"**.txt"` or `'**.txt'`. For information on supported syntax for glob patterns, see the [ Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
