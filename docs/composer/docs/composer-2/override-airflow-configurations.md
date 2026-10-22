---
url: https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations/
title: Override Airflow configuration options \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:11.760393+00:00
---

# Override Airflow configuration options  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Override Airflow configuration options Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to override Airflow configuration options for new and existing Managed Airflow environments.

When you [create](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) or [update](https://docs.cloud.google.com/composer/docs/composer-2/update-environments) an environment, you can override [Apache Airflow configuration options](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) with different values. By doing so you can adjust the Airflow instance to your needs and requirements.

**Note:** some Airflow configuration options are [blocked](https://docs.cloud.google.com/composer/docs/airflow-configurations) and you cannot override them.

## Override Airflow configuration options for new environments

You can override Airflow configuration options when you create your environment. For more information, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#overrides-env-vars).

## Override Airflow configuration options for existing environments

###  Console 

To override [Airflow configuration options](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) for an existing environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details page opens**.

  3. Go to the **Airflow configuration overrides** tab.

  4. Click **Edit**.

  5. Enter the **Section** , **Key** , and **Value** for the Airflow configuration option that you want to change.




For example:

Section | Key | Value  
---|---|---  
`webserver` | `dag_orientation` | `RL`  
  
###  gcloud 

Following arguments override [Airflow configuration options](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) for an existing environment:

  * `--update-airflow-configs` adds or changes specified Airflow configuration overrides.
  * `--remove-airflow-configs` removes specified Airflow configuration overrides.
  * `--clear-airflow-configs` removes all Airflow configuration overrides.


    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --update-airflow-configs=KEY=VALUE,KEY=VALUE,...
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `KEY` with the configuration section and the option name separated by a hyphen, for example, `webserver-dag_orientation`.
  * `VALUE` with the corresponding value for an option.



For example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --update-airflow-configs=webserver-dag_default_view=graph,webserver-dag_orientation=RL
    

###  API 

To override [Airflow configuration options](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) for an existing environment:

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     * To replace all existing Airflow configuration overrides with the specified options, in the `updateMask` parameter, specify the `config.softwareConfig.airflowConfigOverrides` mask.

     * To override a specific Airflow configuration option, in the `updateMask` parameter, specify the `config.softwareConfig.airflowConfigOverrides.KEY` mask. Replace `KEY` with the configuration section and the option name separated by a hyphen, for example, `webserver-dag_orientation`.

If you want to override several Airflow configuration options, in the `updateMask` parameter, specify several masks separated by commas.

  3. The request body must contain the list of Airflow configuration options. If you are replacing all existing overrides, make sure to include all overrides that you want to keep.



    
    
    {
      "config": {
        "softwareConfig": {
          "airflowConfigOverrides": {
            "KEY": "VALUE"
          }
        }
      }
    }
    

Replace:

  * `KEY` with the configuration section and the option name separated by a hyphen, for example, `webserver-dag_orientation`.
  * `VALUE` with the corresponding value for an option.



The following example overrides two specific Airflow configuration options:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.airflowConfigOverrides.webserver-dag_default_view,
    // config.softwareConfig.airflowConfigOverrides.webserver-dag_orientation
    
    {
      "config": {
        "softwareConfig": {
          "airflowConfigOverrides": {
            "webserver-dag_default_view": "graph",
            "webserver-dag_orientation": "RL"
          }
        }
      }
    }
    

###  Terraform 

The `airflow_config_overrides` block in the `software_config` block controls overrides of [Airflow configuration options](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) for your environment:
    
    
    resource "google_composer_environment" "example" {
    
    config {
    
        # ... Other environment configuration parameters
    
        software_config {
          airflow_config_overrides = {
            KEY = "VALUE"
          }
        }
      }
    }
    

Replace:

  * `KEY` with the configuration section and the option name separated by a hyphen, for example, `webserver-dag_orientation`.
  * `VALUE` with the corresponding value for an option.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      # ... Other environment configuration parameters
    
      config {
        software_config {
          airflow_config_overrides = {
            webserver-dag_default_view = "graph"
            webserver-dag_orientation  = "RL"
          }
        }
      }
    }
    

## What's next

  * [Blocked Airflow configurations](https://docs.cloud.google.com/composer/docs/airflow-configurations)
  * [Update environments](https://docs.cloud.google.com/composer/docs/composer-2/update-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
