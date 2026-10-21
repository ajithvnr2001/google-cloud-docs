---
url: https://docs.cloud.google.com/pubsub/docs/delete-schema-revision/
title: Delete a schema revision for a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:55.826684+00:00
---

# Delete a schema revision for a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/delete-schema-revision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Delete a schema revision for a topic Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to delete schema revisions for Pub/Sub topics. The delete operation for a schema also deletes all the revisions associated with the schema.

**Caution:** Deletion is permanent. You cannot restore a schema revision that is deleted. Any messages that validated against the deleted schema revision at the time of publish cannot be written to BigQuery using a [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery) with [use topic schema](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#use-topic-schema) enabled. Instead of deleting a revision, consider [rolling back a schema](https://docs.cloud.google.com/pubsub/docs/roll-back-schemas).

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to delete and manage schema revisions, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete and manage schema revisions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete and manage schema revisions:

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

## Delete a schema revision

**Important:** If all revisions within the revision range of the schema settings for a topic are deleted, all attempts to publish messages to that topic fail.

The following are some important guidelines for deleting a schema revision:

  * You can delete one or multiple schema revisions from a schema.

  * If the schema has only one revision, you cannot delete the revision. Instead, delete the schema.

  * The delete operation for a schema also deletes all the revisions associated with the schema.

  * If you delete a schema, publishing messages to topics associated with that schema fails.

  * If you delete a schema revision, and it's specified as the first revision for a topic, the next revision is used instead for validation.

If the deleted schema revision is specified as the last revision for a topic, the previous schema revision is used instead for validation.

If the deleted schema revision falls within the specified revision range for a topic for validation, the revision is skipped.




You can delete a schema revision using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

### Console

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

  2. Click the name of an existing schema.

The **Schema details** page for the schema opens.

  3. Select the revision that you want to delete. You can also select multiple revisions.

  4. Click **Delete revision**.

  5. Confirm the delete operation.




### gcloud
    
    
    gcloud pubsub schemas delete-revision SCHEMA_NAME@REVISION_ID

Where:

  * REVISION_ID is the revision to which you want to roll back.



### REST

To delete a schema revision, send a DELETE request like the following:
    
    
    POST https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/SCHEMA_ID@REVISION_ID:deleteRevision
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json --data @response-body.json
    

The response body should contain a JSON representation of the deleted [schema resource](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema).

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
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

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import SchemaServiceClient
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    # revision_id = "your-revision-id"
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.schema_path(project_id, schema_id + "@" + revision_id)
    
    try:
        schema_client.delete_schema_revision(request={"name": schema_path})
        print(f"Deleted a schema revision:\n{schema_path}")
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
    
    async function deleteSchemaRevision(schemaNameOrId, revisionId) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
    
      // Use the gapic client to delete the schema revision.
      const schemaClient = await pubSubClient.[getSchemaClient](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
      await schemaClient.deleteSchemaRevision({
        name: `${name}@${revisionId}`,
      });
    
      console.log(`Schema ${name} revision ${revisionId} deleted.`);
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
    
    async function deleteSchemaRevision(
      schemaNameOrId: string,
      revisionId: string,
    ) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.getName();
    
      // Use the gapic client to delete the schema revision.
      const schemaClient = await pubSubClient.getSchemaClient();
      await schemaClient.deleteSchemaRevision({
        name: `${name}@${revisionId}`,
      });
    
      console.log(`Schema ${name} revision ${revisionId} deleted.`);
    }

## What's next

  * [Delete a schema](https://docs.cloud.google.com/pubsub/docs/delete-schema)
  * [List schemas](https://docs.cloud.google.com/pubsub/docs/list-schemas)
  * [List revisions of a schema](https://docs.cloud.google.com/pubsub/docs/list-schema-revisions)
  * [Subscribe to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/schemas-valid)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
