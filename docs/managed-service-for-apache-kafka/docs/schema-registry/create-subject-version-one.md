---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one/
title: Create a subject \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:17.844531+00:00
---

# Create a subject  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a subject Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create a subject in a schema registry. A _subject_ is a logical container for different versions of a schema. When you create a subject for the first time, you also create the first version of the schema for that subject.

You can create a subject in one of the following ways:

  * **Implicit (default):** the default behavior for many producer and consumer clients is to automatically create a schema that does not exist when the client connects. The subject and version referencing the schema are also automatically created. This is convenient, but can lead to potential inconsistencies in the data if multiple clients create versions concurrently.

  * **Explicit (recommended):** in this method, each schema must be created in the registry before a producer or consumer client can use it. You can use Google Cloud console or the Managed Kafka API to do this.




This behavior must be configured in your client settings. Consult your serializer or deserializer client library documentation for the details.

## Before you begin

  * Learn about [schema overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview).

  * [Create a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-schema-registry) if you don't have one already.

  * Understand [schema references](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#schema-references).




### Required roles and permissions

To get the permissions that you need to create a subject, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on your project or schema registry. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a subject. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a subject:

  * Grant this permission on the parent context or the default context: `managedkafka.versions.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a subject or first version of a schema

When you create a subject, you also create its first version. This first version creates a new schema or is a reference to an existing schema.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry where you want to create a subject.

  3. Click add_box **Create subject**.

  4. For **Subject name** , enter a unique name for your subject.

The name must start with a letter and contain only letters, numbers, and the following special characters: dash (`-`), period (`.`), underscore (`_`), tilde (`~`), percent (`%`), or plus sign (`+`). The name of a subject is immutable.

For more information about choosing a subject name, see [Subject naming strategies](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource#subject-naming-strategies).

  5. For **Context** , choose a context or create a new context. Contexts act like namespaces to organize your subjects and schemas, providing isolation between different groups.

     * To use an existing context, select the context from the **Context** list. The default context is displayed as `(default context)`.

     * To create a new context, perform the following steps:

       1. Select **Create context** from the **Context** list.

       2. In the **Context name** field, enter a name for the context.

The name must start with a letter and contain only letters, numbers, and the following special characters: dash (`-`), period (`.`), underscore (`_`), tilde (`~`), percent (`%`), or plus sign (`+`). The name of a context is immutable.

       3. Click **Save**.

  6. For **Schema type** , select **Avro** or **Protocol Buffer**.

  7. In the **Schema definition** field, enter the schema definition. The format of the schema must match the schema type. Don't include sensitive information such as personally identifiable information (PII) or security data in your schema field names.

  8. If your schema uses or depends on data structures defined in _other_ schemas in the schema registry, perform the following steps:

     1. Click **Add Schema reference**.
     2. In the **Reference name** field, enter the reference name of the referenced schema. 
     3. In the **Subject** list, select the subject that contains the referenced schema.
     4. In the **Version** list, select the version number of the referenced schema.
     5. Click **OK**.

Repeat these steps for each referenced schema.

  9. Click **Create**.




### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

The following REST API samples create the first version of a subject.

To create a subject within the default context, make a `POST` request to the specified URI using the [`projects.locations.schemaRegistries.subjects.versions.create`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/create) method:
    
    
    POST https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json
    

Alternatively, if using a specific context, include the context in the subject collection URI using the [`projects.locations.schemaRegistries.contexts.subjects.versions.create`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.subjects.versions/create) method:
    
    
    POST https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects/SUBJECT_ID/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json
    

Replace the following:

  * PROJECT_ID (required): your Google Cloud project ID.

  * LOCATION (required): the Google Cloud region where the schema registry exists.

  * REGISTRY_ID (required): the ID of the target schema registry.

  * CONTEXT_ID (optional): the ID of the context containing the subject. Use `.` for the default context if you wish to be explicit, otherwise omit `/contexts/CONTEXT_ID` to use the default context implicitly.

The name must start with a letter, and contain only letters, numbers, and the following special characters: dashes `-`, periods `.`, underscores `_`, tildes `~`, percents `%`, or plus signs `+`. The name of a context is immutable.

  * SUBJECT_ID (required): the ID for the new subject under which to create the first version.

The name must start with a letter, and contain only letters, numbers, and the following special characters: dashes `-`, periods `.`, underscores `_`, tildes `~`, percents `%`, or plus signs `+`. The name of a subject is immutable.




**Request Body:**

Include a JSON object in the request body specifying the schema details:
    
    
    {
      "schema": "YOUR_SCHEMA_DEFINITION_STRING",
      "schema_type": "AVRO" | "PROTOBUF", // Optional, defaults to AVRO
      "references": [ // Optional
        {
          "name": "REFERENCE_NAME",
          "subject": "REFERENCED_SUBJECT_ID",
          "version": REFERENCED_VERSION_NUMBER
        }
        // ... more references
      ]
      // "version": VERSION_NUMBER, // Optional: Usually omitted, let service assign next
      // "id": SCHEMA_ID, // Optional: Usually omitted, let service assign or reuse
    }
    

Replace the following:

  * `YOUR_SCHEMA_DEFINITION_STRING` (required): a string containing the actual schema definition payload.

Do not include sensitive information such as personally identifiable information (PII) or security data in your schema field names.

  * `schemaType` (optional): the type of the schema. Can be `AVRO` or `PROTOBUF`. Defaults to `AVRO` if omitted.

  * `references` (optional): an array of objects defining any schemas referenced by this schema.

    * `REFERENCE_NAME`: the name used to reference the other schema within this schema's definition.
    * `REFERENCED_SUBJECT_ID`: the subject ID of the schema being referenced.
    * `REFERENCED_VERSION_NUMBER`: the specific version number of the referenced subject's schema.
  * `versionId`, `schemaId`: optional fields usually handled by the service. For the first version of a subject, `versionId` will be "1".




If the request is successful and the schema is valid and passes compatibility checks if configured, the API returns a `200 OK` status code. The response body contains the schema ID used by the created version, which is different from the version ID.

For more information, see the [REST API documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest).

## What's next

  * [Learn more about schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry)
  * [List subjects](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subjects)
  * [Register a new schema version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/register-schema-version)
  * [Delete a subject](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
