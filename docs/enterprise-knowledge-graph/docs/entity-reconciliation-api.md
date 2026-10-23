---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/entity-reconciliation-api/
title: Manage entity reconciliation jobs with the API \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:40.119722+00:00
---

# Manage entity reconciliation jobs with the API  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/entity-reconciliation-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Manage entity reconciliation jobs with the API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this product as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This quickstart introduces you to the Entity Reconciliation API. In this quickstart, you use the Google Cloud console to set up your Google Cloud project and authentication, create schema mapping files, and then make a request for Enterprise Knowledge Graph to run an entity reconciliation job.

## Create an entity reconciliation job

Use the following steps to create an entity reconciliation job:

### REST

To create a simple job with one source table (deduplication), call the [`projects.locations.entityReconciliationJobs.create`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/create) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * DATASET_ID: ID of the BigQuery Dataset
  * TABLE_ID: ID of the BigQuery Table
  * MAPPING_FILE_URI: Cloud Storage path to a mapping file in YAML format. 
    * Example: `gs://ekg-test-gcs/mapping.yml`
  * ENTITY_TYPE: Entity Type for reconciliation.



HTTP method and URL: 
    
    
    POST https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs

Request JSON body: 
    
    
    {
      "inputConfig": {
        "bigqueryInputConfigs": [
          {
            "bigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID",
            "gcsUri": "MAPPING_FILE_URI"
          }
        ],
        "entityType": "ENTITY_TYPE"
      },
      "outputConfig": {
        "bigqueryDataset": "projects/PROJECT_ID/datasets/DATASET_ID"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID",
      "inputConfig": {
        "bigqueryInputConfigs": [
          {
            "bigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID",
            "gcsUri": "MAPPING_FILE_URI"
          }
        ],
        "entityType": "ENTITY_TYPE"
      },
      "outputConfig": {
        "bigqueryDataset": "projects/PROJECT_ID/datasets/DATASET_ID"
      },
      "state": "JOB_STATE_RUNNING",
      "createTime": "2021-07-31T14:39:14.145568Z",
      "updateTime": "2021-07-31T14:39:14.145568Z"
    }
    

To create a job with advanced options and multiple BigQuery tables, use a request body similar to this example: 
    
    
    {
      "inputConfig": {
        "bigqueryInputConfigs": [
          {
            "bigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID",
            "gcsUri": "MAPPING_FILE_URI"
          },
          {
            "bigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID",
            "gcsUri": "MAPPING_FILE_URI"
          }
        ],
        "entityType": "ENTITY_TYPE",
        "previousResultBigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/clusters_13689265293502324307"
      },
      "outputConfig": {
        "bigqueryDataset": "projects/PROJECT_ID/datasets/DATASET_ID"
      },
      "reconConfig": {
        "affinityClusteringConfig": {
          "compressionRoundCount": "2"
        },
        "options": {
          "enableGeocodingSeparation": true
        }
      }
    }
    

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'          # Values: 'global'
    # input_dataset = 'YOUR_INPUT_DATASET'      # BigQuery Dataset Name
    # input_table = 'YOUR_INPUT_TABLE'          # BigQuery Table Name
    # mapping_file_uri = 'YOUR_MAPPING_FILE     # GCS Path. Example: gs://ekg-test-gcs/mapping.yml
    # output_dataset = 'YOUR_OUTPUT_DATASET'    # BigQuery Dataset Name
    
    # Refer to https://cloud.google.com/enterprise-knowledge-graph/docs/schema
    # entity_type = ekg.InputConfig.EntityType.Person
    
    
    def create_entity_reconciliation_job_sample(
        project_id: str,
        location: str,
        input_dataset: str,
        input_table: str,
        mapping_file_uri: str,
        entity_type: int,
        output_dataset: str,
    ) -> None:
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the location
        # e.g. projects/{project_id}/locations/{location}
        parent = client.common_location_path(project=project_id, location=location)
    
        # Input Parameters
        input_config = ekg.InputConfig(
            bigquery_input_configs=[
                ekg.BigQueryInputConfig(
                    bigquery_table=client.table_path(
                        project=project_id, dataset=input_dataset, table=input_table
                    ),
                    gcs_uri=mapping_file_uri,
                )
            ],
            entity_type=entity_type,
        )
    
        # Output Parameters
        output_config = ekg.OutputConfig(
            bigquery_dataset=client.dataset_path(project=project_id, dataset=output_dataset)
        )
    
        entity_reconciliation_job = ekg.EntityReconciliationJob(
            input_config=input_config, output_config=output_config
        )
    
        # Initialize request argument(s)
        request = ekg.CreateEntityReconciliationJobRequest(
            parent=parent, entity_reconciliation_job=entity_reconciliation_job
        )
    
        # Make the request
        response = client.create_entity_reconciliation_job(request=request)
    
        print(f"Job: {response.name}")
        print(
            f"Input Table: {response.input_config.bigquery_input_configs[0].bigquery_table}"
        )
        print(f"Output Dataset: {response.output_config.bigquery_dataset}")
        print(f"State: {response.state.name}")
    
    

## Get an entity reconciliation job

### REST

To retrieve job status from the API, call the [`projects.locations.entityReconciliationJobs.get`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/get) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * JOB_ID: Entity Reconciliation Job ID. 
    * Example: `2628838070002699773`



HTTP method and URL: 
    
    
    GET https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID",
      "inputConfig": {
        "bigqueryInputConfigs": [
          {
            "bigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID",
            "gcsUri": "MAPPING_FILE_URI"
          }
        ],
        "entityType": "ENTITY_TYPE"
      },
      "outputConfig": {
        "bigqueryDataset": "projects/PROJECT_ID/datasets/DATASET_ID"
      },
      "state": "JOB_STATE_SUCCEEDED",
      "createTime": "2021-07-31T14:39:14.145568Z",
      "updateTime": "2021-07-31T14:39:14.145568Z"
    }
    

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'  # Values: 'global'
    # job_id = 'YOUR_JOB_ID'            # Entity Reconciliation Job ID
    
    
    def get_entity_reconciliation_job_sample(
        project_id: str, location: str, job_id: str
    ) -> None:
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the job
        # e.g. projects/{project_id}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}
        name = client.entity_reconciliation_job_path(
            project=project_id, location=location, entity_reconciliation_job=job_id
        )
    
        # Initialize request argument(s)
        request = ekg.GetEntityReconciliationJobRequest(name=name)
    
        # Make the request
        response = client.get_entity_reconciliation_job(request=request)
    
        print(f"Job: {response.name}")
        print(
            f"Input Table: {response.input_config.bigquery_input_configs[0].bigquery_table}"
        )
        print(f"Output Dataset: {response.output_config.bigquery_dataset}")
        print(f"State: {response.state.name}")
    
    

