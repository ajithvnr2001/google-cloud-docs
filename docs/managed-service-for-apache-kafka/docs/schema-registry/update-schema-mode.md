---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-schema-mode/
title: Update schema mode \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:58:34.934807+00:00
---

# Update schema mode  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-schema-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Update schema mode Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The schema mode defines whether a schema registry or a specific subject allows changes, such as writing or editing schemas.

  * The supported values for schema mode are **Readonly** and **Readwrite**.

  * Schema mode is managed as a JSON object containing key-value pairs. For example, the following is a sample:
        
        {
          "mode": "READWRITE"
        }
        

  * If not explicitly set at the schema registry level, the schema mode defaults to **Readwrite**.

  * If a schema mode is not explicitly specified at the subject level, it inherits the value from the schema registry.

  * Configurations set at the subject level override those set at the schema registry level.




For more information about schema mode including its values, see [Schema mode](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#schema-mode).

## Required roles and permissions to update schema mode

To get the permissions that you need to update schema mode for a schema registry or subject, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to update schema mode for a schema registry or subject. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to update schema mode for a schema registry or subject:

  * Grant the following permission on the resource for which you want to update the mode: `managedkafka.mode.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update schema mode for a schema registry

### Console

To update the schema mode for the entire schema registry, follow these steps:

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

A list of schema registries in your project is displayed.

  2. Click the name of the schema registry for which you want to update the schema mode. 

The **Schema registry details** page opens.

  3. In the main details section for the registry, find the **Schema mode** setting and click the **Edit** icon next to it. 

The **Edit schema mode** page opens.

  4. From the **Schema mode** dropdown menu, select the value. 

For more information about these values, see [About schema mode](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#schema-mode).

  5. Click **Save**.



### gcloud

To update the schema mode for a schema registry, use the [`gcloud alpha managed-kafka schema-registries update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/schema-registries/update) command:
    
    
    gcloud alpha managed-kafka schema-registries update SCHEMA_REGISTRY_ID \
        --location=LOCATION \
        --mode=MODE_TYPE
    

  * `SCHEMA_REGISTRY_ID`: the ID of the schema registry to update.
  * `LOCATION`: the region of the schema registry to update.
  * `MODE_TYPE`: the new schema mode. The valid values are: 
    * `READWRITE`
    * `READONLY`



Example:

To update the schema mode of the `test-registry` schema registry in the `us-central1` region to `READONLY`, run the following command:
    
    
    gcloud alpha managed-kafka schema-registries update test-registry \
        --location=us-central1 \
        --mode=READONLY
    

### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [` gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To update the schema mode, make a `PUT` request to the REST API endpoint for the schema registry using the [`projects.locations.schemaRegistries.contexts.mode.update`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.mode/update) method.

Updating schema mode for the schema registry with a default context:
    
    
    PUT https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID/mode
    

Replace the following path parameters:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where the schema registry exists.
  * `SCHEMA_REGISTRY_ID`: the unique ID of the schema registry.



Request body:

Include a JSON object in the request body specifying the mode details.
    
    
    {
      "mode": "MODE_TYPE"
    }

Replace `MODE_TYPE` with one of the valid string options for the mode:

  * `READWRITE`
  * `READONLY`



If successful, the API returns a `200 OK` status code and a response body containing the JSON representation of the updated mode configuration.

For more information, see the [REST API documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest).

## Update schema mode for a subject

### Console

To update the schema mode for a specific subject, follow these steps:

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry that contains the subject. 

The **Schema registry details** page opens.

  3. In the **Subjects in this schema registry** table, click the name of the subject for which you want to update the schema mode.
  4. Find the **Schema mode** setting for the subject and click the **Edit** icon next to it. 

The **Edit schema mode** page opens.

  5. From the **Schema mode** dropdown menu, select the value. Choosing a value here overrides the registry-level setting for this specific subject. 

For more information about these values, see [ About schema mode](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#schema-mode).

  6. Click **Save**.



### gcloud

To update the schema mode for a subject, use the [`gcloud alpha managed-kafka schema-registries subject update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/schema-registries/subject/update) command:
    
    
    gcloud alpha managed-kafka schema-registries subject update SUBJECT_NAME \
        --schema-registry=SCHEMA_REGISTRY_ID \
        --location=LOCATION \
        --mode=MODE_TYPE
    

  * `SUBJECT_NAME`: the name of the subject to update.
  * `SCHEMA_REGISTRY_ID`: the ID of the schema registry that contains the subject.
  * `LOCATION`: the region of the schema registry that contains the subject.
  * `MODE_TYPE`: the new schema mode. The valid values are: 
    * `READWRITE`
    * `READONLY`



Example:

To update the schema mode of the `test-subject` subject in the `test-registry` schema registry in the `us-central1` region to `READONLY`, run the following command:
    
    
    gcloud alpha managed-kafka schema-registries subject update test-subject \
        --schema-registry=test-registry \
        --location=us-central1 \
        --mode=READONLY
    

### REST

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [` gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

To update the schema mode for a subject, make a `PUT` request to the REST API endpoint for a specific subject using the [`projects.locations.schemaRegistries.contexts.mode.update`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries.contexts.mode/update) method.

Updating schema mode for a subject in the default context:
    
    
    PUT https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID/mode/SUBJECT_NAME
    

Replace the following path parameters:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where the schema registry exists.
  * `SCHEMA_REGISTRY_ID`: the unique ID of the schema registry.
  * `SUBJECT_NAME`: the name of the subject.



Request body:

Include a JSON object in the request body specifying the mode details.
    
    
    {
      "mode": "MODE_TYPE"
    }

Replace `MODE_TYPE` with one of the valid string options for the mode:

  * `READWRITE`
  * `READONLY`



Example—Set subject `user_events` schema mode to `Readonly` in the default context:

Request to `PUT https://managedkafka.googleapis.com/v1main/projects/test-gcp-project/locations/us-east1/schemaRegistries/main_registry/mode/user_events`

With body:
    
    
    {
      "mode": "READONLY"
    }

If successful, the API returns a `200 OK` status code and a response body containing the JSON representation of the updated subject or context resource reflecting this change.

Updating schema mode for a subject in a specific context:
    
    
    PUT https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID/contexts/CONTEXT_NAME/mode/SUBJECT_NAME
    

Replace the following path parameters:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where the schema registry exists.
  * `SCHEMA_REGISTRY_ID`: the unique ID of the schema registry.
  * `CONTEXT_NAME`: the name of the context.
  * `SUBJECT_NAME`: the name of the subject.



Request body:

Include a JSON object in the request body specifying the mode details.
    
    
    {
      "mode": "MODE_TYPE"
    }

Replace `MODE_TYPE` with one of the valid string options for the mode:

  * `READWRITE`
  * `READONLY`



Example—Set subject `user_events` schema mode to `Readonly` in the context `test_context`:

Request to `PUT https://managedkafka.googleapis.com/v1main/projects/test-gcp-project/locations/us-east1/schemaRegistries/main_registry/contexts/test_context/mode/user_events`

With body:
    
    
    {
      "mode": "READONLY"
    }

If successful, the API returns a `200 OK` status code and a response body containing the JSON representation of the updated subject or context resource reflecting this change.

For more information, see the [REST API documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest).

## What's next

  * [Update compatibility type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-compatibility-type)

  * [Create a subject and register schemas](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one)

  * [View details of a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry)

  * [List subjects in a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-subjects)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
