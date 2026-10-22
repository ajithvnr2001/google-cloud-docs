---
url: https://docs.cloud.google.com/healthcare-api/docs/tutorials/fhir-bigquery-streaming-tutorial/
title: Stream and synchronize FHIR resources with BigQuery \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:33.013754+00:00
---

# Stream and synchronize FHIR resources with BigQuery  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/tutorials/fhir-bigquery-streaming-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Stream and synchronize FHIR resources with BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains scenarios in which you can use BigQuery streaming to keep a FHIR store in sync with a BigQuery dataset in near real time.

## Objectives

The tutorial demonstrates the following steps:

  1. Configure BigQuery permissions.
  2. Create a FHIR store and add Patient resources.
  3. Configure BigQuery streaming on the FHIR store.
  4. Verify streaming configuration to BigQuery.
  5. Export existing FHIR resources to BigQuery.
  6. Stream resources from multiple FHIR stores to the same BigQuery dataset.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Healthcare API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=healthcare.googleapis.com&redirect=https%3A//cloud.google.com/healthcare-api/docs/store-healthcare-data-rest)

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Step 1: Configure BigQuery permissions

To stream FHIR resource changes to BigQuery, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [FHIR store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#fhir_store_bigquery_permissions).

## Step 2: Configure and verify BigQuery streaming

To enable streaming to BigQuery, follow these instructions:

### Create a FHIR store and add Patient resources

To create a FHIR store and add two Patient resources, follow these steps:

  1. Create the FHIR store:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: an identifier for the FHIR store. The FHIR store ID must have the following: 
       * A unique ID in its dataset
       * A Unicode string of 1-256 characters consisting of the following:
         * Numbers
         * Letters
         * Underscores
         * Dashes
         * Periods
     * FHIR_STORE_VERSION: the FHIR version of the FHIR store. The available options are DSTU2, STU3, or R4.

Request JSON body: 
    
    {
      "version": "FHIR_STORE_VERSION"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "version": "FHIR_STORE_VERSION"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=FHIR_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "version": "FHIR_STORE_VERSION"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=FHIR_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "FHIR_STORE_VERSION"
    }
    

  2. Create the first Patient resource in the FHIR store:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID

Request JSON body: 
    
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "birthDate": "1970-01-01",
      "gender": "female",
      "id": "PATIENT_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

  3. Create the second Patient resource in the FHIR store:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID

Request JSON body: 
    
    {
      "name": [
        {
          "use": "official",
          "family": "Zhang",
          "given": [
            "Michael"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1980-01-01",
      "resourceType": "Patient"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "name": [
        {
          "use": "official",
          "family": "Zhang",
          "given": [
            "Michael"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1980-01-01",
      "resourceType": "Patient"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "name": [
        {
          "use": "official",
          "family": "Zhang",
          "given": [
            "Michael"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1980-01-01",
      "resourceType": "Patient"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "birthDate": "1980-01-01",
      "gender": "male",
      "id": "PATIENT_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "name": [
        {
          "family": "Zhang",
          "given": [
            "Michael"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

  4. Search for Patient resources in the FHIR store and verify that the store contains the two Patient resources:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/d5d0d3a7-29a1-4bb6-b388-35e8ce218fc5",
          "resource": {
            "birthDate": "1980-01-01",
            "gender": "male",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "versionId": "VERSION_ID"
            },
            "name": [
              {
                "family": "Zhang",
                "given": [
                  "Michael"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/f2aa0885-390d-437d-ac73-8d41516a2c05",
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "versionId": "VERSION_ID"
            },
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Darcy"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?"
        }
      ],
      "resourceType": "Bundle",
      "total": 2,
      "type": "searchset"
    }
    




### Configure BigQuery streaming on the FHIR store

Update the FHIR store to configure BigQuery streaming. After configuring streaming, the Cloud Healthcare API streams any resource changes to the BigQuery dataset.

  1. Update your existing FHIR store to add the location of the BigQuery dataset:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: your FHIR store ID
     * BIGQUERY_PROJECT_ID: the Google Cloud project containing the BigQuery dataset for streaming FHIR resource changes
     * BIGQUERY_DATASET_ID: the BigQuery dataset where you are streaming FHIR resource changes

Request JSON body: 
    
    {
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS_V2"
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS_V2"
            }
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=streamConfigs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS_V2"
            }
          }
        }
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=streamConfigs" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "FHIR_STORE_VERSION",
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS_V2"
            }
          }
        }
      ]
    }
    




### Verify streaming configuration to BigQuery

Verify that streaming is configured correctly by completing the following steps:

  1. Create a third Patient resource in the FHIR store:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID

Request JSON body: 
    
    {
      "name": [
        {
          "use": "official",
          "family": "Lee",
          "given": [
            "Alex"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1990-01-01",
      "resourceType": "Patient"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "name": [
        {
          "use": "official",
          "family": "Lee",
          "given": [
            "Alex"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1990-01-01",
      "resourceType": "Patient"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "name": [
        {
          "use": "official",
          "family": "Lee",
          "given": [
            "Alex"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1990-01-01",
      "resourceType": "Patient"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "birthDate": "1990-01-01",
      "gender": "male",
      "id": "PATIENT_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "name": [
        {
          "family": "Lee",
          "given": [
            "Alex"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

  2. Query the `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.Patient` table by running [`bq query`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query). BigQuery organizes tables by FHIR resource type. The third Patient resource you created is in the `Patient` table.
         
         bq query \
            --project_id=BIGQUERY_PROJECT_ID \
            --use_legacy_sql=false \
            'SELECT COUNT(*) FROM `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.Patient`'

The query returns the following result. The result shows that there is one Patient resource record in the BigQuery table, because you added the Patient resource after configuring streaming on the FHIR store.
         
         +-----+
         | f0_ |
         +-----+
         |   1 |
         +-----+
         




## Step 3: Export existing FHIR resources to BigQuery

If you have an existing FHIR store containing data that you want to sync with a BigQuery dataset, you must complete the following steps to ensure that the existing data is in BigQuery:

  1. Configure streaming to BigQuery.
  2. Export the existing data to the BigQuery dataset.



To export the two Patient resources that existed in the FHIR store before you configured streaming to the BigQuery dataset, complete the following steps:

  1. To export the resources in the FHIR store to BigQuery, run the [`gcloud healthcare fhir-stores export bq`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq) command. The command uses the `--write-disposition=write-append` flag, which appends data to the existing BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.`Patient` table.
         
         gcloud healthcare fhir-stores export bq FHIR_STORE_ID \
            --dataset=DATASET_ID \
            --location=LOCATION \
            --bq-dataset=bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET \
            --schema-type=analytics_v2 \
            --write-disposition=write-append

  2. Query the `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.Patient` table to verify the number of Patient resources in the BigQuery dataset:
         
         bq query \
            --project_id=BIGQUERY_PROJECT_ID \
            --use_legacy_sql=false \
            'SELECT COUNT(*) FROM `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.Patient`'

The query returns the following result, showing that there are 4 Patient resource records in the BigQuery table:
         
         +-----+
         | f0_ |
         +-----+
         |   4 |
         +-----+
         

The actual number of Patient resources in the BigQuery table is 3, but the query returns 4. Inconsistencies might occur when a resource contains duplicates from different operations. In this case, the first Patient resource was added to the BigQuery table these two times:

     * When the Patient resource creation was streamed
     * When the resources in the FHIR store were exported to BigQuery

The BigQuery table also contains a mutation history of the first Patient resource. For example, if you delete the Patient resource using [`fhir.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/delete), the BigQuery table has a `meta.tag.code` column with the value `DELETE`.

  3. To get the latest snapshot of the data in the FHIR store, query the [view](https://docs.cloud.google.com/bigquery/docs/views-intro). The Cloud Healthcare API constructs the view by only looking at the latest version of each resource. Querying views is the most accurate way to keep a FHIR store and its corresponding BigQuery table in sync.

To query the view, run the following command:
         
         bq query \
            --project_id=BIGQUERY_PROJECT_ID \
            --use_legacy_sql=false \
            'SELECT COUNT(*) FROM `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.PatientView`'

The query returns the following result, which correctly shows that there are 3 Patient resources in the BigQuery table:
         
         +-----+
         | f0_ |
         +-----+
         |   3 |
         +-----+
         




## Step 4: Stream resources from multiple FHIR stores to the same BigQuery dataset

In some cases, you might want to stream FHIR resources from multiple FHIR stores to the same BigQuery dataset to perform analytics on the aggregated FHIR resources from the FHIR stores.

In the following steps, you create a second FHIR store in the same Cloud Healthcare API dataset as the first FHIR store, but you can use FHIR stores from different datasets when aggregating FHIR resources.

  1. Create a second FHIR store with BigQuery streaming enabled and use the same BigQuery dataset that you used in Configure BigQuery streaming on the FHIR store.

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * SECOND_FHIR_STORE_ID: an identifier for the second FHIR store. The FHIR store ID must be unique in the dataset. The FHIR store ID can be any Unicode string from 1 through 256 characters consisting of numbers, letters, underscores, dashes, and periods.
     * FHIR_STORE_VERSION: the FHIR store version: DSTU2, STU3, or R4
     * BIGQUERY_PROJECT_ID: the Google Cloud project containing the BigQuery dataset for streaming FHIR resource changes
     * BIGQUERY_DATASET_ID: the BigQuery dataset where you are streaming FHIR resource changes

Request JSON body: 
    
    {
      "version": "FHIR_STORE_VERSION"
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS"
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "version": "FHIR_STORE_VERSION"
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS"
            }
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=SECOND_FHIR_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "version": "FHIR_STORE_VERSION"
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS"
            }
          }
        }
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=SECOND_FHIR_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/SECOND_FHIR_STORE_ID",
      "version": "VERSION",
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "ANALYTICS"
            }
          }
        }
      ]
    }
    

  2. Create a Patient resource in the second FHIR store:

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * SECOND_FHIR_STORE_ID: the second FHIR store ID

Request JSON body: 
    
    {
      "name": [
        {
          "use": "official",
          "family": "Lee",
          "given": [
            "Alex"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1990-01-01",
      "resourceType": "Patient"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "name": [
        {
          "use": "official",
          "family": "Lee",
          "given": [
            "Alex"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1990-01-01",
      "resourceType": "Patient"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/SECOND_FHIR_STORE_ID/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "name": [
        {
          "use": "official",
          "family": "Lee",
          "given": [
            "Alex"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "1990-01-01",
      "resourceType": "Patient"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/SECOND_FHIR_STORE_ID/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "birthDate": "1990-01-01",
      "gender": "male",
      "id": "PATIENT_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "name": [
        {
          "family": "Cruz",
          "given": [
            "Taylor"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

  3. Query the `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.Patient` table to verify the number of Patient resources in the BigQuery table:
         
         bq query \
            --project_id=BIGQUERY_PROJECT_ID \
            --use_legacy_sql=false \
            'SELECT COUNT(*) FROM `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.Patient`'

When streaming the data about the new Patient resource, BigQuery used the existing `Patient` table in the BigQuery dataset. The query returns the following result, showing that there are 5 Patient resource records in the BigQuery table. See Export existing FHIR resources to BigQuery for an explanation of why the table contains 5 resources instead of 4.
         
         +-----+
         | f0_ |
         +-----+
         |   5 |
         +-----+
         

  4. Run the following command to query the view:
         
         bq query \
            --project_id=BIGQUERY_PROJECT_ID \
            --use_legacy_sql=false \
            'SELECT COUNT(*) FROM `BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID.PatientView`'

The query returns the following result, showing that there are 4 Patient resources in the combined first and second FHIR stores and in the BigQuery table:
         
         +-----+
         | f0_ |
         +-----+
         |   4 |
         +-----+
         




## Clean up

**Note:** To avoid incurring charges for the resources that you created, you can delete them by following the instructions in this section.

If you created a new project for this tutorial, follow the steps in Delete the project. To only delete the Cloud Healthcare API and BigQuery resources, complete the steps in Delete the Cloud Healthcare API dataset and Delete the BigQuery dataset.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Cloud Healthcare API dataset

If you no longer need the Cloud Healthcare API dataset created in this tutorial, you can delete it. Deleting a dataset permanently deletes the dataset and any FHIR stores it contains.

  1. To delete a dataset, use the [`gcloud healthcare datasets delete`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/delete) command:
         
         gcloud healthcare datasets delete DATASET_ID \
         --location=LOCATION \
         --project=PROJECT_ID

Replace the following:

     * DATASET_ID: the Cloud Healthcare API dataset
     * LOCATION: the location of the dataset
     * PROJECT_ID: your Google Cloud project ID
  2. To confirm, type **Y**.




The output is the following:
    
    
    Deleted dataset [DATASET_ID].
    

### Delete the BigQuery dataset

If you no longer need the BigQuery dataset created in this tutorial, you can delete it. Deleting a dataset permanently deletes the dataset and any tables it contains.

  1. Remove the BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID dataset by running the [`bq rm`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_rm) command:
         
         bq rm --recursive=true BIGQUERY_PROJECT_ID.BIGQUERY_DATASET_ID

The `--recursive` flag deletes all tables in the dataset, including the `Patient` table.

  2. To confirm, type **Y**.




## What's next

  * If errors occur when streaming to BigQuery, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).
  * See an overview of [exporting FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).
  * To create, view, list, or delete FHIR stores, see [Creating and managing FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
