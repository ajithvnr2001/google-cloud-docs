---
url: https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines/
title: Deploy orchestration pipelines \u00a0|\u00a0 Orchestration Pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:03.000962+00:00
---

# Deploy orchestration pipelines  |  Orchestration Pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Guides ](https://docs.cloud.google.com/orchestration-pipelines/overview)



Send feedback 

#  Deploy orchestration pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the process of creating deployment environment configurations for your orchestration pipelines.

## About deployment environments

Your project can have one or more _deployment environments_. Each deployment environment's configuration defines how pipelines and resources that belong to this environment are deployed. For example, you can have one deployment environment for developing, and another environment for production. These deployment environments can have separate sets of pipelines and run in different runner environments.

Each deployment environment must have a _runner environment_. Managed Airflow is the orchestration engine that runs your pipelines after they're deployed. In Preview, the only supported runner environment is a [Managed Airflow environment](https://docs.cloud.google.com/composer/docs/latest/composer-overview) that you've assigned to your deployment environment.

You can specify an _artifact bucket_ for a deployment environment. This bucket will store versioned pipeline assets that pipeline executes and results of some [actions](https://docs.cloud.google.com/orchestration-pipelines/reference/orchestration-pipelines-dsl-reference) that output to the artifact bucket.

## About pipeline bundles

Orchestration pipelines are deployed in _pipeline bundles_. A pipeline bundle contains one or more pipelines and pipeline assets that share a common deployment cycle.

Each bundle can have _multiple versions_ :

  * When you deploy a bundle, all pipelines and accompanying scripts in the bundle package of a specific version are deployed together.
  * There is exactly one current version of the bundle (the one that was deployed as the latest one), while individual pipeline runs that were triggered with previous code version will continue the execution uninterrupted.
  * You can't manually trigger pipeline in versions different than the current one.
  * If a pipeline is deleted from a bundle and the new version of the bundle is deployed, the pipeline will not run in the new version, but previous actively running executions will continue.



## Before you begin

  * Make sure that you've already [created a runner environment](https://docs.cloud.google.com/orchestration-pipelines/create-runner-environments).



## Initialize pipeline bundle scaffolding

Orchestration Pipelines provides a gcloud CLI command to initialize a scaffolding for orchestration pipelines in your repository.

**Important:** Initialize pipeline scaffolding **only once**. After you initialize pipelines, it's no longer possible to do so again because the new scaffolding would overwrite the configuration changes you might have made. You can add new pipelines by creating new pipeline definition files in your project and adding them to the deployment configuration.

The scaffolding contains the following:

  * `orchestration-pipeline.yaml`: an example pipeline definition which contains a schedule, but no defined actions.
  * `deployment.yaml`: an example pipeline deployment configuration which defines how your pipeline must be deployed. Contains configuration for the runner environment, the artifacts bucket, and any other resources used by your pipeline actions.
  * `.github/workflows/validate.yaml`: An example GitHub action that validates your pipeline when a pull request to the `main` branch is created.
  * `.github/workflows/deploy.yaml`: An example GitHub action that deploys your pipeline when you merge changes to the `main` branch of your GitHub repository.



To initialize an orchestration pipeline:

  1. Navigate to your repository or project directory. The command will create new files in the directory where you run it.

  2. Run the following gcloud CLI command:
         
         gcloud beta orchestration-pipelines init PIPELINE_NAME \
           --environment DEPLOYMENT_ENVIRONMENT \
           --composer-environment RUNNER_ENVIRONMENT \
           --artifacts-bucket ARTIFACTS_BUCKET_NAME \
           --project PROJECT_ID \
           --region REGION \
           --service-account SERVICE_ACCOUNT
         

Replace the following:

     * `PIPELINE_NAME`: name for the initial pipeline.
     * `DEPLOYMENT_ENVIRONMENT`: name for the initial deployment environment.
     * `RUNNER_ENVIRONMENT`: name of the [runner environment](https://docs.cloud.google.com/orchestration-pipelines/create-runner-environments). 
     * `ARTIFACTS_BUCKET_NAME`: a Cloud Storage bucket that will be used to store pipeline action artifacts, without the `gs://` prefix. 
     * `PROJECT_ID`: the project ID of a Google Cloud project where the runner environment is located.
     * `REGION`: the region where the runner environment is located.
     * `SERVICE_ACCOUNT`: the service account which will be preset as a variable. Set this value to the runner environment's service account. You can use this variable in pipeline definitions and resource profiles. For example, as a value for the `impersonationChain` parameter [in actions that use an impersonation chain](https://docs.cloud.google.com/orchestration-pipelines/reference/orchestration-pipelines-dsl-reference).

You can obtain the service account of your runner environment by [viewing the environment's details](https://docs.cloud.google.com/composer/docs/latest/update-environments#details). In gcloud CLI, the environment service account is provided in the `nodeConfig.serviceAccount` key.

**Important:** This parameter specifies a value for a variable. Your runner environment **still runs with the original service account** that you specified when you've created it. Even if you change the variable's value to a different service account, it will still execute all pipeline actions using the runner environment's service account.

Example:
    
    gcloud beta orchestration-pipelines init example-pipeline \
      --environment development \
      --composer-environment production-runner-us-central1 \
      --artifacts-bucket production-artifacts \
      --project example-production-project \
      --region us-central1 \
      --service-account example-account@example-project.iam.gserviceaccount.com
    




## Add runner environment configuration

Runner environment is specified in the `composer_environment` key of a deployment environment. If you use several deployment environments, you can specify a separate runner environment for each.

Runner environment's name in the `composer_environment` key along with `project` and `region` keys in the development environment's configuration specify the runner environment where the pipeline is deployed.

The following example demonstrates adding a runner environment with the name `example-runner-environment` located in the `us-central1` region, in the `example-development-project` project:
    
    
    environments:
      example-development-environment:
        project: "example-development-project"
        region: "us-central1"
        composer_environment: "example-runner-environment"
        ...
    

**Note:** The full resource path for this environment is `//composer.googleapis.com/projects/example-development-project/locations/us-central1/environments/example-runner-environment`. You can use the full resource path, for example, to [trigger pipeline runs](https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines#trigger) specifically in this runner environment.

### Adjust runner environment configuration

You can configure your runner environment just like any other Managed Service for Apache Airflow environment:

  * [Install Python dependencies](https://docs.cloud.google.com/composer/docs/latest/install-python-dependencies), for example, to run your pipeline's Python scripts locally on the runner environment.
  * [Scale environments](https://docs.cloud.google.com/composer/docs/latest/scale-environments) to provide more or less resources, or change how the runner environment should scale its Airflow workers.
  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/latest/override-airflow-configurations) to configure Airflow.



## Add your pipeline assets and configure actions

Edit your pipeline's definition file to include actions and pipeline assets:

  * See [Orchestration Pipelines DSL reference](https://docs.cloud.google.com/orchestration-pipelines/reference/orchestration-pipelines-dsl-reference) for code examples and descriptions of action parameters.
  * For an extended walkthrough example, see [Build data engineering pipelines](https://docs.cloud.google.com/data-agent-kit/build-pipelines) in the Google Cloud Data Agent Kit documentation.



### Hello world action example

The following is an example of a minimalistic pipeline action. You can use it to test the deployment environment's configuration.

  1. Add the following action to your scaffolding pipeline, replacing `actions: []`:
         
         actions:
           - python:
               name: "hello_world_script_run"
               executionTimeout: "30m"
               mainFilePath: "scripts/hello_world.py"
               pythonCallable: "main"
               engine:
                 local: {}
         

  2. Create a new subdirectory named `scripts` in your repository, and save the following file as `/scripts/hello_world.py`:
         
         def main():
           print("Hello, World!")
         




## Validate pipelines

The validation command checks the syntax and type correctness of the pipeline definition files, and also performs semantic checks for resources such as the Google Cloud project and Managed Service for Apache Airflow environment in both deployment configuration and pipeline definition files.

By default, the full validation of all deployment environments is performed, including reaching out to remote runner environments. You can validate specific parts of your deployment configuration with the following parameters:

  * `--mode`: set to `syntax-only` to not reach to remote runner environments. Default is `full`.
  * `--environment`: validate only a specific environment.
  * `--pipeline-paths`: comma-separated list of paths to pipeline definition files to validate.
  * `--substitutions` and `--substitutions-file`: substitute deployment configuration parameters during the validation.



You can run this command as a quick check before deploying local pipeline versions and as a GitHub action as a part of your CI/CD workflow.

Run the following command in your repository to validate your pipelines:
    
    
    gcloud beta orchestration-pipelines validate
    

## Deploy a pipeline bundle

This section describes different ways to deploy your pipelines.

Orchestration Pipelines support two ways to deploy your pipeline bundles. These approaches are designed to work together during different stages of the development and release workflow:

  * Deploy a local bundle version: Deploy current versions of pipeline assets, pipeline definitions, and deployment configuration. The new bundle ID will be auto-generated based on the working space name and md5 of files in the bundle.

This deployment type is intended for development purposes. We also recommend to create a separate deployment configuration that deploys the pipelines to a staging runner environment.

  * Deploy committed changes: After you've committed changes to your pipeline assets, pipeline definitions, and deployment configuration, you can deploy a new version of the pipeline bundle to the runner environment. The new bundle's ID will be linked to the git commit SHA in your repository.

This deployment type is intended to be run as part of CI/CD, For example, through a GitHub Action. You can also deploy committed changes from a local Git repository.




Orchestration Pipelines support several ways to substitute parameters in your pipeline definition and deployment configuration files, which might be useful when you deploy pipelines both for local development and for commands executed in GitHub actions. For example, you can substitute parameters through using the `--substitutions` argument in gcloud CLI commands, or through setting an environment variable, or through obtaining the value from GitHub secrets.

### Run deployment commands

###  Local 

**Important:** Pipelines in local bundle versions are always **[paused](https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines#pause) when deployed**. If a pipeline has a schedule, it won't trigger on it. You can [trigger a manual pipeline run](https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines#trigger) instead.

To deploy a local bundle version, use the `--local` argument:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment DEPLOYMENT_ENVIRONMENT \
      --local
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment of the pipeline.



Example:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment example-deployment-environment \
      --local
    

**Note:**

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

Example output contains the pipeline bundle name and version, and the deployment status:
    
    
    Bundle ID: bundle-local-example-orchestrationpipelines
    Version ID: local-14776d43ebba
    
    ...
    
    --- Pipeline Deployment Status ---
    Pipeline 'example-pipeline': [OK] (Status: HEALTHY)
    
    --- Pipeline Deployment full details ---
    
    ...
    
    

###  Committed 

To deploy changes, make sure that your changes are committed in your repository. Run the following command in gcloud CLI:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment DEPLOYMENT_ENVIRONMENT
    

Replace the following:

  * `DEPLOYMENT_ENVIRONMENT`: deployment environment of the pipeline.



Example:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment example-deployment-environment
    

**Note:**

As an alternative, you can run this command for a specific runner environment. In this case, replace the `--environment` argument with the `--runner` argument and specify the full resource ID of your runner environment. Example: `//composer.googleapis.com/projects/example-project/locations/us-central1/environments/example-runner-environment`.

Example output contains the pipeline bundle name and version, and the deployment status:
    
    
    Bundle ID: bundle-local-example-orchestrationpipelines
    Version ID: local-14776d43ebba
    
    ...
    
    --- Pipeline Deployment Status ---
    Pipeline 'example-pipeline': [OK] (Status: HEALTHY)
    
    --- Pipeline Deployment full details ---
    
    ...
    
    

###  GitHub Action 

The pipeline scaffolding has two example GitHub actions that can get you started with deploying and validating your pipelines through a GitHub action. When you upload these files to GitHub, your repository is configured with these actions. For information about configuring more complex GitHub actions, see [Deploying with GitHub Actions](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments) in GitHub documentation.

To use the example GitHub actions:

  1. [Create a separate service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) that is going to run gcloud CLI commands from GitHub actions.

  2. Assign roles that allow running deployment and validation commands to this service account. 

**Important:** It's not possible to use a Google Account for this purpose. Don't use your runner environment's service account because it has permissions that are too broad for this task.
  3. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) for this service account.

  4. Add the `GCP_SA_KEY` secret to your GitHub repository and set its value to the created service account key. For more information about adding secrets, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets#creating-secrets-for-a-repository).




## Deployment configuration

This section provides additional configuration you can apply to a deployment environment.

### Add or remove another pipeline

To add another pipeline to an existing deployment environment:

  1. Add a pipeline definition file and pipeline assets to the repository.
  2. In your deployment configuration, add a new `source` key with the value pointing to the new pipeline definition file.



Example:
    
    
    environments:
      dev:
    
        ...
    
        pipelines:
          - source: example-pipeline.yaml
          - source: another-pipeline.yaml
    

To remove a pipeline:

  1. In your deployment configuration, remove the `source` key for the pipeline.
  2. Remove the pipeline definition file and pipeline assets to the repository.
  3. Deploy the new version of the pipeline. The pipeline will not be present in the new bundle version.



### Add another deployment environment

To add another deployment environment:

  1. In your deployment configuration add a new key to the `environments` mapping.
  2. Make sure that your deployment configuration and pipeline definitions use variables and deployment configuration variables to run pipeline actions that require differentiating between Google Cloud resources that belong to each environment.



Example:
    
    
    environments:
    
      example-development-environment:
        project: "example-development-project"
        region: "us-central1"
        composer_environment: "development-runner-us-central1"
        ...
        variables:
          service_account: "another-service-account@example-development-project.iam.gserviceaccount.com"
        ...
    
      example-production-environment:
        project: "example-production-project"
        region: "us-central1"
        composer_environment: "production-runner-us-central1"
        ...
        variables:
          service_account: "example-account@example-project.iam.gserviceaccount.com"
    
    

### Variables, secrets, and substitution

After you define variables in your deployment configuration, you can use them in pipeline definitions and resource profiles.

#### Add custom variables

You can add your own variables to the `variables` key in the deployment configuration:

  1. In your deployment configuration environment, add the `variables` key.
  2. Add a mapping of variable names and values.
  3. Obtain the variable's value in your pipeline definitions and resource profiles by enclosing the variable's name in double curly brackets: `{{ example_variable }}`. 



The following example sets the same variables in two deployment environments.
    
    
    environments:
      example-development-environment:
        project: "example-development-project"
        region: "us-central1"
        composer_environment: "development-runner-us-central1"
        artifact_storage:
          bucket: "development-artifacts"
          path_prefix: pipelines
        pipelines:
          - source: example-pipeline.yaml
        variables:
          service_account: "another-service-account@example-development-project.iam.gserviceaccount.com"
          network_uri: projects/example-development-project/global/networks/default
    
      example-production-environment:
        project: "example-production-project"
        region: "us-central1"
        composer_environment: "production-runner-us-central1"
        artifact_storage:
          bucket: "production-artifacts"
          path_prefix: pipelines
        pipelines:
          - source: example-pipeline.yaml
        variables:
          service_account: "example-account@example-project.iam.gserviceaccount.com"
          network_uri: projects/example-production-project/global/networks/vpc-main
    

The following is a Managed Service for Apache Spark resource profile that reads these variables. Actions in your pipeline definition file (`example-pipeline.yaml`) can use the same resource profile and you don't need to adjust them between production and development environments.
    
    
    profileId: serverless-standard
    type: dataproc.session
    definition:
      environmentConfig:
        execution_config:
          service_account: "{{ service_account }}"
          network_uri: "{{ network_uri }}"
    

#### Access deployment configuration parameters

Some parameters of your deployment configuration are available as variables as well:

  * `project`
  * `region`
  * `composer_environment`
  * `COMMIT_SHA`: the current commit SHA of the git repository. You can use this variable, for example, by substituting its value when you deploy a local pipeline bundle version. In this way, actions that depend on the commit SHA value will still operate on the correct file content.



In the following example, the pipeline definition sets defaults for pipeline actions based on the deployment configuration parameters `project` and `region`.
    
    
    pipelineId: example-pipeline
    description: Example pipeline
    runner: 'airflow'
    owner: 'data-eng-team'
    modelVersion: '1.0'
    defaults:
      projectId: {{ project }}
      location: {{ region }}
      executionConfig:
        retries: 1
    

#### Access GitHub Action secrets

You can use GitHub secrets in your pipeline definition and deployment configuration files. When a pipeline is deployed through a GitHub action, the values of these secrets are passed both into the pipeline definitions and deployment configuration.

To create a secret that will be accessible during the deployment:

  1. On GitHub, add a secret with the `DEPLOY_VAR_` prefix. Example: `DEPLOY_VAR_API_KEY`.

For more information about creating secrets, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets#creating-secrets-for-a-repository) in GitHub documentation.

  2. Add the same environment variable to your GitHub workflow. Read the value of this variable from GitHub secrets.

Example:
         
         jobs:
           deploy:
             runs-on: ubuntu-latest
             env:
               DEPLOY_VAR_API_KEY: ${{ secrets.API_KEY }}
         
             steps:
         
             ...
         
         

For more information about adding environment variables to workflows, see [Store information in variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables#defining-environment-variables-for-a-single-workflow) in GitHub documentation.

  3. Use the variable name (without the `DEPLOY_VAR_` prefix) in your pipeline definition files and deployment configuration. Example: `{{ API_KEY }}`.

  4. (Optional) To deploy a local version of a pipeline that uses GitHub secrets, you can substitute `DEPLOY_VAR_*` environment variables from the secret either through command-line parameters, or by defining them in the environment where you run deploy commands.




#### Substitute variables through command-line parameters

gcloud CLI deployment commands support the `--substitutions` argument, which you can use to override or set variables for your pipeline definitions and deployment configuration.

To substitute variables through command-line parameters, provide the list of variables and their values on the command-line:

Example:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment example-deployment-environment \
      --local \
      --substitutions=VARIABLE_NAME_1=value_1,VARIABLE_NAME_2=value_2
    

As an alternative, you can store substitutions in a YAML file and specify it in the `--substitutions-file` argument:
    
    
    gcloud beta orchestration-pipelines deploy \
      --environment example-deployment-environment \
      --local \
      --substitutions-file=substitutions.yaml
    

In the substitutions file, provide a mapping of variables: 
    
    
    VARIABLE_NAME_1: value_1
    VARIABLE_NAME_2: value_2
    

You can use the variable name in your pipeline definition files and deployment configuration. Example: `{{ VARIABLE_NAME_1 }}`.

#### Provide and substitute variables through environment variables

Your pipeline definitions and deployment configuration can use environment variables that have the `DEPLOY_VAR_` prefix.

  1. Set an environment variable:
         
         export DEPLOY_VAR_VARIABLE_NAME_1=value_1
         

  2. You can use the variable name (without the `DEPLOY_VAR_` prefix) in your pipeline definition files and deployment configuration. Example: `{{ VARIABLE_NAME_1 }}`.




## What's next

  * [Manage pipelines and check pipeline run history and status](https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
