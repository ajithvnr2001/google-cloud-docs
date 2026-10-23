---
url: https://docs.cloud.google.com/pubsub/docs/associate-schema-topic/
title: Associate a schema with a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:00.320719+00:00
---

# Associate a schema with a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/associate-schema-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Associate a schema with a topic Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to associate schemas for Pub/Sub topics.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to associate and manage schemas, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to associate and manage schemas. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to associate and manage schemas:

  * Create schema: `pubsub.schemas.create`
  * Attach schema to topic: `pubsub.schemas.attach`
  * Commit a schema revision: `pubsub.schemas.commit`
  * Delete a schema or a schema revision: `pubsub.schemas.delete`
  * Get a schema or schema revisions: `pubsub.schemas.get`
  * List schemas: `pubsub.schemas.list`
  * List schema revisions: `pubsub.schemas.listRevisions`
  * Rollback a schema: `pubsub.schemas.rollback`
  * Validate a message: `pubsub.schemas.validate`
  * Get the IAM policy for a schema: `pubsub.schemas.getIamPolicy`
  * Configure the [IAM policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy) for a schema: `pubsub.schemas.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can grant roles and permissions to principals such as users, groups, domains, or service accounts. You can create a schema in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Guidelines to associate a schema with a topic

You can associate a schema with a topic when you create or edit a topic. Here are the guidelines for associating a schema with a topic:

  * You can associate a schema with one or more topics.

After a schema is associated with a topic, every message that the topic receives from the publishers must follow that schema.

  * When you associate a schema with a topic, you must also specify the encoding of the messages to be published as `BINARY` or `JSON`. If using JSON with an Avro schema, pay close attention to the [encoding rules for unions](https://avro.apache.org/docs/1.11.1/specification/#json-encoding).

  * If a schema associated with a topic has revisions, messages must match the encoding and validate against a revision within the available range. If they don't validate, the message fails to publish.

Revisions are tried in reverse chronological order that is based on creation time. To create a schema revision, see [Commit a schema revision](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision).




## Validation logic for a message schema

When you associate a schema with a topic and if the schema has revisions, you can specify a subset range of revisions to use. If you don't specify a range, the entire range is used for validation.

If you don't specify a revision as **First revision allowed** , then the oldest existing revision for the schema is used for validation. If you don't specify a revision as **Last revision allowed** , then the newest existing revision for the schema is used.

Let's take the example of Schema `S` that is attached to topic `T`.

Schema `S` has the revision IDs `A`,`B`, `C`, and `D` created in order, where `A` is the first or oldest revision. None of the schemas are identical to each other, or rollbacks of an existing schema.

  * If you only set the **First revision allowed** field as `B`, messages conforming only to schema `A` are rejected, while messages conforming to schemas `B`, `C`, and `D` are accepted.

  * If you only set the **Last revision allowed** field as `C`, messages that conform to schemas `A`, `B`, and `C` are accepted, and messages that conform only to schema `D` are rejected.

  * If you set both fields **First revision allowed** as `B` and **Last revision allowed** as `C`, messages that conform to schemas `B` and `C` are accepted.

  * You can also set the first and last revision to the same revision ID. In this case, only messages that conform to that revision are accepted.




## Create and associate a schema when you create a topic

You can create a topic with a schema using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

### Console

  1. In the Google Cloud console, go to the **Pub/Sub topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click **Create topic**.

  3. In the **Topic ID** field, enter an ID for your topic.

To name a topic, see the [guidelines](https://docs.cloud.google.com/pubsub/docs/create-topic#resource_names).

  4. Check the box for **Use a schema**.

Retain the default settings for the remaining fields.

You can create a schema or use an existing schema.

  5. If you are creating a schema, follow these steps: `

     1. For **Select a Pub/Sub schema** , select **Create a new schema**.

The **Create schema** page is displayed in a secondary tab.

Follow the steps in [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).

     1. Go back to the **Create topic** tab and click **Refresh**.

     2. Search for your schema in the **Select a Pub/Sub schema** field.

     3. Select the message encoding as **JSON** or **Binary**.

