---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-cloud-storage-ingestion/
title: Create topic with Cloud Storage ingestion \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:01.970524+00:00
---

# Create topic with Cloud Storage ingestion  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-cloud-storage-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create topic with Cloud Storage ingestion Stay organized with collections  Save and categorize content based on your preferences. 

Create a Pub/Sub topic that ingests from a Cloud Storage bucket

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    
    public class CreateTopicWithCloudStorageIngestionSample
    {
        public Topic CreateTopicWithCloudStorageIngestion(string projectId, string topicId, string bucket, string inputFormat, string textDelimiter, string matchGlob, DateTimeOffset minimumObjectCreateTime)
        {
    
            IngestionDataSourceSettings.Types.CloudStorage cloudStorageSettings = new IngestionDataSourceSettings.Types.CloudStorage
            {
                Bucket = bucket,
                MinimumObjectCreateTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTimeOffset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTimeOffset_System_DateTimeOffset_)(minimumObjectCreateTime),
            };
    
            switch (inputFormat)
            {
                case "text":
                    cloudStorageSettings.TextFormat = new IngestionDataSourceSettings.Types.CloudStorage.Types.TextFormat
                    {
                        Delimiter = textDelimiter
                    };
                    break;
                case "avro":
                    cloudStorageSettings.AvroFormat = new IngestionDataSourceSettings.Types.CloudStorage.Types.AvroFormat();
                    break;
                case "pubsub_avro":
                    cloudStorageSettings.PubsubAvroFormat = new IngestionDataSourceSettings.Types.CloudStorage.Types.PubSubAvroFormat();
                    break;
                default:
                    throw new [RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html)(new [Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html)([StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[InvalidArgument](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_InvalidArgument), $"inputFormat must be in ('text', 'avro', 'pubsub_avro'); got value: {inputFormat}"));
            }
    
            if (!string.IsNullOrEmpty(matchGlob))
            {
                cloudStorageSettings.[MatchGlob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.Types.CloudStorage.html#Google_Cloud_PubSub_V1_IngestionDataSourceSettings_Types_CloudStorage_MatchGlob) = matchGlob;
            }
    
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = new [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html)()
            {
                Name = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FormatProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FormatProjectTopic_System_String_System_String_)(projectId, topicId),
                IngestionDataSourceSettings = new [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html)() { CloudStorage = cloudStorageSettings }
            };
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) createdTopic = publisher.[CreateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_)(topic);
            Console.WriteLine($"Topic {createdTopic.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} created.");
    
            return createdTopic;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    use Google\Cloud\PubSub\V1\IngestionDataSourceSettings\CloudStorage\AvroFormat;
    use Google\Cloud\PubSub\V1\IngestionDataSourceSettings\CloudStorage\PubSubAvroFormat;
    use Google\Cloud\PubSub\V1\IngestionDataSourceSettings\CloudStorage\TextFormat;
    use Google\Protobuf\Timestamp;
    
    /**
     * Creates a topic with Cloud Storage Ingestion.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $bucket  Cloud Storage bucket.
     * @param string $inputFormat  Input format for the Cloud Storage data. Must be one of text, avro, or pubsub_avro.
     * @param string $minimumObjectCreatedTime  Only objects with a larger or equal creation timestamp will be ingested.
     * @param string $textDelimiter  Delimiter for text format input.
     * @param string $matchGlob  Glob pattern used to match objects that will be ingested. If unset, all objects will be ingested.
     */
    function create_topic_with_cloud_storage_ingestion(
        string $projectId,
        string $topicName,
        string $bucket,
        string $inputFormat,
        string $minimumObjectCreatedTime,
        string $textDelimiter = '',
        string $matchGlob = ''
    ): void {
        $datetime = new \DateTimeImmutable($minimumObjectCreatedTime);
        $timestamp = (new Timestamp())
            ->setSeconds($datetime->getTimestamp())
            ->setNanos($datetime->format('u') * 1000);
    
        $cloudStorageData = [
            'bucket' => $bucket,
            'minimum_object_create_time' => $timestamp
        ];
    
        $cloudStorageData[$inputFormat . '_format'] = match($inputFormat) {
            'text' => new TextFormat(['delimiter' => $textDelimiter]),
            'avro' => new AvroFormat(),
            'pubsub_avro' => new PubSubAvroFormat(),
            default => throw new \InvalidArgumentException(
                'inputFormat must be in (\'text\', \'avro\', \'pubsub_avro\'); got value: ' . $inputFormat
            )
        };
    
        if (!empty($matchGlob)) {
            $cloudStorageData['match_glob'] = $matchGlob;
        }
    
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->createTopic($topicName, [
            'ingestionDataSourceSettings' => [
                'cloud_storage' => $cloudStorageData
            ]
        ]);
    
        printf('Topic created: %s' . PHP_EOL, $topic->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    # bucket = "your-bucket-id"
    # input_format = "text"
    # text_delimiter = "\n"
    # match_glob = "**.txt"
    # minimum_object_create_time = Google::Protobuf::Timestamp.new
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    topic_admin = pubsub.topic_admin
    cloud_storage =
      Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage
    
    settings = cloud_storage.new \
      bucket: bucket,
      minimum_object_create_time: minimum_object_create_time
    
    case input_format
    when "text"
      settings.text_format = cloud_storage::TextFormat.new \
        delimiter: text_delimiter
    when "avro"
      settings.avro_format = cloud_storage::AvroFormat.new
    when "pubsub_avro"
      settings.pubsub_avro_format = cloud_storage::PubSubAvroFormat.new
    else
      raise "input_format must be in ('text', 'avro', 'pubsub_avro');" \
            "got value: #{input_format}"
    end
    
    if !match_glob.nil? && !match_glob.empty?
      settings.match_glob = match_glob
    end
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id),
                                     ingestion_data_source_settings: {
                                       cloud_storage: settings
                                     }
    
    puts "Topic with Cloud Storage Ingestion #{topic.name} created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
