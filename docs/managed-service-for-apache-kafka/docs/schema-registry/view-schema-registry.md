---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry/
title: View schema registry details \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:09.001380+00:00
---

# View schema registry details  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View schema registry details Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to view the details of a schema registry resource within Managed Service for Apache Kafka. You can view details such as its configuration, associated contexts, and subjects.

You can't use the open source Apache Kafka client APIs to view these specific Managed Service for Apache Kafka schema registry resource details.

## Required roles and permissions

To get the permissions that you need to view a schema registry, ask your administrator to grant you the [Managed Kafka Schema Registry Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`) IAM role on the schema registry instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view a schema registry. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view a schema registry:

  * Grant this permission on the schema registry resource: `managedkafka.schemaRegistries.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View schema registry details

To retrieve the configuration and details of a specific schema registry, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

A list of schema registries in your project is displayed.

  2. Click the name of the schema registry whose details you want to view. 

The **Schema registry details** page opens. The information displayed on this page is explained in the  Schema registry page details section.




### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. To retrieve the configuration and details of a specific schema registry, run the [ `gcloud beta managed-kafka schema-registries describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/schema-registries/describe) command:
    
    gcloud beta managed-kafka schema-registries describe SCHEMA_REGISTRY_ID \
        --location=LOCATION \

Replace the following:

     * SCHEMA_REGISTRY_ID (required): the ID of the schema registry you want to describe.
     * LOCATION (required): the Google Cloud region where the schema registry is located.



For example, the following command gets the details of a schema registry called `test_SR` located in the region `us-central1`:
    
    
    gcloud beta managed-kafka schema-registries describe test_SR \
        --location=us-central1

The command returns the output similar to the following:
    
    
    Describing schema registry: projects/test-pubsub/locations/us-central1/schemaRegistries/test_SR
    name: projects/test-pubsub/locations/us-central1/schemaRegistries/test_SR
    mode: READWRITE
    config:
      - compatibility: BACKWARD
    contexts:
      - projects/test-pubsub/locations/us-central1/schemaRegistries/test_SR/contexts/.
      - projects/test-pubsub/locations/us-central1/schemaRegistries/test_SR/contexts/user-record

### REST

  * To retrieve the details of a specific schema registry instance using the REST API, make a `GET` request to the following URI:
    
    GET https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Replace the following:

    * PROJECT_ID (required): your Google Cloud project ID.
    * LOCATION (required): the region where the schema registry exists.
    * SCHEMA_REGISTRY_ID (required): the unique ID of the schema registry that you want to view.



If the request is successful, the API returns a `200 OK` status code. The response body contains a JSON object representing the details of the requested schema registry.

For example, the following is a response to a command to get the details of a schema registry called `gcloud_test` located in the region `us-central1`:
    
    
    {
      "name": "projects/testing-311516/locations/us-central1/schemaRegistries/gcloud_test",
      "contexts": [
        "projects/testing-311516/locations/us-central1/schemaRegistries/gcloud_test/contexts/default",
        "projects/testing-311516/locations/us-central1/schemaRegistries/gcloud_test/contexts/."
      ]
    }

For more information, see the [REST API documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest).

## Schema registry page details

When you view a schema registry in the Google Cloud console, the **Schema registry details** page displays the following information for the selected registry:

  * **Region** : the Google Cloud region where the registry resides.
  * **Schema registry URL** : the endpoint URL for the schema registry. This is of the format `https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID`. 

For example—`https://managedkafka.googleapis.com/v1main/projects/managed-kafka-project/locations/us-central1/schemaRegistries/testschemaregistry`

  * **Schema mode** : the operational mode that you can set at the schema registry level and the individual subject level. This setting controls whether modifications can be made.
  * **Compatibility type** : the registry-level configuration for the default compatibility setting enforced for new subjects or schema versions within this registry (unless overridden at the subject or context level). Common values include `BACKWARD`, `FORWARD`, `FULL`, or `NONE`.
  * **Subjects in this schema registry** : a list of subject names associated with the registry. If a context is available, you can also view the context for each subject.



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
