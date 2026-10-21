---
url: https://docs.cloud.google.com/pubsub/docs/create-schemas/
title: Create a schema for a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:56.216083+00:00
---

# Create a schema for a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create a schema for a topic Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create schemas for Pub/Sub topics.

## Before you begin

Before you create a schema, complete the following:

  * Learn about [topics and the publishing workflow](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).
  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).



### Required roles and permissions

To get the permissions that you need to create and manage schemas, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage schemas. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage schemas:

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

## Create a schema

You can create a schema using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

Before creating a schema, review this [important information about schemas](https://docs.cloud.google.com/pubsub/docs/schemas#schema-info).

### Console

To create a schema, follow these steps:

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

  2. Click **Create schema**.

  3. In the **Schema ID** field, enter an ID for your schema.

For guidelines to name a schema, see [Guidelines to name a topic, subscription, or snapshot](https://docs.cloud.google.com/pubsub/docs/create-topic#resource_names).

  4. For **Schema type** , select either Avro or Protocol Buffer.

Learn more about [schema types](https://docs.cloud.google.com/pubsub/docs/schemas#types-schema).

  5. In the **Schema definition** field, enter the Avro or Protocol Buffer definition for your schema.

For example, here's a sample schema in Avro.
         
         {
           "type": "record",
           "name": "Avro",
           "fields": [
             {
               "name": "ProductName",
               "type": "string",
               "default": ""
             },
             {
               "name": "SKU",
               "type": "int",
               "default": 0
             },
             {
               "name": "InStock",
               "type": "boolean",
               "default": false
             }
           ]
         }
         
         

  6. Optional: Click **Validate definition** to check if the schema definition is correct.

The validation check does not check the compatibility of the schema with the messages to be published. Test messages in the next step.

  7. Optional: You can test if messages with the correct schema get published.

     1. Click **Test message**.

     2. In the **Test message** window, select a type of **Message encoding**.

     3. In the **Message body** , enter a test message.

     4. Click **Test**.

For example, here's a sample message for the test schema. In this example, select the **Message encoding** as `JSON`.
            
            {"ProductName":"GreenOnions", "SKU":34543, "InStock":true}
            

     5. Exit the test message page.

  8. Click **Create** to save the schema.




### gcloud
    
    
    gcloud pubsub schemas create SCHEMA_ID \
            --type=SCHEMA_TYPE \
            --definition=SCHEMA_DEFINITION

Where:

  * SCHEMA_TYPE is either `avro` or `protocol-buffer`.
  * SCHEMA_DEFINITION is a `string` containing the definition of the schema, formatted according to the chosen [schema type](https://docs.cloud.google.com/pubsub/docs/schemas).



You can also specify the schema definition in a file:
    
    
    gcloud pubsub schemas create SCHEMA_ID \
            --type=SCHEMA_TYPE \
            --definition-file=SCHEMA_DEFINITION_FILE

Where:

  * SCHEMA_TYPE is either `avro` or `protocol-buffer`.
  * SCHEMA_DEFINITION_FILE is a `string` containing the path to the file with the definition of the schema, formatted according to the chosen [schema type](https://docs.cloud.google.com/pubsub/docs/schemas#types-schema).



### REST

To create a schema, send a POST request like the following:
    
    
    POST https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas?schemaId=SCHEMA_ID
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json --data @response-body.json
    

Specify the following fields in the request body:
    
    
    {
      "definition": SCHEMA_DEFINITION,
      "type": SCHEMA_TYPE
    }

Where:

  * SCHEMA_TYPE is either `avro` or `protocol-buffer`.
  * SCHEMA_DEFINITION is a string containing the definition of the schema, formatted according to the chosen [schema type](https://docs.cloud.google.com/pubsub/docs/schemas#types-schema).



The response body should contain a JSON representation of a [schema resource](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema). For example:
    
    
    {
      "name": SCHEMA_NAME,
      "type": SCHEMA_TYPE,
      "definition": SCHEMA_DEFINITION,
      "revisionId": REVISION_ID,
      "revisionCreateTime": REVISION_CREATE_TIME
    }
    

Where:

  * REVISION_ID is the server-generated ID for the revision.
  * REVISION_CREATE_TIME is the ISO 8601 timestamp at which the revision was created.



### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

### Avro
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& schema_definition_file) {
      std::string const definition = ReadFile(schema_definition_file);
    
      google::pubsub::v1::CreateSchemaRequest request;
      request.set_parent(google::cloud::Project(project_id).FullName());
      request.set_schema_id(schema_id);
      request.mutable_schema()->set_type(google::pubsub::v1::Schema::AVRO);
      request.mutable_schema()->set_definition(definition);
      auto schema = client.CreateSchema(request);
      if (schema.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The schema already exists\n";
        return;
      }
      if (!schema) throw std::move(schema).status();
    
      std::cout << "Schema successfully created: " << schema->DebugString()
                << "\n";
    }

### Proto
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& schema_definition_file) {
      std::string const definition = ReadFile(schema_definition_file);
    
      google::pubsub::v1::CreateSchemaRequest request;
      request.set_parent(google::cloud::Project(project_id).FullName());
      request.set_schema_id(schema_id);
      request.mutable_schema()->set_type(
          google::pubsub::v1::Schema::PROTOCOL_BUFFER);
      request.mutable_schema()->set_definition(definition);
      auto schema = client.CreateSchema(request);
      if (schema.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The schema already exists\n";
        return;
      }
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema successfully created: " << schema->DebugString()
                << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

### Avro
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.IO;
    
    public class CreateAvroSchemaSample
    {
        public Schema CreateAvroSchema(string projectId, string schemaId, string pathToDefinition)
        {
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html) schemaService = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_Create)();
            var schemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId);
            string schemaDefinition = File.ReadAllText(pathToDefinition);
            [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html) schema = new [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html)
            {
                SchemaName = schemaName,
                Type = [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html).[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html)s.[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html).[Avro](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html#Google_Cloud_PubSub_V1_Schema_Types_Type_Avro),
                Definition = schemaDefinition
            };
            [CreateSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSchemaRequest.html) createSchemaRequest = new [CreateSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSchemaRequest.html)
            {
                ParentAsProjectName = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId),
                SchemaId = schemaId,
                Schema = schema
            };
    
            try
            {
                schema = schemaService.[CreateSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_CreateSchema_Google_Api_Gax_ResourceNames_ProjectName_Google_Cloud_PubSub_V1_Schema_System_String_Google_Api_Gax_Grpc_CallSettings_)(createSchemaRequest);
                Console.WriteLine($"Schema {schema.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html#Google_Cloud_PubSub_V1_Schema_Name)} created.");
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
            {
                Console.WriteLine($"Schema {schemaName} already exists.");
            }
            return schema;
        }
    }

### Proto
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.IO;
    
    public class CreateProtoSchemaSample
    {
        public Schema CreateProtoSchema(string projectId, string schemaId, string pathToDefinition)
        {
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html) schemaService = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_Create)();
            var schemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId);
            string schemaDefinition = File.ReadAllText(pathToDefinition);
            [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html) schema = new [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html)
            {
                SchemaName = schemaName,
                Type = [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html).[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html)s.[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html).[ProtocolBuffer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html#Google_Cloud_PubSub_V1_Schema_Types_Type_ProtocolBuffer),
                Definition = schemaDefinition
            };
            [CreateSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSchemaRequest.html) createSchemaRequest = new [CreateSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSchemaRequest.html)
            {
                ParentAsProjectName = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId),
                SchemaId = schemaId,
                Schema = schema
            };
    
            try
            {
                schema = schemaService.[CreateSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_CreateSchema_Google_Api_Gax_ResourceNames_ProjectName_Google_Cloud_PubSub_V1_Schema_System_String_Google_Api_Gax_Grpc_CallSettings_)(createSchemaRequest);
                Console.WriteLine($"Schema {schema.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html#Google_Cloud_PubSub_V1_Schema_Name)} created.");
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
            {
                Console.WriteLine($"Schema {schemaName} already exists.");
            }
            return schema;
        }
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).

### Avro
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	pubsub "cloud.google.com/go/pubsub/v2/apiv1"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    // createAvroSchema creates a schema resource from a JSON-formatted Avro schema file.
    func createAvroSchema(w io.Writer, projectID, schemaID, avscFile string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	// avscFile = "path/to/an/avro/schema/file(.avsc)/formatted/in/json"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	avscSource, err := os.ReadFile(avscFile)
    	if err != nil {
    		return fmt.Errorf("error reading from file: %s", avscFile)
    	}
    
    	req := &pubsubpb.CreateSchemaRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		Schema: &pubsubpb.Schema{
    			Type:       pubsubpb.Schema_AVRO,
    			Definition: string(avscSource),
    		},
    		SchemaId: schemaID,
    	}
    	s, err := client.CreateSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("error calling CreateSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Schema created: %#v\n", s)
    	return nil
    }
    

