---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/run/
title: gcloud alpha composer environments run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:12.067414+00:00
---

# gcloud alpha composer environments run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha composer environments run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha composer environments run - run an Airflow sub-command remotely in a Cloud Composer environment 
SYNOPSIS
    

`gcloud alpha composer environments run` (`ENVIRONMENT` : `--location`=`LOCATION`) `SUBCOMMAND` [`SUBCOMMAND_NESTED`] [`GCLOUD_WIDE_FLAG …`] [-- `CMD_ARGS` …]
DESCRIPTION
     `(ALPHA)` Executes an Airflow CLI sub-command remotely in an environment. If the sub-command takes flags, separate the environment name from the sub-command and its flags with ``--´´. This command waits for the sub-command to complete; its exit code will match the sub-command's exit code. 

Note: Airflow CLI sub-command syntax differs between Airflow 1 and Airflow 2. Refer to the Airflow CLI reference documentation for more details. 

EXAMPLES
     The following command in environments with Airflow 2: 
    
    
    gcloud alpha composer environments run myenv dags trigger -- some_dag --run_id=foo

is equivalent to running the following command from a shell inside the `my-environment` environment: 
    
    
    airflow dags trigger --run_id=foo some_dag

The same command, but for environments with Airflow 1.10.14+: 
    
    
    gcloud alpha composer environments run myenv trigger_dag -- some_dag --run_id=foo

is equivalent to running the following command from a shell inside the `my-environment` environment: 
    
    
    airflow trigger_dag some_dag --run_id=foo

The following command (for environments with Airflow 1.10.14+): 
    
    
    gcloud alpha composer environments run myenv dags list

is equivalent to running the following command from a shell inside the `my-environment` environment: 
    
    
    airflow dags list

POSITIONAL ARGUMENTS
    

Environment resource - The environment in which to run an Airflow command. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `environment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENVIRONMENT`
     ID of the environment or fully qualified identifier for the environment. 

To set the `environment` attribute: 

  * provide the argument `environment` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Region where Composer environment runs or in which to create the environment. 

To set the `location` attribute: 

  * provide the argument `environment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `composer/location`. 


`SUBCOMMAND`
     The Airflow CLI subcommand to run. Available subcommands include (listed with Airflow versions that support): backfill [**, 3.4.0), clear [**, 2.0.0), config [2.11.0, 3.4.0), connections [**, 3.4.0), dag_state [**, 2.0.0), dags [1.10.14, 3.4.0), db [2.3.0, 3.4.0), delete_dag [1.10.1, 2.0.0), kerberos [**, 3.4.0), kubernetes [2.1.4, 3.4.0), list-import-errors [**, 3.0.0), list_dag_runs [1.10.2, 2.0.0), list_dags [**, 2.0.0), list_tasks [**, 2.0.0), next_execution [1.10.2, 2.0.0), pause [**, 2.0.0), pool [**, 2.0.0), pools [1.10.14, 3.4.0), render [**, 2.0.0), roles [2.0.0, 3.4.0), run [**, 2.0.0), sync-perm [1.10.14, 3.4.0), sync_perm [1.10.2, 2.0.0), task_failed_deps [**, 2.0.0), task_state [**, 2.0.0), tasks [1.10.14, 3.4.0), test [**, 2.0.0), trigger_dag [**, 2.0.0), unpause [**, 2.0.0), upgrade_check [1.10.15, 2.0.0), users [1.10.14, 3.4.0), variables [**, 3.4.0), version [**, 3.4.0) (see <https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html> for more info). 
[`SUBCOMMAND_NESTED`]
     Additional subcommand in case it is nested. The following is a list of allowed nested subcommands: 

  * config: lint 
  * db: check, trim 
  * all other subcommands: all nested subcommands are allowed 


[-- `CMD_ARGS` …]
     Command line arguments to the subcommand. 

The '--' argument must be specified between gcloud specific args on the left and CMD_ARGS on the right. Example: 

gcloud alpha composer environments run myenv trigger_dag -- some_dag \--run_id=foo 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud composer environments run](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run)
    
    
    [gcloud beta composer environments run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
