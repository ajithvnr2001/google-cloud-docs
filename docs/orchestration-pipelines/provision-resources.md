---
url: https://docs.cloud.google.com/orchestration-pipelines/provision-resources/
title: Provision resources \u00a0|\u00a0 Orchestration Pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:12.976720+00:00
---

# Provision resources  |  Orchestration Pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/provision-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Guides ](https://docs.cloud.google.com/orchestration-pipelines/overview)



Send feedback 

#  Provision resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to provision resources for your pipelines.

## About resource provisioning in Orchestration Pipelines

Orchestration Pipelines uses an Infrastructure-as-Code (IaC) approach to manage Google Cloud resources used by your data pipelines, which brings the following benefits:

  * Version Control. Infrastructure changes are tracked in Git.
  * Repeatability. Environments can be recreated reliably.
  * Collaboration. Team members can review and contribute to infrastructure definitions.
  * Automation. Integrates into CI/CD pipelines.
  * Optionality and Coexistence. The resource provisioning framework is optional. If you already use Terraform or other established IaC practices for resource provisioning, you can continue to do so. You can manage a subset of resources relevant to a specific pipeline or application, potentially coexisting with resources managed by other tools.



In Orchestration Pipelines, your project can have one or more _deployment environments_. Each deployment environment's configuration defines how pipelines and resources that belong to this environment are deployed. For example, you can have one deployment environment for developing, and another environment for production.

Example of a deployment environment configuration. Provisioned resources are defined in the `resources` mapping.

