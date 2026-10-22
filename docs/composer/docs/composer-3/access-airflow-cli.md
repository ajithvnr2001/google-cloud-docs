---
url: https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli/
title: Access Airflow command-line interface \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:38.797548+00:00
---

# Access Airflow command-line interface  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Access Airflow command-line interface Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli "View this page for Managed Airflow \(Legacy Gen 1\)")

Apache Airflow has a command-line interface (CLI) that you can use to perform tasks such as triggering and managing DAGs, getting information about DAG runs and tasks, adding and deleting connections and users.

## Supported Airflow CLI commands

Airflow uses [Airflow CLI syntax](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html), which is described in the Airflow documentation.

Managed Airflow (Gen 3) supports the following Airflow CLI commands:

  * _(Airflow 2 and 3)_ The `gcloud composer environments run` command runs Airflow CLI commands for your environment. Some commands are blocked and it's not possible to run them. See the [command's reference](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run#SUBCOMMAND) for the list of supported Airflow CLI commands.

  * _(Airflow 3)_ The `airflowctl` command-line tool supports a subset of Airflow CLI commands and runs them using Airflow REST API. All commands available in `airflowctl` are supported in Managed Airflow. Make sure that the user's Airflow account has [an Airflow role](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac#manage-rbac-roles) that can run a specific command.




## Before you begin

For executing Airflow CLI commands through Google Cloud CLI:

  * Your Google Account must have [permissions](https://docs.cloud.google.com/composer/docs/composer-3/access-control#cli) to use Google Cloud CLI with Managed Airflow and run Airflow CLI commands.

**Caution:** Users with the `composer.environments.executeairflowcommand` permission can execute Python code available to Airflow components on behalf of the environment's service account. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control#service-account-security).
  * Airflow CLI commands executed through Google Cloud CLI consume the `environments.executeAirflowCommand` [quota](https://docs.cloud.google.com/composer/quotas).

**Important:** If you want to trigger a large number of DAGs, we recommend to do it [with Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api#call-api) or with the `airflowctl` command-line tool in Airflow 3. Triggering DAGs through Google Cloud CLI might cause your environment to reach the quota limit, and as a result, Airflow CLI commands will no longer be executed.



For executing Airflow CLI commands through the `airflowctl` command-line tool (in Airflow 3):

  * Your Google Account must have the `composer.environments.get` permission. It is provided by the role that can [view Managed Airflow environments](https://docs.cloud.google.com/composer/docs/composer-3/access-control#role-view-environments). The `airflowctl` command-line tool doesn't require [permissions for running Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-3/access-control#cli).

  * Airflow CLI commands executed through `airflowctl` don't consume the `environments.executeAirflowCommand` [quota](https://docs.cloud.google.com/composer/quotas).


**Note:** It is not possible to run Airflow CLI commands through `kubectl` in Managed Airflow (Gen 3). This approach was deprecated and is required only for Managed Airflow versions earlier than 2.4.0.

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

  * Specify compound CLI commands as a sub-command.
  * Specify any arguments for compound commands as sub-command arguments, after a `--` separator.



Example:
    
    
    gcloud composer environments run example-environment \
        dags list -- --output=json
    

### Default location

Most `gcloud composer` commands require a location. You can specify the location with the `--location` flag, or by [setting the default location](https://docs.cloud.google.com/composer/docs/gcloud-installation#set-default).

For example, to trigger a DAG named `sample_quickstart` with the ID `5077` in your Managed Airflow environment:
    
    
    gcloud composer environments run example-environment \
        --location us-central1 dags trigger -- sample_quickstart \
        --run-id=5077
    

## Run Airflow CLI commands with airflowctl

The [`airflowctl` command-line tool](https://pypi.org/project/apache-airflow-ctl/) is a command-line utility provided by Airflow for running Airflow CLI commands. It supports a subset of Airflow CLI commands and runs them using Airflow REST API. All commands available in `airflowctl` are supported in Managed Airflow.

Authorization and authentication with `airflowctl` in Managed Airflow works in the following way:

  * Because `airflowctl` uses the Airflow REST API, make sure that the Airflow user account associated with your Google Account or service account has [an Airflow role](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac#manage-rbac-roles) with enough permissions to run a command. For example, some commands can be executed only by Airflow users that have the `Admin` role.

  * The API token used by `airflowctl` is provided with the [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth) command. By default, the token has an expiration period of 1 hour. You can change it with the `--lifetime` argument provided to this command.




To authenticate with `airflowctl`, run the following command:
    
    
    airflowctl auth login \
      --api-url WEB_SERVER_URL \
      --api-token $(gcloud auth application-default print-access-token)
    

Replace the following:

  * `WEB_SERVER_URL`: the [URL of the Airflow web server](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#obtain-airflow-ui-url). Make sure that this URL doesn't have a trailing slash ("/").



Example:
    
    
    airflowctl auth login \
      --api-url https://example-dot-us-central1.composer.googleusercontent.com \
      --api-token $(gcloud auth application-default print-access-token)
    

After you authenticate with `airflowctl`, you can run Airflow CLI commands:
    
    
    airflowctl dags list
    
    

## Run Airflow CLI commands through Cloud Composer API

In Managed Airflow (Gen 3), you can run Airflow CLI commands through Cloud Composer API.

### Execute a command

Construct an [`environments.executeAirflowCommand`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/executeAirflowCommand) API request:
    
    
    {
      "environment": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "command": "AIRFLOW_COMMAND",
      "subcommand": "AIRFLOW_SUBCOMMAND",
      "parameters": [
        "SUBCOMMAND_PARAMETER"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `LOCATION`: the region where the environment is located.
  * `ENVIRONMENT_NAME`: the name of your environment.
  * `AIRFLOW_COMMAND`: Airflow CLI command that you want to execute, such as `dags`.
  * `AIRFLOW_SUBCOMMAND`: Sub-command for the Airflow CLI command that you want to execute, such as `list`.
  * (optional) `SUBCOMMAND_PARAMETER`: Parameters for the sub-command. If you want to use more than one parameter, add more items to the list.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{environment=projects/*/locations/*/environments/*}:executeAirflowCommand
    {
      "environment": "projects/example-project/locations/us-central1/environments/example-environment",
      "command": "dags",
      "subcommand": "list",
      "parameters": [
        "-o json",
        "--verbose"
      ]
    }
    

### Poll command status

After you execute an Airflow CLI command through Cloud Composer API, check if the command was successfully completed by making a [PollAirflowCommand](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/pollAirflowCommand) request and inspecting the fields in `exitInfo` for errors and status codes. The `output` field contains log lines.

**Note:** You can also stop executing a command with [StopAirflowCommand](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/stopAirflowCommand).

To get the command execution status and fetch logs, provide `executionId`, `pod`, and `podNamespace` values returned by `ExecuteAirflowCommandRequest`:

Example:
    
    
    // POST https://composer.googleapis.com/v1/{environment=projects/*/locations/*/environments/*}:pollAirflowCommand
    {
      "executionId": "a117da94-355d-4ad4-839e-ac39ccb0bf48",
      "pod": "airflow-webserver-66d96b858f-tn96b",
      "podNamespace": "airflow-2-10-2-build-13-226523e4",
      "nextLineNumber": 1
    }
    

## What's next

  * [Access Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface)
  * [Access control (Airflow CLI)](https://docs.cloud.google.com/composer/docs/composer-3/access-control#cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
