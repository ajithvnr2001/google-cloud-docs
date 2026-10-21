---
url: https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli/
title: Access Airflow command-line interface \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:56.414787+00:00
---

# Access Airflow command-line interface  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Access Airflow command-line interface Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli "View this page for Managed Airflow \(Legacy Gen 1\)")

Apache Airflow has a command-line interface (CLI) that you can use to perform tasks such as triggering and managing DAGs, getting information about DAG runs and tasks, adding and deleting connections and users.

## Supported Airflow CLI commands

Airflow uses [Airflow CLI syntax](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html), which is described in the Airflow documentation.

See the [`gcloud composer environments run`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run#SUBCOMMAND) command's reference for the full list of supported Airflow CLI commands.

## Before you begin

For executing Airflow CLI commands through Google Cloud CLI:

  * Your Google Account must have [permissions](https://docs.cloud.google.com/composer/docs/composer-2/access-control#cli) to use Google Cloud CLI with Managed Airflow and run Airflow CLI commands.

**Caution:** Users with the `composer.environments.executeairflowcommand` permission can execute Python code available to Airflow components on behalf of the environment's service account. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account-security).
  * Airflow CLI commands executed through Google Cloud CLI consume the `environments.executeAirflowCommand` [quota](https://docs.cloud.google.com/composer/quotas).

**Important:** If you want to trigger a large number of DAGs, we recommend to do it [with Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-api#call-api). Triggering DAGs through Google Cloud CLI might cause your environment to reach the quota limit, and as a result, Airflow CLI commands will no longer be executed.
  * In Managed Airflow versions before 2.4.0, you need access to the control plane of your environment's cluster to run Airflow CLI commands.




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
    

### Running commands on a private IP environment

**Important:** This section is relevant only for Managed Airflow versions before 2.4.0. In later versions, you can run Airflow CLI commands on a private IP environment without additional configuration. Your machine doesn't need access to the environment's cluster control plane endpoint to run these commands.

In Managed Airflow versions before 2.4.0:

To run Airflow CLI commands on a Private IP environment, run them on a machine that can access the GKE cluster's control plane endpoint. Your options may vary depending on your [private cluster configuration](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments#cluster).

If public endpoint access is disabled in your environment's cluster, then it's not possible to use `gcloud composer` commands to run Airflow CLI. To be able to run Airflow CLI commands, perform the following steps:

  1. [Create a VM in your VPC network](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#creating_an_instance_in_a_specific_subnet)
  2. Acquire cluster credentials. Run the following command:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
           --region REGION \
           --project PROJECT \
           --internal-ip
         




Use `kubectl` to run your Airflow command. For example:
    
    
    kubectl exec deployment/airflow-scheduler -n COMPOSER_NAMESPACE \
      --container airflow-scheduler -- airflow dags list
    

Replace `COMPOSER_NAMESPACE` withe a namespace similar to: `composer-2-0-28-airflow-2-3-394zxc12411`. You can find your Managed Airflow in the workloads list or by using the `kubectl get namespaces` command.

If public endpoint access is enabled in your environment's cluster, you can also run Airflow CLI commands from a machine with an external IP address that is added to authorized networks. To enable access from your machine, add the external address of your machine to your environment's [list of authorized networks](https://docs.cloud.google.com/composer/docs/composer-2/configure-authorized-networks#existing-environment).

When running `gcloud composer environments run` or `kubectl` commands, you might encounter the following error:
    
    
    Get "https://<IP Address>/api?timeout=32s": dial tcp <IP Address>:443: i/o timeout"
    

**Symptom** : This error message indicates that there is no network connectivity from a computer where you run these commands.

**Solution** : Follow the guidelines presented in the Running commands on a private IP environment section or use the instructions available in the [`kubectl` command times out](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#kubectl-times-out) section.

## Run Airflow CLI commands through Cloud Composer API

Starting from Managed Airflow version 2.4.0, you can run Airflow CLI commands through Cloud Composer API.

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
      "executionId": "39b82312-3a19-4d21-abac-7f8f19855ce7",
      "pod": "airflow-scheduler-1327d8cd68-hblpd",
      "podNamespace": "composer-2-4-0-airflow-2-5-3-184dadaf",
      "nextLineNumber": 1
    }
    

## What's next

  * [Access Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface)
  * [Access control (Airflow CLI)](https://docs.cloud.google.com/composer/docs/composer-2/access-control#cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
