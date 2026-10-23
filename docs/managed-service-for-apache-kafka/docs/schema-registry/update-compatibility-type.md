---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-compatibility-type/
title: Update compatibility type \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:22.499602+00:00
---

# Update compatibility type  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-compatibility-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Update compatibility type Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you create a new schema version, the schema registry checks that the new version is compatible with previous versions. Enforcing schema compatibility helps ensure that data producers and consumers continue to work correctly as the data structure evolves.

  * The supported values for compatibility type are **Backward** , **Backward transitive** , **Forward** , **Forward transitive** , **Full** , **Full transitive** , or **None**.

  * Compatibility type is managed as a JSON object. For example:
        
        {
          "compatibility": "BACKWARD"
        }
        

  * If not explicitly set, the compatibility type for a schema registry defaults to **Backward**.

  * If a compatibility type isn't set on a subject, it inherits the value from the schema registry.

  * Configurations set at the subject level override those at the schema registry level.

  * Updating the compatibility type only affects new schema versions registered after the update.




For more information about the compatibility types, see [About compatibility type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle#compatibility-type).

## Required roles and permissions to update compatibility type

To get the permissions that you need to update compatibility type for a schema registry or subject, ask your administrator to grant you the [**Managed Kafka Schema Registry Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to update compatibility type for a schema registry or subject. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to update compatibility type for a schema registry or subject:

  * Grant the following permission on the resource for which you want to update the compatibility type: `managedkafka.config.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update compatibility type for a schema registry

### Console

To update the compatibility type for the entire schema registry, follow these steps:

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

A list of schema registries in your project is displayed.

  2. Click the name of the schema registry for which you want to update the compatibility type. 

The **Schema registry details** page opens.

  3. In the main details section for the registry, find the **Compatibility type** setting and click the **Edit** icon next to it. 

The **Edit compatibility type** page opens.

  4. From the **Compatibility type** dropdown menu, select the value.
  5. Click **Save**.



### gcloud

To update the compatibility type for a schema registry, use the [`gcloud alpha managed-kafka schema-registries update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/schema-registries/update) command.
    
    
      gcloud alpha managed-kafka schema-registries update SCHEMA_REGISTRY_ID   
    
          --location=LOCATION   
    
          --compatibility=COMPATIBILITY_TYPE
      

  * `SCHEMA_REGISTRY_ID`: the ID of the schema registry to update.
  * `LOCATION`: the region of the schema registry.
  * `COMPATIBILITY_TYPE`: the new compatibility type. Valid values include `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`, `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, or `NONE`.



**Example** : Update the compatibility type of the `test-registry` schema registry in the `us-central1` region to `FORWARD`.
    
    
      gcloud alpha managed-kafka schema-registries update test-registry   
    
          --location=us-central1   
    
          --compatibility=FORWARD
      

### REST

To update the compatibility type for a schema registry, make a `PUT` request to the REST API.

First, get an access token:
    
    
    gcloud auth application-default print-access-token

Then, send a `PUT` request to the registry's config endpoint:
    
    
    PUT https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID/config
    

Replace the following path parameters:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where the schema registry exists.
  * `SCHEMA_REGISTRY_ID`: the ID of the schema registry.



Include the following JSON object in the request body:
    
    
    {
      "compatibility": "COMPATIBILITY_TYPE"
    }

Replace `COMPATIBILITY_TYPE` with a valid value, such as `NONE`, `BACKWARD`, `FORWARD`, or `FULL`.

If successful, the API returns a `200 OK` status code.

## Update compatibility type for a subject

### Console

To update the compatibility type for a specific subject, follow these steps:

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

  2. Click the name of the schema registry that contains the subject. 

The **Schema registry details** page opens.

  3. In the **Subjects in this schema registry** table, click the name of the subject.
  4. Find the **Compatibility type** setting for the subject and click the **Edit** icon next to it. 

The **Edit compatibility type** page opens.

  5. From the **Compatibility type** dropdown menu, select the value. Choosing a value here overrides the registry-level setting for this subject.
  6. Click **Save**.



### gcloud

To update the compatibility type for a subject, use the [`gcloud alpha managed-kafka schema-registries subject update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/schema-registries/subject/update) command.
    
    
      gcloud alpha managed-kafka schema-registries subject update SUBJECT_ID   
    
          --schema-registry=SCHEMA_REGISTRY_ID   
    
          --location=LOCATION   
    
          --compatibility=COMPATIBILITY_TYPE
      

  * `SUBJECT_ID`: the ID of the subject to update.
  * `SCHEMA_REGISTRY_ID`: the ID of the schema registry that contains the subject.
  * `LOCATION`: the region of the schema registry.
  * `COMPATIBILITY_TYPE`: the new compatibility type. Valid values include `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`, `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, or `NONE`.



**Example** : Update the compatibility type of the `test-subject` subject in the `test-registry` schema registry in the `us-central1` region to `FORWARD_TRANSITIVE`.
    
    
      gcloud alpha managed-kafka schema-registries subject update test-subject   
    
          --schema-registry=test-registry   
    
          --location=us-central1   
    
          --compatibility=FORWARD_TRANSITIVE
      

### REST

To update the compatibility type for a subject, make a `PUT` request to the REST API.

First, get an access token:
    
    
    gcloud auth application-default print-access-token

Update compatibility for a subject in the default context:
    
    
    PUT https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID/config/SUBJECT_ID
    

Update compatibility for a subject in a specific context:
    
    
    PUT https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID/contexts/CONTEXT_ID/config/SUBJECT_ID
    

Replace the following path parameters:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where the schema registry exists.
  * `SCHEMA_REGISTRY_ID`: the ID of the schema registry.
  * `SUBJECT_ID`: the ID of the subject.
  * `CONTEXT_ID`: the ID of the context (if applicable).



Include the following JSON object in the request body:
    
    
    {
      "compatibility": "COMPATIBILITY_TYPE"
    }

Replace `COMPATIBILITY_TYPE` with a valid value, such as `FORWARD_TRANSITIVE`.

**Example:** Set subject `user_events` compatibility to `FORWARD_TRANSITIVE`.

Request to `PUT https://managedkafka.googleapis.com/v1main/projects/test-project/locations/us-central1/schemaRegistries/test_registry/config/user_events`

With body:
    
    
    {
      "compatibility": "FORWARD_TRANSITIVE"
    }

If successful, the API returns a `200 OK` status code.

## What's next

  * [Update schema mode](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-schema-mode)
  * [Create a subject and register schemas](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one)
  * [View details of a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
