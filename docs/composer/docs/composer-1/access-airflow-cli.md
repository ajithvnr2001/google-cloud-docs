---
url: https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli/
title: Access Airflow command-line interface \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:40.373734+00:00
---

# Access Airflow command-line interface  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Access Airflow command-line interface Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

Apache Airflow has a command-line interface (CLI) that you can use to perform tasks such as triggering and managing DAGs, getting information about DAG runs and tasks, adding and deleting connections and users.

## Supported Airflow CLI commands

Airflow in Managed Airflow (Legacy Gen 1) provides two different syntaxes for CLI commands:

  * [Airflow 1.10 CLI syntax](https://airflow.apache.org/docs/apache-airflow/1.10.12/cli-ref.html), available in Managed Airflow environments with Airflow 1.10.

  * [Airflow 2 CLI syntax](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html), available Managed Airflow environments with Airflow 2.




For a full list of supported Airflow CLI commands, see the reference for the [`gcloud composer environments run`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run#SUBCOMMAND) command.

## Before you begin

For executing Airflow CLI commands through Google Cloud CLI:

  * Your Google Account must have [permissions](https://docs.cloud.google.com/composer/docs/composer-1/access-control#cli) to use Google Cloud CLI with Managed Airflow and run Airflow CLI commands.

**Caution:** Users with the `composer.environments.executeairflowcommand` permission can execute Python code available to Airflow components on behalf of the environment's service account. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account-security).
  * Airflow CLI commands executed through Google Cloud CLI consume the `environments.executeAirflowCommand` [quota](https://docs.cloud.google.com/composer/quotas).

**Important:** If you want to trigger a large number of DAGs, we recommend to do it [with Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api#call-api). Triggering DAGs through Google Cloud CLI might cause your environment to reach the quota limit, and as a result, Airflow CLI commands will no longer be executed.



## Run Airflow CLI commands with gcloud CLI

To run Airflow CLI commands in your environments, use gcloud CLI:
    
    
    gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        SUBCOMMAND \
        -- SUBCOMMAND_ARGUMENTS
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `SUBCOMMAND`: one of the [supported Airflow CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run#SUBCOMMAND).
  * `SUBCOMMAND_ARGUMENTS` with arguments for the Airflow CLI command.



### Sub-command arguments separator

Separate the arguments for the specified Airflow CLI command with `--`:

###  Airflow 2 

  * Specify compound CLI commands as a sub-command.
  * Specify any arguments for compound commands as sub-command arguments, after a `--` separator.



Example:
    
    
    gcloud composer environments run example-environment \
        dags list -- --output=json
    

###  Airflow 1 

  * Specify CLI commands as a sub-command.
  * Specify any arguments after a `--` separator.



Example:
    
    
    gcloud composer environments run example-environment \
        list_dags -- --report
    

### Default location

Most `gcloud composer` commands require a location. You can specify the location with the `--location` flag, or by [setting the default location](https://docs.cloud.google.com/composer/docs/gcloud-installation#set-default).

For example, to trigger a DAG named `sample_quickstart` with the ID `5077` in your Managed Airflow environment:

###  Airflow 2 
    
    
    gcloud composer environments run example-environment \
        --location us-central1 dags trigger -- sample_quickstart \
        --run-id=5077
    

###  Airflow 1 
    
    
    gcloud composer environments run example-environment \
        --location us-central1 trigger_dag -- sample_quickstart \
        --run_id=5077
    

## What's next

  * [Access Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface)
  * [Access control (Airflow CLI)](https://docs.cloud.google.com/composer/docs/composer-1/access-control#cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
