---
url: https://docs.cloud.google.com/composer/docs/composer-3/use-deferrable-operators/
title: Use deferrable operators in Airflow DAGs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:52.069194+00:00
---

# Use deferrable operators in Airflow DAGs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/use-deferrable-operators/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Use deferrable operators in Airflow DAGs Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page explains how to enable support for Deferrable Operators in your environment and use deferrable Google Cloud operators in your DAGs.

## About Deferrable Operators in Managed Airflow

If you have at least one triggerer instance (or at least two in [highly resilient environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments)), you can use [Deferrable Operators and Triggers](https://airflow.apache.org/docs/apache-airflow/stable/concepts/deferring.html) in your DAGs.

For deferrable operators, Airflow splits task execution into the following stages:

  1. Start the operation. In this stage, the task occupies an Airflow worker slot. The task performs an operation that delegates the job to a different service.

For example, running a BigQuery job can take from a few seconds to several hours. After creating the job, the operation passes the work identifier (BigQuery job ID) to an Airflow trigger.

  2. The trigger monitors the job until it finishes. In this stage, a worker slot is not occupied. The Airflow triggerer has asynchronous architecture and is capable of handling hundreds of such jobs. When the trigger detects that the job is finished, it sends an event that triggers the last stage.

  3. In the last stage, an Airflow worker executes a callback. This callback, for example, can mark the task as successful, or execute another operation and set the job to be monitored by the triggerer again.




The triggerer is stateless and therefore resilient to interruptions or restarts. Because of this, long-running jobs are resilient to pod restarts, unless the restart happens during the last stage, which is expected to be short.

## Before you begin

**Caution:** Terraform provider support for Airflow triggerers is in Preview. Use the `google-beta` Terraform provider when changing scale and performance parameters of your environment, even if these changes are not related to the triggerer. For example, when changing parameters for Airflow workers.

## Enable support for deferrable operators

An environment component called _Airflow triggerer_ asynchronously monitors all deferred tasks in your environment. After a deferred operation from such a task is completed, triggerer passes the task to an Airflow worker.

You need at least one triggerer instance in your environment (or at least two in highly resilient environments) to use deferrable mode in your DAGs. You can configure the triggerers [when you create an environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#scale-and-performance) or [adjust the number of triggerers and performance parameters for an existing environment](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#triggerer-parameters).

## Google Cloud operators that support deferrable mode

Only some Airflow operators have been extended to support the deferrable model. The following list is a reference for the operators in the [`apache-airflow-providers-google`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/) package that support the deferrable mode. The column with the minimum required `apache-airflow-providers-google` package version represents the earliest package version where that operator supports deferrable mode.

**Important:** The following tables **don't list every operator that supports deferrable mode**. Many other operators from `apache-airflow-providers-google` and other provider packages are supported by Airflow and Managed Airflow. These operators are not described on this page. To check if a particular operator supports deferrable mode, see its [Provider package documentation](https://airflow.apache.org/docs/#providers-packages-docs-apache-airflow-providers-index-html) provided by Airflow.**Note:** BigQuery operators in defferable mode **fail if the location is not set to US**. This happens because of [a bug](https://github.com/apache/airflow/issues/29307) in a dependency of Airflow, not in BigQuery operators.

### BigQuery operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[BigQueryCheckOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryCheckOperator) | 8.4.0  
[BigQueryValueCheckOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryValueCheckOperator) | 8.4.0  
[BigQueryIntervalCheckOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryIntervalCheckOperator) | 8.4.0  
[BigQueryGetDataOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryGetDataOperator) | 8.4.0  
[BigQueryInsertJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryInsertJobOperator) | 8.4.0  
  
### BigQuery Data Transfer Service operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[BigQueryDataTransferServiceStartTransferRunsOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery_dts/index.html#airflow.providers.google.cloud.operators.bigquery_dts.BigQueryDataTransferServiceStartTransferRunsOperator) | 8.9.0  
  
### Batch operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudBatchSubmitJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_batch/index.html#airflow.providers.google.cloud.operators.cloud_batch.CloudBatchSubmitJobOperator) | 10.7.0  
  
### Cloud Build operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudBuildCreateBuildOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_build/index.html#airflow.providers.google.cloud.operators.cloud_build.CloudBuildCreateBuildOperator) | 8.7.0  
  
### Managed Service for Apache Airflow operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudComposerCreateEnvironmentOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_composer/index.html#airflow.providers.google.cloud.operators.cloud_composer.CloudComposerCreateEnvironmentOperator) | 6.4.0  
[CloudComposerDeleteEnvironmentOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_composer/index.html#airflow.providers.google.cloud.operators.cloud_composer.CloudComposerDeleteEnvironmentOperator) | 6.4.0  
[CloudComposerUpdateEnvironmentOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_composer/index.html#airflow.providers.google.cloud.operators.cloud_composer.CloudComposerUpdateEnvironmentOperator) | 6.4.0  
[CloudComposerRunAirflowCLICommandOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_composer/index.html#airflow.providers.google.cloud.operators.cloud_composer.CloudComposerRunAirflowCLICommandOperator) | 11.0.0  
  
### Cloud Run operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudRunExecuteJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_run/index.html#airflow.providers.google.cloud.operators.cloud_run.CloudRunExecuteJobOperator) | 10.7.0  
  
### Cloud SQL operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudSQLExportInstanceOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_sql/index.html#airflow.providers.google.cloud.operators.cloud_sql.CloudSQLExportInstanceOperator) | 10.3.0  
  
### Storage Transfer Service operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudDataTransferServiceS3ToGCSOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_storage_transfer_service/index.html#airflow.providers.google.cloud.operators.cloud_storage_transfer_service.CloudDataTransferServiceS3ToGCSOperator) | 14.0.0  
[CloudDataTransferServiceGCSToGCSOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_storage_transfer_service/index.html#airflow.providers.google.cloud.operators.cloud_storage_transfer_service.CloudDataTransferServiceGCSToGCSOperator) | 14.0.0  
  
### Dataflow operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[DataflowTemplatedJobStartOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataflow/index.html#airflow.providers.google.cloud.operators.dataflow.DataflowTemplatedJobStartOperator) | 8.9.0  
[DataflowStartFlexTemplateOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataflow/index.html#airflow.providers.google.cloud.operators.dataflow.DataflowStartFlexTemplateOperator) | 8.9.0  
[DataflowStartYamlJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataflow/index.html#airflow.providers.google.cloud.operators.dataflow.DataflowStartYamlJobOperator) | 11.0.0  
  
### Cloud Data Fusion operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[CloudDataFusionStartPipelineOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/datafusion/index.html#airflow.providers.google.cloud.operators.datafusion.CloudDataFusionStartPipelineOperator) | 8.9.0  
  
### Knowledge Catalog operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[DataplexRunDataQualityScanOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataplex/index.html#airflow.providers.google.cloud.operators.dataplex.DataplexRunDataQualityScanOperator) | 10.8.0  
[DataplexGetDataQualityScanResultOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataplex/index.html#airflow.providers.google.cloud.operators.dataplex.DataplexGetDataQualityScanResultOperator) | 10.8.0  
[DataplexRunDataProfileScanOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataplex/index.html#airflow.providers.google.cloud.operators.dataplex.DataplexRunDataProfileScanOperator) | 11.0.0  
  
### Managed Service for Apache Spark operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[DataprocCreateClusterOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocCreateClusterOperator) | 8.9.0  
[DataprocDeleteClusterOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocDeleteClusterOperator) | 8.9.0  
[DataprocJobBaseOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocJobBaseOperator) | 8.4.0  
[DataprocInstantiateWorkflowTemplateOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocInstantiateWorkflowTemplateOperator) | 9.0.0  
[DataprocInstantiateInlineWorkflowTemplateOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocInstantiateInlineWorkflowTemplateOperator) | 10.1.0  
[DataprocSubmitJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocSubmitJobOperator) | 8.4.0  
[DataprocUpdateClusterOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocUpdateClusterOperator) | 8.9.0  
[DataprocDiagnoseClusterOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocDiagnoseClusterOperator) | 11.0.0  
[DataprocCreateBatchOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocCreateBatchOperator) | 8.9.0  
  
### Google Kubernetes Engine operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[GKEDeleteClusterOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/kubernetes_engine/index.html#airflow.providers.google.cloud.operators.kubernetes_engine.GKEDeleteClusterOperator) | 9.0.0  
[GKECreateClusterOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/kubernetes_engine/index.html#airflow.providers.google.cloud.operators.kubernetes_engine.GKECreateClusterOperator) | 9.0.0  
[GKEStartPodOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/kubernetes_engine/index.html#airflow.providers.google.cloud.operators.kubernetes_engine.GKEStartPodOperator) | 12.0.0  
[GKEStartJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/kubernetes_engine/index.html#airflow.providers.google.cloud.operators.kubernetes_engine.GKEStartJobOperator) | 11.0.0  
  
### Pub/Sub operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[PubSubPullOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/pubsub/index.html#airflow.providers.google.cloud.operators.pubsub.PubSubPullOperator) | 14.0.0  
  
### AI Platform operators

Operator name | Required `apache-airflow-providers-google` version  
---|---  
[MLEngineStartTrainingJobOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/mlengine/index.html#airflow.providers.google.cloud.operators.mlengine.MLEngineStartTrainingJobOperator) | 8.9.0  
  
## Use deferrable operators in your DAGs

A common convention for all Google Cloud operators is to enable the deferrable mode with the `deferrable` boolean parameter. If a Google Cloud operator does not have this parameter, then it cannot run in the deferrable mode. Other operators can have a different convention. For example, some community operators have a separate class with the `Async` suffix in the name.

**Important:** The `dags/` and `/plugins` folders from your environment bucket are not synchronized to the triggerer. You can use triggers that are installed with [PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies), or included in a preinstalled provider package.

The following example DAG uses `DataprocSubmitJobOperator` operator in the deferrable mode:
    
    
    PYSPARK_JOB = {
        "reference": { "project_id": "PROJECT_ID" },
        "placement": { "cluster_name": "PYSPARK_CLUSTER_NAME" },
        "pyspark_job": {
            "main_python_file_uri": "gs://dataproc-examples/pyspark/hello-world/hello-world.py"
        },
    }
    
    DataprocSubmitJobOperator(
            task_id="dataproc-deferrable-example",
            job=PYSPARK_JOB,
            deferrable=True,
        )
    

## View triggerer logs

The triggerer generates logs that are available together with logs of other environment components. For more information about viewing your environment logs, see [View logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs#streaming).

## Monitor triggerer

For more information about monitoring the triggerer component, see [Airflow metrics](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments#airflow-metrics).

In addition to monitoring the triggerer, you can check the number of deferred tasks in the **Unfinished Task** metrics on the Monitoring dashboard of your environment.

## What's next

  * [Troubleshooting Airflow triggerer issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-triggerer)
  * [Airflow triggerer metrics](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments#airflow-metrics)
  * [Airflow triggerer logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs#streaming)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