## List entity reconciliation jobs

### REST

To retrieve all the jobs from the API, call the [`projects.locations.entityReconciliationJobs.list`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint



HTTP method and URL: 
    
    
    GET https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entityReconciliationJobs": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID",
          "inputConfig": {
            "bigqueryInputConfigs": [
              {
                "bigqueryTable": "projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID",
                "gcsUri": "MAPPING_FILE_URI"
              }
            ],
            "entityType": "ENTITY_TYPE"
          },
          "outputConfig": {
            "bigqueryDataset": "projects/PROJECT_ID/datasets/DATASET_ID"
          },
          "state": "JOB_STATE_SUCCEEDED",
          "createTime": "2021-07-31T14:39:14.145568Z",
          "updateTime": "2021-07-31T14:39:14.145568Z"
        }
      ],
      "nextPageToken": ""
    }
    

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'  # Values: 'global'
    
    
    def list_entity_reconciliation_jobs_sample(project_id: str, location: str) -> None:
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the location
        # e.g. projects/{project_id}/locations/{location}
        parent = client.common_location_path(project=project_id, location=location)
    
        # Initialize request argument(s)
        request = ekg.ListEntityReconciliationJobsRequest(parent=parent)
    
        # Make the request
        pager = client.list_entity_reconciliation_jobs(request=request)
    
        for response in pager:
            print(f"Job: {response.name}")
            print(
                f"Input Table: {response.input_config.bigquery_input_configs[0].bigquery_table}"
            )
            print(f"Output Dataset: {response.output_config.bigquery_dataset}")
            print(f"State: {response.state.name}\n")
    
    

## Cancel an entity reconciliation job

### REST

To stop a running job from the API, call the [`projects.locations.entityReconciliationJobs.cancel`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/cancel) method.

Enterprise Knowledge Graph stops the job at the earliest opportunity. Note that canceling a job is on a best-efforts basis. The success of the `cancel` command isn't guaranteed.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * JOB_ID: Entity Reconciliation Job ID. 
    * Example: `2628838070002699773`



HTTP method and URL: 
    
    
    POST https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID:cancel

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID:cancel"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID:cancel" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'  # Values: 'global'
    # job_id = 'YOUR_JOB_ID'            # Entity Reconciliation Job ID
    
    
    def cancel_entity_reconciliation_job_sample(
        project_id: str, location: str, job_id: str
    ) -> None:
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the job
        # e.g. projects/{project_id}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}
        name = client.entity_reconciliation_job_path(
            project=project_id, location=location, entity_reconciliation_job=job_id
        )
    
        # Initialize request argument(s)
        request = ekg.CancelEntityReconciliationJobRequest(name=name)
    
        # Make the request
        client.cancel_entity_reconciliation_job(request=request)
    
        print(f"Job: {name} successfully cancelled")
    
    

## Delete an entity reconciliation job

### REST

To remove a completed or failed job with the API, call the [`projects.locations.entityReconciliationJobs.delete`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/delete) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * JOB_ID: Entity Reconciliation Job ID. 
    * Example: `2628838070002699773`



HTTP method and URL: 
    
    
    DELETE https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entityReconciliationJobs/JOB_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'  # Values: 'global'
    # job_id = 'YOUR_JOB_ID'            # Entity Reconciliation Job ID
    
    
    def delete_entity_reconciliation_job_sample(
        project_id: str, location: str, job_id: str
    ) -> None:
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the job
        # e.g. projects/{project_id}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}
        name = client.entity_reconciliation_job_path(
            project=project_id, location=location, entity_reconciliation_job=job_id
        )
    
        # Initialize request argument(s)
        request = ekg.DeleteEntityReconciliationJobRequest(name=name)
    
        # Make the request
        client.delete_entity_reconciliation_job(request=request)
    
        print(f"Job: {name} successfully deleted")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
