---
url: https://docs.cloud.google.com/data-cloud-extension/vs-code/build-pipelines/
title: Build data engineering pipelines \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:23:38.241927+00:00
---

# Build data engineering pipelines  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-cloud-extension/vs-code/build-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Build data engineering pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to create and deploy an orchestration pipeline using Google Cloud Data Agent Kit.

The example pipeline runs a PySpark script in Managed Service for Apache Spark.

**Note:** This guide describes the steps to take after installing the Data Agent Kit IDE extension. You can also achieve these tasks with a supported CLI or coding agent if you install the Data Agent Kit plugin and then use natural language prompts.

You can deploy orchestration pipelines from your IDE as local versions or through a GitHub action such as when merging changes to the `main` branch. This document demonstrates how to deploy the local version of an orchestration pipeline.

## Before you begin

Before you begin, complete the following:

  1. [Install Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/install).
  2. [Configure your settings](https://docs.cloud.google.com/data-agent-kit/configure).
  3. Add a GitHub repository to your IDE workspace to store orchestration pipelines and assets such as scripts.



### Review the required IAM roles

To obtain the permissions to create resources in your project, deploy, and run orchestration pipelines, ask your administrator to grant you the required roles.

To create and manage Managed Service for Apache Airflow environments and manage objects in their associated buckets, you need the following roles. For more information about these user roles, see [Grant roles to users](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account) in the Managed Service for Apache Airflow documentation.

  * **Environment and Storage Object Administrator** (composer.environmentAndStorageObjectAdmin)
  * **Service Account User** (`iam.serviceAccountUser`)



To work with BigQuery and Cloud Storage resources, you need the following roles.

  * **BigQuery Data Editor** (`roles/bigquery.dataEditor`)
  * **Storage Object Admin** (`roles/storage.objectAdmin`)



Depending on the resources you plan to access, you might need additional roles beyond the roles that let you use the extension and work with orchestration pipelines.

### Create a service account and grant it IAM roles

Use a unique service account for the Managed Airflow Gen 3 environment. The service account creates a Managed Airflow Gen 3 environment and runs all orchestration pipelines you deploy.

Ask your administrator to complete the following steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) as described in the IAM documentation.
  2. Grant the **Composer Worker** (`composer.worker`) role to the service account. This role provides the required permissions in most cases.



As a best practice, if you need to access other resources in your Google Cloud project, grant additional permissions to this service account only when necessary for the orchestration pipeline operation.

## Create Google Cloud resources for your orchestration pipeline

In this step, create Google Cloud resources for your orchestration pipeline.

### Create a Managed Airflow Gen 3 environment

[Create a Managed Airflow Gen 3 environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) with the following configuration:

  * **Environment name** : Enter a name that you will use later to configure the orchestration pipeline. For example, `example-pipeline-scheduler`.
  * **Location** : Select a location. We recommend creating all resources in this guide in the same location. For example, `us-central1`.
  * **Service account** : Select the service account you created for this environment.



The following Google Cloud CLI command example demonstrates the syntax:
    
    
    gcloud composer environments create example-pipeline-scheduler \
      --location us-central1 \
      --image-version composer-3-airflow-2 \
      --service-account "example-account@example-project.iam.gserviceaccount.com"
    

**Important:** Creating a Managed Airflow Gen 3 environment takes approximately 25 minutes.

### Add environment parameters to the scheduler configuration

Provide connection details for the Managed Airflow environment that will execute your orchestration pipeline.

Add the configuration parameters of the environment you've created using the Google Cloud Data Agent Kit Settings editor:

  1. Click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Select **Scheduler**.
  4. Enter the parameters for the Managed Airflow Gen 3 environment that you created earlier: 
     * **Project ID** : name of the project where the environment is located. Example: `example-project`.
     * **Region** : region where the environment is located. Example: `us-central1`.
     * **Environment** : name of the environment. Example: `example-pipeline-scheduler`.
  5. Click **Save**.



### Create a bucket for pipeline artifacts

[Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in the same project as the Managed Airflow environment and give it a name similar to `example-pipelines-bucket`. This bucket is required to store your Managed Service for Apache Spark job.

**Note:** Pipeline scenarios that don't involve Managed Service for Apache Spark don't always require a Cloud Storage bucket.

Some pipeline actions, such as the output the results to a Cloud Storage bucket.

### Create a new dataset and table in BigQuery

This guide demonstrates a pipeline that writes data to a BigQuery table. Create the following BigQuery resources in your project:

  1. [Create a new dataset](https://docs.cloud.google.com/bigquery/docs/datasets) named `wordcount_dataset`.
  2. [Create a new BigQuery table](https://docs.cloud.google.com/bigquery/docs/tables) named `wordcount_output`.

**Important:** Don't use an existing BigQuery table because the PySpark script in this guide overwrites data in the table.

## Add pipeline assets

This guide demonstrates a common data engineering task (ETL: Extract, Transform, Load) using PySpark, reading from BigQuery, transforming the data (word count), and loading it back to BigQuery.

**Note:** For some of the actions in this guide, we provide both agentic and non-agentic steps so that you can experiment or use the path you prefer. If the Agent Chat panel isn't displayed, open the command palette by pressing **Cmd/Ctrl+Shift+P** , then search for and run **Open Chat**.

###  Non-agentic 

Add the following file to the `/scripts` folder of your repository. You later add a pipeline action that runs this script in Managed Service for Apache Spark.

Example `wordcount.py` file:
    
    
    #!/usr/bin/python
    """BigQuery I/O PySpark example for Word Count"""
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession \
    .builder \
    .appName('spark-bigquery-demo') \
    .getOrCreate()
    
    # Use the Cloud Storage bucket for temporary BigQuery export data used
    # by the connector.
    bucket = ARTIFACTS_BUCKET_NAME
    spark.conf.set('temporaryGcsBucket', bucket)
    
    # Load data from BigQuery public dataset (Shakespeare).
    words = spark.read.format('bigquery') \
    .option('table', 'bigquery-public-data:samples.shakespeare') \
    .load()
    words.createOrReplaceTempView('words')
    
    # Perform word count using Spark SQL.
    # This query counts occurrences of each word.
    word_count = spark.sql(
        'SELECT word, SUM(word_count) AS word_count FROM words GROUP BY word ORDER BY word_count DESC'
    )
    word_count.show()
    word_count.printSchema()
    
    # Saving the results to a new table in BigQuery.
    # Replace YOUR_PROJECT_ID with your project ID.
    destination_table = 'PROJECT_ID:wordcount_dataset.wordcount_output'
    word_count.write.format('bigquery') \
    .option('table', destination_table) \
    .mode('overwrite') \
    .save()
    
    print(f"Successfully wrote word counts to BigQuery table: {destination_table}")
    

Replace the following:

  * ARTIFACTS_BUCKET_NAME: the name of the Cloud Storage bucket you created earlier. Example: `example-pipelines-bucket`.
  * PROJECT_ID: the name of the project where the environment resides. Example: `example-project`.



###  Agentic 

Prompt the Agent to generate a sample PySpark script in the `/scripts` folder of your repository. You later add a pipeline action that runs this script in Managed Service for Apache Spark.

Enter a prompt similar to the following:
    
    
    I want to create a PySpark script that does the following:
    
    1. Loads data from the bigquery-public-data:samples.shakespeare.
    2. Counts occurrences of each word across all works using a Spark SQL query.
    Sum the existing word counts for each word to get the total occurrences.
    I want the results to be ordered by the word popularity, most popular first.
    3. Saves results to a new table in BigQuery, in my project.
    
    My project is sample-project, the destination table is
    wordcount_dataset.wordcount_output, and I want to store temporary BigQuery
    export data in example-pipelines-bucket.
    
    Save the resulting script to /scripts as wordcount.py
    

## Initialize orchestration pipelines in your repository

When you initialize orchestration pipelines, Data Agent Kit creates a scaffolding that includes the following:

  * An orchestration pipeline YAML file: An example pipeline definition that contains a schedule but no defined actions.
  * `deployment.yaml`: An example pipeline deployment configuration that defines how your pipeline must be deployed. This file demonstrates the required configuration for the Managed Airflow environment, the artifacts bucket, and any other resources used by your pipeline actions.
  * `.github/workflows/deploy.yaml`: Sets up a GitHub action that deploys your pipeline when you merge changes to the `main` branch of your GitHub repository.
  * `.github/workflows/validate.yaml`: Sets up a GitHub action that validates your pipeline after it's deployed.



In later steps of this document, you expand these definitions using the Data Agent Kit to create and deploy an orchestration pipeline locally.

###  Non-agentic 

To initialize orchestration pipelines, do the following:

  1. Click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Data Engineering** , and then click **Initialize orchestration pipeline**.
  3. Enter parameters for the new orchestration pipeline:

     1. **Environment ID** : the name of the environment you want to develop with. Example: `dev/staging`.
     2. **Pipeline ID** : Enter your pipeline's ID. Example: `example-pipeline`.
     3. **Google Cloud Project ID** : the name of the project where the environment resides. Example: `example-project`.
     4. **Region** : the region where your environment resides. Example: `us-central1`.
     5. **Scheduler Managed Service for Apache Airflow Environment** : the name of the environment where you want to orchestrate your pipelines. For this document, specify the same environment in this parameter.

**Note:** Data Agent Kit provides separate options for deploying and running pipelines, and for monitoring their execution. For example, you might want to deploy pipelines to your development environment, but monitor the production environment.
     6. **Artifacts Bucket** : the name of the bucket used for pipeline artifacts, without the `gs://` prefix. Example: `example-pipelines-bucket`.

  4. Click **Initialize**.

  5. Specify a workspace where you want the pipeline initialized.




###  Agentic 

Ask the Agent to create a scaffolding for orchestration pipelines of your repository.

Enter a prompt similar to the following:
    
    
    Initialize orchestration pipelines in my repository. Don't add any actions
    or schedule yet. I want to do it later.
    
    The pipeline is my-sample-pipeline, the project ID is my-project, and the
    region is us-central1.
    
    The environment ID is my-test-environment. Use the same environment ID for
    the Scheduler Managed Service.
    
    Store pipeline artifacts in example-pipelines-bucket.
    

After you initialize pipelines in your repository, you cannot do so again because the new scaffolding would overwrite any configuration changes you made. You can add new pipelines by creating new pipeline definition files in your project and adding them to the deployment configuration.

## Add a new task to the pipeline

Because the initial pipeline configuration doesn't have any actions, you add an action that runs your PySpark script to it.

###  Non-agentic 

To edit a pipeline, do the following:

  1. Click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Data Engineering** , then **Orchestration Pipelines**.
  3. Select `example-pipeline.yaml`. A pipeline editor opens for the selected pipeline.
  4. Optional: Select the **Schedule trigger** node. You can adjust the schedule for your pipeline by specifying a cron-like expression and schedule start and end times. The default schedule for the newly initialized pipeline is `0 2 * * *`, which runs at 2 AM daily.

**Note:** Each pipeline run defined by a schedule corresponds to a **logical date**. A logical date, for example, denotes the start of the data interval to be processed by the pipeline, not when it is executed. For example, if a particular pipeline run fails for a specific logical date, Managed Service for Apache Airflow can retry it later for the same logical date. If the start time for the schedule you define is in the past, you can optionally execute pipeline runs for all past logical dates defined by the schedule by selecting **Catchup**.

  1. Add a new task. In this guide, you add a PySpark task that runs a PySpark script that you added earlier:

     1. Click **Add first task** to add a new task node.
     2. Select **Execute PySpark script** and the `script/wordcount.py` file.

The **Execute PySpark script** panel opens.

     1. In Spark Cluster Mode, select **Serverless Spark**.
     2. In **Location** , specify the location where your environment resides. Example: `us-central1`.
     3. Click **Save**.



###  Agentic 

Run the following prompt:
    
    
    Add the wordcount.py script to the pipeline. I want to run it in Serverless
    Spark every day at 1 AM. Run it in the same region where the environment that
    runs my pipeline is located. Use the minimal resource profile.
    

## Deploy the local version of the pipeline

Deploy the local version of the pipeline to confirm that it's configured correctly.

When you deploy a local version of the orchestration pipeline, Data Agent Kit uploads a local version of the pipeline bundle to the Managed Airflow environment and runs it. Local deployment is intended to be used when working in a development environment.

The deploy command deploys an unpaused schedule. To prevent this, you can pause the schedule manually in the Pipelines Management pane. You can also edit your pipeline YAML file to comment out or remove the `triggers: - schedule` block.

**Note:** In notebooks or jobs hosted on an existing Managed Service for Apache Spark cluster, you can't add Python dependencies in a requirements path. If you need to add Python dependencies, use ephemeral or serverless jobs.**Note:** Local build with dependencies is supported for Linux and macOS, but not for Windows.

###  Non-agentic 

To deploy a local version of the example orchestration pipeline, do the following:

  1. Click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Data Engineering** and then **Orchestration Pipelines**.
  3. Select `example-pipeline.yaml`. A pipeline editor opens for the selected pipeline.
  4. Select **Run pipeline** and then select the development or staging environment that you previously created.

**Note:** The **Trigger run** option runs a pipeline run outside of the defined schedule. You can use this option only for an already deployed pipeline. This option is in the pipeline management pane in the **Actions** menu for the pipeline.

###  Agentic 

Run the following prompt:
    
    
    Deploy my pipeline
    

## Monitor the pipeline execution and check execution logs

After your pipeline is deployed, you can see the detailed information, history of pipeline runs, and the pipeline execution logs for it:

  1. Click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Data Engineering** , then select **Pipelines management**.
  3. Click the name of your pipeline (`example-pipeline`) to see its execution history. In the list of runs for a specific date, you can see individual pipeline runs and the breakdown of individual actions within each pipeline run.
  4. Click a task ID to see the task execution logs. Because the example PySpark script was executed in Managed Service for Apache Spark, the task logs will have a link to the Batch logs.



## Troubleshoot and fix pipeline failures

When your pipeline fails, you see a **Diagnose** button in the **Pipelines management** pane.

###  Agentic 

When you click the **Diagnose** button, the Agent generates a prompt to troubleshoot the pipeline failure. The prompt is either copied to your clipboard or opened in a new chat session.

The agent uses specialized skills to troubleshoot pipelines, focusing on collecting logs, cross-checking deployed code and the workspace, and generating a root cause analysis (RCA).

Possible next steps after receiving the RCA are as follows:

  * Apply the root cause analysis in the current workspace.
  * Ask the agent to create a new branch and apply the changes there.
  * Open a Cloud Customer Care ticket with the RCA details.



For help troubleshooting issues with the extension, see [Troubleshoot](https://docs.cloud.google.com/data-agent-kit/troubleshooting).

## What's next

  * [Mitigate prompt injection risks](https://docs.cloud.google.com/data-agent-kit/prompt-injection-risk)
  * [Managed Service for Apache Spark overview](https://docs.cloud.google.com/dataproc-serverless/docs/overview)
  * [Codelab: Analytics with the Data Agent Kit and Antigravity](https://codelabs.developers.google.com/dak-analytics-eng-antigravity-ide#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
