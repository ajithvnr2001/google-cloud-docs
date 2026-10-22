---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-commit-avro-schema/
title: Commit a revision for an Avro schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:00.870011+00:00
---

# Commit a revision for an Avro schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-commit-avro-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Commit a revision for an Avro schema Stay organized with collections  Save and categorize content based on your preferences. 

Commit a revision for an Avro schema

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Commit a schema revision](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& schema_definition_file) {
      std::string const definition = ReadFile(schema_definition_file);
    
      google::pubsub::v1::CommitSchemaRequest request;
      std::string const name =
          google::cloud::pubsub::Schema(project_id, schema_id).FullName();
      request.set_name(name);
      request.mutable_schema()->set_name(name);
      request.mutable_schema()->set_type(google::pubsub::v1::Schema::AVRO);
      request.mutable_schema()->set_definition(definition);
      auto schema = client.CommitSchema(request);
      if (schema.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The schema revision already exists\n";
        return;
      }
      if (!schema) throw std::move(schema).status();
    
      std::cout << "Schema revision successfully committed: "
                << schema->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.IO;
    
    public class CommitAvroSchemaSample
    {
        public Schema CommitAvroSchema(string projectId, string schemaId, string pathToNewDefinition)
        {
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html) schemaService = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_Create)();
            var schemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId);
            string schemaDefinition = File.ReadAllText(pathToNewDefinition);
            [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html) schema = new [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html)
            {
                SchemaName = schemaName,
                Type = [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html).[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html)s.[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html).[Avro](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.Types.Type.html#Google_Cloud_PubSub_V1_Schema_Types_Type_Avro),
                Definition = schemaDefinition
            };
    
            schema = schemaService.[CommitSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_CommitSchema_Google_Cloud_PubSub_V1_CommitSchemaRequest_Google_Api_Gax_Grpc_CallSettings_)(schemaName, schema);
            Console.WriteLine($"Schema {schema.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Schema.html#Google_Cloud_PubSub_V1_Schema_Name)} committed.");
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
    
    // commitAvroSchema commits a new Avro schema revision to an existing schema.
    func commitAvroSchema(w io.Writer, projectID, schemaID, avscFile string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema-id"
    	// avscFile = "path/to/an/avro/schema/file(.avsc)/formatted/in/json"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	// Read an Avro schema file formatted in JSON as a byte slice.
    	avscSource, err := os.ReadFile(avscFile)
    	if err != nil {
    		return fmt.Errorf("error reading from file: %s", avscFile)
    	}
    
    	schema := &pubsubpb.Schema{
    		Name:       fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		Type:       pubsubpb.Schema_AVRO,
    		Definition: string(avscSource),
    	}
    	req := &pubsubpb.CommitSchemaRequest{
    		Name:   fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		Schema: schema,
    	}
    	s, err := client.CommitSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("error calling CommitSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Committed a schema using an Avro schema: %#v\n", s)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class CommitAvroSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id";
        String avscFile = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json";
    
        commitAvroSchemaExample(projectId, schemaId, avscFile);
      }
    
      public static [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) commitAvroSchemaExample(String projectId, String schemaId, String avscFile)
          throws IOException {
    
        [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html).of(projectId);
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        // Read an Avro schema file formatted in JSON as a string.
        String avscSource = new String(Files.readAllBytes(Paths.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier.html#com_google_api_gax_rpc_InputStreamSupplier_get__)(avscFile)));
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema =
              schemaServiceClient.commitSchema(
                  schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)(),
                  [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).newBuilder()
                      .setName(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)())
                      .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setType_com_google_pubsub_v1_Schema_Type_)([Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).Type.AVRO)
                      .[setDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setDefinition_java_lang_String_)(avscSource)
                      .build());
    
          System.out.println("Committed a schema using an Avro schema:\n" + schema);
          return schema;
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.out.println(schemaName + "does not exist.");
          return null;
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Core\Exception\NotFoundException;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Commit a new AVRO schema revision to an existing schema.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $schemaId The ID of the schema to commit.
     * @param string $avscFile The path to the Avro schema file.
     */
    function commit_avro_schema(string $projectId, string $schemaId, string $avscFile): void
    {
        $client = new PubSubClient([
            'projectId' => $projectId
        ]);
    
        try {
            $schema = $client->schema($schemaId);
            $definition = file_get_contents($avscFile);
            $info = $schema->commit($definition, 'AVRO');
    
            printf("Committed a schema using an Avro schema: %s\n", $info['name']);
        } catch (NotFoundException $e) {
            printf("%s does not exist.\n", $schemaId);
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # schema_id = "your-schema-id"
    # avsc_file = "path/to/a/avsc_file.avsc"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    schemas = pubsub.schemas
    
    schema = schemas.get_schema name: pubsub.schema_path(schema_id)
    schema.definition = File.read avsc_file
    
    result = schemas.commit_schema name: schema.name,
                                   schema: schema
    
    puts "Schema committed with revision #{result.revision_id}."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
