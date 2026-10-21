---
url: https://docs.cloud.google.com/composer/docs/composer-3/run-dataproc-workloads/
title: Run Managed Service for Apache Spark workloads with Managed Airflow \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:48.845998+00:00
---

# Run Managed Service for Apache Spark workloads with Managed Airflow  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/run-dataproc-workloads/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Run Managed Service for Apache Spark workloads with Managed Airflow Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/run-dataproc-workloads "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page describes how to use Managed Airflow (Gen 2) to run [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/overview) workloads on Google Cloud.

Examples in the following sections show you how to use [operators for managing Managed Service for Apache Spark batch workloads](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataproc.html#create-a-batch). You use these operators in DAGs that create, delete, list, and get a Managed Service for Apache Spark batch workload:

  * Create DAGs for [operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataproc.html#create-a-batch) that work with Managed Service for Apache Spark batch workloads:

    * DataprocCreateBatchOperator
    * DataprocDeleteBatchOperator
    * DataprocListBatchesOperator
    * DataprocGetBatchOperator
  * Create DAGs that use [custom containers](https://docs.cloud.google.com/dataproc-serverless/docs/guides/custom-containers), and [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview).

  * Configure [Persistent History Server](https://docs.cloud.google.com/dataproc/docs/concepts/jobs/history-server) for these DAGs.




## Before you begin

  1. Enable the Dataproc API:

###  Console 

Enable the Managed Service for Apache Spark API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

###  gcloud 

Enable the Managed Service for Apache Spark API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataproc.googleapis.com

  2. Select the location for your batch workload file. You can use any of the following options:

     * [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) that stores this file.
     * Use your environment's bucket. Because you do not need to sync this file with Airflow, you can create a separate subfolder outside the `/dags` or `/data` folders. For example, `/batches`.
     * Use an existing bucket.



## Set up files and Airflow variables

This section demonstrates how to set up files and configure Airflow variables for this tutorial.

### Upload a Managed Service for Apache Spark ML workload file to a bucket

The workload in this tutorial runs a pyspark script:

  1. Save any pyspark script to a local file named `spark-job.py`. For example, you can use the [sample pyspark script](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/dataproc/snippets/pyspark_sort.py).

  2. [Upload the file](https://docs.cloud.google.com/storage/docs/uploading-objects) to the location that you selected in Before you begin.




### Set Airflow variables

Examples in the following sections use Airflow variables. You set values for these variables in Airflow, then your DAG code can access these values.

Examples in this tutorial use the following Airflow variables. You can set them as needed, depending on the example you use.

Set the following Airflow variables for use in your DAG code:

  * `project_id`: [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `bucket_name`: URI of a bucket where the main python file of the workload (`spark-job.py`) is located. You selected this location in Before you begin.
  * `phs_cluster`: Persistent History Server cluster name. You set this variable when you Create a Persistent History Server.
  * `image_name`: name and tag of the custom container image (`image:tag`). You set this variable when you use custom container image with DataprocCreateBatchOperator.
  * `metastore_cluster`: Dataproc Metastore service name. You set this variable when you use Dataproc Metastore service with DataprocCreateBatchOperator.
  * `region_name`: region where the Dataproc Metastore service is located. You set this variable when you use Dataproc Metastore service with DataprocCreateBatchOperator.



**Use the Google Cloud console and Airflow UI to set each Airflow variable**

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the **Airflow** link for your environment. Airflow UI opens.

  3. In Airflow UI, select **Admin** > **Variables**.

  4. Click **Add a new record**.

  5. Specify the name of the variable in the **Key** field, and set the value for it in the **Val** field.

  6. Click **Save**.




## Create a Persistent History Server

Use a Persistent History Server (PHS) to view Spark history files of your batch workloads:

  1. [Create a Persistent History Server](https://docs.cloud.google.com/dataproc/docs/concepts/jobs/history-server).
  2. Make sure that you specified the name of the PHS cluster in the `phs_cluster` Airflow variable.



## DataprocCreateBatchOperator

The following DAG starts a Managed Service for Apache Spark batch workload.

For more information about `DataprocCreateBatchOperator` arguments, see [operator's source code](https://github.com/apache/airflow/blob/main/airflow/providers/google/cloud/operators/dataproc.py#L2029).

For more information about attributes that you can pass in the `batch` parameter of `DataprocCreateBatchOperator`, see the [description of the Batch class](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Batch).
    
    
    """
    Examples below show how to use operators for managing Dataproc Serverless batch workloads.
     You use these operators in DAGs that create, delete, list, and get a Dataproc Serverless Spark batch workload.
    https://airflow.apache.org/docs/apache-airflow/stable/concepts/variables.html
    * project_id is the Google Cloud Project ID to use for the Cloud Dataproc Serverless.
    * bucket_name is the URI of a bucket where the main python file of the workload (spark-job.py) is located.
    * phs_cluster is the Persistent History Server cluster name.
    * image_name is the name and tag of the custom container image (image:tag).
    * metastore_cluster is the Dataproc Metastore service name.
    * region_name is the region where the Dataproc Metastore service is located.
    """
    
    import datetime
    
    from airflow import models
    from airflow.providers.google.cloud.operators.dataproc import (
        DataprocCreateBatchOperator,
        DataprocDeleteBatchOperator,
        DataprocGetBatchOperator,
        DataprocListBatchesOperator,
    )
    from airflow.utils.dates import days_ago
    
    PROJECT_ID = "{{ var.value.project_id }}"
    REGION = "{{ var.value.region_name}}"
    BUCKET = "{{ var.value.bucket_name }}"
    PHS_CLUSTER = "{{ var.value.phs_cluster }}"
    METASTORE_CLUSTER = "{{var.value.metastore_cluster}}"
    DOCKER_IMAGE = "{{var.value.image_name}}"
    
    PYTHON_FILE_LOCATION = "gs://{{var.value.bucket_name }}/spark-job.py"
    # for e.g.  "gs//my-bucket/spark-job.py"
    # Start a single node Dataproc Cluster for viewing Persistent History of Spark jobs
    PHS_CLUSTER_PATH = "projects/{{ var.value.project_id }}/regions/{{ var.value.region_name}}/clusters/{{ var.value.phs_cluster }}"
    # for e.g. projects/my-project/regions/my-region/clusters/my-cluster"
    SPARK_BIGQUERY_JAR_FILE = "gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar"
    # use this for those pyspark jobs that need a spark-bigquery connector
    # https://cloud.google.com/dataproc/docs/tutorials/bigquery-connector-spark-example
    # Start a Dataproc MetaStore Cluster
    METASTORE_SERVICE_LOCATION = "projects/{{var.value.project_id}}/locations/{{var.value.region_name}}/services/{{var.value.metastore_cluster }}"
    # for e.g. projects/my-project/locations/my-region/services/my-cluster
    CUSTOM_CONTAINER = "us.gcr.io/{{var.value.project_id}}/{{ var.value.image_name}}"
    # for e.g. "us.gcr.io/my-project/quickstart-image",
    
    default_args = {
        # Tell airflow to start one day ago, so that it runs as soon as you upload it
        "start_date": days_ago(1),
        "project_id": PROJECT_ID,
        "region": REGION,
    }
    with models.DAG(
        "dataproc_batch_operators",  # The id you will see in the DAG airflow page
        default_args=default_args,  # The interval with which to schedule the DAG
        schedule_interval=datetime.timedelta(days=1),  # Override to match your needs
    ) as dag:
        create_batch = DataprocCreateBatchOperator(
            task_id="batch_create",
            batch={
                "pyspark_batch": {
                    "main_python_file_uri": PYTHON_FILE_LOCATION,
                    "jar_file_uris": [SPARK_BIGQUERY_JAR_FILE],
                },
                "environment_config": {
                    "peripherals_config": {
                        "spark_history_server_config": {
                            "dataproc_cluster": PHS_CLUSTER_PATH,
                        },
                    },
                },
            },
            batch_id="batch-create-phs",
        )
        list_batches = DataprocListBatchesOperator(
            task_id="list-all-batches",
        )
    
        get_batch = DataprocGetBatchOperator(
            task_id="get_batch",
            batch_id="batch-create-phs",
        )
        delete_batch = DataprocDeleteBatchOperator(
            task_id="delete_batch",
            batch_id="batch-create-phs",
        )
        create_batch >> list_batches >> get_batch >> delete_batch

### Use custom container image with DataprocCreateBatchOperator

The following example shows how to use a custom container image to run your workloads. You can use a custom container, for example, to add Python dependencies not provided by the default container image.

**Note:** To execute DAGs that run Managed Service for Apache Spark runs with custom Docker containers, your Managed Airflow environment must use Managed Airflow 2.0.6 and Airflow 2.2.3, or later versions.

To use a custom container image:

  1. [Create a custom container image and upload it to Container Registry](https://docs.cloud.google.com/dataproc-serverless/docs/guides/custom-containers#dataproc_serverless_custom_containers_include-drest).

  2. Specify the image in the `image_name` Airflow variable.

  3. Use DataprocCreateBatchOperator with your custom image:



    
    
    create_batch_with_custom_container = DataprocCreateBatchOperator(
        task_id="dataproc_custom_container",
        batch={
            "pyspark_batch": {
                "main_python_file_uri": PYTHON_FILE_LOCATION,
                "jar_file_uris": [SPARK_BIGQUERY_JAR_FILE],
            },
            "environment_config": {
                "peripherals_config": {
                    "spark_history_server_config": {
                        "dataproc_cluster": PHS_CLUSTER_PATH,
                    },
                },
            },
            "runtime_config": {
                "container_image": CUSTOM_CONTAINER,
            },
        },
        batch_id="batch-custom-container",
    )
    get_batch_custom = DataprocGetBatchOperator(
        task_id="get_batch_custom",
        batch_id="batch-custom-container",
    )
    delete_batch_custom = DataprocDeleteBatchOperator(
        task_id="delete_batch_custom",
        batch_id="batch-custom-container",
    )
    create_batch_with_custom_container >> get_batch_custom >> delete_batch_custom

### Use Dataproc Metastore service with DataprocCreateBatchOperator

To use a [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview) service from a DAG:

  1. Check that your metastore service is already started.

To learn about starting a metastore service, see [Enable and disable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service).

For detailed information about the Batch operator for creating the configuration, see [PeripheralsConfig](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches#peripheralsconfig).

  2. Once the metastore service is up and running, specify its name in the `metastore_cluster` variable and its region in the `region_name` Airflow variable.

  3. Use the metastore service in DataprocCreateBatchOperator:



    
    
    create_batch_with_metastore = DataprocCreateBatchOperator(
        task_id="dataproc_metastore",
        batch={
            "pyspark_batch": {
                "main_python_file_uri": PYTHON_FILE_LOCATION,
                "jar_file_uris": [SPARK_BIGQUERY_JAR_FILE],
            },
            "environment_config": {
                "peripherals_config": {
                    "metastore_service": METASTORE_SERVICE_LOCATION,
                    "spark_history_server_config": {
                        "dataproc_cluster": PHS_CLUSTER_PATH,
                    },
                },
            },
        },
        batch_id="dataproc-metastore",
    )
    get_batch_metastore = DataprocGetBatchOperator(
        task_id="get_batch_metatstore",
        batch_id="dataproc-metastore",
    )
    delete_batch_metastore = DataprocDeleteBatchOperator(
        task_id="delete_batch_metastore",
        batch_id="dataproc-metastore",
    )
    
    create_batch_with_metastore >> get_batch_metastore >> delete_batch_metastore
    

## DataprocDeleteBatchOperator

You can use DataprocDeleteBatchOperator to delete a batch based on the batch id of the workload.
    
    
    delete_batch = DataprocDeleteBatchOperator(
        task_id="delete_batch",
        batch_id="batch-create-phs",
    )

## DataprocListBatchesOperator

DataprocDeleteBatchOperator lists batches that exist within a given project_id and region.
    
    
    list_batches = DataprocListBatchesOperator(
        task_id="list-all-batches",
    )

## DataprocGetBatchOperator

DataprocGetBatchOperator fetches one particular batch workload.
    
    
    get_batch = DataprocGetBatchOperator(
        task_id="get_batch",
        batch_id="batch-create-phs",
    )

## What's next

  * [Managed Service for Apache Spark overview](https://docs.cloud.google.com/dataproc-serverless/docs/overview)
  * [Trigger DAGs with Cloud Run functions](https://docs.cloud.google.com/composer/docs/composer-3/triggering-with-gcf)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
