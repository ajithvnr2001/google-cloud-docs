---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-bigquery/
title: Connector for BigQuery \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:25.858087+00:00
---

# Connector for BigQuery  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access BigQuery within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the BigQuery connector:
    # Create a dataset and then insert a table with data from a public dataset
    # Delete both the table and dataset
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - dataset_id: "example_dataset"
          - table_id: "example_table"
          - query: "SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 5000;"
          - create_disposition: "CREATE_IF_NEEDED"  # creates table if it doesn't exist
          - write_disposition: "WRITE_TRUNCATE"  # truncates table if it already exists
    - create_dataset:
        call: googleapis.bigquery.v2.datasets.insert
        args:
          projectId: ${project_id}
          body:
            datasetReference:
              datasetId: ${dataset_id}
              projectId: ${project_id}
            access[].role: "roles/bigquery.dataViewer"
            access[].specialGroup: "projectReaders"
    - insert_table_into_dataset:
        call: googleapis.bigquery.v2.jobs.insert
        args:
          projectId: ${project_id}
          body:
            configuration:
              query:
                query: ${query}
                destinationTable:
                  projectId: ${project_id}
                  datasetId: ${dataset_id}
                  tableId: ${table_id}
                create_disposition: ${create_disposition}
                write_disposition: ${write_disposition}
                allowLargeResults: true
                useLegacySql: false
    - delete_table_from_dataset:
        call: googleapis.bigquery.v2.tables.delete
        args:
          projectId: ${project_id}
          datasetId: ${dataset_id}
          tableId: ${table_id}
    - delete_dataset:
        call: googleapis.bigquery.v2.datasets.delete
        args:
          projectId: ${project_id}
          datasetId: ${dataset_id}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
