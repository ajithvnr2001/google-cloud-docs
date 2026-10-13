---
url: https://docs.cloud.google.com/pubsub/docs/roll-back-schemas/
title: Roll back a schema revision \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:01.428521+00:00
---

# Roll back a schema revision  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/roll-back-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Roll back a schema revision Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to roll back a schema for a Pub/Sub topic.

The rollback operation lets you create another schema revision with the exact schema definition as the specified previous revision.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to roll back schemas and manage them, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to roll back schemas and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to roll back schemas and manage them:

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

## Roll back a schema revision

You can roll back a schema using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries. Follow these steps:

### Console

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

  2. Click the name of an existing schema.

The **Schema details** page for the schema opens.

  3. Click **Roll back**.

The **Roll back schema** dialog opens.

  4. Select the revision to which you want to roll back your schema.

  5. Click **Confirm** to save the rollback operation.

A new revision is created with the schema specified in the rollback operation.

  6. In the **Schema details** page, select the latest version of the schema and the version you selected as source for the rollback operation.

  7. Click **View diff**.

You can verify that the two schemas are identical.

You can use the schema revision that you just created as the last revision for validating a topic by updating the **Last revision allowed** field.




### gcloud
    
    
    gcloud pubsub schemas rollback SCHEMA_ID \
            --revision-id=REVISION_ID

Where:

  * REVISION_ID is the revision to which you want to roll back.



### REST

To roll back a schema, send a POST request like the following:
    
    
    POST https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/SCHEMA_ID:rollback
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json --data @response-body.json
    

Specify the following fields in the request body:
    
    
    {
      "revisionId": REVISION_KD
    }

Where:

  * REVISION_ID is the ID of the revision to which to roll back.



The response body should contain a JSON representation of a [schema resource](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema).

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& revision_id) {
      google::pubsub::v1::RollbackSchemaRequest request;
      request.set_name(pubsub::Schema(project_id, schema_id).FullName());
      request.set_revision_id(revision_id);
      auto schema = client.RollbackSchema(request);
      if (!schema) throw std::move(schema).status();
    
      std::cout << "Rolledback schema. Created a new schema and its metadata is:"
                << "\n"
                << schema->DebugString() << "\n";
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
    
    // rollbackSchema creates a new schema revision that is a copy of the provided revisionID.
    func rollbackSchema(w io.Writer, projectID, schemaID, revisionID string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	// revisionID := "a1b2c3d4"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.RollbackSchemaRequest{
    		Name:       fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		RevisionId: revisionID,
    	}
    	s, err := client.RollbackSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("RollbackSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Rolled back schema: %#v\n", s)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    
    public class RollbackSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project";
        String schemaId = "your-schema";
        String revisionId = "your-revision";
    
        rollbackSchemaExample(projectId, schemaId, revisionId);
      }
    
      public static void rollbackSchemaExample(String projectId, String schemaId, String revisionId)
          throws IOException {
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema = schemaServiceClient.rollbackSchema(schemaName, revisionId);
    
          System.out.println("Rolled back a schema:" + schema);
    
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.out.println(schemaName + "not found.");
        }
      }
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
    schema_path = schema_client.[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)(project_id, schema_id)
    
    try:
        result = schema_client.rollback_schema(
            request={"name": schema_path, "revision_id": schema_revision_id}
        )
        print(f"Rolled back a schema revision:\n{result}")
    except NotFound:
        print(f"{schema_id} not found.")

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    // const revisionId = 'YOUR_REVISION_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function rollbackSchema(schemaNameOrId, revisionId) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
    
      // Use the gapic client to roll back the schema revision.
      const schemaClient = await pubSubClient.[getSchemaClient](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
      await schemaClient.rollbackSchema({
        name,
        revisionId,
      });
    
      console.log(`Schema ${name} revision ${revisionId} rolled back.`);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const schemaNameOrId = 'YOUR_SCHEMA_NAME_OR_ID';
    // const revisionId = 'YOUR_REVISION_ID';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function rollbackSchema(schemaNameOrId: string, revisionId: string) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.getName();
    
      // Use the gapic client to roll back the schema revision.
      const schemaClient = await pubSubClient.getSchemaClient();
      await schemaClient.rollbackSchema({
        name,
        revisionId,
      });
    
      console.log(`Schema ${name} revision ${revisionId} rolled back.`);
    }

## What's next

  * [Delete a schema revision](https://docs.cloud.google.com/pubsub/docs/delete-schema-revision)
  * [Delete a schema](https://docs.cloud.google.com/pubsub/docs/delete-schema)
  * [List schemas](https://docs.cloud.google.com/pubsub/docs/list-schemas)
  * [List revisions of a schema](https://docs.cloud.google.com/pubsub/docs/list-schema-revisions)
  * [Subscribe to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/schemas-valid)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
