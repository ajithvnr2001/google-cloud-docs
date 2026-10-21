---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject/
title: Delete a subject \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:14.837037+00:00
---

# Delete a subject  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Delete a subject Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to delete a subject from a schema registry. There are two ways to delete a subject:

  * **Soft-delete**. Marks the subject as deleted, but its information is retained and can be recovered. All versions for the subject are also soft-deleted.

  * **Hard-delete**. Permanently removes the subject and its associated data.




You can also delete a specific schema version from a subject. For more information, see [Delete a schema subject version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject-version).

## Required roles and permissions

To get the permissions that you need to delete a subject, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on your subject. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete a subject. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete a subject:

  * Grant the following permission on the subject to be deleted: `managedkafka.subjects.delete`
  * If deleting in the console, grant the following permission to view the subject: `managedkafka.subjects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Soft-delete a subject

Make sure the following conditions are met:

  * The subject that you are going to delete is not referenced by other schemas. A request for deletion fails if any version in the subject is referenced by other schemas.

  * The schema registry to which the subject belongs or the subject itself must not be in the `Read-only` mode.




To soft-delete a subject, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry that contains the subject to delete.

  3. Under **Subjects in this schema registry** , click the name of the subject.

  4. In the **Subject details** page, click delete **Delete**.

  5. Select **Soft Delete**.

  6. In the **Delete schema subject** dialog, type `delete` into the field.

  7. Click **Delete**. This action soft-deletes the subject before permanently deleting it.




### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To soft-delete a subject using the REST API, make a `DELETE` request to the appropriate URI using the [`projects.locations.schemaRegistries.contexts.subjects.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.subjects/delete) method.
    
    
    DELETE https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

To soft-delete a subject under a specific context by using the REST API, make a `DELETE` request to the appropriate URI using the [`projects.locations.schemaRegistries.contexts.subjects.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.subjects/delete) method.
    
    
    DELETE https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects/SUBJECT_ID
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Replace the following:

  * PROJECT_ID (required): your Google Cloud project ID.
  * LOCATION (required): the Google Cloud region where the schema registry is located.
  * REGISTRY_ID (required): the ID of your schema registry.
  * CONTEXT_ID (optional): the ID or name of the context, if deleting a subject within a specific context.
  * SUBJECT_ID (optional): the ID or name of the subject you want to delete.



For example, to soft-delete `orders-topic-value` from schema registry `test_registry` in project `test-gcp-project` and location `us-central1`, make the following request:
    
    
    DELETE https://managedkafka.googleapis.com/v1/projects/test-gcp-project/locations/us-central1/schemaRegistries/test_registry/subjects/orders-topic-value
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

If the request is successful, the API returns a `200 OK` status code. The response body contains a JSON array of the version numbers of the schemas that belonged to the deleted subject.

## Hard-delete a subject

Hard-deleting a subject is irreversible and also deletes all associated schema versions.

Make sure the following conditions are met:

  * The subject that you are going to delete is not referenced by other schemas. A request for deletion fails if any version in the subject is referenced by other schemas.

  * The schema registry to which the subject belongs or the subject itself must not be in the `Read-only` mode.

  * Back up any necessary schema information before proceeding with the deletion.

  * No active producers or consumers must rely on the schemas within this subject, as deleting it can cause disruptions.




### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry that contains the subject to delete.

  3. Under **Subjects in this schema registry** , click the name of the subject.

  4. In the **Subject details** page, click delete **Delete**.

  5. Select **Hard Delete**.

  6. In the **Delete schema subject** dialog, type `delete` into the field.

  7. Click **Delete**. This action soft-deletes the subject before permanently deleting it.




### REST

To hard-delete a subject using the REST API, you must first soft-delete it. Once soft-deleted, you can proceed with the hard-deletion.

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To hard-delete a subject using the REST API, make a `DELETE` request to the appropriate URI, including the `permanent=true` query parameter and using the [`projects.locations.schemaRegistries.subjects.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects/delete) method.
    
    
    DELETE https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID?permanent=true
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

To hard-delete a subject under a specific context by using the REST API, make a `DELETE` request to the appropriate URI, including the `permanent=true` query parameter and using the [`projects.locations.schemaRegistries.contexts.subjects.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.subjects/delete) method.
    
    
    DELETE https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects/SUBJECT_ID?permanent=true
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Replace the following:

  * PROJECT_ID (required): your Google Cloud project ID.
  * LOCATION (required): the Google Cloud region where the schema registry is located.
  * REGISTRY_ID (required): the ID of your schema registry.
  * CONTEXT_ID (optional): the ID of the context, if deleting a subject within a specific context.
  * SUBJECT_ID (optional): the ID or name of the subject you want to delete.



For example, to hard-delete the previously soft-deleted subject `orders-topic-value` from schema registry `test_registry` in project `test-gcp-project` and location `us-central1`, make the following request:
    
    
    DELETE https://managedkafka.googleapis.com/v1/projects/test-gcp-project/locations/us-central1/schemaRegistries/test_registry/subjects/orders-topic-value?permanent=true
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

If the request is successful, the API returns a `200 OK` status code. The response body contains a JSON array of the version numbers of the schemas that belonged to the deleted subject.

For more information, see [`projects.locations.schemaRegistries.contexts.subjects.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.subjects/delete).

## Restore a soft-deleted subject

To restore a soft-deleted subject, perform the following steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry that contains the soft-deleted subject.

  3. For filter_list **Filter** , click cancel **Cancel** to clear the **Soft-deleted: No** filter.

  4. Click the name of the subject to restore.

  5. In the **Subject details** page, click add_box **Create version to restore**.

  6. For **Schema type** , select **Avro** or **Protocol Buffer**.

  7. In the **Schema definition** field, enter the definition of the schema. Don't include sensitive information such as personally identifiable information (PII) or security data in your schema field names.

  8. If your schema uses or depends on data structures defined in _other_ schemas in the schema registry, perform the following steps:

     1. Click **Add Schema reference**.
     2. In the **Reference name** field, enter the reference name of the referenced schema. 
     3. In the **Subject** list, select the subject that contains the referenced schema.
     4. In the **Version** list, select the version number of the referenced schema.
     5. Click **OK**.

Repeat these steps for each referenced schema.

  9. Click **Create**.




### REST

To restore a soft-deleted subject, use the [`schemaRegistries.subjects.versions.create`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the schema registry 
  * `REGISTRY_ID`: the ID of the schema registry 
  * `SUBJECT`: the subject name 
  * `SCHEMA_DEFINITION`: a string that contains the schema definition 



HTTP method and URL: 
    
    
    POST https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT/versions

Request JSON body: 
    
    
    {
      "schema": "SCHEMA_DEFINITION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT/versions"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT/versions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "id": SCHEMA_ID
    }
    

## What's next

  * [Learn more about schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry)
  * [List subjects](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subjects)
  * [List subject versions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subject-versions)
  * [Delete a schema subject version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject-version)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
