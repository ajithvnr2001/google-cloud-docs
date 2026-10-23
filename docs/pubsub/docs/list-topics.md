---
url: https://docs.cloud.google.com/pubsub/docs/list-topics/
title: List topics \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:53.108857+00:00
---

# List topics  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/list-topics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  List topics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to list a Pub/Sub topic. To list a topic you can use the Google Cloud console, the gcloud CLI, the client library, or the Pub/Sub API.

## Before you begin

  * Learn about [topics](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#about_topics) and the publish messages workflow.
  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).



### Required roles and permissions

To get the permissions that you need to list topics and manage them, ask your administrator to grant you the Pub/Sub Editor(`roles/pubsub.editor`) IAM role on your topic or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list topics and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list topics and manage them:

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

## List a topic

### Console

  * In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

The **Topics** page lists all the available topics.

By default, the console returns 50 topics. You can increase this value to return a maximum of 200 topics by using the **Rows per page** drop-down toggle. This toggle only appears in the console if you have more than 20 topics in a project. 




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To list topics, use the [`gcloud pubsub topics list`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/list) command:
         
         gcloud pubsub topics list




By default, a maximum of 100 results are returned per query. You can specify an alternative value of up to 1,000 using the page size parameter. For example, using the Google Cloud CLI, specify [`--page-size=1000`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/list#LIST-COMMAND-FLAGS).

### REST

To list topics, use the [`projects.topics.list`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/list) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    GET https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics
    Authorization: Bearer ACCESS_TOKEN
      

Where:

* PROJECT_ID is your project ID.

Response:
    
    
    {
    "topics": [
      {
        "name": "projects/PROJECT_ID/topics/mytopic1",
        ...
      },
      {
        "name": "projects/PROJECT_ID/topics/mytopic2",
        ...
      }
    ]
    }

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string const& project_id) {
      int count = 0;
      for (auto& topic : client.ListTopics("projects/" + project_id)) {
        if (!topic) throw std::move(topic).status();
        std::cout << "Topic Name: " << topic->name() << "\n";
        ++count;
      }
      if (count == 0) {
        std::cout << "No topics found in project " << project_id << "\n";
      }
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System.Collections.Generic;
    
    public class ListProjectTopicsSample
    {
        public IEnumerable<Topic> ListProjectTopics(string projectId)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId);
            IEnumerable<Topic> topics = publisher.[ListTopics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_ListTopics_Google_Api_Gax_ResourceNames_ProjectName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(projectName);
            return topics;
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
    	"google.golang.org/api/iterator"
    )
    
    func listTopics(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.ListTopicsRequest{
    		Project: fmt.Sprintf("projects/%s", projectID),
    	}
    	it := client.TopicAdminClient.ListTopics(ctx, req)
    	for {
    		topic, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("error listing topics: %w", err)
    		}
    		fmt.Fprintf(w, "got topic: %s\n", topic)
    
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import java.io.IOException;
    
    public class ListTopicsExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
    
        listTopicsExample(projectId);
      }
    
      public static void listTopicsExample(String projectId) throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html).of(projectId);
          for ([Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic : topicAdminClient.listTopics(projectName).iterateAll()) {
            System.out.println(topic.getName());
          }
          System.out.println("Listed all topics.");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listAllTopics() {
      // Lists all topics in the current project
      const [topics] = await pubSubClient.getTopics();
      console.log('Topics:');
      topics.forEach(topic => console.log(topic.name));
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    // Imports the Google Cloud client library
    import {PubSub, Topic} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listAllTopics() {
      // Lists all topics in the current project
      const [topics] = await pubSubClient.getTopics();
      console.log('Topics:');
      topics.forEach((topic: Topic) => console.log(topic.name));
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Lists all Pub/Sub topics.
     *
     * @param string $projectId  The Google project ID.
     */
    function list_topics($projectId)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        foreach ($pubsub->topics() as $topic) {
            printf('Topic: %s' . PHP_EOL, $topic->name());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    project_path = f"projects/{project_id}"
    
    for topic in publisher.list_topics(request={"project": project_path}):
        print(topic)

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    topics = topic_admin.list_topics project: pubsub.project_path
    
    puts "Topics in project:"
    topics.each do |topic|
      puts topic.name
    end

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_pubsub::client::TopicAdmin;
    
    pub async fn sample(client: &TopicAdmin, project: &str) -> anyhow::Result<()> {
        let mut topics = client
            .list_topics()
            .set_project(format!("projects/{}", project))
            .by_item();
    
        println!("listing topics");
        while let Some(topic) = topics.next().await.transpose()? {
            println!("{topic:?}");
        }
        println!("DONE");
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
