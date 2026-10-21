---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-bigquerydatatransfer/
title: Connector for BigQuery Data Transfer \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:25.575052+00:00
---

# Connector for BigQuery Data Transfer  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-bigquerydatatransfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for BigQuery Data Transfer Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access BigQuery Data Transfer within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery Data Transfer API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/Overview)



## Code sample

### YAML
    
    
    # This workflow creates a new dataset and a new table inside that dataset, which are required
    # for the BigQuery Data Transfer Job to run. It creates a new TransferJob configuration and starts
    # a manual run of the transfer (30 seconds after the config is created).
    # The transferRun is a blocking LRO.
    # All resources get deleted once the transfer run completes.
    #
    # On success, it returns "SUCCESS".
    #
    # Features included in this test:
    # - BigQuery Data Transfer connector
    # - Waiting for long-running transfer run to complete
    #
    # This workflow expects following items to be provided through input argument for execution:
    #   - projectID (string)
    #     - The user project ID.
    #   - datasetID (string)
    #     - The dataset name, expected to have an unique value to avoid the
    #       instance being referred by multiple tests.
    #   - tableID (string)
    #     - The table name, expected to have an unique value to avoid the
    #       instance being referred by multiple tests.
    #   - runConfigDisplayName (string)
    #     - The transfer run configuration display name.
    #
    # Expected successful output: "SUCCESS"
    main:
      params: [args]
      steps:
        - init:
            assign:
              - project_id: ${args.projectID}
              - destination_dataset: ${args.datasetID}
              - destination_table: ${args.tableID}
              - run_config_display_name: ${args.runConfigDisplayName}
              - run_config_data_source_id: "google_cloud_storage"
              - location: "us"
              - data_path_template: "gs://xxxxxx-bucket/xxxxx/xxxx"
        - create_dataset:
            call: googleapis.bigquery.v2.datasets.insert
            args:
              projectId: ${project_id}
              body:
                datasetReference:
                  datasetId: ${destination_dataset}
                  projectId: ${project_id}
        - create_table:
            call: googleapis.bigquery.v2.tables.insert
            args:
              datasetId: ${destination_dataset}
              projectId: ${project_id}
              body:
                tableReference:
                  datasetId: ${destination_dataset}
                  projectId: ${project_id}
                  tableId: ${destination_table}
                schema:
                  fields:
                    - name: "column1"
                      type: "STRING"
                    - name: "column2"
                      type: "STRING"
        - list_config:
            call: googleapis.bigquerydatatransfer.v1.projects.locations.transferConfigs.list
            args:
              parent: ${"projects/" + project_id + "/locations/us"}
        - create_run_config:
            call: googleapis.bigquerydatatransfer.v1.projects.locations.transferConfigs.create
            args:
              parent: ${"projects/" + project_id + "/locations/" + location}
              body:
                displayName: ${run_config_display_name}
                schedule: "every day 19:22"
                scheduleOptions:
                  disableAutoScheduling: true
                destinationDatasetId: ${destination_dataset}
                dataSourceId: ${run_config_data_source_id}
                params:
                  destination_table_name_template: ${destination_table}
                  file_format: "CSV"
                  data_path_template: ${data_path_template}
            result: config
        - get_time_in_30s:
            assign:
              - now_plus_30s: ${time.format(sys.now() + 30)}
        - start_run:
            call: googleapis.bigquerydatatransfer.v1.projects.locations.transferConfigs.startManualRuns
            args:
              parent: ${config.name}
              body:
                requestedRunTime: ${now_plus_30s}
            result: runsResp
        - remove_run_config:
            call: googleapis.bigquerydatatransfer.v1.projects.locations.transferConfigs.delete
            args:
              name: ${config.name}
        - delete_table:
            call: googleapis.bigquery.v2.tables.delete
            args:
              datasetId: ${destination_dataset}
              projectId: ${project_id}
              tableId: ${destination_table}
        - delete_dataset:
            call: googleapis.bigquery.v2.datasets.delete
            args:
              projectId: ${project_id}
              datasetId: ${destination_dataset}
        - the_end:
            return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
