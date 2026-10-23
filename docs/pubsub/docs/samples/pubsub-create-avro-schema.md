---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-avro-schema/
title: Create Avro-typed schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:50.736543+00:00
---

# Create Avro-typed schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-avro-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create Avro-typed schema Stay organized with collections  Save and categorize content based on your preferences. 

Create a schema resource using an Avro schema file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a schema for a topic](https://docs.cloud.google.com/pubsub/docs/create-schemas)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Rust
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
