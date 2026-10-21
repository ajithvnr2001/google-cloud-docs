---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/orchestrate-pipelines/
title: Orchestrate pipelines \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:33.468150+00:00
---

# Orchestrate pipelines  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/orchestrate-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Orchestrate pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page explains pipeline orchestration with Managed Service for Apache Airflow and triggers. Cloud Data Fusion recommends using Managed Airflow to orchestrate pipelines. If you require a simpler way to manage orchestration, use triggers.

### Composer

## Orchestrate pipelines with Managed Airflow

Orchestrating pipeline execution in Cloud Data Fusion with Managed Airflow provides following benefits:

  * **Centralized workflow management:** uniformly manage the execution of multiple Cloud Data Fusion pipelines.
  * **Dependency management:** to ensure proper execution order, define dependencies between pipelines.
  * **Monitoring and alerting:** Managed Airflow provides monitoring capabilities and alerts for failures.
  * **Integration with other services:** Managed Airflow lets you orchestrate workflows that span across Cloud Data Fusion and other Google Cloud services.



To orchestrate Cloud Data Fusion pipelines using Managed Airflow, follow this process:

  1. **Set up the Managed Airflow environment.**

     * **Create a Managed Airflow environment.** If you don't have one, provision the environment in your Google Cloud project. This environment is your orchestration workspace.
     * **Give permissions.** Ensure the Managed Airflow service account has the necessary permissions to access Cloud Data Fusion (such as permission to start, stop, and list pipelines).
  2. **Define Directed Acyclic Graphs (DAG) for orchestration.**

     * **Create a DAG:** In Managed Airflow, create a DAG that defines the orchestration workflow for your Cloud Data Fusion pipelines.
     * **Cloud Data Fusion Operators:** Use Managed Airflow's Cloud Data Fusion Operators within your DAG. These operators let you interact programmatically with Cloud Data Fusion.



### Cloud Data Fusion operators

Cloud Data Fusion pipeline orchestration has the following operators:

`CloudDataFusionStartPipelineOperator`
    

Triggers the execution of a Cloud Data Fusion pipeline by its ID. It has the following parameters:

  * Pipeline ID
  * Location (Google Cloud region)
  * Pipeline namespace
  * Runtime arguments (optional)
  * Wait for completion (optional)
  * Timeout (optional)


`CloudDataFusionStopPipelineOperator`
    

Lets you stop a running Cloud Data Fusion pipeline.

`CloudDataFusionDeletePipelineOperator`
    

Deletes a Cloud Data Fusion pipeline.

### Build the DAG workflow

When you build the DAG workflow, consider the following:

  * **Defining dependencies:** Use the DAG structure to define dependencies between tasks. For example, you might have a task that waits for a pipeline in one namespace to complete successfully before triggering another pipeline in a different namespace.
  * **Scheduling:** Schedule the DAG to run at specific intervals, such as daily or hourly, or set it to be triggered manually.



For more information, see the [Managed Airflow overview](https://docs.cloud.google.com/composer/docs/concepts/overview).

### Triggers

## Orchestrate pipelines with triggers

Cloud Data Fusion triggers let you automatically execute a downstream pipeline upon the completion (success, failure, or any specified condition) of one or more upstream pipelines.

Triggers are useful for the following tasks:

  * Cleaning your data once, and then making it available to multiple downstream pipelines for consumption.
  * Sharing information, such as runtime arguments and plugin configurations, between pipelines. This task is called _payload configuration_.
  * Having a set of dynamic pipelines that run using the data from the hour, day, week, or month, instead of a static pipeline that must be updated for every run.



For example, you have a dataset that contains all information about your company's shipments. Based on this data, you want to answer several business questions. To do this, you create one pipeline that cleanses the raw data about shipments, called _Shipments Data Cleaning_. Then you create a second pipeline, _Delayed Shipments USA_ , which reads the cleansed data and finds the shipments within the USA that were delayed by more than a specified threshold. The _Delayed Shipments USA_ pipeline can be triggered as soon as the upstream _Shipments Data Cleaning_ pipeline successfully completes.

Additionally, since the downstream pipeline consumes the output of the upstream pipeline, you must specify that when the downstream pipeline runs using this trigger, it also receives the input directory to read from (which is the directory where the upstream pipeline generated its output). This process is called _passing payload configuration_ , which you define with runtime arguments. It lets you have a set of dynamic pipelines that run using the data of the hour, day, week, or month (not a static pipeline, which must be updated for every run).

**Note:** Don't trigger upgrades with Terraform. For more information, see the [limitations for Cloud Data Fusion upgrades](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#limitations).

To orchestrate pipelines with triggers, follow this process:

  1. **Create upstream and downstream pipelines.**

     * In the Cloud Data Fusion Studio, design and deploy the pipelines that form your orchestration chain.
     * Consider which pipeline's completion will activate the next pipeline (downstream) in your workflow.
  2. **Optional: pass runtime arguments for upstream pipelines.**

     * If you need to pass payload configuration as runtime arguments between pipelines, configure runtime arguments. These arguments can be passed to the downstream pipeline during execution.
  3. **Create an inbound trigger on the downstream pipeline.**

     * In the Cloud Data Fusion Studio, go to the **List** page. In the **Deployed** tab, click the name of the downstream pipeline. The Deploy view for that pipeline appears.
     * On the middle left side of the page, click **Inbound triggers**. A list of available pipelines appears.
     * Click the upstream pipeline. Select one or more of the upstream pipeline completion states (**Succeeds** , **Fails** , or **Stops**) as the condition for when the downstream pipeline should run.
     * If you want the upstream pipeline to share information (called _payload configuration_) with the downstream pipeline, click **Trigger config** and then follow the steps to pass payload configuration as runtime arguments. Otherwise, click **Enable trigger**.
  4. **Test the trigger.**

     * Initiate a run of the upstream pipeline.
     * If the trigger is configured correctly, the downstream pipeline automatically executes upon completion of the upstream pipelines, based on your configured condition.



### Pass payload configuration as runtime arguments

Payload configuration allows sharing of information from the upstream pipeline to the downstream pipeline. This information can be, for example, the output directory, the data format, or the day the pipeline was run. This information is then used by the downstream pipeline for decisions such as determining the right dataset to read from.

To pass information from the upstream pipeline to the downstream pipeline, you set the runtime arguments of the downstream pipeline with the values of either the runtime arguments or the configuration of any plugin in the upstream pipeline.

Whenever the downstream pipeline triggers and runs, its payload configuration is set using the runtime arguments of the particular run of the upstream pipeline that triggered the downstream pipeline.

To pass payload configuration as runtime arguments, follow these steps:

  1. Picking up where you left off in the [Creating an inbound trigger](https://docs.cloud.google.com/data-fusion/docs/how-to/using-triggers#create_inbound_trigger), after clicking **Trigger config** , any runtime arguments you [previously set](https://docs.cloud.google.com/data-fusion/docs/how-to/using-triggers#before_you_begin) for your upstream pipeline will appear. Choose the runtime arguments to pass from the upstream pipeline to the downstream pipeline when this trigger executes.
  2. Click the **Plugin config** tab to see a list of what will be passed from your upstream pipeline to your downstream pipeline when it is triggered.
  3. Click **Configure and Enable Trigger**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
