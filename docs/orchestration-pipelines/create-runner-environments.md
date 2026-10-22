---
url: https://docs.cloud.google.com/orchestration-pipelines/create-runner-environments/
title: Create runner environments \u00a0|\u00a0 Orchestration Pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:28.137955+00:00
---

# Create runner environments  |  Orchestration Pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/create-runner-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Guides ](https://docs.cloud.google.com/orchestration-pipelines/overview)



Send feedback 

#  Create runner environments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the process of creating runner environments that will execute your orchestration pipelines.

## About runner environments

Each deployment environment must have a _runner environment_. Managed Airflow is the orchestration engine that runs your pipelines after they're deployed. A runner environment is a [Managed Airflow environment](https://docs.cloud.google.com/composer/docs/latest/composer-overview) that you've assigned to your deployment environment.

## Before you begin

  * At the moment, the only available runner for Orchestration Pipelines on Google Cloud is Managed Service for Apache Airflow. All Managed Airflow [quotas](https://docs.cloud.google.com/composer/docs/quotas) and system limits apply. See [Managed Airflow pricing](https://cloud.google.com/composer/pricing) for more information about the costs of a runner environment.

  * Orchestration Pipelines can run on Managed Airflow (Gen 3) and (Gen 2) runner environments. In Managed Airflow (Gen 3), you can use both Airflow 3 and Airflow 2.

  * Orchestration Pipelines packages is preinstalled in Managed Airflow starting from the following [versions](https://docs.cloud.google.com/composer/docs/composer-versions):

    * `composer-3-airflow-3.1.7-build.5`
    * `composer-3-airflow-2.11.1-build.1`, `composer-3-airflow-2.10.5-build.34`, and `composer-3-airflow-2.9.3-build.54`
    * `composer-2.16.11-airflow-2.11.1`, `composer-2.16.11-airflow-2.10.5`

If you use an earlier version of Managed Airflow, you can Install the `orchestration-pipelines` package from PyPI manually.

  * The approximate time to create an Managed Airflow environment is 25 minutes.

  * You can create Managed Airflow environments in Google Cloud console, gcloud CLI, and Terraform. This guide demonstrates only gcloud CLI commands. For instructions and examples of other approaches, see [Create environments](https://docs.cloud.google.com/composer/docs/latest/create-environments) in Managed Airflow documentation.

  * The default configuration provided in this guide creates a Public IP Managed Airflow environment. Managed Airflow provides many more options for networking and security configuration. For more information about different ways to set up a runner environment, see [Create environments](https://docs.cloud.google.com/composer/docs/latest/create-environments) in Managed Airflow documentation. 




### Review the required IAM roles

To get the permissions that you need to create runner environments in your project, ask your administrator to grant you the following roles:

  * **Environment and Storage Object Administrator** (`composer.environmentAndStorageObjectAdmin`) and **Service Account User** (`iam.serviceAccountUser`) role to create and manage environments in Managed Service for Apache Airflow and manage objects in buckets associated with these environments. For more information about these user roles, see [Grant roles to users](https://docs.cloud.google.com/composer/docs/latest/access-control#user-account) in the Managed Service for Apache Airflow documentation.



### Enable the Cloud Composer API and APIs for actions

  1. [Enable the Cloud Composer API](https://docs.cloud.google.com/composer/docs/latest/enable-composer-service). For the full list of services used by Managed Airflow, see [Services required by Managed Airflow](https://docs.cloud.google.com/composer/docs/latest/enable-composer-service#required-services).
  2. Enable APIs for Google Cloud services that you want to use (such as Dataproc API).



## Create a new service account for the runner environment and grant it IAM roles

The service account of the runner environment is used to create a new Managed Service for Apache Airflow environment and run all orchestration pipelines that you deploy to it.

Ask your administrator to do the following:

  1. [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) as described in the Identity and Access Management documentation.

  2. Grant the **Composer Worker** (`composer.worker`) role to it. This role provides this required set of permissions in most cases.

To access other resources in your Google Cloud project, grant extra permissions to access those resources to this service account. Add extra permissions to this service account only when it's necessary for the operation of your orchestration pipeline.

  3. If you want to use a Managed Airflow (Gen 2) environment, follow instructions in [Grant required permissions to Managed Airflow service account](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#grant-permissions) to grant extra permissions.

  4. Grant permissions that will be required by your pipeline. All orchestration tasks in a pipeline will be run by this runner environment's service account, so you must manually grant all required permissions on this service account.

For example, if your pipeline uses an action that runs on a Managed Service for Apache Spark ephemeral cluster, the runner environment's service account must have permissions to create and delete a Managed Service for Apache Spark cluster, as well as trigger and manage Managed Service for Apache Spark jobs. Also, the Dataproc API must be enabled.




## Create a Managed Service for Apache Airflow environment

**Important:** Some actions in the first Preview versions of Orchestration Pipelines **might require more memory and CPU resources**. If you see any issues with pipeline parsing or execution, consider increasing Worker, and DAG Processor resources to 4 vCPU, 8 GB memory, and Scheduler resources to 2 vCPU, 8 GB memory. You can always [adjust the resource configuration](https://docs.cloud.google.com/composer/docs/latest/scale-environments) of your runner environment later.

[Create a Managed Service for Apache Airflow environment](https://docs.cloud.google.com/composer/docs/latest/create-environments), with the following considerations.

  * Environment name: any name. You will use this name later to [deploy][op-deploy] your pipelines. Example: `example-runner`.
  * Image version: version of Managed Service for Apache Airflow and Airflow to use. In gcloud CLI, you can use an alias that points to the default version, for example, `composer-3-airflow-3`, or `composer-2-airflow-2`.
  * Location: any location. Example: `us-central1`.
  * Service account: service account that you've created for this environment.



Example gcloud CLI command:
    
    
    gcloud composer environments create example-runner \
      --location us-central1 \
      --image-version composer-3-airflow-3 \
      --service-account "example-account@example-project.iam.gserviceaccount.com"
    
    

Example recommended workloads configuration for Preview (you can always scale it up or down later):
    
    
    gcloud composer environments create example-runner \
      --location us-central1 \
      --image-version composer-3-airflow-3 \
      --service-account "example-account@example-project.iam.gserviceaccount.com" \
      --scheduler-cpu 2 \
      --scheduler-memory 8GB \
      --dag-processor-cpu 4 \
      --dag-processor-memory 8GB \
      --worker-cpu 4 \
      --worker-memory 8GB
    

It takes approximately 25 minutes to create a Managed Airflow environment.

## (Optional) Install Orchestration Pipelines package from PyPI

Orchestration Pipelines depends on the [`orchestration-pipelines` PyPI package](https://pypi.org/project/orchestration-pipelines/). By default, your runner environment already has this package preinstalled.

If you use an earlier version of Managed Airflow which doesn't have this package preinstalled or want to install a different version of the package, then you can [install this package from PyPI](https://docs.cloud.google.com/composer/docs/latest/install-python-dependencies).

**Important:** We recommend to avoid specifying strict requirements (`==`). This might cause package conflicts because the version is fixed to a single option. Instead, use non-strict version requirements (`>=`).

Example:
    
    
    gcloud composer environments update example-runner \
        --location us-central1 \
        --update-pypi-package "orchestration-pipelines>=0.11.1"
    

For more information about installing PyPI packages in your runner environment and for examples of doing this in Google Cloud console and Terraform, see [Install Python dependencies](https://docs.cloud.google.com/composer/docs/latest/install-python-dependencies) in Managed Service for Apache Airflow documentation.

## What's next

  * Add the runner environment to the [deployment configuration][op-deploy].



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
