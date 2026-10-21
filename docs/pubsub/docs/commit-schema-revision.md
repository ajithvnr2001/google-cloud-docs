---
url: https://docs.cloud.google.com/pubsub/docs/commit-schema-revision/
title: Commit a schema revision \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:57.408110+00:00
---

# Commit a schema revision  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/commit-schema-revision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Commit a schema revision Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to commit a schema revision for Pub/Sub topics.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to commit a schema revision and manage schemas, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to commit a schema revision and manage schemas. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to commit a schema revision and manage schemas:

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

## Revise a schema

You can commit a schema revision using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

The following are some guidelines to commit a schema revision:

  * You can revise a schema within specific constraints:

    * For Protocol Buffer schemas, you can add or remove optional fields. You cannot add or delete other fields. You also cannot edit any existing field.

    * For Avro schemas, refer to the [Avro documentation](https://avro.apache.org/docs/++version++/specification/#schema-resolution) for rules about schema resolution. A new revision must follow the rules as though it is both the reader schema and the writer schema.

    * A schema can have a maximum of 20 revisions at one time. If you exceed the limit, delete a schema revision before creating another.

  * Each revision has a unique revision ID associated with it. The revision ID is an auto-generated eight-character UUID.

  * When you update the revision range or the revision of a schema used for topic validation, it might take a few minutes for the changes to take effect.




### Console

To create a schema revision, follow these steps:

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

  2. Click the **Schema ID** of an existing schema.

The **Schema details** page for the schema opens.

  3. Click **Create revision**.

The **Create schema revision** page opens.

  4. Make changes as required.

For example, for the sample schema in Avro that you created in [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas), you can add an additional optional field called `Price` as follows:
         
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
              },
              {
                "name": "Price",
                "type": "double",
                "default": "0.0"
              }
            ]
          }
         

  5. Click **Validate definition** to check if the schema definition is correct.

**Note:** The validation check does not check the compatibility of the new revision with the older revisions.
  6. You can also validate the messages for the schema.

     1. Click **Test message** to test a sample message.

     2. In the **Test message** window, select a type of **Message encoding**.

     3. In the **Message body** , enter a test message.

For example, here's a sample message for the test schema. In this example, select the **Message encoding** as `JSON`.
            
            {"ProductName":"GreenOnions", "SKU":34543, "Price":12, "InStock":true}
            

     4. Click **Test**.

  7. Click **Commit** to save the schema.




### gcloud
    
    
    gcloud pubsub schemas commit SCHEMA_ID \
            --type=SCHEMA_TYPE \
            --definition=SCHEMA_DEFINITION