### Proto
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	pubsub "cloud.google.com/go/pubsub/v2/apiv1"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    // createProtoSchema creates a schema resource from a schema proto file.
    func createProtoSchema(w io.Writer, projectID, schemaID, protoFile string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	// protoFile = "path/to/a/proto/schema/file(.proto)/formatted/in/protocol/buffers"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	protoSource, err := os.ReadFile(protoFile)
    	if err != nil {
    		return fmt.Errorf("error reading from file: %s", protoFile)
    	}
    
    	req := &pubsubpb.CreateSchemaRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		Schema: &pubsubpb.Schema{
    			Type:       pubsubpb.Schema_PROTOCOL_BUFFER,
    			Definition: string(protoSource),
    		},
    		SchemaId: schemaID,
    	}
    	s, err := client.CreateSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("error calling CreateSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Schema created: %#v\n", s)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

### Avro
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class CreateAvroSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id";
        String avscFile = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json";
    
        createAvroSchemaExample(projectId, schemaId, avscFile);
      }
    
      public static [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) createAvroSchemaExample(String projectId, String schemaId, String avscFile)
          throws IOException {
    
        [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html).of(projectId);
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        // Read an Avro schema file formatted in JSON as a string.
        String avscSource = new String(Files.readAllBytes(Paths.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier.html#com_google_api_gax_rpc_InputStreamSupplier_get__)(avscFile)));
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema =
              schemaServiceClient.createSchema(
                  projectName,
                  [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).newBuilder()
                      .setName(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)())
                      .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setType_com_google_pubsub_v1_Schema_Type_)([Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).Type.AVRO)
                      .[setDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setDefinition_java_lang_String_)(avscSource)
                      .build(),
                  schemaId);
    
          System.out.println("Created a schema using an Avro schema:\n" + schema);
          return schema;
        } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) e) {
          System.out.println(schemaName + "already exists.");
          return null;
        }
      }
    }