The schema you just created has a revision ID. You can create additional schema revisions as discussed in [Commit a schema revision](https://docs.cloud.google.com/pubsub/docs/create-schemas).

  6. If you are associating an already-created schema, follow these steps:

     1. For **Select a Pub/Sub schema** , select an existing schema.

     2. Select the message encoding as **JSON** or **Binary**.

  7. Optional: If the selected schema has revisions, for **Revision Range** , use the drop-down menus for **First revision allowed** and **Last revision allowed**.




You can specify both fields, specify only one, or retain the default settings based on your requirements.

  1. Retain the default settings for the remaining fields.

  2. Click **Create** to save the topic and assign it to the selected schema.




### gcloud

To create a topic assigned with a previously created schema, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
    
    
    gcloud pubsub topics create TOPIC_ID \
            --message-encoding=ENCODING_TYPE \
            --schema=SCHEMA_ID \
            --first-revision-id=FIRST_REVISION_ID \
            --last-revision-id=LAST_REVISION_ID \

Where:

  * TOPIC_ID is the ID for the topic that you're creating.
  * ENCODING_TYPE is the encoding of messages validated against the schema. This value must be set to either `JSON` or `BINARY`.
  * SCHEMA_ID is the ID of an existing schema.
  * FIRST_REVISION_ID is the ID of the oldest revision to validate against.
  * LAST_REVISION_ID is the ID of the newest revision to validate against.



Both `--first-revision-id` and `--last-revision-id` are optional.

You can also assign a schema from a different Google Cloud project:
    
    
    gcloud pubsub topics create TOPIC_ID \
            --message-encoding=ENCODING_TYPE \
            --schema=SCHEMA_ID \
            --schema-project=SCHEMA_PROJECT \
            --project=TOPIC_PROJECT

Where:

  * SCHEMA_PROJECT is the project ID of the Google Cloud project for the schema.
  * TOPIC_PROJECT is the project ID of the Google Cloud project for the topic.



### REST

To create a topic, use the [`projects.topics.create`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/create) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    PUT https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID
    Authorization: Bearer ACCESS_TOKEN
    

Request body: 
    
    
    {
      "schemaSettings": {
        "schema": "SCHEMA_NAME",
        "encoding": "ENCODING_TYPE"
        "firstRevisionId": "FIRST_REVISION_ID"
        "lastRevisionId": "LAST_REVISION_ID"
      }
    }

Where:

  * PROJECT_ID is your project ID.
  * TOPIC_ID is your topic ID.
  * SCHEMA_NAME is the name of the schema that messages published should be validated against. The format is: `projects/PROJECT_ID/schemas/SCHEMA_ID`.
  * ENCODING_TYPE is the encoding of messages validated against the schema. This must be set to either `JSON` or `BINARY`.
  * FIRST_REVISION_ID is the ID of the oldest revision to validate against.
  * LAST_REVISION_ID is the ID of the newest revision to validate against.



Both `firstRevisionId` and `lastRevisionId` are optional.

Response:
    
    
    {
      "name": "projects/PROJECT_ID/topics/TOPIC_ID",
      "schemaSettings": {
        "schema": "SCHEMA_NAME",
        "encoding": "ENCODING_TYPE"
        "firstRevisionId": "FIRST_REVISION_ID"
        "lastRevisionId": "LAST_REVISION_ID"
      }
    }

Both `firstRevisionId` and `lastRevisionId` are omitted if not provided in the request.

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string schema_id, std::string const& encoding) {
      google::pubsub::v1::Topic request;
      request.set_name(pubsub::Topic(project_id, std::move(topic_id)).FullName());
      request.mutable_schema_settings()->set_schema(
          pubsub::Schema(std::move(project_id), std::move(schema_id)).FullName());
      request.mutable_schema_settings()->set_encoding(
          encoding == "JSON" ? google::pubsub::v1::JSON
                             : google::pubsub::v1::BINARY);
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

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    
    public class CreateTopicWithSchemaSample
    {
        public Topic CreateTopicWithSchema(string projectId, string topicId, string schemaId, [Encoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Encoding.html) encoding)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            var topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = new [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html)
            {
                TopicName = topicName,
                SchemaSettings = new [SchemaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaSettings.html)
                {
                    SchemaAsSchemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId),
                    Encoding = encoding
                }
            };
    
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) receivedTopic = null;
            try
            {
                receivedTopic = publisher.[CreateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_)(topic);
                Console.WriteLine($"Topic {topic.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} created.");
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
            {
                Console.WriteLine($"Topic {topicName} already exists.");
            }
            return receivedTopic;
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
    
    func createTopicWithSchemaRevisions(w io.Writer, projectID, topicID, schemaID, firstRevisionID, lastRevisionID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// schemaID := "my-schema-id"
    	// firstRevisionID := "my-revision-id"
    	// lastRevisionID := "my-revision-id"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	topic := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    		SchemaSettings: &pubsubpb.SchemaSettings{
    			Schema:          fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    			FirstRevisionId: firstRevisionID,
    			LastRevisionId:  lastRevisionID,
    			// Alternative encoding is pubsubpb.Encoding_JSON
    			Encoding: pubsubpb.Encoding_BINARY,
    		},
    	}
    	t, err := client.TopicAdminClient.CreateTopic(ctx, topic)
    	if err != nil {
    		return fmt.Errorf("CreateTopicWithConfig: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic with schema revision: %#v\n", t)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import com.google.pubsub.v1.[SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class CreateTopicWithSchemaRevisionsExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Use an existing schema.
        String schemaId = "your-schema-id";
        // Choose either BINARY or JSON message serialization in this topic.
        [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding = [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html).BINARY;
        // Set the minimum and maximum revsion ID
        String firstRevisionId = "your-revision-id";
        String lastRevisionId = "your-revision-id";
    
        createTopicWithSchemaRevisionsExample(
            projectId, topicId, schemaId, firstRevisionId, lastRevisionId, encoding);
      }
    
      public static void createTopicWithSchemaRevisionsExample(
          String projectId,
          String topicId,
          String schemaId,
          String firstRevisionid,
          String lastRevisionId,
          [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding)
          throws IOException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        [SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html) schemaSettings =
            [SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html).newBuilder()
                .setSchema(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)())
                .[setFirstRevisionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.Builder.html#com_google_pubsub_v1_SchemaSettings_Builder_setFirstRevisionId_java_lang_String_)(firstRevisionid)
                .[setLastRevisionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.Builder.html#com_google_pubsub_v1_SchemaSettings_Builder_setLastRevisionId_java_lang_String_)(lastRevisionId)
                .setEncoding(encoding)
                .build();
    
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setSchemaSettings_com_google_pubsub_v1_SchemaSettings_)(schemaSettings)
                      .build());
    
          System.out.println("Created topic with schema: " + topic.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getName__)());
        } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) e) {
          System.out.println(schemaName + "already exists.");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const schemaName = 'YOUR_SCHEMA_NAME_OR_ID';
    // const encodingType = 'BINARY';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function createTopicWithSchema(
      topicNameOrId,
      schemaNameOrId,
      encodingType,
    ) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const fullName = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
    
      // Creates a new topic with a schema. Note that you might also
      // pass Encodings.Json or Encodings.Binary here.
      await pubSubClient.createTopic({
        name: topicNameOrId,
        schemaSettings: {
          schema: fullName,
          encoding: encodingType,
        },
      });
      console.log(`Topic ${topicNameOrId} created with schema ${fullName}.`);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const schemaName = 'YOUR_SCHEMA_NAME_OR_ID';
    // const encodingType = 'BINARY';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopicWithSchema(
      topicNameOrId: string,
      schemaNameOrId: string,
      encodingType: 'BINARY' | 'JSON',
    ) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const fullName = await schema.getName();
    
      // Creates a new topic with a schema. Note that you might also
      // pass Encodings.Json or Encodings.Binary here.
      await pubSubClient.createTopic({
        name: topicNameOrId,
        schemaSettings: {
          schema: fullName,
          encoding: encodingType,
        },
      });
      console.log(`Topic ${topicNameOrId} created with schema ${fullName}.`);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    use Google\Cloud\PubSub\Schema;
    
    /**
     * Create a topic with a schema.
     *
     * @param string $projectId
     * @param string $topicId
     * @param string $schemaId
     * @param string $encoding
     */
    function create_topic_with_schema($projectId, $topicId, $schemaId, $encoding)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $schema = $pubsub->schema($schemaId);
    
        $topic = $pubsub->createTopic($topicId, [
            'schemaSettings' => [
                // The schema may be provided as an instance of the schema type,
                // or by using the schema ID directly.
                'schema' => $schema,
                // Encoding may be either `BINARY` or `JSON`.
                // Provide a string or a constant from Google\Cloud\PubSub\V1\Encoding.
                'encoding' => $encoding,
            ]
        ]);
    
        printf('Topic %s created', $topic->name());
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.api_core.exceptions import AlreadyExists, InvalidArgument
    from google.cloud.pubsub import [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html), SchemaServiceClient
    from google.pubsub_v1.types import Encoding
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # schema_id = "your-schema-id"
    # first_revision_id = "your-revision-id"
    # last_revision_id = "your-revision-id"
    # Choose either BINARY or JSON as valid message encoding in this topic.
    # message_encoding = "BINARY"
    
    publisher_client = PublisherClient()
    topic_path = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).topic_path(project_id, topic_id)
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)(project_id, schema_id)
    
    if message_encoding == "BINARY":
        encoding = Encoding.BINARY
    elif message_encoding == "JSON":
        encoding = Encoding.JSON
    else:
        encoding = Encoding.ENCODING_UNSPECIFIED
    
    try:
        response = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).create_topic(
            request={
                "name": topic_path,
                "schema_settings": {
                    "schema": schema_path,
                    "encoding": encoding,
                    "first_revision_id": first_revision_id,
                    "last_revision_id": last_revision_id,
                },
            }
        )
        print(f"Created a topic:\n{response}")
    
    except AlreadyExists:
        print(f"{topic_id} already exists.")
    except InvalidArgument:
        print("Please choose either BINARY or JSON as a valid message encoding type.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # topic_id = "your-topic-id"
    # schema_id = "your-schema-id"
    # Choose either BINARY or JSON as valid message encoding in this topic.
    # message_encoding = :BINARY
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id),
                                     schema_settings: {
                                       schema: pubsub.schema_path(schema_id),
                                       encoding: message_encoding
                                     }
    
    puts "Topic #{topic.name} created."

