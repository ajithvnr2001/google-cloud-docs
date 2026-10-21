---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-schema-registries/
title: List all schema registries \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:14.086157+00:00
---

# List all schema registries  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/list-schema-registries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List all schema registries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list the schema registries in your project. This document shows you how to list schema registries using the Google Cloud console, the Google Cloud CLI, or the Managed Kafka API.

### Required roles and permissions

To get the permissions that you need to list schema registries, ask your administrator to grant you the [Managed Kafka Schema Registry Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`) IAM role on your project and location. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list schema registries. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list schema registries:

  * Grant the following permission on the parent location: `managedkafka.schemaRegistries.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List your schema registries

To list all your schema registries within your project, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Schema registries** page. 

[Go to schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

The page displays a list of schema registries in your project. The list includes columns for the following properties:

     * **Name** : the unique identifier for the schema registry.
     * **Region** : the Google Cloud region where the schema registry is hosted.



### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Run the [ `gcloud beta managed-kafka schema-registries list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/schema-registries/list) command:
    
    gcloud beta managed-kafka schema-registries list \
        --location=LOCATION \

Replace the following:

     * LOCATION (required): the Google Cloud region for which to list schema registries.

For example, to list all schema registries in the `us-central1` location, run the following command:
    
    gcloud beta managed-kafka schema-registries list --location=us-central1

Sample output:
    
    NAME             LOCATION
    sr_docs      us-central1
    sr_docs23    us-central1
    sr23wert     us-central1




### REST

To list schema registries, use the [ `projects.locations.schemaRegistries.list`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.schemaRegistries/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location where you want to get the list of schema registries; for example, `us-central1`



HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries?view=SCHEMA_REGISTRY_VIEW_FULL

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries?view=SCHEMA_REGISTRY_VIEW_FULL"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/schemaRegistries?view=SCHEMA_REGISTRY_VIEW_FULL" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "schemaRegistries": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/REGISTRY_ID",
          "contexts": [
            "projects/PROJECT_ID/locations/LOCATION/REGISTRY_ID/contexts/.",
            "projects/PROJECT_ID/locations/LOCATION/REGISTRY_ID/contexts/CONTEXT_NAME"
          ]
        }
    }
    

The returned JSON object includes a list of schema registries found in the specified location. If the `view` query parameter is `SCHEMA_REGISTRY_VIEW_FULL`, the response also includes the contexts associated with each schema registry.

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
