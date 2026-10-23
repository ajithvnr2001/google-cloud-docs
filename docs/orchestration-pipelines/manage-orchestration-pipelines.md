---
url: https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines/
title: Manage orchestration pipelines \u00a0|\u00a0 Orchestration Pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:16.901938+00:00
---

# Manage orchestration pipelines  |  Orchestration Pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Guides ](https://docs.cloud.google.com/orchestration-pipelines/overview)



Send feedback 

#  Manage orchestration pipelines Stay organized with collections  Save and categorize content based on your preferences. 

You can manage orchestration pipelines manage orchestration pipelines deployed to runner environments using Google Cloud CLI commands.

## About deployment environments

Your project can have one or more _deployment environments_. Each deployment environment's configuration defines how pipelines and resources that belong to this environment are deployed. For example, you can have one deployment environment for developing, and another environment for production. These deployment environments can have separate sets of pipelines and run in different runner environments.

Each deployment environment must have a _runner environment_. Managed Airflow is the orchestration engine that runs your pipelines after they're deployed. A runner environment is a [Managed Airflow environment](https://docs.cloud.google.com/composer/docs/latest/composer-overview) that you've assigned to your deployment environment.

## About pipeline bundles

Orchestration pipelines are deployed in _pipeline bundles_. A pipeline bundle contains one or more pipelines and pipeline assets that share a common deployment cycle.

Each bundle can have _multiple versions_. When you deploy a bundle, all pipelines and accompanying scripts in the bundle package of a specific version are deployed together. If a pipeline run is triggered, all pipelines and pipeline assets will remain at the bundle version that was used to start the run, even if you deploy a new version meanwhile.

## View the list of pipelines

###  gcloud 

To view the list of orchestration pipelines in a deployment environment, run the following Google Cloud CLI command in the directory where the `deployment.yaml` file is located:
    
    
    gcloud beta orchestration-pipelines list \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --owner OWNER_NAME
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: list pipelines in the specified deployment environment.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * (Optional) `BUNDLE_NAME`: list pipelines that belong to the specified bundle.

  * (Optional) `OWNER_NAME`: if specified, list pipelines that belong to the specified owner.




Example:
    
    
    gcloud beta orchestration-pipelines list \
      --environment example-deployment-environment \
      --bundle example-pipeline-bundle \
      --owner example-pipeline-owner
    

###  Console 

To view the list of orchestration pipelines in a deployment environment:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Orchestration Pipelines** tab. The tab displays the list of all pipelines deployed in your environment.




## View the detailed description of a pipeline

###  gcloud 

To view the description of a specific pipeline, run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines describe \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --pipeline PIPELINE_NAME
    
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment of the pipeline.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * `BUNDLE_NAME`: bundle that the pipeline belongs to.

  * `PIPELINE_NAME`: name of the pipeline.




Example:
    
    
    gcloud beta orchestration-pipelines list \
      --bundle example-pipeline-bundle \
      --pipeline example-pipeline \
      --environment example-deployment-environment
    

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Orchestration Pipelines** tab. The tab displays the list of all pipelines deployed in your environment.

  4. Click the name of the pipeline. The **Pipeline details** page opens:

     * The **Details** tab displays detailed information about the pipeline, such as pipeline ID, status, and source commit SHA.
     * The **Graph** tab displays a graph that outlines individual actions of the pipeline. Click graph nodes to see detailed information about each action.
     * The **YAML source** tab shows the pipeline definition.
     * The **Run history** tab shows the history and status of the pipeline runs.



## Deploy a pipeline bundle

This command deploys pipeline bundles and pipeline assets according to the provided deployment configuration. Make sure that you've already [configured the pipeline deployment](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines) before running this command.

To deploy a pipeline bundle for a deployment environment:

  * Deploy committed changes: After you've committed changes to your pipeline assets, pipeline definitions, and deployment configuration, you can deploy a new version of the pipeline bundle to the runner environment. The new bundle's ID will be linked to the commit in your repository. This deployment type is intended to usually be run as part of CI/CD. For example, through the GitHub Actions workflow.
  * Deploy a local bundle version: Deploy current versions of pipeline assets, pipeline definitions, and deployment configuration. The new bundle ID will be marked as a local deployment. This deployment type is intended for development purposes.

**Important:** Pipelines in local bundle versions are always **paused when deployed**. If a pipeline has a schedule, it won't trigger on it. You can trigger a manual pipeline run instead.



To deploy committed changes, run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment DEPLOYMENT_ENVIRONMENT \
    

To deploy a local version, use the `--local` argument:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment DEPLOYMENT_ENVIRONMENT \
      --local
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment of the pipeline.



Example:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment example-deployment-environment
    

Example output contains the deployment status.
    
    
    --- Pipeline Deployment Status ---
    Pipeline 'example-pipeline': [OK] (Status: HEALTHY)
    
    --- Pipeline Deployment full details ---
    ...
    
    

## Trigger a manual run of a pipeline

