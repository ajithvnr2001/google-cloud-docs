---
url: https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables/
title: Set environment variables \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:53.527703+00:00
---

# Set environment variables  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Set environment variables Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/set-environment-variables "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/set-environment-variables "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to set environment variables in your Managed Airflow environment.

You can use environment variables as an alternative to [Airflow variables](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html) when providing runtime configuration for your DAGs. Airflow variables are set in the Airflow database, while environment variables are set in the Airflow worker's container.

As an example, you can use an environment variable's name as is in a command that is run by a BashOperator, or get this value from the `os.environ` object in the DAG, or use an Airflow variable instead.

Environment variables are persistent. Once you specify an environment variable, Airflow keeps using it until you remove the variable from your environment.

**Important:** It's not possible to use environment variables to configure Airflow. [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) instead.

Managed Service for Apache Airflow sets its own reserved environment variables for controlling environments.

## Name format

Environment variables must match the regular expression `[a-zA-Z_][a-zA-Z0-9_]*`.

## Airflow configuration options

It is not possible to specify variables that change Apache Airflow configuration options.

The variables cannot use the `AIRFLOW__{SECTION}__{KEY}` format or match the regular expression `AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+`. For example, it is not possible to set `AIRFLOW__WEBSERVER__DAG_DEFAULT_VIEW`.

Instead, you can [override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations).

## Reserved variables

The following variable names are reserved by Managed Airflow. It is not possible to create variables with these names.

  * `AIRFLOW_DATABASE_VERSION`
  * `AIRFLOW_HOME`
  * `AIRFLOW_SRC_DIR`
  * `AIRFLOW_WEBSERVER`
  * `AUTO_GKE`
  * `CLOUDSDK_METRICS_ENVIRONMENT`
  * `CLOUD_LOGGING_ONLY`
  * `COMPOSER_AGENT_BUILD_SERVICE_ACCOUNT`
  * `COMPOSER_ENVIRONMENT`
  * `COMPOSER_ENVIRONMENT_SIZE`
  * `COMPOSER_GKE_LOCATION`
  * `COMPOSER_GKE_NAME`
  * `COMPOSER_GKE_ZONE`
  * `COMPOSER_LOCATION`
  * `COMPOSER_OPERATION_UUID`
  * `COMPOSER_PYTHON_VERSION`
  * `COMPOSER_VERSION`
  * `CONTAINER_NAME`
  * `C_FORCE_ROOT`
  * `DAGS_FOLDER`
  * `GCE_METADATA_TIMEOUT`
  * `GCP_PROJECT`
  * `GCP_TENANT_PROJECT`
  * `GCSFUSE_EXTRACTED`
  * `GCS_BUCKET`
  * `GKE_CLUSTER_NAME`
  * `GKE_IN_TENANT`
  * `GOOGLE_APPLICATION_CREDENTIALS`

  * `GOOGLE_CLOUD_PROJECT`

  * `MAJOR_VERSION`

  * `MINOR_VERSION`

  * `PATH`

  * `PIP_DISABLE_PIP_VERSION_CHECK`

  * `PORT`

  * `PROJECT_ID`

  * `PYTHONPYCACHEPREFIX`

  * `PYTHONWARNINGS`

  * `REDIS_PASSWORD`

  * `REDIS_PORT`

  * `REDIS_USER`

  * `SQL_DATABASE`

  * `SQL_HOST`

  * `SQL_INSTANCE`

  * `SQL_PASSWORD`

  * `SQL_PROJECT`

  * `SQL_REGION`

  * `SQL_USER`


**Caution:** Managed Airflow uses these reserved names for variables that are used by its processes. Don't refer to reserved names in your DAGs. Values of these variables can change without notice.

## Set environment variables for new environments

You can specify environment variables when you create an environment. For more information, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#overrides-env-vars).

## Set environment variables for existing environments

###  Console 

To set environment variables for an existing environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment variables** tab and click **Edit**.

  4. Add, change, or delete environment variables for your environment:

     * In the **Name** field, specify the variable name.
     * In the **Value** field, specify the variable value.
     * To add an extra variable, click **Add environment variable**.
     * To delete a variable, hold the pointer over a variable, then click **Delete item**.



###  gcloud 

Following arguments control environment variables:

  * `--update-env-variables` specifies a comma-separated list of environment variables to create or update.

  * `--remove-env-variables` specifies a comma-separated list of environment variables to delete.

  * `--clear-env-variables` deletes all existing environment variables.



    
    
    gcloud composer environments update \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --update-env-variables=NAME=VALUE
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `NAME` with the name of the variable that you want to create or update.
  * `VALUE` with the value for the variable.
  * To add more than one variable, separate the definitions with commas: `NAME=VALUE,NAME=VALUE,...`.



Example:
    
    
    gcloud composer environments update \
      example-environment \
      --location us-central1 \
      --update-env-variables=EXAMPLE_VARIABLE=True,ANOTHER_VARIABLE=test
    

###  API 

Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

In this request:

  1. In the `updateMask` parameter, specify the `config.softwareConfig.envVariables` mask to replace all existing variables with the specified variables. Variables that you don't specify are deleted.

  2. In the request body, specify variables and their values:
         
         {
           "config": {
             "softwareConfig": {
               "envVariables": {
                 "VAR_NAME": "VAR_VALUE"
               }
             }
           }
         }
         

Replace:

     * `VAR_NAME` with the name of the environment variable.
     * `VAR_VALUE` with the value of the environment variable.
     * To add more than one variable, add extra entries for variables to `envVariables`.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.envVariables
    {
      "config": {
        "softwareConfig": {
          "envVariables": {
            "EXAMPLE_VARIABLE": "True",
            "ANOTHER_VARIABLE": "test"
          }
        }
      }
    }
    

###  Terraform 

The `env_variables` block in the `software_config` block specifies environment variables.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        software_config {
    
          env_variables = {
            VAR_NAME = "VAR_VALUE"
          }
    
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `VAR_NAME` with the name of the environment variable.
  * `VAR_VALUE` with the value of the environment variable.
  * To add more than one variable, add extra entries for variables to `env_variables`.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        software_config {
    
          env_variables = {
            EXAMPLE_VARIABLE = "True"
            ANOTHER_VARIABLE = "test"
          }
        }
      }
    }
    

## What's next

  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations)
  * [Update environments](https://docs.cloud.google.com/composer/docs/composer-3/update-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