### Proto
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class CreateProtoSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id";
        String protoFile = "path/to/a/proto/file/(.proto)/formatted/in/protocol/buffers";
    
        createProtoSchemaExample(projectId, schemaId, protoFile);
      }
    
      public static [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) createProtoSchemaExample(String projectId, String schemaId, String protoFile)
          throws IOException {
    
        [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html).of(projectId);
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        // Read a proto file as a string.
        String protoSource = new String(Files.readAllBytes(Paths.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier.html#com_google_api_gax_rpc_InputStreamSupplier_get__)(protoFile)));
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema =
              schemaServiceClient.createSchema(
                  projectName,
                  [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).newBuilder()
                      .setName(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)())
                      .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setType_com_google_pubsub_v1_Schema_Type_)([Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).Type.PROTOCOL_BUFFER)
                      .[setDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setDefinition_java_lang_String_)(protoSource)
                      .build(),
                  schemaId);
    
          System.out.println("Created a schema using a protobuf schema:\n" + schema);
          return schema;
        } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) e) {
          System.out.println(schemaName + "already exists.");
          return null;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

### Avro
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    // const avscFile = 'path/to/an/avro/schema/file/(.avsc)/formatted/in/json';
    
    // Imports the Google Cloud client library
    const {PubSub, SchemaTypes} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    const fs = require('fs');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function createAvroSchema(schemaNameOrId, avscFile) {
      const definition = fs.readFileSync(avscFile).toString();
      const schema = await pubSubClient.createSchema(
        schemaNameOrId,
        [SchemaTypes](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Avro,
        definition,
      );
    
      const name = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
      console.log(`Schema ${name} created.`);
    }

### Proto
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    // const protoFile = 'path/to/a/proto/schema/file/(.proto)/formatted/in/protcol/buffers';
    
    // Imports the Google Cloud client library
    const {PubSub, SchemaTypes} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    const fs = require('fs');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function createProtoSchema(schemaNameOrId, protoFile) {
      const definition = fs.readFileSync(protoFile).toString();
      const schema = await pubSubClient.createSchema(
        schemaNameOrId,
        [SchemaTypes](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).ProtocolBuffer,
        definition,
      );
    
      const fullName = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
      console.log(`Schema ${fullName} created.`);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

### Avro
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    // const avscFile = 'path/to/an/avro/schema/file/(.avsc)/formatted/in/json';
    
    // Imports the Google Cloud client library
    import {PubSub, SchemaTypes} from '@google-cloud/pubsub';
    
    import * as fs from 'fs';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createAvroSchema(schemaNameOrId: string, avscFile: string) {
      const definition: string = fs.readFileSync(avscFile).toString();
      const schema = await pubSubClient.createSchema(
        schemaNameOrId,
        SchemaTypes.Avro,
        definition,
      );
    
      const name = await schema.getName();
      console.log(`Schema ${name} created.`);
    }

### Proto
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    // const protoFile = 'path/to/a/proto/schema/file/(.proto)/formatted/in/protcol/buffers';
    
    // Imports the Google Cloud client library
    import {PubSub, SchemaTypes} from '@google-cloud/pubsub';
    
    import * as fs from 'fs';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createProtoSchema(schemaNameOrId: string, protoFile: string) {
      const definition: string = fs.readFileSync(protoFile).toString();
      const schema = await pubSubClient.createSchema(
        schemaNameOrId,
        SchemaTypes.ProtocolBuffer,
        definition,
      );
    
      const fullName: string = await schema.getName();
      console.log(`Schema ${fullName} created.`);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 

### Avro
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Create a Schema with an AVRO definition.
     *
     * @param string $projectId
     * @param string $schemaId
     * @param string $avscFile
     */
    function create_avro_schema(string $projectId, string $schemaId, string $avscFile): void
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $definition = (string) file_get_contents($avscFile);
        $schema = $pubsub->createSchema($schemaId, 'AVRO', $definition);
    
        printf('Schema %s created.', $schema->name());
    }

### Proto
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Create a Schema with an Protocol Buffer definition.
     *
     * @param string $projectId
     * @param string $schemaId
     * @param string $protoFile
     */
    function create_proto_schema($projectId, $schemaId, $protoFile)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $definition = (string) file_get_contents($protoFile);
        $schema = $pubsub->createSchema($schemaId, 'PROTOCOL_BUFFER', $definition);
    
        printf('Schema %s created.', $schema->name());
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

### Avro
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud.pubsub import SchemaServiceClient
    from google.pubsub_v1.types import Schema
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    project_path = f"projects/{project_id}"
    
    # Read a JSON-formatted Avro schema file as a string.
    with open(avsc_file, "rb") as f:
        avsc_source = f.read().decode("utf-8")
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)(project_id, schema_id)
    schema = Schema(name=schema_path, type_=Schema.Type.AVRO, definition=avsc_source)
    
    try:
        result = schema_client.create_schema(
            request={"parent": project_path, "schema": schema, "schema_id": schema_id}
        )
        print(f"Created a schema using an Avro schema file:\n{result}")
        return result
    except AlreadyExists:
        print(f"{schema_id} already exists.")

### Proto
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud.pubsub import SchemaServiceClient
    from google.pubsub_v1.types import Schema
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    # proto_file = "path/to/a/proto/file/(.proto)/formatted/in/protocol/buffers"
    
    project_path = f"projects/{project_id}"
    
    # Read a protobuf schema file as a string.
    with open(proto_file, "rb") as f:
        proto_source = f.read().decode("utf-8")
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)(project_id, schema_id)
    schema = Schema(
        name=schema_path, type_=Schema.Type.PROTOCOL_BUFFER, definition=proto_source
    )
    
    try:
        result = schema_client.create_schema(
            request={"parent": project_path, "schema": schema, "schema_id": schema_id}
        )
        print(f"Created a schema using a protobuf schema file:\n{result}")
        return result
    except AlreadyExists:
        print(f"{schema_id} already exists.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

### Avro
    
    
    # schema_id = "your-schema-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    schemas = pubsub.schemas
    
    schema = schemas.create_schema parent: pubsub.project_path,
                                   schema: {
                                     name: schema_id,
                                     type: :AVRO,
                                     definition: File.read(avsc_file)
                                   },
                                   schema_id: schema_id
    
    puts "Schema #{schema.name} created."

### Proto
    
    
    # schema_id = "your-schema-id"
    # proto_file = "path/to/a/proto/file/(.proto)/formatted/in/protocol/buffers"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    schemas = pubsub.schemas
    
    schema = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1.html)::Schema.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) \
      name: schema_id,
      type: :PROTOCOL_BUFFER,
      definition: File.read(proto_file)
    
    schema = schemas.create_schema parent: pubsub.project_path,
                                   schema: schema,
                                   schema_id: schema_id
    
    puts "Schema #{schema.name} created."

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 

