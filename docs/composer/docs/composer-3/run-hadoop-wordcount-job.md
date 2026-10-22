---
url: https://docs.cloud.google.com/composer/docs/composer-3/run-hadoop-wordcount-job/
title: Run a Hadoop wordcount job on a Cloud Dataproc cluster \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:01.705167+00:00
---

# Run a Hadoop wordcount job on a Cloud Dataproc cluster  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/run-hadoop-wordcount-job/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Run a Hadoop wordcount job on a Cloud Dataproc cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/run-hadoop-wordcount-job "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/run-hadoop-wordcount-job "View this page for Managed Airflow \(Legacy Gen 1\)")

**Note:** This page is **not yet revised for Managed Airflow (Gen 3)** and displays content for Managed Airflow (Gen 2).

This tutorial shows how to use Managed Service for Apache Airflow to create an [Apache Airflow](http://airflow.apache.org) DAG (Directed Acyclic Graph) that runs an Apache Hadoop wordcount job on a Managed Service for Apache Spark cluster.

## Objectives

  1. Access your Managed Airflow environment and use the [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface).
  2. Create and view Airflow environment variables.
  3. Create and run a DAG that includes the following tasks: 
     1. Creates a [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) cluster.
     2. Runs an [Apache Hadoop](http://hadoop.apache.org/) word-count job on the cluster.
     3. Outputs the word-count results to a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket.
     4. Deletes the cluster.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Managed Airflow
  * Managed Service for Apache Spark
  * Cloud Storage



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  * Make sure that the following APIs are enabled in your project:

###  Console 

Enable the Managed Service for Apache Spark, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,storage-component.googleapis.com)

###  gcloud 

Enable the Managed Service for Apache Spark, Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable dataproc.googleapis.com storage-component.googleapis.com

  * In your project, [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) of any storage class and region to store the results of the Hadoop word-count job.

**Note:** For data residency requirements or performance benefits, create the storage bucket in the same region you plan to create your environment in.
  * Note the path of the bucket that you created, for example `gs://example-bucket`. You'll define an Airflow variable for this path and use the variable in the example DAG later in this tutorial.

  * [Create a Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) with default parameters. Wait until environment creation is completed. When done, the green check mark displays to the left of the environment name.

  * Note the region where you created your environment, for example `us-central`. You'll define an Airflow variable for this region and use it in the example DAG to run a Managed Service for Apache Spark cluster in the same region.




## Set Airflow variables

[Set the Airflow variables](https://airflow.apache.org/docs/apache-airflow/stable/howto/variable.html) to use later in the example DAG. For example, you can set Airflow variables in the [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface).

Airflow variable | Value  
---|---  
`gcp_project` |  The [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project you're using for this tutorial, such as `example-project`.  
`gcs_bucket` |  The URI Cloud Storage bucket you created for this tutorial, such as `gs://example-bucket`.``  
`gce_region` |  The region where you created your environment, such as `us-central1`. This is the region where your Managed Service for Apache Spark cluster will be created.  
  
## View the example workflow

An Airflow DAG is a collection of organized tasks that you want to schedule and run. DAGs are defined in standard Python files. The code shown in `hadoop_tutorial.py` is the workflow code.
    
    
    """Example Airflow DAG that creates a Cloud Dataproc cluster, runs the Hadoop
    wordcount example, and deletes the cluster.
    
    This DAG relies on three Airflow variables
    https://airflow.apache.org/docs/apache-airflow/stable/concepts/variables.html
    * gcp_project - Google Cloud Project to use for the Cloud Dataproc cluster.
    * gce_region - Google Compute Engine region where Cloud Dataproc cluster should be
      created.
    * gcs_bucket - Google Cloud Storage bucket to use for result of Hadoop job.
      See https://cloud.google.com/storage/docs/creating-buckets for creating a
      bucket.
    """
    
    import datetime
    import os
    
    from airflow import models
    from airflow.providers.google.cloud.operators import dataproc
    from airflow.utils import trigger_rule
    
    # Output file for Cloud Dataproc job.
    # If you are running Airflow in more than one time zone
    # see https://airflow.apache.org/docs/apache-airflow/stable/timezone.html
    # for best practices
    output_file = (
        os.path.join(
            "{{ var.value.gcs_bucket }}",
            "wordcount",
            datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
        )
        + os.sep
    )
    # Path to Hadoop wordcount example available on every Dataproc cluster.
    WORDCOUNT_JAR = "file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar"
    # Arguments to pass to Cloud Dataproc job.
    input_file = "gs://pub/shakespeare/rose.txt"
    wordcount_args = ["wordcount", input_file, output_file]
    
    HADOOP_JOB = {
        "reference": {"project_id": "{{ var.value.gcp_project }}"},
        "placement": {"cluster_name": "composer-hadoop-tutorial-cluster-{{ ds_nodash }}"},
        "hadoop_job": {
            "main_jar_file_uri": WORDCOUNT_JAR,
            "args": wordcount_args,
        },
    }
    
    CLUSTER_CONFIG = {
        "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
        "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
    }
    
    yesterday = datetime.datetime.combine(
        datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time()
    )
    
    default_dag_args = {
        # Setting start date as yesterday starts the DAG immediately when it is
        # detected in the Cloud Storage bucket.
        "start_date": yesterday,
        # To email on failure or retry set 'email' arg to your email and enable
        # emailing here.
        "email_on_failure": False,
        "email_on_retry": False,
        # If a task fails, retry it once after waiting at least 5 minutes
        "retries": 1,
        "retry_delay": datetime.timedelta(minutes=5),
        "project_id": "{{ var.value.gcp_project }}",
        "region": "{{ var.value.gce_region }}",
    }
    
    
    with models.DAG(
        "composer_hadoop_tutorial",
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args,
    ) as dag:
    
        # Create a Cloud Dataproc cluster.
        create_dataproc_cluster = dataproc.DataprocCreateClusterOperator(
            task_id="create_dataproc_cluster",
            # Give the cluster a unique name by appending the date scheduled.
            # See https://airflow.apache.org/docs/apache-airflow/stable/macros-ref.html
            cluster_name="composer-hadoop-tutorial-cluster-{{ ds_nodash }}",
            cluster_config=CLUSTER_CONFIG,
            region="{{ var.value.gce_region }}",
        )
    
        # Run the Hadoop wordcount example installed on the Cloud Dataproc cluster
        # master node.
        run_dataproc_hadoop = dataproc.DataprocSubmitJobOperator(
            task_id="run_dataproc_hadoop", job=HADOOP_JOB
        )
    
        # Delete Cloud Dataproc cluster.
        delete_dataproc_cluster = dataproc.DataprocDeleteClusterOperator(
            task_id="delete_dataproc_cluster",
            cluster_name="composer-hadoop-tutorial-cluster-{{ ds_nodash }}",
            region="{{ var.value.gce_region }}",
            # Setting trigger_rule to ALL_DONE causes the cluster to be deleted
            # even if the Dataproc job fails.
            trigger_rule=trigger_rule.TriggerRule.ALL_DONE,
        )
    
        # Define DAG dependencies.
        create_dataproc_cluster >> run_dataproc_hadoop >> delete_dataproc_cluster
    

### Operators

To orchestrate the three tasks in the example workflow, the DAG imports the following three Airflow operators:

  * `DataprocClusterCreateOperator`: Creates a Managed Service for Apache Spark cluster.

  * `DataProcHadoopOperator`: Submits a Hadoop wordcount job and writes results to a Cloud Storage bucket.

  * `DataprocClusterDeleteOperator`: Deletes the cluster to avoid incurring ongoing Compute Engine charges.




### Dependencies

You organize tasks that you want to run in a way that reflects their relationships and dependencies. The tasks in this DAG run sequentially.
    
    
    # Define DAG dependencies.
    create_dataproc_cluster >> run_dataproc_hadoop >> delete_dataproc_cluster

### Scheduling

The name of the DAG is `composer_hadoop_tutorial`, and the DAG runs once each day. Because the `start_date` that is passed in to `default_dag_args` is set to `yesterday`, Managed Airflow schedules the workflow to start immediately after the DAG is uploaded to the environment's bucket.
    
    
    with models.DAG(
        "composer_hadoop_tutorial",
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args,
    ) as dag:

## Upload the DAG to the environment's bucket

Managed Airflow stores DAGs in the `/dags` folder in your environment's bucket.

To upload the DAG:

  1. On your local machine, save `hadoop_tutorial.py`.

  2. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  3. In the list of environments, in the **DAGs folder** column for your environment, click the **DAGs** link.

  4. Click **Upload** files.

  5. Select `hadoop_tutorial.py` on your local machine and click **Open**.




Managed Airflow adds the DAG to Airflow and schedules the DAG automatically. DAG changes occur within 3-5 minutes.

## Explore DAG runs

### View task status

When you upload your DAG file to the `dags/` folder in Cloud Storage, Managed Airflow parses the file. When completed successfully, the name of the workflow appears in the DAG listing, and the workflow is queued to run immediately.

  1. To see task status, go to the Airflow web interface and click **DAGs** in the toolbar.

![](https://docs.cloud.google.com/static/composer/docs/images/ui-dag-tab.png)
  2. To open the DAG details page, click `composer_hadoop_tutorial`. This page includes a graphical representation of workflow tasks and dependencies.

![](https://docs.cloud.google.com/static/composer/docs/images/dag-details.png)
  3. To see each task's status, click **Graph View** and then mouseover the graphic for each task.

![](https://docs.cloud.google.com/static/composer/docs/images/graph-view.png)



### Queue the workflow again

To run the workflow again from the **Graph View** :

  1. In the Airflow UI Graph View, click the `create_dataproc_cluster` graphic.
  2. To reset the three tasks, click **Clear** and then click **OK** to confirm.
  3. Click `create_dataproc_cluster` again in Graph View.
  4. To queue the workflow again, click **Run**.

![](https://docs.cloud.google.com/static/composer/docs/images/create-clear.png)

### View task results

You can also check the status and results of the `composer_hadoop_tutorial` workflow by going to the following Google Cloud console pages:

  * **Managed Service for Apache Spark Clusters** : to monitor cluster creation and deletion. Note that the cluster created by the workflow is ephemeral: it only exists for the duration of the workflow and is deleted as part of the last workflow task.

[Go to Managed Service for Apache Spark Clusters](https://console.cloud.google.com/dataproc/clusters)

  * **Managed Service for Apache Spark Jobs** : to view or monitor the Apache Hadoop wordcount job. Click the Job ID to see job log output.

[Go to Managed Service for Apache Spark Jobs](https://console.cloud.google.com/dataproc/jobs)

  * **Cloud Storage Browser** : to see the results of the wordcount in the `wordcount` folder in the Cloud Storage bucket you created for this tutorial.

[Go to Cloud Storage Browser](https://console.cloud.google.com/storage/browser)




## Cleanup

Delete the **resources** used in this tutorial:

  1. [Delete the Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments), including manually deleting the environment's bucket.

  2. [Delete the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) that stores the results of the Hadoop word-count job.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
