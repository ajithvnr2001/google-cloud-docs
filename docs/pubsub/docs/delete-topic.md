---
url: https://docs.cloud.google.com/pubsub/docs/delete-topic/
title: Delete topics \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:32.626989+00:00
---

# Delete topics  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/delete-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Delete topics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to delete a Pub/Sub topic. To delete a topic, you can use the Google Cloud console, the Google CLI, the client library, or the Pub/Sub API.

**Caution:** Deletion is permanent. You cannot restore a topic that is deleted.

## Before you begin

  * Learn about [topics](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#about_topics) and the publish messages workflow.
  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).



### Required roles and permissions

To get the permissions that you need to delete topics and manage them, ask your administrator to grant you the Pub/Sub Editor(`roles/pubsub.editor`) IAM role on your topic or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete topics and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete topics and manage them:

  * Create a topic: `pubsub.topics.create`
  * Delete a topic: `pubsub.topics.delete`
  * Detach a subscription from a topic: `pubsub.topics.detachSubscription`
  * Get a topic: `pubsub.topics.get`
  * List a topic: `pubsub.topics.list`
  * Publish to a topic: `pubsub.topics.publish`
  * Update a topic: `pubsub.topics.update`
  * Get the IAM policy for a topic: `pubsub.topics.getIamPolicy`
  * Configure the [IAM policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy) for a topic: `pubsub.topics.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level. You can create a subscription in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Delete a topic

When you delete a topic, its subscriptions are not deleted. The message backlog from the subscription is available for subscribers. After a topic is deleted, its subscriptions have the topic name `_deleted-topic_`. If you try to create a topic with the same name as the one you had just deleted, expect an error for a brief period.

### Console

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Select a topic and click more_vert**More actions**.

  3. Click **Delete**.

The **Delete topic** window appears.

  4. Enter `delete` and then click **Delete**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To delete a topic, use the [`gcloud pubsub topics delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/delete) command:
         
         gcloud pubsub topics delete TOPIC_ID




### REST

To delete a topic, use the [`projects.topics.delete`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/delete) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    DELETE https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID
    Authorization: Bearer ACCESS_TOKEN
      

Where:

  * PROJECT_ID is your project ID.
  * TOPIC_ID is your topic ID.



Response:

If the request is successful, the response is an empty JSON object.

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string const& project_id,
       std::string const& topic_id) {
      auto status =
          client.DeleteTopic(pubsub::Topic(project_id, topic_id).FullName());
      // Note that kNotFound is a possible result when the library retries.
      if (status.code() == google::cloud::StatusCode::kNotFound) {
        std::cout << "The topic was not found\n";
        return;
      }
      if (!status.ok()) throw std::runtime_error(status.message());
    
      std::cout << "The topic was successfully deleted\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class DeleteTopicSample
    {
        public void DeleteTopic(string projectId, string topicId)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            publisher.[DeleteTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_DeleteTopic_Google_Cloud_PubSub_V1_DeleteTopicRequest_Google_Api_Gax_Grpc_CallSettings_)(topicName);
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
    
    func delete(w io.Writer, projectID, topicID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.DeleteTopicRequest{
    		Topic: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    	}
    	err = client.TopicAdminClient.DeleteTopic(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to delete topic: %w", err)
    	}
    	fmt.Fprintln(w, "Deleted topic")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class DeleteTopicExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        deleteTopicExample(projectId, topicId);
      }
    
      public static void deleteTopicExample(String projectId, String topicId) throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
          try {
            topicAdminClient.deleteTopic(topicName);
            System.out.println("Deleted topic.");
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
            System.out.println(e.getMessage());
          }
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
    
    async function deleteTopic(topicNameOrId) {
      /**
       * TODO(developer): Uncomment the following line to run the sample.
       */
      // const topicName = 'my-topic';
    
      // Deletes the topic
      await pubSubClient.topic(topicNameOrId).delete();
      console.log(`Topic ${topicNameOrId} deleted.`);
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
    
    async function deleteTopic(topicNameOrId: string) {
      /**
       * TODO(developer): Uncomment the following line to run the sample.
       */
      // const topicName = 'my-topic';
    
      // Deletes the topic
      await pubSubClient.topic(topicNameOrId).delete();
      console.log(`Topic ${topicNameOrId} deleted.`);
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
    function delete_topic($projectId, $topicName)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $topic = $pubsub->topic($topicName);
        $topic->delete();
    
        printf('Topic deleted: %s' . PHP_EOL, $topic->name());
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    publisher.delete_topic(request={"topic": topic_path})
    
    print(f"Topic deleted: {topic_path}")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    topic_admin.delete_topic topic: pubsub.topic_path(topic_id)
    
    puts "Topic #{topic_id} deleted."

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_pubsub::client::TopicAdmin;
    
    pub async fn sample(client: &TopicAdmin, project_id: &str, topic_id: &str) -> anyhow::Result<()> {
        client
            .delete_topic()
            .set_topic(format!("projects/{project_id}/topics/{topic_id}"))
            .send()
            .await?;
    
        println!("successfully deleted topic");
        Ok(())
    }

## What's next

  * Choose the [type of subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) for your topic.

  * Create a subscription for your topic: [pull](https://docs.cloud.google.com/pubsub/docs/create-subscription), [push](https://docs.cloud.google.com/pubsub/docs/create-push-subscription), or [BigQuery](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).

  * Create or modify a topic with [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics).

  * Create or modify a topic with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
