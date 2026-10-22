---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples/enterpriseknowledgegraph-create-entity-reconciliation-job/
title: Create an entity reconciliation job \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:22.568734+00:00
---

# Create an entity reconciliation job  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples/enterpriseknowledgegraph-create-entity-reconciliation-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Samples ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples)



#  Create an entity reconciliation job Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new entity reconciliation job.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage entity reconciliation jobs with the API](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/entity-reconciliation-api)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=enterpriseknowledgegraph). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
