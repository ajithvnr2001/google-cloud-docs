---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-get-schema/
title: Get schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:43.401770+00:00
---

# Get schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-get-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Get schema Stay organized with collections  Save and categorize content based on your preferences. 

Get a schema resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [View the details of a schema](https://docs.cloud.google.com/pubsub/docs/view-schema-details)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id) {
      google::pubsub::v1::GetSchemaRequest request;
      request.set_name(pubsub::Schema(project_id, schema_id).FullName());
      request.set_view(google::pubsub::v1::FULL);
      auto schema = client.GetSchema(request);
      if (!schema) throw std::move(schema).status();
    
      std::cout << "The schema exists and its metadata is:" << "\n"
                << schema->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class GetSchemaSample
    {
        public Schema GetSchema(string projectId, string schemaId)
        {
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html) schemaService = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_Create)();
            [GetSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetSchemaRequest.html) request = new [GetSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetSchemaRequest.html)
            {
                SchemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId),
                View = [SchemaView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaView.html).[Full](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaView.html#Google_Cloud_PubSub_V1_SchemaView_Full)
            };
    
            return schemaService.[GetSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_GetSchema_Google_Cloud_PubSub_V1_GetSchemaRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	pubsub "cloud.google.com/go/pubsub/v2/apiv1"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    func getSchema(w io.Writer, projectID, schemaID string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	// Retrieve the full schema view. If you don't want to retrieve the
    	// definition, pass in pubsubpb.SchemaView_BASIC which retrieves
    	// just the name and type of the schema.
    	req := &pubsubpb.GetSchemaRequest{
    		Name: fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		View: pubsubpb.SchemaView_FULL,
    	}
    	s, err := client.GetSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Got schema: %#v\n", s)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    
    public class GetSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id";
    
        getSchemaExample(projectId, schemaId);
      }
    
      public static void getSchemaExample(String projectId, String schemaId) throws IOException {
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema = schemaServiceClient.getSchema(schemaName);
    
          System.out.println("Got a schema:\n" + schema);
    
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.out.println(schemaName + "not found.");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    ]
    
    exports['command line option "outputpath" causes the output to move 1'] = [

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function getSchema(schemaNameOrId: string) {
      const schema = pubSubClient.schema(schemaNameOrId);
      const info = await schema.get();
      const fullName = await schema.getName();
      console.log(`Schema ${fullName} info: ${JSON.stringify(info, null, 4)}.`);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Get a schema.
     *
     * @param string $projectId
     * @param string $schemaId
     */
    function get_schema($projectId, $schemaId)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $schema = $pubsub->schema($schemaId);
        $schema->info();
    
        printf('Schema %s retrieved', $schema->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # schema_id = "your-schema-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    schemas = pubsub.schemas
    
    schema = schemas.get_schema name: pubsub.schema_path(schema_id)
    
    puts "Schema #{schema.name} retrieved."

### Rust
    
    
    use google_cloud_pubsub::client::SchemaService;
    
    pub async fn sample(client: &SchemaService, project: &str, schema_id: &str) -> anyhow::Result<()> {
        let schema = client
            .get_schema()
            .set_name(format!("projects/{project}/schemas/{schema_id}"))
            .send()
            .await?;
    
        println!("successfully retrieved schema {schema:?}");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
