---
url: https://docs.cloud.google.com/orchestration-pipelines/reference/orchestration-pipelines-dsl-reference/
title: Orchestration Pipelines DSL reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:02.796923+00:00
---

# Orchestration Pipelines DSL reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/reference/orchestration-pipelines-dsl-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Reference ](https://docs.cloud.google.com/orchestration-pipelines/apis)



Send feedback 

#  Orchestration Pipelines DSL reference Stay organized with collections  Save and categorize content based on your preferences. 

This page contains Orchestration Pipelines DSL reference.

## Limitations

Orchestration Pipelines has the following limitations:

  * For `pyspark` and `notebook` actions:

    * Only one `requirements.txt` file for all `pyspark` and `notebook` actions is supported.
    * Windows platform isn't supported for building packages through the `uv` tool.
    * Only Python packages with prebuilt binaries are supported.
  * For `sql` actions:

    * The `inline` definition in the `query` key isn't supported.



## About the format and values

Pipelines are defined in the YAML format, and must be stored in separate files, one per pipeline, in your repository.

Orchestration Pipelines provides several ways to use variables in your pipeline definitions and deployment configuration. For example, you can define custom variables, use GitHub secrets, and substitute variable values on the command-line. For more information, see [Variables, secrets, and substitution](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines#variables-secrets-substitution).

For more information about adding extra pipelines to the pipeline bundle, see [Add another pipeline](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines#add_another_pipeline).

## Code examples

The [orchestration-pipelines repository](https://github.com/GoogleCloudPlatform/orchestration-pipelines/tree/main/examples) on GitHub has the latest code examples for many pipeline actions and engines combinations. We recommend these examples as a starting point in exploring Orchestration Pipelines capabilities.

## Pipeline definition

**Note:** See [orchestration_pipeline.proto](https://github.com/GoogleCloudPlatform/orchestration-pipelines/blob/main/orchestration_pipelines_models/pipeline_v1_model/protos/orchestration_pipeline.proto) for the full proto definition file.

A pipeline definition has the following top-level keys:

  * `modelVersion`: The version of the pipeline definition model. The latest model version is `1.0`.

  * `pipelineId`: A unique identifier for the pipeline. This ID remains consistent across multiple deployments and versions, allowing for tracking and management of the logical pipeline entity.

  * `description`: Pipeline description, which is mapped to the description of the Airflow DAG in the runner environment.

  * `owner`: Owner of the pipeline. 

  * `tags`: String identifiers applied on the pipeline, used for filtering the pipelines.

  * `notifications`: notifications on pipeline events. Supported notification types:

    * `onPipelineFailure`: email on pipeline failures.

Notifications requires configured SendGrid email services in your runner environment. For instructions, see [Configure email notifications](https://docs.cloud.google.com/composer/docs/latest/configure-email#sendgrid).

Example:
    
    notifications:
      onPipelineFailure:
        email: ["user1@example.com", "user2@example.com"]
    

  * `runner`: Specifies the target orchestration engine. Reserved for future use. Set this value to `airflow`.

  * `defaults`: Sets default values for properties like `project_id`, `location`, and `executionConfig` that apply to all actions unless overridden within a specific action. The `project_id` and `location` properties can be overridden by individual action properties. The `executionConfig` property can't be overridden in individual actions and specifies the number of retries for all the actions in the pipeline in the `retries` field.

  * `triggers`: Defines how the pipeline is initiated:

    * No value. The pipeline can still be [triggered manually](https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines#deploy).

    * `schedule`. Trigger the pipeline on a schedule, using cron expressions.

Example schedule: 
          
          triggers:
            - schedule:
                interval: "0 5 * * *"
                startTime: "2025-10-01T00:00:00"
                endTime: "2026-10-01T00:00:00"
                catchup: false
                timezone: "UTC"
          

  * `actions`

A mapping of tasks to be executed. Each mapping entry corresponds to one action. See Actions.




## Actions

Pipeline actions define individual steps in pipeline execution. Each action must have an engine or a framework specified for it. Engine or framework determines which resources are used to execute the action.

Orchestration Pipelines supports the following actions:

  * Pyspark (`pyspark`): Run a PySpark script.
  * Notebook (`notebook`): Run a notebook file.
  * SQL query (`notebook`): Run a SQL query.
  * Python (`python`): Run a Python script.
  * Pipeline (`pipeline`): Execute a data processing pipelines.



Orchestration Pipelines supports the following engines and frameworks:

  * `dataprocOnGce` > `existingCluster`: [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters) identified by clusterName, project and location.

  * `dataprocOnGce` > `ephemeral`: [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters) created and deleted after executing the job.

  * `dataprocServerless`: Managed Service for Apache Spark [batch submission](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches).

  * `bigquery`: BigQuery [job](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/jobs).

  * `python` > `local`: Python script executed on an Airflow Worker in the runner environment.

  * `dbt` > `airflowWorker`: dbt models executed on an Airflow worker in the runner environment using [`dbt-core`](https://github.com/dbt-labs/dbt-core). 

  * `dataform` > `airflowWorker`: Dataform workflows executed on an Airflow worker in the runner environment using [dataform core cli](https://github.com/dataform-co/dataform).

  * `dataform` > `dataformService`: Dataform workflows executed on the [Dataform service](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations).




The following table lists possible action type, engine, and framework combinations. See engine and framework descriptions for action code examples.

Action | Engine or Framework | Outputs to  
---|---|---  
`pyspark` | `dataprocOnGce` > `existingCluster` | Managed Service for Apache Spark job logs  
`pyspark` | `dataprocOnGce` > `ephemeralCluster` | Managed Service for Apache Spark job logs  
`pyspark` | `dataprocServerless` | Managed Service for Apache Spark Batch logs  
`notebook` | `dataprocOnGce` > `existingCluster` | Runner bucket, under the `composer_declarative_dags_resources` directory  
`notebook` | `dataprocOnGce` > `ephemeralCluster` | Managed Service for Apache Spark job logs  
`notebook` | `dataprocServerless` | Runner bucket, under the `composer_declarative_dags_resources` directory  
`sql` | `bigquery` | Table specified in the `destinationTable` parameter  
`sql` | `dataprocServerless` | Managed Service for Apache Spark Batch logs.  
`python` | `local` (local execution) | Logs  
`pipeline` | `dbt` > `airflowWorker` | Logs and BigQuery  
`pipeline` | `dataform` > `airflowWorker` | Specified table in BigQuery  
`pipeline` | `dataform` > `dataformService` | In Dataform  
  
All action have the following common keys. Other keys depend on the action type.

  * `name`: Action name. This name is mapped to the Airflow task name in the runner environment. If an action requires more than one Airflow task, this name is mapped to the task group.

  * `dependsOn`: A list of upstream action names that this action depends on, defining the execution order. If any of the upstream actions fail, the downstream actions that depend on them aren't executed.

  * `executionTimeout`: Timeout to execute the action. Examples: `1h`, `30m`, `40s`.




### python

Actions of `python` type. Execute Python scripts.

Action type-specific keys:

  * `mainFilePath`: relative path to the Python script file.
  * `pythonCallable`: name of the Python callable to execute in the Python script.
  * `opKwargs`: a mapping of keyword arguments for the operator.
  * (Optional) `environment`: execute the script within a dynamically created Python Virtual Environment.

    * `requirements`: requirements for the Virtual Environment. The requirements are resolved at runtime.

      * `inline`: requirements are specified inline.

        * `list`: list of requirements. List individual requirements according to [PEP-508](https://www.python.org/dev/peps/pep-0508/#grammar).

Example:
              
              environment:
                requirements:
                  inline:
                    list: ["pandas>=2.0.0"]
              

      * (Alternative) `path`: Path to the file with requirements. Requirements in this file must be listed according to [PEP-508](https://www.python.org/dev/peps/pep-0508/#grammar).

Example:
            
            environment:
              requirements:
                path: "scripts/requirements.txt"
            

    * `systemSitePackages`: If `true`, the Virtual Environment inherits packages from the site-packages directory of the Airflow worker. You can [install custom PyPI packages](https://docs.cloud.google.com/composer/docs/latest/install-python-dependencies) in your runner environment. 

  * `engine`:

    * `local`: local execution at the runner environment



Example:

###  local 
    
    
    modelVersion: "1.0"
    pipelineId: "python-virtual-env"
    description: "A pipeline that runs Python script on isolated virtual environment with specified dependencies."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["python_virtual_environment", "example"]
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 1
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - python:
          name: "first_script_run"
          executionTimeout: "30m"
          mainFilePath: "scripts/venv_test_script_1.py"
          pythonCallable: "main"
          engine:
            local: {}
          environment:
            systemSitePackages: true
            requirements:
              path: "scripts/requirements.txt"
    
      - python:
          name: "second_script_run"
          executionTimeout: "30m"
          mainFilePath: "scripts/venv_test_script_1.py"
          pythonCallable: "main"
          engine:
            local: {}
          environment:
            requirements:
              inline:
                list: ["pandas>=2.0.0"]
            systemSitePackages: true
          dependsOn: ["first_script_run"]
    
      - python:
          name: "third_script_run"
          executionTimeout: "30m"
          mainFilePath: "scripts/venv_test_script_2.py"
          pythonCallable: "main"
          engine:
            local: {}
          opKwargs:
            api_endpoint: "https://api.my-vendor.example.com/v1/status"
            api_key_secret_name: "my-vendor-api-key"
          dependsOn: ["first_script_run"]
    

### pyspark

Actions of `pyspark` type. Execute PySpark scripts.

Action type-specific keys:

  * `mainFilePath`: Relative path to the PySpark script.
  * `archiveUris`: A list of archive URIs to use with this action. 
  * `stagingBucket`: Cloud Storage bucket to use with this action.
  * `pyFiles`: A list of Python files to use with this Spark job.
  * `environment`: Python environment configuration.

    * `requirements`: Python requirements file to use.

**Important:** This feature has limitations. For details, see Limitations.
      * `path`: Path to the file with requirements. Requirements in this file must be listed according to [PEP-508](https://www.python.org/dev/peps/pep-0508/#grammar).
  * `engine`:

    * `dataprocOnGce` > `existingCluster`
    * `dataprocOnGce` > `ephemeralCluster`
    * `dataprocServerless`



Examples:

###  existingCluster 
    
    
    modelVersion: "1.0"
    pipelineId: "dataproc-existing-cluster-script-pipeline-pyfiles"
    description: "A pipeline with a Dataproc Existing cluster running a PySpark task with additional python files."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc_create_batch", "example", "pyfiles"]
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    triggers:
      - schedule:
          interval: "0 4 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    actions:
      - pyspark:
          name: "run-pyspark-with-pyfiles-on-existing-cluster"
          engine:
            dataprocOnGce:
              existingCluster:
                clusterName: "example-dataproc-cluster"
                location: "us-central1"
                projectId: "example-project"
                impersonationChain: "example-account@example-project.iam.gserviceaccount.com"
          mainFilePath: "scripts/my_spark_job_with_pyfiles.py"
          pyFiles:
            - "data/lib1.py"
    

###  ephemeralCluster 
    
    
    pipelineId: "dataproc-ephemeral-inline-pyspark"
    description: "A pipeline with a Dataproc Ephemeral cluster running the PySpark task."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc_create_batch", "example"]
    modelVersion: "1.0"
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - pyspark:
          name: "run_dataproc_ephemeral"
          executionTimeout: "1h"
          mainFilePath: "scripts/my_spark_job_with_pyfiles.py"
          pyFiles:
            - "data/lib1.py"
          engine:
            dataprocOnGce:
              ephemeralCluster:
                projectId: "example-project"
                location: "us-central1"
                clusterName: "ephemeral-cluster-inline"
                resourceProfile:
                  inline:
                    config:
                      masterConfig:
                        numInstances: 1
                        machineTypeUri: "n1-standard-4"
                        diskConfig:
                          bootDiskType: "pd-standard"
                          bootDiskSizeGb: 1024
                      workerConfig:
                        numInstances: 2
                        machineTypeUri: "n1-standard-4"
                        diskConfig:
                          bootDiskType: "pd-standard"
                          bootDiskSizeGb: 1024
                properties:
                  spark.submit.deployMode: "cluster"
    

###  dataprocServerless 
    
    
    modelVersion: "1.0"
    pipelineId: "dataproc-create-batch-pipeline-pyspark"
    description: "A pipeline with a Batch task."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc_create_batch", "example"]
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    actions:
      - pyspark:
          name: "run-pyspark-on-dataproc-serverless"
          mainFilePath: "scripts/my_spark_job_with_pyfiles.py"
          pyFiles:
            - "data/lib1.py"
          engine:
            dataprocServerless:
              location: "us-central1"
              resourceProfile:
                inline:
                  environmentConfig:
                    executionConfig:
                      serviceAccount: "example-account@example-project.iam.gserviceaccount.com"
                      networkUri: "projects/example-project/global/networks/default"
                  runtimeConfig:
                    version: "2.3"
                    properties:
                      spark.app.name: "run-notebook-on-dataproc-serverless"
                      spark.executor.instances: "2"
                      spark.driver.cores: "4"
    

### notebook

Actions of `notebook` type. Execute an .ipynb notebook through Papermill.

Action type-specific keys:

  * `mainFilePath`: relative path to the notebook file.
  * `archiveUris`: A list of archive URIs to use with this action. 
  * `stagingBucket`: Cloud Storage bucket to use with this action.
  * `environment`: Python environment configuration.

    * `requirements`: Python requirements file to use.

**Important:** This feature has limitations. For details, see Limitations.
      * `path`: Path to the file with requirements. Requirements in this file must be listed according to [PEP-508](https://www.python.org/dev/peps/pep-0508/#grammar).
  * `engine`:

    * `dataprocOnGce` > `existingCluster`
    * `dataprocOnGce` > `ephemeralCluster`
    * `dataprocServerless`



Example:

###  dataprocServerless 
    
    
    modelVersion: "1.0"
    pipelineId: "dataproc-create-batch-pipeline-resource-profile-gcs-overrides"
    description: "A pipeline with a DataprocCreateBatch task."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc_create_batch", "example"]
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - notebook:
          name: "run-notebook-on-dataproc-serverless"
          mainFilePath: "scripts/notebookWithArchivesCheck.ipynb"
          archiveUris:
            - "gs://example-bucket-additional-data/custom_venv.tar.gz"
          staging_bucket: "example-bucket-additional-data-additional-data"
          engine:
            dataprocServerless:
              location: "us-central1"
              resourceProfile:
                externalConfigPath: "gs://example-runner-bucket/data/batch-resource-profile.yml"
                overrides:
                  runtimeConfig:
                    properties:
                      spark.app.name: "run-notebook-on-dataproc-serverless"
                      spark.executor.instances: "2"
                      spark.driver.cores: "4"
    

### sql

Actions of `sql` type. Execute SQL queries.

Action type-specific keys:

  * `query`: defines a query.

    * `path`: the query is defined in a file located at the relative path to the deployment configuration file.
    * `inline`: the query is defined inline.

**Important:** This feature has limitations. For details, see Limitations.
  * `engine`:

    * `bigQuery`
    * `dataprocServerless`
    * `dataprocOnGce` > `existingCluster`
    * `dataprocOnGce` > `ephemeralCluster`



###  bigQuery 
    
    
    modelVersion: "1.0"
    pipelineId: "sql-on-bigquery"
    description: "A pipeline with a BigQueryInsertJob task."
    runner: "airflow"
    tags: ["bigquery", "example"]
    owner: "data-eng-team"
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - sql:
          name: "run_bigquery_insert_job_create"
          query:
            inline: "CREATE TABLE IF NOT EXISTS `example-project.example_dataset.example_table` (id INT64, name STRING, timestamp TIMESTAMP );"
          engine:
            bigquery:
              location: "US"
      - sql:
          name: "run_bigquery_insert_job_select"
          query:
            path: "sql-scripts/count_rows.sql"
          engine:
            bigquery:
              location: "US"
              destinationTable: "example-project.example_dataset.example_table_query_results"
          dependsOn:
            - "run_bigquery_insert_job_create"
    

###  dataprocServerless 
    
    
    modelVersion: "1.0"
    pipelineId: "sql-on-dataproc-serverless"
    description: "A pipeline with a cluster running the PySpark task."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc-serverless", "example"]
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - sql:
          name: "run-sql-on-dataproc"
          query:
            path: "sql-scripts/test_query.sql"
          engine:
            dataprocServerless:
              location: "us-central1"
              impersonationChain: "example-account@example-project.iam.gserviceaccount.com"
              resourceProfile:
                inline:
                  runtimeConfig:
                    properties:
                      spark.sql.catalog.bigquery: "com.google.cloud.spark.bigquery.BigQueryCatalog"
                      spark.sql.catalog.bigquery.project: "example-project"
                      dataproc.sparkBqConnector.version: "0.42.3"
    

###  existingCluster 
    
    
    modelVersion: "1.0"
    pipelineId: "sql-on-dataproc-gce-existing"
    description: "A pipeline running a SQL query on an existing Dataproc cluster."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc-gce", "example", "existing-cluster"]
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - sql:
          name: "run-sql-on-existing-cluster"
          query:
            path: "sql-scripts/test_query.sql"
          engine:
            dataprocOnGce:
              existingCluster:
                clusterName: "cluster-sql"
                projectId: "example-project"
                location: "us-central1"
                impersonationChain: "example-account@example-project.iam.gserviceaccount.com"
                properties:
                  spark.sql.catalog.bigquery: "com.google.cloud.spark.bigquery.BigQueryCatalog"
                  spark.sql.catalog.bigquery.project: "example-project"
                  # This field is needed and important for the Spark-BigQuery connector.
                  spark.jars: "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.42.3.jar"
    

###  ephemeralCluster 
    
    
    modelVersion: "1.0"
    pipelineId: "sql-on-dataproc-gce-ephemeral"
    description: "A pipeline running a SQL query on an ephemeral Dataproc cluster."
    runner: "airflow"
    owner: "data-eng-team"
    tags: ["dataproc-gce", "example", "ephemeral-cluster"]
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    
    actions:
      - sql:
          name: "run-sql-on-ephemeral-cluster"
          query:
            path: "sql-scripts/test_query.sql"
          engine:
            dataprocOnGce:
              ephemeralCluster:
                clusterName: "example-ephemeral-cluster"
                projectId: "example-project"
                location: "us-central1"
                impersonationChain: "example-account@example-project.iam.gserviceaccount.com"
                properties:
                  spark.sql.catalog.bigquery: "com.google.cloud.spark.bigquery.BigQueryCatalog"
                  spark.sql.catalog.bigquery.project: "example-project"
                  # This field is needed and important for the Spark-BigQuery connector.
                  spark.jars: "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.42.3.jar"
                resourceProfile:
                  inline:
                    clusterConfig:
                      gceClusterConfig:
                        zoneUri: "us-central1-a"
                        metadata: # This metadata field is needed and important for the Spark-BigQuery connector.
                          SPARK_BQ_CONNECTOR_URL: "gs://spark-lib/bigquery/spark-3.5-bigquery-0.43.1.jar"
                      masterConfig:
                        numInstances: 1
                        machineTypeUri: "n1-standard-4"
                      workerConfig:
                        numInstances: 2
                        machineTypeUri: "n1-standard-4"
    

### pipeline

Actions of `pipeline` type. Execute a data processing pipeline.

Action type-specific keys:

  * `framework`:

    * `dbt`
    * `dataform` > `airflowWorker`
    * `dataform` > `dataformService`



Examples:

###  dbt 
    
    
    modelVersion: "1.0"
    pipelineId: "dbt-pipeline"
    description: "A pipeline that runs a dbt workflow."
    runner: "airflow"
    owner: "example-owner"
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    actions:
      - pipeline:
          name: "dbt-action"
          framework:
            dbt:
              airflowWorker:
                projectDirectoryPath: "dbt_project"
                selectModels: ["model_1", "model_2"]
    

###  dataform>airflowWorker 
    
    
    modelVersion: "1.0"
    pipelineId: "dataform-pipeline-local"
    description: "A pipeline that runs a Dataform workflow."
    runner: "airflow"
    owner: "example-owner"
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    triggers:
      - schedule:
          interval: "0 5 * * *"
          startTime: "2025-10-01T00:00:00"
          endTime: "2026-10-01T00:00:00"
          catchup: false
          timezone: "UTC"
    actions:
      - pipeline:
          name: "run_dataform"
          framework:
            dataform:
              airflowWorker:
                projectDirectoryPath: "dataform_local"
    

###  dataform>dataformService 
    
    
    modelVersion: "1.0"
    pipelineId: dataform-service
    description: "A pipeline that runs a Dataform workflow."
    owner: "example-owner"
    tags: ["dataform", "example"]
    runner: "airflow"
    
    defaults:
      projectId: "example-project"
      location: "us-central1"
      executionConfig:
        retries: 0
    
    actions:
      - pipeline:
          name: "run_dataform"
          framework:
            dataform:
              dataformService:
                location: "us-central1"
                projectId: "example-project"
                repositoryId: "example-repository"
                workflowInvocation:
                  workflowConfig: "projects/example-project/locations/us-central1/repositories/example-repository/workflowConfigs/example-test"
    
      - pipeline:
          name: "run_dataform_compilation"
          framework:
            dataform:
              dataformService:
                location: "us-central1"
                projectId: "example-project"
                repositoryId: "example-repository"
                workflowInvocation:
                  compilationResult: "projects/example-project/locations/us-central1/repositories/tets/compilationResults/8027975f-9692-42da-a13b-2267a4909f76"
                  invocationConfig:
                    serviceAccount: "example-account@example-project.iam.gserviceaccount.com"
    

## Engines

Engines used in actions.

### dataprocOnGce > existingCluster

Execute in an existing [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters) identified by clusterName, project and location.

You can manage the specified cluster in your [deployment configuration](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines), or manually in Managed Service for Apache Spark. We recommend to keep the cluster regularly upgraded.

Keys:

  * `clusterName`: Name of the cluster
  * `location`: Region where the cluster is located
  * `projectId`: Project ID of the project where the cluster is located
  * `properties`: A map of [Spark job properties](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/PySparkJob).



Example:
    
    
    engine:
      dataprocOnGce:
        existingCluster:
          clusterName: "example-dataproc-cluster"
          location: "us-central1"
          projectId: "example-project"
          impersonationChain: "example-account@example-project.iam.gserviceaccount.com"
    

### dataprocOnGce > ephemeralCluster

Execute in an ephemeral [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters), which is created and deleted after executing the job.

Keys:

  * `clusterName`: Name of the cluster
  * `location`: Region where the cluster is located
  * `projectId`: Project ID of the project where the cluster is located
  * `impersonationChain`: [service account impersonation chain](https://docs.cloud.google.com/iam/docs/service-account-impersonation) to use for running the action.
  * `resourceProfile`: Managed Service for Apache Spark cluster resource profile.

For the description of available fields, see [ClusterConfig](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/ClusterConfig) in the Managed Service for Apache Spark documentation.

A resource profile can be specified in the following ways:

    * `inline`: defined as a part of the pipeline configuration.
    * `path`: defined in a file located at the relative path.
    * `external_config_path`: defined in a file located in a Cloud Storage bucket. Unlike `inline` and `path` options, which require committing and deploying to update resource profile values, an external resource profile is resolved at each pipeline run and you can update it without re-deploying the pipeline.

Overrides can be applied to the specified resource profile with the `override` key. Overrides are applied with deep merge onto the provided presource profile. 

  * `properties`: A map of [Spark job properties](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/PySparkJob).




Example:
    
    
    engine:
      dataprocOnGce:
        ephemeralCluster:
          projectId: "example-project"
          location: "us-central1"
          clusterName: "example-ephemeral-cluster"
          resourceProfile:
            inline:
              config:
                masterConfig:
                  numInstances: 1
                  machineTypeUri: "n1-standard-4"
                  diskConfig:
                    bootDiskType: "pd-standard"
                    bootDiskSizeGb: 1024
                workerConfig:
                  numInstances: 2
                  machineTypeUri: "n1-standard-4"
                  diskConfig:
                    bootDiskType: "pd-standard"
                    bootDiskSizeGb: 1024
          properties:
            spark.submit.deployMode: "cluster"
    

### dataprocServerless

Execute in Managed Service for Apache Spark [batch submission](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches).

Keys:

  * `location`: Region where the Spark job must be executed.
  * `impersonationChain`: [service account impersonation chain](https://docs.cloud.google.com/iam/docs/service-account-impersonation) to use for running the action.
  * `resourceProfile`: Managed Service for Apache Spark resource profile.

A resource profile can be specified in the following ways:

    * `inline`: defined as a part of the pipeline configuration.
    * `path`: defined in a file located at the relative path.
    * `external_config_path`: defined in a file located in a Cloud Storage bucket. Unlike `inline` and `path` options, which require committing and deploying to update resource profile values, an external resource profile is resolved at each pipeline run and you can update it without re-deploying the pipeline.

The following keys specify the resource profile configuration:

    * `environmentConfig`: environment configuration
    * `runtimeConfig`: runtime configuration

For the description of available fields, see [RuntimeConfig](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/RuntimeConfig) and [EnvironmentConfig](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/EnvironmentConfig) in the Managed Service for Apache Spark documentation.

Overrides can be applied to the specified resource profile with the `override` key. Overrides are applied with deep merge onto the provided resource profile.




Example (inline):
    
    
    engine:
      dataprocServerless:
        location: "us-central1"
        resourceProfile:
          inline:
            environmentConfig:
              executionConfig:
                serviceAccount: "example-account@example-project.iam.gserviceaccount.com"
                networkUri: "projects/example-project/global/networks/default"
            runtimeConfig:
              version: "2.3"
              properties:
                spark.app.name: "run-notebook-on-dataproc-serverless"
                spark.executor.instances: "2"
                spark.driver.cores: "4"
    

Example (external path and overrides):
    
    
          engine:
            dataprocServerless:
              location: "us-central1"
              resourceProfile:
                externalConfigPath: "gs://example-runner-bucket/data/batch-resource-profile.yml"
                overrides:
                  runtimeConfig:
                    properties:
                        spark.app.name: "run-notebook-on-dataproc-serverless"
                        spark.executor.instances: "2"
                        spark.driver.cores: "4"
    

### bigQuery

Execute as a BigQuery [job](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/jobs).

Keys:

  * `location`: Region where the destination table is located. 
  * `destinationTable`: BigQuery table to output the data
  * `impersonationChain`: [service account impersonation chain](https://docs.cloud.google.com/iam/docs/service-account-impersonation) to use for running the action.



Example:
    
    
          engine:
            bigquery:
              location: "US"
              destinationTable: "example-project.example_dataset.example_table_query_results"
    

### local

Execute locally in the runner environment.

See the `python` action for ways to configure the Virtual Environment.

Example:
    
    
        engine:
          local: {}
    

## Frameworks

Frameworks used in actions.

### dbt > airflowWorker

Execute a dbt model executed on an Airflow worker in the runner environment using [`dbt-core`](https://github.com/dbt-labs/dbt-core).

Keys:

  * `projectDirectoryPath`: Relative path to a folder that contains the DBT project.
  * `selectModels`: List of models to include in the run by name (equivalent to `dbt --select`).
  * `tags`: List of models to include in the run by tag (equivalent to `dbt --select`).



Example:
    
    
    framework:
      dbt:
        airflowWorker:
          projectDirectoryPath: "dbt_project"
          selectModels: ["model_1", "model_2"]
    

### dataform > airflowWorker

Dataform workflows executed on an Airflow worker in the runner environment using [dataform core cli](https://github.com/dataform-co/dataform).

Keys:

  * `projectDirectoryPath`: Relative path to a folder that contains the Dataform workflow definitions. 



Example:
    
    
    framework:
      dataform:
        airflowWorker:
          projectDirectoryPath: "dataform_local"
    

### dataform > dataformService

Runs Dataform workflows executed on the [Dataform service](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations).

Keys:

  * `location`: Location where the Dataform repository is located. 
  * `projectId`: Project where the Dataform repository is located.
  * `repositoryId`: Dataform repository ID
  * `workflowInvocation`: Configuration for the workflow invocation, which specifies which actions to run. See [WorkflowInvocation](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowInvocation).



Example:
    
    
    framework:
      dataform:
        dataformService:
          location: "us-central1"
          projectId: "example-project"
          repositoryId: "example-repository"
          workflowInvocation:
            compilationResult: "projects/example-project/locations/us-central1/repositories/example-repository/compilationResults/example-compilation-id"
            invocationConfig:
              serviceAccount: "example-account@example-project.iam.gserviceaccount.com"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
