---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject-version/
title: Delete a schema subject version \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:15.246677+00:00
---

# Delete a schema subject version  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Delete a schema subject version Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to delete a specific version of a schema subject from a schema registry. There are two ways to delete a subject version:

  * **Soft-delete**. Marks the version as deleted, but its information is retained and can be recovered.

  * **Hard-delete**. Permanently removes the version and its associated data.




### Required roles and permissions

To get the permissions that you need to delete a schema subject version, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on the parent subject. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete a schema subject version. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete a schema subject version:

  * Grant the following permission on the parent subject: `managedkafka.googleapis.com/subjectVersions.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Soft delete a schema subject version

Here are some best practices for soft-deleting a schema subject version:

  * Verify that no active producers or consumers are using the schema subject version that you intend to delete.

  * After deleting a schema subject version, monitor your applications to ensure they continue to function as expected.

  * Soft-delete allows recovery of deleted schema subject versions, which is useful if you're unsure about deleting a schema subject version.




To soft-delete a schema subject version, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry where your subject is located.

  3. Under **Subjects in this schema registry** , click the name of the subject.

  4. In the **All versions** list, find the version that you want to delete and click **More actions**.

  5. Click **Delete version**.

  6. In the **Delete schema version** window, click **Soft delete**.

  7. Confirm the deletion by typing `delete` and then click **Delete**.




### REST

To soft-delete a schema subject version, make a `DELETE` request to the [`projects.locations.schemaRegistries.subjects.versions.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/delete) method.

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials, run the following command: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To soft-delete the schema subject version:

  * Use the following command for the default context:
        
        DELETE https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID/versions/VERSION_ID
        Authorization: Bearer $(gcloud auth application-default print-access-token)
        

  * Use the following command for a specific context:
        
        DELETE https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects/SUBJECT_ID/versions/VERSION_ID
        Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)
        




Replace the following:

  * PROJECT_ID: your Google Cloud project ID, for example, `test-project`.
  * LOCATION: the Google Cloud region where the schema registry is located, for example, `us-central1`.
  * REGISTRY_ID: the ID of your schema registry, for example, `test_registry`.
  * CONTEXT_ID: the ID of your context, for example, `test_context`.
  * SUBJECT_ID: the ID of the subject, for example, `test_subject`.
  * VERSION_ID: the version of the subject to delete, for example, `2` or `latest`.
  * SERVICE_ACCOUNT: the service account, for example, `test-service-account@test-project.iam.gserviceaccount.com`.



If the request is successful, the API returns a `200 OK` status code and an empty response body.

For more information, see the [`projects.locations.schemaRegistries.subjects.versions.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/delete) method documentation.

## Hard delete a schema subject version

Here are some best practices for hard-deleting a schema subject version:

  * Ensure you have a backup or a way to recreate the schema subject version if needed.

  * Verify that no active producers or consumers are using the schema subject version you intend to delete.

  * Always test schema subject version deletions in a development or staging environment before applying changes to production.

  * After deleting a schema subject version, monitor your applications to ensure they continue to function as expected.

  * Use hard-delete when you need to permanently remove a schema subject version.




To hard-delete a schema subject version, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry where your subject is located.

  3. Under **Subjects in this schema registry** , click the name of the subject.

  4. In the **All versions** list, find the version that you want to delete and click **More actions**.

  5. Click **Delete version**.

  6. In the **Delete schema version** window, click **Hard delete**.

  7. Confirm the deletion by typing `delete` and then click **Delete**. This action soft-deletes the subject version before permanently deleting it.




### REST

To hard-delete a schema subject version using the REST API, you must first soft-delete it. Once soft-deleted, you can proceed with the hard-deletion.

To hard-delete a schema subject version, make a `DELETE` request to the [`projects.locations.schemaRegistries.subjects.versions.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/delete) method. To hard-delete the schema subject version, include the `hardDelete=true` query parameter.

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials, run the following command: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To hard-delete the schema subject version:

  * Use the following command for the default context:
        
        DELETE https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID/versions/VERSION_ID?hardDelete=true
        Authorization: Bearer $(gcloud auth application-default print-access-token)
        

  * Use the following command for a specific context:
        
        DELETE https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects/SUBJECT_ID/versions/VERSION_ID?hardDelete=true
        Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)
        




Replace the following:

  * PROJECT_ID: your Google Cloud project ID, for example, `test-project`.
  * LOCATION: the Google Cloud region where the schema registry is located, for example, `us-central1`.
  * REGISTRY_ID: the ID of your schema registry, for example, `test_registry`.
  * CONTEXT_ID: the ID of your context, for example, `test_context`.
  * SUBJECT_ID: the ID of the subject, for example, `test_subject`.
  * VERSION_ID: the version of the subject to delete, for example, `2` or `latest`.
  * SERVICE_ACCOUNT: the service account, for example, `test-service-account@test-project.iam.gserviceaccount.com`.



If the request is successful, the API returns a `200 OK` status code and an empty response body.

For more information, see the [`projects.locations.schemaRegistries.subjects.versions.delete`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/delete) method documentation.

## What's next

  * [Learn more about schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry)
  * [List subject versions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subject-versions)
  * [Register a new schema version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/register-schema-version)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
