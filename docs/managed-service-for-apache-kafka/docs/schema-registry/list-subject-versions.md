---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subject-versions/
title: List subject versions \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:51.007081+00:00
---

# List subject versions  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subject-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List subject versions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list the versions of a subject within a specific schema registry in your project.

This document shows you how to list subject versions using the Google Cloud console or the Managed Kafka API.

### Required roles and permissions

To get the permissions that you need to list subject versions, ask your administrator to grant you the [Managed Kafka Schema Registry Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`) IAM role on your schema registry. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list subject versions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list subject versions:

  * Grant the following permission on the parent subject: `managedkafka.versions.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List the schema versions in a subject

To list all versions of a subject in a specific schema registry within your project, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry where your subject is located.

  3. Under **Subjects in this schema registry** , click the name of the subject.

  4. In the **Subject details** page, the schema versions are listed under **All Versions**.

  5. Optional: To view the schema definition for a version, select the checkbox for the version ID. The schema definition is shown under **Definition**.

  6. Optional: To view the differences between any two schema versions for this subject, perform the following steps:

     1. Under **All versions** , select the versions to compare.
     2. In the **Definition** area, click compare_arrows **View diff**.

The two schema definitions are displayed side by side, with additions, deletions, and changes highlighted.




### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To list subject versions, make a `GET` request to the [`projects.locations.schemaRegistries.subjects.versions.list`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/list) method.
    
    
    GET https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects/SUBJECT_ID/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Replace the following:

  * PROJECT_ID: your Google Cloud project ID.
  * LOCATION: the Google Cloud region where the schema registry is located.
  * REGISTRY_ID: the ID of your schema registry.
  * SUBJECT_ID: the ID of the subject.



Example:
    
    
    GET https://managedkafka.googleapis.com/v1main/projects/test-project/locations/us-central1/schemaRegistries/test_registry/subjects/test_subject/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Or with a context:
    
    
    GET https://managedkafka.googleapis.com/v1main/projects/test-project/locations/us-central1/schemaRegistries/test_registry/contexts/test_context/subjects/test_subject/versions
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Where:

  * `test-project` is your Google Cloud project ID.
  * `us-central1` is the Google Cloud region where the schema registry is located.
  * `test_registry` is the ID of your schema registry.
  * `test_context` is the ID of the context.
  * `test_subject` is the ID of the subject.



If the request is successful, the API returns a `200 OK` status code. The response body contains a JSON array of subject versions.

The following is a sample successful response:
    
    
    {
      "versions": [
        {
          "name": "projects/test-project/locations/us-central1/schemaRegistries/test_registry/subjects/test_subject/versions/1",
          "revisionId": "1a2b3c4d",
          "schemaId": "S12345",
          "createTime": "2024-07-15T12:00:00Z",
          "revisionCreateTime": "2024-07-15T12:00:00Z"
        },
        {
          "name": "projects/test-project/locations/us-central1/schemaRegistries/test_registry/subjects/test_subject/versions/2",
          "revisionId": "5e6f7g8h",
          "schemaId": "S67890",
          "createTime": "2024-07-16T14:30:00Z",
          "revisionCreateTime": "2024-07-16T14:30:00Z"
        }
      ]
    }
    

For more information, see the [`projects.locations.schemaRegistries.subjects.versions.list`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.subjects.versions/list) method documentation.

## What's next

  * [Learn more about schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry)
  * [List subjects](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subjects)
  * [Delete a schema subject version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject-version)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