Where:

  * SCHEMA_TYPE is either `avro` or `protocol-buffer`.
  * SCHEMA_DEFINITION is a `string` containing the definition of the schema, formatted according to the chosen [schema type](https://docs.cloud.google.com/pubsub/docs/schemas).



You can also specify the schema definition in a file:
    
    
    gcloud pubsub schemas commit SCHEMA_ID \
            --type=SCHEMA_TYPE \
            --definition-file=SCHEMA_DEFINITION_FILE

Where:

  * SCHEMA_TYPE is either `avro` or `protocol-buffer`.
  * SCHEMA_DEFINITION_FILE is a `string` containing the path to the file with the definition of the schema, formatted according to the chosen [schema type](https://docs.cloud.google.com/pubsub/docs/schemas).



### REST

To commit a schema revision, send a POST request like the following:
    
    
    POST https://pubsub.googleapis.com/v1/projects/PROJECT_ID/schemas/SCHEMA_ID:commit
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json --data @response-body.json
    

Specify the following fields in the request body:
    
    
    {
      "definition": SCHEMA_DEFINITION
      "type": SCHEMA_TYPE
      "name": SCHEMA_NAME
    }

Where:

  * SCHEMA_TYPE is either `AVRO` or `PROTOCOL_BUFFER`.
  * SCHEMA_DEFINITION is a string containing the definition of the schema, formatted according to the chosen [schema type](https://docs.cloud.google.com/pubsub/docs/schemas).
  * SCHEMA_NAME is the name of an existing schema.



The response body should contain a JSON representation of a [schema resource](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema). For example:
    
    
    {
      "name": SCHEMA_NAME,
      "type": SCHEMA_TYPE,
      "definition": SCHEMA_DEFINITION
      "revisionId": REVISION_ID
      "revisionCreateTime": REVISION_CREATE_TIME
    }
    

Where:

  * REVISION_ID is the server-generated ID for the revision.
  * REVISION_CREATE_TIME is the ISO 8601 timestamp at which the revision was created.



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
    

### Proto
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	pubsub "cloud.google.com/go/pubsub/v2/apiv1"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    // commitProtoSchema commits a new proto schema revision to an existing schema.
    func commitProtoSchema(w io.Writer, projectID, schemaID, protoFile string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	// protoFile = "path/to/a/proto/schema/file(.proto)/formatted/in/protocol/buffers"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	// Read a proto file as a byte slice.
    	protoSource, err := os.ReadFile(protoFile)
    	if err != nil {
    		return fmt.Errorf("error reading from file: %s", protoFile)
    	}
    
    	schema := &pubsubpb.Schema{
    		// TODO(hongalex): check if name is necessary here
    		Name:       fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		Type:       pubsubpb.Schema_PROTOCOL_BUFFER,
    		Definition: string(protoSource),
    	}
    	req := &pubsubpb.CommitSchemaRequest{
    		Name:   fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		Schema: schema,
    	}
    	s, err := client.CommitSchema(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CommitSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Committed a schema using a protobuf schema: %#v\n", s)
    	return nil
    }
    

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

### Avro
    
    
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

### Proto
    
    
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub::SchemaServiceClient client, std::string const& project_id,
       std::string const& schema_id, std::string const& schema_definition_file) {
      std::string const definition = ReadFile(schema_definition_file);
    
      google::pubsub::v1::CommitSchemaRequest request;
      std::string const name =
          google::cloud::pubsub::Schema(project_id, schema_id).FullName();
      request.set_name(name);
      request.mutable_schema()->set_name(name);
      request.mutable_schema()->set_type(
          google::pubsub::v1::Schema::PROTOCOL_BUFFER);
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

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

### Avro
    
    
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

### Proto
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.pubsub.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class CommitProtoSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String schemaId = "your-schema-id";
        String protoFile = "path/to/a/proto/file/(.proto)/formatted/in/protocol/buffers";
    
        commitProtoSchemaExample(projectId, schemaId, protoFile);
      }
    
      public static [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) commitProtoSchemaExample(String projectId, String schemaId, String protoFile)
          throws IOException {
    
        [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html).of(projectId);
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        // Read a proto file as a string.
        String protoSource = new String(Files.readAllBytes(Paths.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier.html#com_google_api_gax_rpc_InputStreamSupplier_get__)(protoFile)));
    
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema =
              schemaServiceClient.commitSchema(
                  schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)(),
                  [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).newBuilder()
                      .setName(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)())
                      .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setType_com_google_pubsub_v1_Schema_Type_)([Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).Type.PROTOCOL_BUFFER)
                      .[setDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.Builder.html#com_google_pubsub_v1_Schema_Builder_setDefinition_java_lang_String_)(protoSource)
                      .build());
    
          System.out.println("Committed a schema using a protobuf schema:\n" + schema);
          return schema;
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.out.println(schemaName + "does not exist.");
          return null;
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

### Avro
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import SchemaServiceClient
    from google.pubsub_v1.types import Schema
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    # Read a JSON-formatted Avro schema file as a string.
    with open(avsc_file, "rb") as f:
        avsc_source = f.read().decode("utf-8")
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.schema_path(project_id, schema_id)
    schema = Schema(name=schema_path, type_=Schema.Type.AVRO, definition=avsc_source)
    
    try:
        result = schema_client.commit_schema(
            request={"schema": schema, "name": schema_path}
        )
        print(f"Committed a schema revision using an Avro schema file:\n{result}")
        return result
    except NotFound:
        print(f"{schema_id} does not exist.")

### Proto
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import SchemaServiceClient
    from google.pubsub_v1.types import Schema
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # schema_id = "your-schema-id"
    # proto_file = "path/to/a/proto/file/(.proto)/formatted/in/protocol/buffers"
    
    # Read a protobuf schema file as a string.
    with open(proto_file, "rb") as f:
        proto_source = f.read().decode("utf-8")
    
    schema_client = SchemaServiceClient()
    schema_path = schema_client.schema_path(project_id, schema_id)
    schema = Schema(
        name=schema_path, type_=Schema.Type.PROTOCOL_BUFFER, definition=proto_source
    )
    
    try:
        result = schema_client.commit_schema(
            request={"schema": schema, "name": schema_path}
        )
        print(f"Committed a schema revision using a protobuf schema file:\n{result}")
        return result
    except NotFound:
        print(f"{schema_id} does not exist.")

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
    
    async function commitAvroSchema(schemaNameOrId, avscFile) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
    
      // Read the new schema definition from storage.
      const definition = fs.readFileSync(avscFile).toString();
    
      // Use the gapic client to commit the new definition.
      const schemaClient = await pubSubClient.[getSchemaClient](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
      const [result] = await schemaClient.commitSchema({
        name,
        schema: {
          name,
          type: [SchemaTypes](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Avro,
          definition,
        },
      });
    
      console.log(`Schema ${name} committed with revision ${result.revisionId}.`);
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
    
    async function commitProtoSchema(schemaNameOrId, protoFile) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.[getName](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)();
    
      // Read the new schema definition from storage.
      const definition = fs.readFileSync(protoFile).toString();
    
      // Use the gapic client to commit the new definition.
      const schemaClient = await pubSubClient.[getSchemaClient](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
      const [result] = await schemaClient.commitSchema({
        name,
        schema: {
          name,
          type: [SchemaTypes](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).ProtocolBuffer,
          definition,
        },
      });
    
      console.log(`Schema ${name} committed with revision ${result.revisionId}.`);
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
    
    async function commitAvroSchema(schemaNameOrId: string, avscFile: string) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.getName();
    
      // Read the new schema definition from storage.
      const definition: string = fs.readFileSync(avscFile).toString();
    
      // Use the gapic client to commit the new definition.
      const schemaClient = await pubSubClient.getSchemaClient();
      const [result] = await schemaClient.commitSchema({
        name,
        schema: {
          name,
          type: SchemaTypes.Avro,
          definition,
        },
      });
    
      console.log(`Schema ${name} committed with revision ${result.revisionId}.`);
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
    
    async function commitProtoSchema(schemaNameOrId: string, protoFile: string) {
      // Get the fully qualified schema name.
      const schema = pubSubClient.schema(schemaNameOrId);
      const name = await schema.getName();
    
      // Read the new schema definition from storage.
      const definition: string = fs.readFileSync(protoFile).toString();
    
      // Use the gapic client to commit the new definition.
      const schemaClient = await pubSubClient.getSchemaClient();
      const [result] = await schemaClient.commitSchema({
        name,
        schema: {
          name,
          type: SchemaTypes.ProtocolBuffer,
          definition,
        },
      });
    
      console.log(`Schema ${name} committed with revision ${result.revisionId}.`);
    }

After you commit a schema revision, you can [see the details of the new revision](https://docs.cloud.google.com/pubsub/docs/view-schema-details) in the **Schemas** page.

## What's next

  * [Delete a schema revision](https://docs.cloud.google.com/pubsub/docs/delete-schema-revision)
  * [List revisions of a schema](https://docs.cloud.google.com/pubsub/docs/list-schema-revisions)
  * [Roll back a schema revision](https://docs.cloud.google.com/pubsub/docs/roll-back-schemas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
