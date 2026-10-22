---
url: https://docs.cloud.google.com/composer/docs/composer-2/transfer-data-with-transfer-operators/
title: Transfer data from other services with Google Transfer Operators \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:35.248377+00:00
---

# Transfer data from other services with Google Transfer Operators  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/transfer-data-with-transfer-operators/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Transfer data from other services with Google Transfer Operators Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/transfer-data-with-transfer-operators "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/transfer-data-with-transfer-operators "View this page for Managed Airflow \(Legacy Gen 1\)")

This page demonstrates how to transfer data from other services with Google Transfer Operators in your DAGs.

## About Google Transfer Operators

[Google Transfer Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/transfer/index.html) are a set of Airflow operators that you can use to pull data from other services into Google Cloud.

This guide shows operators for Azure FileShare Storage and Amazon S3 that work with Cloud Storage. There are many more transfer operators that work with services within Google Cloud and with services other than Google Cloud.

## Amazon S3 to Cloud Storage

This section demonstrates how to synchronize data from Amazon S3 to a Cloud Storage bucket.

### Install the Amazon provider package

The `apache-airflow-providers-amazon` package contains the connection types and functionality that interacts with Amazon S3. [Install this PyPI package](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-pypi) in your environment.

### Configure a connection to Amazon S3

The Amazon provider package provides a connection type for Amazon S3. You create a connection of this type. The connection for Cloud Storage, named `google_cloud_default` is already set up in your environment.

Set up a connection to Amazon S3 in the following way:

  1. In [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface), go to **Admin** > **Connections**.
  2. Create a new connection.
  3. Select `Amazon S3` as the connection type.
  4. The following example uses a connection named `aws_s3`. You can use this name, or any other name for the connection.
  5. Specify connection parameters as described in the Airflow documentation for [Amazon Web Services Connection](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/connections/aws.html). For example, to set up a connection with AWS access keys, you generate an access key for your account on AWS, then provide the AWS access key ID as a login the AWS secret access key as a password for the connection.

**Note:** We recommend to **store all credentials for connections in Secret Manager**. For more information, see [Configure Secret Manager for your environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-secret-manager). For example, you can create a secret named `airflow-connections-aws_s3` that stores credentials for the `aws_s3` connection.

### Transfer data from Amazon S3

If you want to operate on the synchronized data later in another DAG or task, pull it to the `/data` folder of your environment's bucket. This folder is synchronized to other Airflow workers, so that tasks in your DAG can operate on it.

The following example DAG does the following:

  * Synchronizes contents of the `/data-for-gcs` directory from an S3 bucket to the `/data/from-s3/data-for-gcs/` folder in your environment's bucket.
  * Waits for two minutes, for the data to synchronize to all Airflow workers in your environment. 
  * Outputs the list of files in this directory using the `ls` command. Replace this task with other Airflow operators that work with your data.


    
    
    import datetime
    import airflow
    from airflow.providers.google.cloud.transfers.s3_to_gcs import S3ToGCSOperator
    from airflow.operators.bash_operator import BashOperator
    
    with airflow.DAG(
        'composer_sample_aws_to_gcs',
        start_date=datetime.datetime(2022, 1, 1),
        schedule=None,
    ) as dag:
    
        transfer_dir_from_s3 = S3ToGCSOperator(
            task_id='transfer_dir_from_s3',
            aws_conn_id='aws_s3',
            prefix='data-for-gcs',
            bucket='example-s3-bucket-transfer-operators',
            dest_gcs='gs://us-central1-example-environ-361f2312-bucket/data/from-s3/')
    
        sleep_2min = BashOperator(
            task_id='sleep_2min',
            bash_command='sleep 2m')
    
        print_dir_files = BashOperator(
            task_id='print_dir_files',
            bash_command='ls /home/airflow/gcs/data/from-s3/data-for-gcs/')
    
    
        transfer_dir_from_s3 >> sleep_2min >> print_dir_files
    

## Azure FileShare to Cloud Storage

This section demonstrates how to synchronize data from Azure FileShare to a Cloud Storage bucket.

### Install the Microsoft Azure provider package

The `apache-airflow-providers-microsoft-azure` package contains the connection types and functionality that interacts with Microsoft Azure. [Install this PyPI package](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-pypi) in your environment.

### Configure a connection to Azure FileShare

The Microsoft Azure provider package provides a connection type for Azure File Share. You create a connection of this type. The connection for Cloud Storage, named `google_cloud_default` is already set up in your environment.

Set up a connection to Azure FileShare in the following way:

  1. In [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface), go to **Admin** > **Connections**.
  2. Create a new connection.
  3. Select `Azure FileShare` as the connection type.
  4. The following example uses a connection named `azure_fileshare`. You can use this name, or any other name for the connection.
  5. Specify connection parameters as described in the Airflow documentation for [Microsoft Azure File Share Connection](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/connections/azure_fileshare.html). For example, you can specify a connection string for your storage account access key.

**Note:** We recommend to **store all credentials for connections in Secret Manager**. For more information, see [Configure Secret Manager for your environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-secret-manager). For example, you can create a secret named `airflow-connections-azure_fileshare` that stores credentials for the `azure_fileshare` connection.

### Transfer data from Azure FileShare

If you want to operate on the synchronized data later in another DAG or task, pull it to the `/data` folder of your environment's bucket. This folder is synchronized to other Airflow workers, so that tasks in your DAG can operate on it.

The following DAG does the following:

The following example DAG does the following:

  * Synchronizes contents of the `/data-for-gcs` directory from Azure File Share to the `/data/from-azure` folder in your environment's bucket.
  * Waits for two minutes, for the data to synchronize to all Airflow workers in your environment. 
  * Outputs the list of files in this directory using the `ls` command. Replace this task with other Airflow operators that work with your data.


    
    
    import datetime
    import airflow
    from airflow.providers.google.cloud.transfers.azure_fileshare_to_gcs import AzureFileShareToGCSOperator
    from airflow.operators.bash_operator import BashOperator
    
    with airflow.DAG(
        'composer_sample_azure_to_gcs',
        start_date=datetime.datetime(2022, 1, 1),
        schedule=None,
    ) as dag:
    
        transfer_dir_from_azure = AzureFileShareToGCSOperator(
            task_id='transfer_dir_from_azure',
            azure_fileshare_conn_id='azure_fileshare',
            share_name='example-file-share',
            directory_name='data-for-gcs',
            dest_gcs='gs://us-central1-example-environ-361f2312-bucket/data/from-azure/')
    
        sleep_2min = BashOperator(
            task_id='sleep_2min',
            bash_command='sleep 2m')
    
        print_dir_files = BashOperator(
            task_id='print_dir_files',
            bash_command='ls /home/airflow/gcs/data/from-azure/')
    
    
        transfer_dir_from_azure >> sleep_2min >> print_dir_files
    

## What's next

  * [Use GKE operators](https://docs.cloud.google.com/composer/docs/composer-2/use-gke-operator)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
