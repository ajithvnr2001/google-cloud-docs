---
url: https://docs.cloud.google.com/composer/docs/composer-2/trigger-dags-in-other-environments/
title: Trigger DAGs in other environments and projects \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:41.686648+00:00
---

# Trigger DAGs in other environments and projects  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/trigger-dags-in-other-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Trigger DAGs in other environments and projects Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/trigger-dags-in-other-environments "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This page demonstrates how to implement a DAG that triggers DAGs in other Managed Airflow environments and projects by using Airflow operators for Managed Airflow.

If you want to trigger DAGs in your environment instead, see [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-2/schedule-and-trigger-dags).

## Configure IAM permissions

**If the target environment is located in another project** , then the service account of your environment needs roles that allows interacting with environments in that project.

**Note:** To grant a single permission, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) in the target project, add the permission to it, and then [grant this role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) to a principal.Project | Resource | Principal | Role  
---|---|---|---  
Project where the target environment is located  |  Project  |  Environment's service account of the source environment  |  **Composer Worker** role (`composer.worker`)  
Project where the target environment is located  |  Project  |  Environment's service account of the source environment  |  A [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) with the `composer.environments.executeAirflowCommand` permission  
  
## Trigger a DAG in another environment

The example DAG described in this section does the following:

  1. Trigger a DAG in another Managed Airflow environment.
  2. Checks if a DAG run is completed.



After the DAG run in another environment is completed, the example DAG is marked as successful.

**Note:** Google provides more [Airflow operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_composer/index.html), [sensors](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/sensors/cloud_composer/index.html), [triggers](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/triggers/cloud_composer/index.html), and [hooks](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/hooks/cloud_composer/index.html) that work with Managed Airflow environments. For example, you can create, update and delete environments with these operators.

### Run Airflow CLI commands with CloudComposerRunAirflowCLICommandOperator

You can use the [CloudComposerRunAirflowCLICommandOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/cloud_composer/index.html#airflow.providers.google.cloud.operators.cloud_composer.CloudComposerRunAirflowCLICommandOperator) operator to run Airflow CLI commands in another Managed Airflow environment. The example DAG executes the `dags trigger` command, which triggers a DAG.

This operator can run in the [deferrable mode](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators), you can enable it by setting the `deferrable` parameter to `True`.

**Important:** This operator consumes the `environments.executeAirflowCommand` [quota](https://docs.cloud.google.com/composer/quotas). If you want to **trigger a large number of DAGs** , we recommend to do it [with Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-api#call-api). Triggering DAGs through CloudComposerRunAirflowCLICommandOperator might cause your environment to reach the quota limit, and as a result, Airflow CLI commands will no longer be executed.
    
    
    run_airflow_cli_cmd = CloudComposerRunAirflowCLICommandOperator(
        task_id="run_airflow_cli_cmd",
        project_id="target-project",
        environment_id="target-composer-environment",
        region="us-central1",
        command="dags trigger -- target_dag",
        # You can run this operator in the deferrable mode:
        # deferrable=True
    )
    

### Check if a DAG run is completed

You can use the [CloudComposerDAGRunSensor](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/sensors/cloud_composer/index.html#airflow.providers.google.cloud.sensors.cloud_composer.CloudComposerDAGRunSensor) sensor to checks if a DAG run is completed in another Managed Airflow environment.

This sensor can run in the [deferrable mode](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators), you can enable it by setting the `deferrable` parameter to `True`.
    
    
    dag_run_sensor = CloudComposerDAGRunSensor(
        task_id="dag_run_sensor",
        project_id="target-project",
        environment_id="target-composer-environment",
        region="us-central1",
        composer_dag_id="target_dag",
        allowed_states=["success"],
        # You can run this sensor in the deferrable mode:
        # deferrable=True
    )
    

### Full example code

The following is the full code example of a DAG that combines the two previously described tasks.

**Note:** If the target environment is located in another project, make sure to configure IAM permissions before running this DAG.
    
    
    from datetime import datetime, timedelta
    from airflow.models.dag import DAG
    from airflow.providers.google.cloud.operators.cloud_composer import (
        CloudComposerRunAirflowCLICommandOperator,
    )
    from airflow.providers.google.cloud.sensors.cloud_composer import CloudComposerDAGRunSensor
    
    DAG_ID = "trigger_dag_in_another_composer_environment"
    
    TARGET_PROJECT_ID = "example-target-project"
    TARGET_REGION = "example-target-region"
    TARGET_ENV_ID = "example-target-composer-environment"
    
    TARGET_DAG = "example_target_dag_id"
    COMMAND = f"dags trigger -- {TARGET_DAG}"
    
    with DAG(
        DAG_ID,
        schedule="@once",
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=["example", "composer"],
    ) as dag:
    
        run_airflow_cli_cmd = CloudComposerRunAirflowCLICommandOperator(
            task_id="run_airflow_cli_cmd",
            project_id=TARGET_PROJECT_ID,
            environment_id=TARGET_ENV_ID,
            region=TARGET_REGION,
            command=COMMAND,
            # You can run this operator in the deferrable mode:
            # deferrable=True
        )
    
        dag_run_sensor = CloudComposerDAGRunSensor(
            task_id="dag_run_sensor",
            project_id=TARGET_PROJECT_ID,
            environment_id=TARGET_ENV_ID,
            region=TARGET_REGION,
            composer_dag_id=TARGET_DAG,
            allowed_states=["success"],
            execution_range=timedelta(minutes=5),
            # You can run this sensor in the deferrable mode:
            # deferrable=True
        )
    
        run_airflow_cli_cmd >> dag_run_sensor
    
    

## What's next

  * [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-2/schedule-and-trigger-dags)
  * [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-2/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
