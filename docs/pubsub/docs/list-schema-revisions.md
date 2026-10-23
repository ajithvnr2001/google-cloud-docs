---
url: https://docs.cloud.google.com/pubsub/docs/list-schema-revisions/
title: List schema revisions for a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:52.902553+00:00
---

# List schema revisions for a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/list-schema-revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  List schema revisions for a topic Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to list the revisions of a schema for Pub/Sub topics.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to list schema revisions and manage them, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list schema revisions and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list schema revisions and manage them:

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

## List the revisions of a schema

You can list the revisions of a schema in a Google Cloud project using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

### Console

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

The list of schemas is displayed.

  2. Click the name of the schema that you want to view.

The **Schema details** page for the schema opens.

In the **Revisions** section, you can see the list of available revisions for the schema.




### gcloud

To view the latest revision for a schema:
    
    
    gcloud pubsub schemas list-revisions SCHEMA_ID
    

Use the `gcloud pubsub schemas list-revisions <var>SCHEMA_ID</var> --view=FULL` command to see the definitions for the schema revisions.

### REST

To list the schema revisions for a schema, send a GET request like the following:
    
    
    GET https://pubsub.googleapis.com/v1/projects/SCHEMA_NAME:listRevisions
    

If successful, the response body contains a [JSON object containing all schema revisions for the schema](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas/list#response-body).

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id) {
      auto const parent = pubsub::Schema(project_id, schema_id).FullName();
      for (auto& s : client.ListSchemaRevisions(parent)) {
        if (!s) throw std::move(s).status();
        std::cout << "Schema revision: " << s->DebugString() << "\n";
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
    	"google.golang.org/api/iterator"
    )
    
    func listSchemaRevisions(w io.Writer, projectID, schemaID string) ([]*pubsubpb.Schema, error) {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema-id"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	var schemas []*pubsubpb.Schema
    
    	req := &pubsubpb.ListSchemaRevisionsRequest{
    		Name: fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		View: pubsubpb.SchemaView_FULL,
    	}
    	schemaIter := client.ListSchemaRevisions(ctx, req)
    	for {
    		sc, err := schemaIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return nil, fmt.Errorf("schemaIter.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Got schema revision: %#v\n", sc)
    		schemas = append(schemas, sc)
    	}
    
    	fmt.Fprintf(w, "Got %d schema revisions", len(schemas))
    	return schemas, nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    
    public class ListSchemaRevisionsExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id";
    
        listSchemaRevisionsExample(projectId, schemaId);
      }
    
      public static void listSchemaRevisionsExample(String projectId, String schemaId)
          throws IOException {
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
          for ([Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema : schemaServiceClient.listSchemaRevisions(schemaName).iterateAll()) {
            System.out.println(schema);
          }
          System.out.println("Listed schema revisions.");
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud.pubsub import SchemaServiceClient
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)(project_id, schema_id)
    
    for schema in schema_client.list_schema_revisions(request={"name": schema_path}):
        print(schema)
    
    print("Listed schema revisions.")

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listSchemaRevisions(schemaNameOrId) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.getName();
    
      // Use the gapic client to list the schema revisions.
      const schemaClient = await pubSubClient.getSchemaClient();
      const [results] = await schemaClient.listSchemaRevisions({
        name,
      });
      for (const rev of results) {
        console.log(rev.revisionId, rev.revisionCreateTime);
      }
      console.log(`Listed revisions of schema ${name}.`);
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
    
    async function listSchemaRevisions(schemaNameOrId: string) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.getName();
    
      // Use the gapic client to list the schema revisions.
      const schemaClient = await pubSubClient.getSchemaClient();
      const [results] = await schemaClient.listSchemaRevisions({
        name,
      });
      for (const rev of results) {
        console.log(rev.revisionId, rev.revisionCreateTime);
      }
      console.log(`Listed revisions of schema ${name}.`);
    }

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_pubsub::client::SchemaService;
    use google_cloud_pubsub::model::SchemaView;
    
    pub async fn sample(client: &SchemaService, project: &str, schema_id: &str) -> anyhow::Result<()> {
        let mut subscriptions = client
            .list_schema_revisions()
            .set_name(format!("projects/{}/schemas/{}", project, schema_id))
            .set_view(SchemaView::Full)
            .by_item();
    
        println!("listing subscriptions");
        while let Some(subscription) = subscriptions.next().await.transpose()? {
            println!("{subscription:?}");
        }
        println!("DONE");
        Ok(())
    }

## What's next

  * [Choose and create a subscription](https://docs.cloud.google.com/pubsub/docs/subscription-overview#push_pull).

  * Process messages when subscribing to [topics configured with a schema](https://docs.cloud.google.com/pubsub/docs/schemas-valid).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