## Edit a schema associated with a topic

**Caution:** Changing the schema or encoding associated with a topic or removing the schema from a topic might break publishers that are actively publishing.

You can edit a topic to attach a schema, remove a schema, or update the revision range used for validating messages. In general, if you have changes planned for the schema in use, you can [commit a new revision](https://docs.cloud.google.com/pubsub/docs/create-schemas) and update the range of revisions used for the topic.

You can edit a schema associated with a topic using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

### Console

  1. In the Google Cloud console, go to the **Pub/Sub topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click the **Topic ID** of a topic.

  3. In the topic details page, click **Edit**.

  4. You can make the following changes to the schema.

It might take a few minutes for the changes to take place.

     * If you want to remove the schema from the topic, in the **Edit topic** page, clear the **Use a schema** checkbox.

     * If you want to change the schema, in the **Schema** section, select the name of a schema.

Update the other fields as required.

     * If you want to update the revision range, for **Revision Range** , use the drop-down menus for **First revision allowed** and **Last revision allowed**.

You can specify both fields, specify only one, or retain the default settings based on your requirements.

  5. Click **Update** to save the changes.




### gcloud
    
    
    gcloud pubsub topics update TOPIC_ID \
            --message-encoding=ENCODING_TYPE \
            --schema=SCHEMA_NAME \
            --first-revision-id=FIRST_REVISION_ID \
            --last-revision-id=LAST_REVISION_ID \

Where:

  * TOPIC_ID is the ID for the topic that you're creating.
  * ENCODING_TYPE is the encoding of messages validated against the schema. This value must be set to either `JSON` or `BINARY`.
  * SCHEMA_NAME is the name of an existing schema.
  * FIRST_REVISION_ID is the ID of oldest revision to validate against.
  * LAST_REVISION_ID is the ID of the newest revision to validate against.



Both `--first-revision-id` and `--last-revision-id` are optional.

### REST

To update a topic, use the [`projects.topics.patch`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/patch) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    PATCH https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID
    Authorization: Bearer ACCESS_TOKEN
    

Request body: 
    
    
    {
      "schemaSettings": {
        "schema": "SCHEMA_NAME",
        "encoding": "ENCODING_TYPE"
        "firstRevisionId": "FIRST_REVISION_ID"
        "lastRevisionId": "LAST_REVISION_ID"
        "update_mask":
      }
    }

Where:

  * PROJECT_ID is your project ID.
  * TOPIC_ID is your topic ID.
  * SCHEMA_NAME is the name of the schema that messages published should be validated against. The format is: `projects/PROJECT_ID/schemas/SCHEMA_ID`.
  * ENCODING_TYPE is the encoding of messages validated against the schema. This must be set to either `JSON` or `BINARY`.
  * FIRST_REVISION_ID is the ID of oldest revision to validate against.
  * LAST_REVISION_ID is the ID of the newest revision to validate against.



Both `firstRevisionId` and `lastRevisionId` are optional.

Response:
    
    
    {
      "name": "projects/PROJECT_ID/topics/TOPIC_ID",
      "schemaSettings": {
        "schema": "SCHEMA_NAME",
        "encoding": "ENCODING_TYPE"
        "firstRevisionId": "FIRST_REVISION_ID"
        "lastRevisionId": "LAST_REVISION_ID"
      }
    }

Both `firstRevisionId` and `lastRevisionId` are not set after the update.

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string const& first_revision_id,
       std::string const& last_revision_id) {
      google::pubsub::v1::UpdateTopicRequest request;
      auto* request_topic = request.mutable_topic();
      request_topic->set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      request_topic->mutable_schema_settings()->set_first_revision_id(
          first_revision_id);
      request_topic->mutable_schema_settings()->set_last_revision_id(
          last_revision_id);
      *request.mutable_update_mask()->add_paths() =
          "schema_settings.first_revision_id";
      *request.mutable_update_mask()->add_paths() =
          "schema_settings.last_revision_id";
      auto topic = client.UpdateTopic(request);
    
      if (!topic) throw std::move(topic).status();
    
      std::cout << "The topic was successfully updated: " << topic->DebugString()
                << "\n";
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
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    func updateTopicSchema(w io.Writer, projectID, topicID, firstRevisionID, lastRevisionID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic" // an existing topic that has schema settings attached to it.
    	// firstRevisionID := "my-revision-id"
    	// lastRevisionID := "my-revision-id"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	// This updates the first / last revision ID for the topic's schema.
    	// To clear the schema entirely, use a zero valued (empty) SchemaSettings
    	// with the same field mask.
    	req := &pubsubpb.UpdateTopicRequest{
    		Topic: &pubsubpb.Topic{
    			Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    			SchemaSettings: &pubsubpb.SchemaSettings{
    				FirstRevisionId: firstRevisionID,
    				LastRevisionId:  lastRevisionID,
    			},
    		},
    		// Construct a field mask to indicate which field to update in the topic.
    		// Fields are specified relative to the topic
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{"schema_settings.first_revision_id", "schema_settings.last_revision_id"},
    		},
    	}
    	gotTopicCfg, err := client.TopicAdminClient.UpdateTopic(ctx, req)
    	if err != nil {
    		fmt.Fprintf(w, "topic.Update err: %v\n", gotTopicCfg)
    		return err
    	}
    	fmt.Fprintf(w, "Updated topic with schema: %#v\n", gotTopicCfg)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.pubsub.v1.[SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import com.google.pubsub.v1.[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html);
    import java.io.IOException;
    
    public class UpdateTopicSchemaExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // This is an existing topic that has schema settings attached to it.
        String topicId = "your-topic-id";
        // Set the minimum and maximum revsion ID
        String firstRevisionId = "your-revision-id";
        String lastRevisionId = "your-revision-id";
    
        UpdateTopicSchemaExample.updateTopicSchemaExample(
            projectId, topicId, firstRevisionId, lastRevisionId);
      }
    
      public static void updateTopicSchemaExample(
          String projectId, String topicId, String firstRevisionid, String lastRevisionId)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
    
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          // Construct the schema settings with the changes you want to make.
          [SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html) schemaSettings =
              [SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html).newBuilder()
                  .[setFirstRevisionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.Builder.html#com_google_pubsub_v1_SchemaSettings_Builder_setFirstRevisionId_java_lang_String_)(firstRevisionid)
                  .[setLastRevisionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.Builder.html#com_google_pubsub_v1_SchemaSettings_Builder_setLastRevisionId_java_lang_String_)(lastRevisionId)
                  .build();
    
          // Construct the topic with the schema settings you want to change.
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                  .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                  .[setSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setSchemaSettings_com_google_pubsub_v1_SchemaSettings_)(schemaSettings)
                  .build();
    
          // Construct a field mask to indicate which field to update in the topic.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("schema_settings.first_revision_id")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("schema_settings.last_revision_id")
                  .build();
    
          [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html) request =
              [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html).newBuilder().setTopic(topic).setUpdateMask(updateMask).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) response = topicAdminClient.updateTopic(request);
    
          System.out.println("Updated topic with schema: " + topic.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getName__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.api_core.exceptions import InvalidArgument, NotFound
    from google.cloud.pubsub import PublisherClient
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # first_revision_id = "your-revision-id"
    # last_revision_id = "your-revision-id"
    
    publisher_client = PublisherClient()
    topic_path = publisher_client.topic_path(project_id, topic_id)
    
    try:
        response = publisher_client.update_topic(
            request={
                "topic": {
                    "name": topic_path,
                    "schema_settings": {
                        "first_revision_id": first_revision_id,
                        "last_revision_id": last_revision_id,
                    },
                },
                "update_mask": "schemaSettings.firstRevisionId,schemaSettings.lastRevisionId",
            }
        )
        print(f"Updated a topic schema:\n{response}")
    
    except NotFound:
        print(f"{topic_id} not found.")
    except InvalidArgument:
        print("Schema settings are not valid.")

## What's next

  * [Commit a schema revision](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision)
  * [Publish messages to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/publish-topics-schema)
  * [Validate a schema definition](https://docs.cloud.google.com/pubsub/docs/validate-schema-definition)
  * [Validate a message for a schema](https://docs.cloud.google.com/pubsub/docs/validate-schema-message)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
