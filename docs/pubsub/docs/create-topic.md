---
url: https://docs.cloud.google.com/pubsub/docs/create-topic/
title: Create a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:02.448213+00:00
---

# Create a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create a topic Stay organized with collections  Save and categorize content based on your preferences. 

Within Pub/Sub, a topic is a named resource that represents a feed of messages. You must create a topic before you can publish or subscribe to it. Pub/Sub supports two kinds of topics: a standard topic and an import topic.

This document describes how to create a Pub/Sub standard topic. If you want to learn more about an import topic and how to create one, see [About import topics](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#import-topic-overview).

To create a topic you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API.

## Before you begin

  * Learn about [the Pub/Sub service and its terminology](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

  * Learn about the [publish process](https://docs.cloud.google.com/pubsub/docs/publish-message-overview).




### Required roles and permissions

To get the permissions that you need to create a topic, ask your administrator to grant you the Pub/Sub Editor(`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a topic. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a topic:

  * Grant this permission to create a topic on the project: `pubsub.topics.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level. You can create a subscription in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Properties of a topic

When you create or update a topic, you must specify its properties.

### Add a default subscription

Adds a default subscription to the Pub/Sub topic. You can create another subscription for the topic after the topic is created. The default subscription has the following properties:

  * Subscription ID of `-sub`
  * Pull delivery type
  * Message retention duration of seven days
  * Expiration after 31 days of inactivity
  * Acknowledgment deadline of 10 seconds
  * Immediate retry policy



### Use a schema

A schema is a format that the message data field must follow. A schema is a contract between the publisher and subscriber that Pub/Sub enforces. Topic schemas help standardize message types and permissions to allow them to be consumed by different teams in your organization. Pub/Sub creates a central authority for message types and permissions. To create a topic with schema, see [Schema overview](https://docs.cloud.google.com/pubsub/docs/schemas). 

### Enable ingestion

Enabling this property lets you ingest streaming data from external sources into a topic so that you can use the features of Google Cloud. To create an import topic for ingestion, see the following:

  * [Create an Amazon Kinesis Data Streams import topic](https://docs.cloud.google.com/pubsub/docs/create-aws-kinesis-import-topic)

  * [Create a Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic)

  * [Create an Azure Event Hubs topic](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic)

  * [Create an Amazon MSK topic](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic)

  * [Create a Confluent Cloud topic](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic)




### Enable topic message retention

By default, a Pub/Sub topic discards messages as soon as they are acknowledged by all subscriptions attached to the topic. Optionally, you can configure a topic to retain messages for a period of up to 31 days, with a minimum retention period of 10 minutes.

Message retention lets subscriptions replay previously acknowledged messages or replay messages that were published before you created the subscription. For more information, see [Replay and purge messages with seek](https://docs.cloud.google.com/pubsub/docs/replay-overview).

Storage costs for the messages retained by the topic are billed to the topic's project. After the message retention period has elapsed, Pub/Sub might discard the message regardless of its acknowledgment state.

To view metrics about retained messages, use the following Cloud Monitoring metrics:

  * [`topic/num_retained_messages`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/num_retained_messages): The number of retained messages
  * [`topic/oldest_retained_message_age`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/oldest_retained_message_age): The age of the oldest retained message
  * [`topic/retained_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/retained_bytes): The total size of the retained messages, in bytes



### Export message data to BigQuery

Enabling this property lets you create a BigQuery subscription that writes messages to an existing BigQuery table as they are received. You don't need to configure a separate subscriber client. For more information about BigQuery subscriptions, see [BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/bigquery).

### Backup message data to Cloud Storage

Enabling this property lets you create a Cloud Storage subscription that writes messages to an existing Cloud Storage table as they are received. You don't need to configure a separate subscriber client. For more information about Cloud Storage subscriptions, see [Cloud Storage subscriptions](https://docs.cloud.google.com/pubsub/docs/cloudstorage).

### Transforms

Topic SMTs allow for lightweight modifications to message data and attributes directly within Pub/Sub. This feature enables data cleaning, filtering, or format conversion before the messages are published to the topic.

For more information about SMTs, see the [SMTs overview](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).

### Google-owned and Google-managed encryption key

Specifies that the topic is encrypted using Google-owned and Google-managed encryption keys. Pub/Sub encrypts messages with Google-owned and Google-managed encryption keys by default, so choosing this option maintains the default behavior. Google handles key management and rotation automatically, ensuring your messages are always protected with the strongest available encryption. This option requires no further configuration. For more information about Google-owned and Google-managed encryption keys, see [Default encryption with Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek#default-encryption).

### Cloud KMS key

Specifies if the topic is encrypted with a customer-managed encryption key (CMEK). Pub/Sub encrypts messages with Google-owned and Google-managed encryption keys by default. If you specify this option, Pub/Sub uses the envelope encryption pattern with CMEK. In this approach, Cloud KMS does not encrypt the messages. Instead, Cloud KMS encrypts the Data Encryption Keys (DEKs) that Pub/Sub creates for each topic. Pub/Sub encrypts the messages using the newest DEK that was generated for the topic. Pub/Sub decrypts the messages shortly before they are delivered to subscribers. For more information about creating a key, see [Configure message encryption](https://docs.cloud.google.com/pubsub/docs/encryption).

## Create a topic

Create a topic before you can publish or subscribe to it.

### Console

To create a topic, follow these steps:

  1. In the Google Cloud console, go to the Pub/Sub **Create topic** page.

[Go to Create topic](https://console.cloud.google.com/cloudpubsub/topic/create)

  2. In the **Topic ID** field, enter an ID for your topic. For more information about naming topics, see the [naming guidelines](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  3. To create a default subscription for the topic, select **Add a default subscription**. This option is enabled by default.

  4. Optional. To use a schema with the topic, click **Use a schema** and provide the schema. For more information, see [Create and associate a schema when you create a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic#create-schema-when-creating-topic).

  5. For a standard topic, leave **Enable ingestion** unselected.

  6. Optional. To retain messages after they are published, select **Enable message retention**. Select the retention period in days, hours, and minutes. For more information, see Enable message retention.

  7. Optional. To export published messages to a BigQuery table, select **Export data to BigQuery** and enter the details for the table. For more information, see [Create BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).

  8. Optional. To back up published messages to a Cloud Storage bucket, select **Backup message data to Cloud Storage** and enter the details for the Cloud Storage bucket. For more information, see [Create Cloud Storage subscriptions](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription).

  9. Optional. Under **Transforms** , add one or more [Single Message Transforms](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) (SMTs) to manipulate and filter message data. For more information, see [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt).

  10. Optional. To use a customer-managed encryption key (CMEK) to encrypt messages, select **Cloud KMS key**. By default, Pub/Sub uses Google default encryption, which doesn't require a CMEK. For more information, see [Configure message encryption](https://docs.cloud.google.com/pubsub/docs/encryption).

  11. Optional. To manage the keys associated with the topic, click add**Manage keys**. For more information, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

  12. Click **Create topic**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a topic, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
         
         gcloud pubsub topics create TOPIC_ID
         




### REST

To create a topic, use the [`projects.topics.create`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/create) method:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    PUT https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your project ID.
  * TOPIC_ID is your topic ID.



Response:
    
    
    {
    "name": "projects/PROJECT_ID/topics/TOPIC_ID"
    }
    

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
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

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
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

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
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

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopic(topicNameOrId) {
      // Creates a new topic
      await pubSubClient.createTopic(topicNameOrId);
      console.log(`Topic ${topicNameOrId} created.`);
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopic(topicNameOrId: string) {
      // Creates a new topic
      await pubSubClient.createTopic(topicNameOrId);
      console.log(`Topic ${topicNameOrId} created.`);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    topic = publisher.create_topic(request={"name": topic_path})
    
    print(f"Created topic: {topic.name}")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id)
    
    puts "Topic #{topic.name} created."

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
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

## Organization policy constraints

Organizational policies can restrict topic creation, for example, a policy can restrict message storage in a Compute Engine region. To avoid topic creation errors, examine and update organizational policies, as needed, before creating a topic.

If your project is newly created, wait a few minutes for the organization policy to initialize before creating a topic.

[Go to Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies/gcp-resourceLocations)

For more information, see [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

## What's next

  * Choose the [type of subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) for your topic.

  * Learn how to [publish a message to a topic](https://docs.cloud.google.com/pubsub/docs/publisher).

  * Troubleshoot a [topic](https://docs.cloud.google.com/pubsub/docs/topic-troubleshooting).

  * Create or modify a topic with [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics), [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics), or [Client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