### Avro
    
    
    use google_cloud_pubsub::client::SchemaService;
    use google_cloud_pubsub::model::{Schema, schema::Type};
    
    pub async fn sample(client: &SchemaService, project: &str, schema_id: &str) -> anyhow::Result<()> {
        const AVRO_SCHEMA: &str =
            r#"{"type": "record", "name": "User", "fields": [{"name": "name", "type": "string"}]}"#;
        let schema = client
            .create_schema()
            .set_parent(format!("projects/{project}"))
            .set_schema_id(schema_id)
            .set_schema(
                Schema::new()
                    .set_type(Type::Avro)
                    .set_definition(AVRO_SCHEMA),
            )
            .send()
            .await?;
    
        println!("successfully created schema {schema:?}");
        Ok(())
    }

### Proto
    
    
    use google_cloud_pubsub::client::SchemaService;
    use google_cloud_pubsub::model::{Schema, schema::Type};
    
    pub async fn sample(client: &SchemaService, project: &str, schema_id: &str) -> anyhow::Result<()> {
        const PROTO_SCHEMA: &str = r#"syntax = "proto3";
    message User {
      string name = 1;
    }"#;
        let schema = client
            .create_schema()
            .set_parent(format!("projects/{project}"))
            .set_schema_id(schema_id)
            .set_schema(
                Schema::new()
                    .set_type(Type::ProtocolBuffer)
                    .set_definition(PROTO_SCHEMA),
            )
            .send()
            .await?;
    
        println!("successfully created schema {schema:?}");
        Ok(())
    }

After a schema is created, you can [see the details of the schema](https://docs.cloud.google.com/pubsub/docs/view-schema-details) in the **Schemas** page.

You can [associate the schema with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic).

## What's next

  * [View schema details](https://docs.cloud.google.com/pubsub/docs/view-schema-details)

  * [Associate a schema with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic)

  * [Commit a schema revision](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision)

  * [Validate a message for a schema](https://docs.cloud.google.com/pubsub/docs/validate-schema-message)

  * [Publish messages to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/publish-topics-schema)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
