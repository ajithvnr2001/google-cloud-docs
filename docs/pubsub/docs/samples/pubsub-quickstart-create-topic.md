---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-quickstart-create-topic/
title: Create topic quickstart \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:19.799423+00:00
---

# Create topic quickstart  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-quickstart-create-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create topic quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Creates a topic.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Pub/Sub client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/app-lifecycle-manager/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/cloud-ftp/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/device-streaming/docs/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/fault-injection-testing/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/food-ai/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/location-finder/docs/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/oracle/compute/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/secure-access-connect/docs/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/unified-maintenance/docs/quickstart-client-libraries)
  * [Quickstart: Using client libraries](https://docs.cloud.google.com/universal-ledger/quickstart-client-libraries)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id) {
      auto topic = client.CreateTopic(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
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

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample pubsub-quickstart creates a Google Cloud Pub/Sub topic.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Sets your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Creates a client.
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the id for the new topic.
    	topicID := "my-topic"
    	pbTopic := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    	}
    
    	// Creates the new topic.
    	topic, err := client.TopicAdminClient.CreateTopic(ctx, pbTopic)
    	if err != nil {
    		log.Fatalf("Failed to create topic: %v", err)
    	}
    
    	fmt.Printf("Topic %v created.\n", topic)
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class CreateTopicExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        createTopicExample(projectId, topicId);
      }
    
      public static void createTopicExample(String projectId, String topicId) throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic = topicAdminClient.createTopic(topicName);
          System.out.println("Created topic: " + topic.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getName__)());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Cloud\PubSub\PubSubClient;
    
    # Your Google Cloud Platform project ID
    $projectId = 'YOUR_PROJECT_ID';
    
    # Instantiates a client
    $pubsub = new PubSubClient([
        'projectId' => $projectId
    ]);
    
    # The name for the new topic
    $topicName = 'my-new-topic-2';
    
    # Creates the new topic
    $topic = $pubsub->createTopic($topicName);
    
    echo 'Topic ' . $topic->name() . ' created.';

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    require "google/cloud/pubsub"
    
    # Instantiates a client
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    # The name for the new topic
    # topic_id = "your-topic-id"
    
    # Creates the new topic
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id)
    
    puts "Topic #{topic.name} created."

### Rust
    
    
    use google_cloud_pubsub::client::TopicAdmin;
    
    pub async fn sample(client: &TopicAdmin, project_id: &str, topic_id: &str) -> anyhow::Result<()> {
        let topic = client
            .create_topic()
            .set_name(format!("projects/{project_id}/topics/{topic_id}"))
            .send()
            .await?;
    
        println!("successfully created topic {topic:?}");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