**Note:** For more information about using `variables` and `secrets`, see [Variables, secrets, and substitution](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines#variables-secrets-substitution).
    
    
    environments:
      dev:
        project: example-dev-project
        region: us-central1
        variables:
          dataset_name: marketing_analytics_dev
        secrets:
          dts_api_key: "projects/example-dev-project/secrets/dev-dts-key/versions/latest"
        resources:
          - type: dataproc.cluster
            name: example-static-cluster-resource
            definition:
              clusterName: example-static-cluster
    

When you deploy your pipeline, Orchestration Pipelines uses a stateless "create or update" model to provision resources that you've defined:

  * If a resource is defined but doesn't exist, Orchestration Pipelines creates it.

  * If a resource exists:

    * (Default) Update the resource's configuration to match the definition.

    * If you define this behavior in the resource's configuration, Orchestration Pipelines can ignore changes or re-create a resource.

  * If you delete a resource's definition from the configuration, **it doesn't result in the deletion of the resource**. This approach prioritizes safety and prevents accidental data loss.

  * If you rename an existing resource, Orchestration Pipelines creates a new resource with the new name and keeps the original resource.




### Provisioned resources compared to resource profiles

Resource profiles are template files containing the definition of one or more Google Cloud resources. They are different from provisioned resources and can be used together with them:

  * With provisioned resources: Instead of defining the same resource configuration inline within each development environment in your `deployment.yaml`, you can define it once in a profile and then reference it. Provisioned resources support a wide range of [resource types](https://docs.cloud.google.com/orchestration-pipelines/reference/resource-types) that can be defined in resource profiles.

  * With pipeline actions: You can use resource profiles in actions where resources are provisioned for the duration of an action. By using a resource profile instead of specifying the resource's configuration inline, you can keep the resource configuration separate from the pipeline action and reuse one configuration for several pipeline actions. Pipeline actions support resource profiles only for Managed Service for Apache Spark resources, for example when executing pipeline actions in an ephemeral cluster.




## View available resource types

See [Resource types](https://docs.cloud.google.com/orchestration-pipelines/reference/resource-types).

You can also view all available resources in gcloud CLI with the following command:
    
    
    gcloud beta orchestration-pipelines resource-types list
    

## Add a new resource

**Note:** If you want to manage resources using other means, such as with Terraform, or by creating them manually, you don't need to add them as provisioned resources. Instead, configure your pipeline actions to access them directly.

To add a new provisioned resource to the deployment environment's configuration, add its definition as follows:

  1. In your deployment environment's configuration, add a new item to the `environments.DEVELOPMENT_ENVIRONMENT.resources` list.

  2. Specify the following keys:

     * `type`: The type of the Google Cloud resource to provision. Examples: `bigquery.dataset`, `dataform.repository`. You can view available resource types using a gcloud CLI command.

     * `name`: A logical name for the resource within the `deployment.yaml` file.

**Important:** In addition to the resource's logical name, a provisioned resource can have its own name in Google Cloud as part of its `definition`, usually in the `definition.name` key. We recommend to **omit the`name` key in the `definition` mapping**. In this case, the name for the provisioned resource will be set to the resource's logical name. If you want to explicitly specify a name in the resource's definition, make sure to keep it the same as the resource's logical name.
     * `parent`: Specifies a parent resource for resource types that require one. Put the parent resource's `name` as the value.

     * `updateAction`: Specifies which action must be taken when a change is detected in the resource's configuration:

       * (Default) `patch`: Update the resource's properties that have changed.

The update operation only modifies the properties specified in the resource's configuration (YAML), leaving other existing properties unchanged. You can use this behavior, for example, to manage only properties important to pipeline execution, and keep other properties configured manually.

If changes affect immutable fields or the resource is immutable, the deployment fails. In such cases, we recommend adjusting the definition to only modify mutable fields. If this isn't possible, you can change the update action to `recreate`.

       * `skip`: Ignore changes and don't update the resource's configuration.

We recommend to use this option when you want to manage the resource's existence but perform the configuration changes and updates using other means, for example, manually.

       * `recreate`: If any changes are detected, delete the existing resource and then create a new one based on the current resource's definition.

**Caution:** This operation is **destructive** and can result in data loss. This operation has two steps: first, the resource is deleted, and then a new resource is created. If a resource creation fails, the deletion operation **isn't rolled back**.

We recommend to use this option for resources that are entirely immutable or when changes are made to fields that can't be updated in-place.

     * `definition`: Resource's specification, as a mapping that reflects resource's configuration structure in the resource's API.

     * (Optional) `metadata`: Orchestration Pipelines-specific metadata. Some resource types use metadata fields to configure the resource in Google Cloud For example, the `metadata.location` field can be used to create zonal resources.

  3. [Validate and deploy](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines) your pipeline. Orchestration Pipelines will provision the new resource when the pipeline is deployed.




### Example: Long-running resources

This example demonstrates adding a long-running resource, in this case, a static Managed Service for Apache Spark cluster. Once provisioned, it can be used in pipeline actions. We recommend to use this general approach when your pipelines use persistent resources.

The following example adds a static Managed Service for Apache Spark cluster named `example-static-cluster` to the `dev` deployment environment. The resource's definition is provided based on the [Dataproc API](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters).
    
    
    environments:
      dev:
        project: "example-project"
        region: "us-central1"
        # A runner environment for executing pipeline actions
        composer_environment: "example-runner-environment"
    
        resources:
          - type: dataproc.cluster
            name: example-static-cluster
            updateAction: patch
            definition:
              config:
                masterConfig:
                  numInstances: 1
                  machineTypeUri: n1-standard-4
                workerConfig:
                  numInstances: 3
                  machineTypeUri: n1-standard-4
    

This cluster can be used in pipeline actions as usual. There's no difference in usage compared to, for example, a manually created cluster.
    
    
    modelVersion: "1.0"
    pipelineId: "example-dataproc-pipeline"
    ...
    actions:
      - pyspark:
          name: "run-pyspark-with-pyfiles-on-existing-cluster"
          engine:
            dataprocOnGce:
              existingCluster:
                clusterName: "example-static-cluster"
                location: {{ region }}
                projectId: {{ project }}
          mainFilePath: "scripts/my_spark_job_with_pyfiles.py"
          pyFiles:
            - "scripts/lib1.py"
    

### Example: Automated build and release process for Dataform

This example demonstrates an automated build and release process for Dataform. In the example scenario:

  1. A Dataform repository is [connected to a GitHub repository through Developer Connect](https://docs.cloud.google.com/dataform/docs/connect-repository).

  2. You push changes to the GitHub repository.

  3. After the changes are pushed, you deploy the pipeline.

  4. Dataform pulls the code from the GitHub repository, creates a compilation result, and makes it ready for execution.

  5. A workflow configuration is then used run workflows with this automatically compiled release.




The following code example defines a Dataform repository, a release configuration, and a workflow configuration for it in the `dev` deployment environment:

  * The `gitCommitish: "{{ COMMIT_SHA }}"` line ties the release configuration to the specific Git commit being deployed. The `COMMIT_SHA` is a [variable](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines#variables-secrets-substitution) that resolves to the deployed pipeline bundle's commit SHA.
  * The `codeCompilationConfig.pipelineConfig.path` key points to a subfolder that contains pipeline assets. In this way, you can keep multiple Dataform pipelines in a single repository.
  * Setting `releaseCompilationResult` to `auto` in the definition of the `releaseConfig` instructs Orchestration Pipelines to trigger a Dataform compilation after the `releaseConfig` resource is created or updated with the new `gitCommitish`:

    1. The framework first upserts (updates or creates) the `releaseConfig` resource to point to the specified commit.
    2. Then, because of the `auto` setting, it calls the Dataform API to create a new Compilation Result based on the code at that commit.
    3. The `releaseConfig` is updated again to point to the newly created Compilation Result ID, making that version the "live" one.


    
    
    environments:
      dev:
        project: example-project
        region: us-central1
        composer_environment: example-runner-environment
        artifact_storage:
          bucket: example-bucket
          path_prefix: initialized-artifact-bucket
        pipelines:
          - source: initialized-pipeline.yaml
          - source: dataform_local_pipeline.yaml
          - source: dataform_service_pipeline.yaml
        resources:
          - name: {{ repository_name }}
            type: dataform.repository
            definition:
              labels:
                bigquery-deployment: preview
          - type: dataform.repository.releaseConfig
            name: subfolder-release
            parent: {{ repository_name }}
            definition:
              gitCommitish: {{ COMMIT_SHA }}
              releaseCompilationResult: auto
              codeCompilationConfig:
                pipelineConfig:
                  pipelineType: DATAFORM
                  path: weather_dataform
          - type: dataform.repository.workflowConfig
            name: {{ workflow_config_name }}
            parent: {{ repository_name }}
            definition:
              releaseConfig: subfolder-release
              invocationConfig:
                serviceAccount: {{ service_account }}
        variables:
          service_account: example-account@example-project.iam.gserviceaccount.com
          network_uri: projects/example-project/global/networks/default
          subnetwork_uri: projects/example-project/regions/us-central1/subnetworks/default
          region: us-central1
          repository_name: weather-aggregation-repo
          workflow_config_name: updated-subfolder-workflow
    

An example pipeline action that runs a workflow with the created workflow configuration:
    
    
    modelVersion: '1.0'
    pipelineId: dataform_service_pipeline
    description: Updated run Dataform pipeline via Dataform Service
    runner: airflow
    owner: data-eng-team
    
    defaults:
      projectId: {{ project }}
      location: {{ region }}
      executionConfig:
        retries: 1
    
    actions:
      - pipeline:
          name: run_dataform_service
          framework:
            dataform:
              dataformService:
                location: {{ region }}
                projectId: {{ project }}
                repositoryId: {{ repository_name }}
                workflowInvocation:
                  workflowConfig: projects/{{ project }}/locations/{{ region }}/repositories/{{
                    repository_name }}/workflowConfigs/{{ workflow_config_name }}
      - python:
          name: fibonacci_python
          mainFilePath: scripts/fibonacci.py
          pythonCallable: fibonacciTen
          engine:
            local: {}
      - sql:
          name: dummy_bq_query
          engine:
            bigquery:
              location: {{ region }}
          query:
            inline: 'SELECT COUNT(*) FROM `{{ project }}.weather_data.sensor_readings`'
    tags:
      - job:datacloud:vscode
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
