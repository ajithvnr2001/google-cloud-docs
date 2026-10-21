---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subjects/
title: List subjects \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:18:20.689732+00:00
---

# List subjects  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subjects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List subjects Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list the subjects within a specific schema registry or context in your project.

This document shows you how to list subjects using the Google Cloud console or the Managed Kafka API.

### Required roles and permissions

To get the permissions that you need to list subjects, ask your administrator to grant you the [Managed Kafka Schema Registry Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`) IAM role on your schema registry or context. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list subjects. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list subjects:

  * Grant the following permission on the parent schema registry or context: `managedkafka.googleapis.com/subjects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List the subjects in a schema registry

To list all subjects in a specific schema registry or context within your project, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry whose details you want to view.

  3. In the **Schema registry details** page, the subjects are listed under **Subjects in this schema registry**.

  4. Optional: To filter which subjects are displayed, click filter_list **Filter**. You can filter by the following properties:

     * **Name**
     * **Context**
     * **Soft deleted** (Yes/No)
  5. Optional: To show or hide columns, click view_column **Column display options** , and then select the columns you want to see or hide.




### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To list subjects directly under a schema registry, make a `GET` request to the specific URI using the [`projects.locations.schemaRegistries.schemas.subjects.list`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.schemas.subjects/list) method for the default context.
    
    
    GET https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/subjects
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

To list subjects under a context within a schema registry, make a `GET` request to the specific URI using the [`projects.locations.schemaRegistries.contexts.schemas.subjects.list`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.schemas.subjects/list) method:
    
    
    GET https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/REGISTRY_ID/contexts/CONTEXT_ID/subjects?subjectPrefix=SUBJECT_PREFIX
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Replace the following:

  * PROJECT_ID (required): your Google Cloud project ID.

  * LOCATION (required): the Google Cloud region where the schema registry is located.

  * REGISTRY_ID (required): the ID of your schema registry.

  * CONTEXT_ID (optional): the ID of the context (if listing subjects within a context).

  * SUBJECT_PREFIX (optional): the context to filter the subjects by, in the format of `:.{context}:`. If unset, all subjects in the registry are returned. If set to an empty string, lists subjects in the default context.




If the request is successful, the API returns a `200 OK` status code. The response body contains a JSON array of subject names.

The following is a sample successful response of subjects in a JSON array for the default context:
    
    
    [
      "orders-topic-key",
      "orders-topic-value",
      "user-profile-event"
    ]
    

Subjects in non-default contexts are returned in the format `:.context:subject`.

For more information, see the [`projects.locations.schemaRegistries.contexts.schemas.subjects/list`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.schemas.subjects.list) method documentation.

## What's next

  * [Learn more about schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry)
  * [List subject versions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry//list-subject-versions)
  * [Register a new schema version](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/register-schema-version)
  * [Delete a subject](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-subject)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
