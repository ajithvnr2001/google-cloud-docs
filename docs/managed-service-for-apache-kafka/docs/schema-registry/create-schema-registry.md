---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-schema-registry/
title: Create a schema registry \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:06.123365+00:00
---

# Create a schema registry  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-schema-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a schema registry Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A schema registry is a repository for managing schemas used by your Kafka producers and consumers.

This document shows you how to create a schema registry resource within Managed Service for Apache Kafka using the Google Cloud console, the Google Cloud CLI, or the Managed Kafka API.

## Before you begin

Before you create a schema registry, complete the following:

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster) in the same region where you are planning to create a schema registry.



### Required roles and permissions

To get the permissions that you need to create a schema registry, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a schema registry. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a schema registry:

  * Grant this permission on the parent location: `managedkafka.schemaRegistries.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a schema registry

### Console

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

The **Schema registries** page opens.

  2. On the **Schema registries** page, click **Create**. 

The **Create Schema registry** page opens.

  3. For **Schema registry name** , enter a unique identifier for your registry. 

The name must start with a letter, contain only letters (a-z, A-Z), numbers (0-9), and underscores (_), and be 63 characters or less.

  4. Select or enter a **Region** from the menu. 

You must already have a single or multiple active Managed Service for Apache Kafka clusters in the region specified. To check the regions of your clusters, see the documentation about [listing your clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters#list).

For a list of supported locations, see [Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).

  5. Click **Create**.



### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Use the [ `gcloud beta managed-kafka schema-registries create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/schema-registries/create) command to create a schema registry: 
         
         gcloud beta managed-kafka schema-registries create SCHEMA_REGISTRY_ID \
             --location=LOCATION \

Replace the following:

     * SCHEMA_REGISTRY_ID (required): a unique identifier for your new schema registry. This forms part of the registry's resource name. The name must start with a letter, contain only letters (a-z, A-Z), numbers (0-9), and underscores (_), and be 63 characters or less.
     * LOCATION (required): the Google Cloud region where the schema registry is going to be created. This location must match the region of the Managed Service for Apache Kafka cluster or clusters using this registry. For supported locations, see [ Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).

To create a schema registry named `test_schema_registry` in the `us-central1` region, run the following command:
    
    gcloud beta managed-kafka schema-registries create test_schema_registry \
        --location=us-central1

After the command completes successfully, the schema registry is created. You can then configure Kafka clients to use its URL. To view the schema registry URL, see [ Schema registry page details](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry#schema-registry-page-details).




### REST

To create a schema registry instance using the REST API, perform the following steps.

  1. Send a `POST` request similar to the following:
    
    POST https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    Content-Type: application/json --data @response-body.json
    

  2. Create a JSON file `request-body.json` with the following structure:
    
    {
      "schemaRegistryId": "SCHEMA_REGISTRY_ID"
    }

Replace the following:

     * SCHEMA_REGISTRY_ID (required): a unique identifier for your new schema registry. This forms part of the registry's resource name. The name must start with a letter, contain only letters (a-z, A-Z), numbers (0-9), and underscores (_), and be 63 characters or less.

Run the `POST` request with the constructed URI, headers, and body. If successful, the API returns a `200 OK` status code and a response body containing the JSON representation of the newly created SchemaRegistry resource.

The following is a sample successful response.
    
    {
      "name": "projects/testing-311516/locations/us-central1/schemaRegistries/test",
      "contexts": [
        "projects/testing-311516/locations/us-central1/schemaRegistries/test/contexts/."
      ]
    }

The `projects/testing-311516/locations/us-central1/schemaRegistries/test/contexts/.` represents the default context. Resources in the default context don't require any context to be specified.

For more information, see the [REST API documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest).




## What's next

  * [List all schema registries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-schema-registries)

  * [View a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry)

  * [Create a subject](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one)

  * [Delete a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-schema-registry)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
