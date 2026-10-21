---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-schema-registry/
title: Delete a schema registry \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:14.400917+00:00
---

# Delete a schema registry  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/delete-schema-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Delete a schema registry Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Deleting a schema registry is an irreversible action. All subjects, schemas, and versions contained within the registry are permanently deleted. Ensure that no active Kafka clients rely on this registry before proceeding.

## Required roles and permissions

To get the permissions that you need to delete a schema registry, ask your administrator to grant you the [Managed Kafka Schema Registry Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`) IAM role on the schema registry instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete a schema registry. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete a schema registry:

  * Grant the following permission on the schema registry: `managedkafka.schemaRegistries.delete`
  * Grant the following permission for console users to list schema registries: `managedkafka.schemaRegistries.list`
  * Grant the following permission for console users to get schema registry details: `managedkafka.schemaRegistries.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a schema registry

To permanently delete a schema registry and all its contents, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

A list of schema registries in your project is displayed.

  2. Click the name of the schema registry that you want to delete.
  3. On the **Schema registry details** page, click the **Delete** button.
  4. Confirm the deletion when prompted.



### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Use the `gcloud beta managed-kafka schema-registries delete` command:
         
         gcloud beta managed-kafka schema-registries delete SCHEMA_REGISTRY_ID \
             --location=LOCATION \




Replace the following:

  * `SCHEMA_REGISTRY_ID` (required): the ID of the schema registry you want to delete.
  * `LOCATION` (required): the Google Cloud region where the schema registry is located.



For example—to delete a schema registry named `testRegistry` in the `us-central1` region, run the following command:
    
    
    gcloud beta managed-kafka schema-registries delete testRegistry \
        --location=us-central1

### API

Make a `DELETE` request to the specific resource URI of the schema registry you want to delete.
    
    
    DELETE https://managedkafka.googleapis.com/v1main/projects/PROJECT_ID/locations/LOCATION/schemaRegistries/SCHEMA_REGISTRY_ID
    

Replace the following:

  * `PROJECT_ID` (required): your Google Cloud project ID.
  * `SCHEMA_REGISTRY_ID` (required): the ID of the schema registry you want to delete.
  * `LOCATION` (required): the Google Cloud region where the schema registry is located.



If the request is successful and the schema registry is deleted, the API typically returns a `200 OK` status code with an empty JSON body indicating the completion of a long-running operation or the operation resource itself.

If the specified schema registry does not exist, you receive a `404 Not Found` error.

If you lack permissions, you receive a `403 Forbidden` error.

## What's next?

  * [Update compatibility type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-compatibility-type)

  * [Update schema mode](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-schema-mode)

  * [View details of a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/view-schema-registry)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
