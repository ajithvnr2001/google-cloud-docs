---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-delete-schema-revision/
title: Delete a revision from a schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:54.403749+00:00
---

# Delete a revision from a schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-delete-schema-revision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Delete a revision from a schema Stay organized with collections  Save and categorize content based on your preferences. 

Delete a revision from a schema

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Delete a schema revision for a topic](https://docs.cloud.google.com/pubsub/docs/delete-schema-revision)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& revision_id) {
      std::string const schema_id_with_revision = schema_id + "@" + revision_id;
    
      google::pubsub::v1::DeleteSchemaRevisionRequest request;
      request.set_name(
          pubsub::Schema(project_id, schema_id_with_revision).FullName());
      auto schema = client.DeleteSchemaRevision(request);
      if (!schema) throw std::move(schema).status();
    
      std::cout << "Deleted schema. Its metadata is:" << "\n"
                << schema->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class DeleteSchemaRevisionSample
    {
        public void DeleteSchemaRevision(string projectId, string schemaId, string revisionId)
        {
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html) schemaService = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_Create)();
            [DeleteSchemaRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.DeleteSchemaRevisionRequest.html) request = new [DeleteSchemaRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.DeleteSchemaRevisionRequest.html)
            {
                SchemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId + "@" + revisionId)
            };
            schemaService.[DeleteSchemaRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaServiceClient.html#Google_Cloud_PubSub_V1_SchemaServiceClient_DeleteSchemaRevision_Google_Cloud_PubSub_V1_DeleteSchemaRevisionRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
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
    
    func deleteSchemaRevision(w io.Writer, projectID, schemaID, revisionID string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema-id"
    	// revisionID := "my-revision-id"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.DeleteSchemaRevisionRequest{
    		Name: fmt.Sprintf("projects/%s/schemas/%s@%s", projectID, schemaID, revisionID),
    	}
    	if _, err := client.DeleteSchemaRevision(ctx, req); err != nil {
    		return fmt.Errorf("client.DeleteSchemaRevision: %w", err)
    	}
    	fmt.Fprintf(w, "Deleted a schema revision: %s@%s", schemaID, revisionID)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[DeleteSchemaRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeleteSchemaRevisionRequest.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    
    public class DeleteSchemaRevisionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id@your-revision-id";
    
        deleteSchemaRevisionExample(projectId, schemaId);
      }
    
      public static void deleteSchemaRevisionExample(String projectId, String schemaId)
          throws IOException {
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [DeleteSchemaRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeleteSchemaRevisionRequest.html) request =
              [DeleteSchemaRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeleteSchemaRevisionRequest.html).newBuilder().setName(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)()).build();
    
          schemaServiceClient.deleteSchemaRevision(request);
    
          System.out.println("Deleted a schema revision:" + schemaName);
    
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.out.println(schemaName + "not found.");
        }
      }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # schema_id = "your-schema-id"
    # revision_id = "your-revision-id"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    schemas = pubsub.schemas
    
    result = schemas.delete_schema_revision \
      name: pubsub.schema_path("#{schema_id}@#{revision_id}")
    
    puts "Schema #{schema_id}@#{revision_id} deleted."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
