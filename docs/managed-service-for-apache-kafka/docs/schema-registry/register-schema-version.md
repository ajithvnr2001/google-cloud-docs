---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/register-schema-version/
title: Register a new schema version \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:14.741473+00:00
---

# Register a new schema version  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/register-schema-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Register a new schema version Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you create a subject, you can add new versions to it. This process is known as registering a new schema version. Each new version represents an evolution of the schema associated with that subject.

A subject can have multiple versions. Versions within a subject follow configurable compatibility rules to ensure safe schema evolution. For example, a subject can require that all changes be backwards-compatible. An example of a backwards-compatible change is adding an optional field. Adding a required field would be considered a backwards-incompatible change; if your subject is configured for backwards compatibility, this change is not allowed. However, if your subject is configured for forwards-compatibility, adding a required field would be acceptable.

Compatibility checks are not retroactive. If compatibility rules are changed for a subject or schema registry, versions already existing within the subject are not re-validated against the new rules. For more information about compatibility, see [About compatibility type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#compatibility-type).

## Required roles and permissions

To get the permissions that you need to register a schema version for a subject, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on your project or the specific schema registry and subject. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to register a schema version for a subject. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to register a schema version for a subject:

  * Grant this permission on the parent context or the default context: `managedkafka.versions.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Register a new schema version

To register a new schema version, perform the following steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry where you want to register a new schema version.

  3. Under **Subjects in this schema registry** , click the name of the subject.

  4. In the **Subject details** page, click add_box **Create version**.

  5. The **Schema definition** field shows the definition of the latest version. Update the definition in this field for the new version. Don't include sensitive information such as personally identifiable information (PII) or security data in your schema field names.

  6. If your schema uses or depends on data structures defined in _other_ schemas in the schema registry, perform the following steps:

     1. Click **Add Schema reference**.
     2. In the **Reference name** field, enter the reference name of the referenced schema. 
     3. In the **Subject** list, select the subject that contains the referenced schema.
     4. In the **Version** list, select the version number of the referenced schema.
     5. Click **OK**.

Repeat these steps for each referenced schema.

  7. Optional: To check whether the new schema is compatible with the previous version, click **Check compatibility**.

If the schema is compatible, a check_circle check mark is shown. Otherwise, an error message appears. In that case, fix the error and click **Check compatibility** again.

The compatibility check that is performed depends on the subject's [compatibility type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#compatibility-type).

  8. Click **Create**. If the schema definition is valid and passes the subject's compatibility checks, the new version appears under **All versions**.




### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To register a new schema version for a subject within the default context, make a `POST` request to the specific URI using the [`projects.locations.schemaRegistries.subjects.versions.create`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/create) method:
    
    
    POST https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json
    

Alternatively, if using a specific context, include the context in the versions collection URI and use the [`projects.locations.schemaRegistries.contexts.subjects.versions.create`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.subjects.versions/create) method.
    
    
    POST https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects/SUBJECT_ID/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json
    

Replace the following:

  * PROJECT_ID (required): your Google Cloud project ID.
  * LOCATION (required): the Google Cloud region where the schema registry exists.
  * REGISTRY_ID (required): the ID of the target schema registry.
  * CONTEXT_ID (optional): the ID of the context containing the subject. Use `.` (a single period) for the default context if you wish to be explicit, otherwise omit `/contexts/CONTEXT_ID` to use the default context implicitly.
  * SUBJECT_ID (required): the ID of the subject under which to create the new version.



**Request Body:**

Include a JSON object in the request body specifying the schema details:
    
    
    {
      "schema": "YOUR_SCHEMA_DEFINITION_STRING",
      "schema_type": "AVRO" | "PROTOBUF" | "JSON", // Optional, defaults to AVRO
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

  * `schemaType` (optional, within `schema` object): the type of the schema. Can be `AVRO` or `PROTOBUF`. Defaults to `AVRO` if omitted.

  * `references` (optional, within `schema` object): an array of objects defining any schemas referenced by this schema.

    * `REFERENCE_NAME`: the name used to reference the other schema within this schema's definition.

    * `REFERENCED_SUBJECT_ID`: the fully qualified subject name of the schema being referenced. Example: `projects/test-project/locations/us-central1/schemaRegistries/test-registry/subjects/test-referenced-subject`.

    * `REFERENCED_VERSION_NUMBER`: the specific version number (integer) of the referenced subject's schema.

  * `versionId`, `schemaId`: optional fields usually handled by the service. When registering the schema version, the service assigns the next available version number.




If the request is successful, the API returns a `200 OK` status code and a response body containing the schema ID.

For more information, see the [REST API documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest).

## What's next

  * [Learn more about schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry)
  * [List subject versions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subject-versions)
  * [Delete a schema subject version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject-version)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
