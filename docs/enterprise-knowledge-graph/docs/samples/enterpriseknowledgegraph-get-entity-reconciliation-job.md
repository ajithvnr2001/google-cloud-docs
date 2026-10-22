---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples/enterpriseknowledgegraph-get-entity-reconciliation-job/
title: Get an entity reconciliation job \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:30.139902+00:00
---

# Get an entity reconciliation job  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples/enterpriseknowledgegraph-get-entity-reconciliation-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Samples ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples)



#  Get an entity reconciliation job Stay organized with collections  Save and categorize content based on your preferences. 

Get details about an entity reconciliation job.

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=enterpriseknowledgegraph). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
