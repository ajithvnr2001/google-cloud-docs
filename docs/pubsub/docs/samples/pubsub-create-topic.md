---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic/
title: Create topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:04.892888+00:00
---

# Create topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create topic Stay organized with collections  Save and categorize content based on your preferences. 

Creates a topic.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic)
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

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    
    public class CreateTopicSample
    {
        public Topic CreateTopic(string projectId, string topicId)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            var topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = null;
    
            try
            {
                topic = publisher.[CreateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_)(topicName);
                Console.WriteLine($"Topic {topic.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} created.");
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
            {
                Console.WriteLine($"Topic {topicName} already exists.");
            }
            return topic;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    func create(w io.Writer, projectID, topicID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	topic := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    	}
    	t, err := client.TopicAdminClient.CreateTopic(ctx, topic)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Topic created: %v\n", t)
    	return nil
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

### Kotlin
    
    
    import com.google.api.gax.rpc.AlreadyExistsException
    import com.google.api.gax.rpc.ApiException
    import com.google.cloud.pubsub.v1.TopicAdminClient
    import com.google.pubsub.v1.TopicName
    import java.io.IOException
    
    /**
     * Creates a Google Cloud Pub/Sub topic for publishing messages.
     *
     * @param projectId Google Cloud project identifier (for example, "example-project-id").
     * @param topicId Identifier for the new Pub/Sub topic (for example, "example-topic-id").
     */
    fun createTopic(projectId: String, topicId: String) {
      val topicName = TopicName.of(projectId, topicId)
    
      try {
        TopicAdminClient.create().use { topicAdminClient ->
          val response = topicAdminClient.createTopic(topicName)
    
          println("Resource ID: ${response.name}")
          println("Kms Key Name: ${response.kmsKeyName}")
          println("Labels: ${response.labelsMap}")
        }
      } catch (err: AlreadyExistsException) {
        System.err.println(
          "error: topic '$topicId' already exists in project '$projectId': ${err.message}"
        )
      } catch (err: ApiException) {
        System.err.println(
          "error: failed to create topic '$topicId' in project '$projectId': ${err.message}"
        )
      } catch (err: IOException) {
        System.err.println(
          "error: failed to initialize TopicAdminClient for topic '$topicId' in project '$projectId': ${err.message}"
        )
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
      }
    ]
    
    exports['sample transformation correctly transforms TS 1'] = `
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //      http://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // This is a generated sample, using the typeless sample bot. Please
    // look for the source TypeScript sample (.ts) for modifications.
    'use strict';
    
    /**
     * This application demonstrates how to perform basic operations on
     * schemas with the Google Cloud Pub/Sub API.
     *
     * For more information, see the README.md under /pubsub and the documentation
     * at https://cloud.google.com/pubsub/docs.
     */
    
    // sample-metadata:
    //   title: List schemas on a project
    //   description: Gets a list of schemas which were previously created in the project.
    //   usage: node listSchemas.js
    
    
    // Imports the Google Cloud client library
    const { PubSub } = require("@google-cloud/pubsub");
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listSchemas() {
      for await (const s of pubSubClient.listSchemas()) {
        console.log(s.name);
      }
      console.log('Listed schemas.');
    }
    
    function main() {
      listSchemas().catch((err) => {
        console.error(err.message);
        process.exitCode = 1;
      });
    }
    
    main();
    `
    
    exports['command line option "targets" works with a single sample file 1'] = `
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //      http://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // This is a generated sample, using the typeless sample bot. Please
    // look for the source TypeScript sample (.ts) for modifications.
    'use strict';
    
    /**
     * This application demonstrates how to perform basic operations on
     * schemas with the Google Cloud Pub/Sub API.
     *
     * For more information, see the README.md under /pubsub and the documentation
     * at https://cloud.google.com/pubsub/docs.
     */
    
    // sample-metadata:
    //   title: List schemas on a project
    //   description: Gets a list of schemas which were previously created in the project.
    //   usage: node listSchemas.js
    
    
    // Imports the Google Cloud client library
    const { PubSub } = require("@google-cloud/pubsub");
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listSchemas() {
      for await (const s of pubSubClient.listSchemas()) {
        console.log(s.name);
      }
      console.log('Listed schemas.');
    }
    
    function main() {
      listSchemas().catch((err) => {
        console.error(err.message);
        process.exitCode = 1;
      });
    }
    
    main();
    `
    
    exports['command line option "targets" works with multiple sample files 1'] = [
    ]
    
    exports['command line option "outputpath" causes the output to move 1'] = [
    ]
    
    exports['command line option "recursive" causes recursion and only matches samples 1'] = [
    ]
    

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Creates a Pub/Sub topic.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     */
    function create_topic($projectId, $topicName)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $topic = $pubsub->createTopic($topicName);
    
        printf('Topic created: %s' . PHP_EOL, $topic->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
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