You can trigger a manual run of a specific orchestration pipeline:

  * The pipeline bundle must already be deployed before you trigger it.

  * You can trigger only the latest deployed version of the pipeline in the bundle. After the run is triggered, pipelines will always execute all of its tasks in the bundle version it was started with, even if you upload a newer bundle version of code in the meantime.


**Important:** The pipeline will **run immediately** , outside its defined schedule.

To trigger a manual run, execute the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines trigger \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --pipeline PIPELINE_NAME
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment of the pipeline.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * `BUNDLE_NAME`: bundle that the pipeline belongs to.

  * `PIPELINE_NAME`: name of the pipeline.




Example:
    
    
    gcloud beta orchestration-pipelines trigger \
      --environment example-deployment-environment \
      --bundle example-pipeline-bundle \
      --pipeline example-pipeline
    

## List run history of a pipeline

###  gcloud 

To view the history of runs of a single orchestration pipeline, including runs across all previous pipeline versions, run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines runs list \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --pipeline PIPELINE_NAME
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment where the pipeline is located.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * `BUNDLE_NAME`: bundle that the pipeline belongs to.

  * `PIPELINE_NAME`: name of the pipeline.




Example:
    
    
    gcloud beta orchestration-pipelines runs list \
      --environment example-deployment-environment \
      --bundle example-pipeline-bundle \
      --pipeline example-pipeline
    

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Orchestration Pipelines** tab. The tab displays the list of all pipelines deployed in your environment.

  4. Click the name of the pipeline. The **Pipeline details** page opens.

  5. Go to the **Run history** tab. The tab displays the history and status of the pipeline runs.

  6. Click a DAG run ID to go to the DAG run details page.




## List pipeline run details

To view the details of a single orchestration pipeline run, run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines runs describe \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --pipeline PIPELINE_NAME \
      --run-id RUN_ID
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment where the pipeline is located.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * `BUNDLE_NAME`: bundle that the pipeline belongs to.

  * `PIPELINE_NAME`: name of the pipeline.

  * `RUN_ID`: the identifier of the pipeline run. You can obtain this ID from the list of runs.




Example:
    
    
    gcloud beta orchestration-pipelines runs describe \
      --environment example-deployment-environment \
      --bundle example-pipeline-bundle \
      --pipeline example-pipeline \
      --run-id scheduled__2026-04-20T02:00:00+00:00
    

Example output:
    
    
    pipelineRuns:
    - actions:
      - end_date: '2026-04-21T02:02:31.947672Z'
        execution_date: '2026-04-20T02:00:00Z'
        max_retries: 1
        metadata:
          airflow_dag_id: example-pipeline-bundle__v__33816e2690e93d03ee7b67d16765d9825549636c__example-pipeline
          airflow_task_instances:
          - end_date: '2026-04-21T02:02:31.947672Z'
            execution_date: '2026-04-20T02:00:00Z'
            max_retries: 1
            name: new_pyspark_task_1775735209136
            start_date: '2026-04-21T02:00:17.256040Z'
            state: SUCCEEDED
            try_number: 1
        name: new_pyspark_task_1775735209136
        start_date: '2026-04-21T02:00:17.256040Z'
        state: SUCCEEDED
        try_number: 1
      bundle_id: example-pipeline-bundle
      end_date: '2026-04-21T02:02:32.455241Z'
      execution_date: '2026-04-20T02:00:00Z'
      metadata:
        airflow_dag_id: example-pipeline-bundle__v__33816e2690e93d03ee7b67d16765d9825549636c__example-pipeline
      pipeline_id: example-pipeline
      pipeline_run_id: scheduled__2026-04-20T02:00:00+00:00
      start_date: '2026-04-21T02:00:00.952825Z'
      state: SUCCEEDED
      type: SCHEDULED
      version: 33816e2690e93d03ee7b67d16765d9825549636c
    

## Pause scheduled pipeline runs

Once paused, the pipeline won't run on its schedule. You can trigger a manual pipeline run for such pipelines. Doing so will keep the pipeline paused and will create a manual pipeline run outside of the schedule. Unpause the pipeline to enable its schedule.

**Important:** Pipelines in local bundle versions are always **paused when deployed**. Even if a local pipeline version pipeline has a defined schedule, it won't trigger on it.

To pause all scheduled pipeline runs, run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines pause \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --pipeline PIPELINE_NAME \
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment where the pipeline is located.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * `BUNDLE_NAME`: bundle that the pipeline belongs to.

  * `PIPELINE_NAME`: name of the pipeline.




Example:
    
    
    gcloud beta orchestration-pipelines pause \
      --environment example-deployment-environment \
      --bundle example-pipeline-bundle \
      --pipeline example-pipeline
    

## Unpause scheduled pipeline runs

To unpause scheduled pipeline runs, run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines unpause \
      --environment DEPLOYMENT_ENVIRONMENT \
      --bundle BUNDLE_NAME \
      --pipeline PIPELINE_NAME \
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment where the pipeline is located.

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

  * `BUNDLE_NAME`: bundle that the pipeline belongs to.

  * `PIPELINE_NAME`: name of the pipeline.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
