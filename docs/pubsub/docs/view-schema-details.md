---
url: https://docs.cloud.google.com/pubsub/docs/view-schema-details/
title: View the details of a schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:02.925217+00:00
---

# View the details of a schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/view-schema-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  View the details of a schema Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to view schema details for Pub/Sub topics.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to view schema details and manage them, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view schema details and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view schema details and manage them:

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

## View schema details

You can get the details of a schema using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries. The results return the details for the latest revision ID.

### Console

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

  2. Click the name of the schema that you want to view.

The **Schema details** page for the schema opens.




### gcloud

To view the latest revision for a schema:
    
    
    gcloud pubsub schemas describe SCHEMA_NAME
    

To view a specific revision for a schema:
    
    
    gcloud pubsub schemas describe SCHEMA_ID@REVISION_ID
    

Where:

  * REVISION_ID is the revision to which you want to view.



### REST

To get the details of the latest revision of a schema, send a GET request like the following:
    
    
    GET https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/SCHEMA_ID
    

For example, for a schema with schema ID `schema-inventory`, send the following request: `https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/schema-inventory`

To get the details of a specific revision of a schema, send a GET request like the following:
    
    
    GET https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/SCHEMA_ID@REVISION_ID
    

For example, for a schema with schema ID `schema-inventory` and revision ID `fa567a3e`, send the following request: `https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/schema-inventory@fa567a3e`

Where:

  * PROJECT_ID is your project ID.
  * SCHEMA_ID is your schema ID.
  * REVISION_ID is the ID of the revision of the specific schema.



If successful, the response body contains an instance of the [Schema class](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema).

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& revision_id) {
      std::string const schema_id_with_revision = schema_id + "@" + revision_id;
    
      google::pubsub::v1::GetSchemaRequest request;
      request.set_name(
          pubsub::Schema(project_id, schema_id_with_revision).FullName());
      request.set_view(google::pubsub::v1::FULL);
      auto schema = client.GetSchema(request);
      if (!schema) throw std::move(schema).status();
    
      std::cout << "The schema revision exists and its metadata is:" << "\n"
                << schema->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
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

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	pubsub "cloud.google.com/go/pubsub/v2/apiv1"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    func getSchemaRevision(w io.Writer, projectID, schemaID string) error {
    	// projectID := "my-project-id"
    	// schemaID := my-schema@c7cfa2a8 // with revision
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.GetSchemaRequest{
    		Name: fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		View: pubsubpb.SchemaView_FULL,
    	}
    	s, err := client.GetSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetSchema revision: %w", err)
    	}
    	fmt.Fprintf(w, "Got schema revision: %#v\n", s)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    
    public class GetSchemaRevisionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id[@your-schema-revision]";
        getSchemaRevisionExample(projectId, schemaId);
      }
    
      public static void getSchemaRevisionExample(String projectId, String schemaId)
          throws IOException {
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

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function getSchema(schemaNameOrId) {
      const schema = pubSubClient.schema(schemaNameOrId);
      const info = await schema.get();
      const fullName = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
      console.log(`Schema ${fullName} info: ${JSON.stringify(info, null, 4)}.`);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
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

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import SchemaServiceClient
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    # schema_revision_id = "your-schema-revision-id"
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)(
        project_id, schema_id + "@" + schema_revision_id
    )
    
    try:
        result = schema_client.get_schema(request={"name": schema_path})
        print(f"Got a schema revision:\n{result}")
    except NotFound:
        print(f"{schema_id} not found.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # schema_id = "your-schema-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    schemas = pubsub.schemas
    
    schema = schemas.get_schema name: pubsub.schema_path(schema_id)
    
    puts "Schema #{schema.name} retrieved."

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
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

  * [Delete a schema revision](https://docs.cloud.google.com/pubsub/docs/delete-schema-revision)
  * [Delete a schema](https://docs.cloud.google.com/pubsub/docs/delete-schema)
  * [List schemas](https://docs.cloud.google.com/pubsub/docs/list-schemas)
  * [List revisions of a schema](https://docs.cloud.google.com/pubsub/docs/list-schema-revisions)
  * [Subscribe to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/schemas-valid)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
