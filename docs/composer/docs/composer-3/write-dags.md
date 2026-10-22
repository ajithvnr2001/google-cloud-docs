---
url: https://docs.cloud.google.com/composer/docs/composer-3/write-dags/
title: Write Airflow DAGs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:04.363031+00:00
---

# Write Airflow DAGs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/write-dags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Write Airflow DAGs Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/write-dags "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/write-dags "View this page for Managed Airflow \(Legacy Gen 1\)")

This guide shows you how to write an Apache Airflow directed acyclic graph (DAG) that runs in a Managed Service for Apache Airflow environment.

Because Apache Airflow does not provide strong DAG and task isolation, we recommend that you use separate production and test environments to prevent DAG interference. For more information, see [Testing DAGs](https://docs.cloud.google.com/composer/docs/composer-3/test-dags).

**Note:** The way you implement your DAGs influences performance of DAG scheduling and execution. The [Scheduler troubleshooting](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling) and [DAG Troubleshooting](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags) sections provide information about how to implement and deploy your DAGs optimally and avoid common mistakes.

## Structuring an Airflow DAG

An Airflow DAG is defined in a Python file and is composed of the following components:

  * DAG definition
  * Airflow operators
  * Operator relationships



The following code snippets show examples of each component out of context.

### A DAG definition

The following example demonstrates an [Airflow DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) definition:
    
    
    import datetime
    
    from airflow import models
    
    default_dag_args = {
        # The start_date describes when a DAG is valid / can be run. Set this to a
        # fixed point in time rather than dynamically, since it is evaluated every
        # time a DAG is parsed. See:
        # https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date
        "start_date": datetime.datetime(2018, 1, 1),
    }
    
    # Define a DAG (directed acyclic graph) of tasks.
    # Any task you create within the context manager is automatically added to the
    # DAG object.
    with models.DAG(
        "composer_sample_simple_greeting",
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args,
    ) as dag:

### Operators and tasks

[Airflow Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html) describe the work to be done. A task [task](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html) is a specific instance of an operator.
    
    
    from airflow.operators.bash import BashOperator
    from airflow.operators.python import PythonOperator
    
        def greeting():
            import logging
    
            logging.info("Hello World!")
    
        # An instance of an operator is called a task. In this case, the
        # hello_python task calls the "greeting" Python function.
        hello_python = PythonOperator(task_id="hello", python_callable=greeting)
    
        # Likewise, the goodbye_bash task calls a Bash script.
        goodbye_bash = BashOperator(task_id="bye", bash_command="echo Goodbye.")

### Task relationships

[Task relationships](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#relationships) describe the order in which the work must be completed.
    
    
    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hello_python >> goodbye_bash

### Full DAG workflow example in Python

The following workflow is a complete working DAG template that is composed of two tasks: a `hello_python` task and a `goodbye_bash` task:
    
    
    import datetime
    
    from airflow import models
    
    from airflow.operators.bash import BashOperator
    from airflow.operators.python import PythonOperator
    
    
    
    default_dag_args = {
        # The start_date describes when a DAG is valid / can be run. Set this to a
        # fixed point in time rather than dynamically, since it is evaluated every
        # time a DAG is parsed. See:
        # https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date
        "start_date": datetime.datetime(2018, 1, 1),
    }
    
    # Define a DAG (directed acyclic graph) of tasks.
    # Any task you create within the context manager is automatically added to the
    # DAG object.
    with models.DAG(
        "composer_sample_simple_greeting",
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args,
    ) as dag:
        def greeting():
            import logging
    
            logging.info("Hello World!")
    
        # An instance of an operator is called a task. In this case, the
        # hello_python task calls the "greeting" Python function.
        hello_python = PythonOperator(task_id="hello", python_callable=greeting)
    
        # Likewise, the goodbye_bash task calls a Bash script.
        goodbye_bash = BashOperator(task_id="bye", bash_command="echo Goodbye.")
    
        # Define the order in which the tasks complete by using the >> and <<
        # operators. In this example, hello_python executes before goodbye_bash.
        hello_python >> goodbye_bash

For more information about defining Airflow DAGs, see the [Airflow tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) and [Airflow concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html).

## Airflow operators

The following examples show a few popular Airflow operators. For an authoritative reference of Airflow operators, see the [Operators and Hooks Reference](https://airflow.apache.org/docs/apache-airflow-providers/operators-and-hooks-ref/index.html) and [Providers index](https://airflow.apache.org/docs/#providers-packages-docs-apache-airflow-providers-index-html).

### BashOperator

Use the [BashOperator](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html) to run command-line programs.
    
    
    from airflow.operators import bash
    
        # Create BigQuery output dataset.
        make_bq_dataset = bash.BashOperator(
            task_id="make_bq_dataset",
            # Executing 'bq' command requires Google Cloud SDK which comes
            # preinstalled in Cloud Composer.
            bash_command=f"bq ls {bq_dataset_name} || bq mk {bq_dataset_name}",
        )

Managed Airflow runs the provided commands in a Bash script on an Airflow worker. The worker is a Debian-based Docker container and includes several packages.

  * [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference), including the `gcloud storage` sub-command for working with Cloud Storage buckets.
  * [`bq` command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference)
  * [`kubectl` command](https://kubernetes.io/docs/reference/kubectl/overview/)

**Note:** To access pods in the GKE cluster, use namespace-aware `kubectl` commands. For all namespaces, use `--all-namespaces`. To specify a namespace, use `-n <namespace>`.

### PythonOperator

Use the [PythonOperator](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/python.html) to run arbitrary Python code.

Managed Airflow runs the Python code in a container that includes packages for the [Managed Airflow image version](https://docs.cloud.google.com/composer/docs/composer-versions) used in your environment.

To install additional Python packages, see [Installing Python Dependencies](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies).

### Google Cloud Operators

To run tasks that use Google Cloud products, use the Google Cloud Airflow operators. For example, [BigQuery operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html) query and process data in [BigQuery](https://docs.cloud.google.com/bigquery/docs).

There are many more Airflow operators for Google Cloud and individual services provided by Google Cloud. See [Google Cloud Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html) for the full list.

**Note:** Managed Airflow automatically configures [Airflow connections](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html) for many Google Cloud services. For more information, see [Manage Airflow connections](https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections).
    
    
    from airflow.providers.google.cloud.operators import bigquery
    from airflow.providers.google.cloud.transfers import bigquery_to_gcs
    
        bq_recent_questions_query = bigquery.BigQueryInsertJobOperator(
            task_id="bq_recent_questions_query",
            configuration={
                "query": {
                    "query": RECENT_QUESTIONS_QUERY,
                    "useLegacySql": False,
                    "destinationTable": {
                        "projectId": project_id,
                        "datasetId": bq_dataset_name,
                        "tableId": bq_recent_questions_table_id,
                    },
                }
            },
            location=location,
        )

### EmailOperator

Use the [EmailOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/email/index.html) to send email from a DAG. To send email from a Managed Airflow environment, [configure your environment to use SendGrid](https://docs.cloud.google.com/composer/docs/composer-3/configure-email).
    
    
    from airflow.operators import email
    
        # Send email confirmation (you will need to set up the email operator
        # See https://cloud.google.com/composer/docs/how-to/managing/creating#notification
        # for more info on configuring the email operator in Cloud Composer)
        email_summary = email.EmailOperator(
            task_id="email_summary",
            to="{{var.value.email}}",
            subject="Sample BigQuery notify data ready",
            html_content="""
            Analyzed Stack Overflow posts data from {min_date} 12AM to {max_date}
            12AM. The most popular question was '{question_title}' with
            {view_count} views. Top 100 questions asked are now available at:
            {export_location}.
            """.format(
                min_date=min_query_date,
                max_date=max_query_date,
                question_title=(
                    "{{ ti.xcom_pull(task_ids='bq_read_most_popular', "
                    "key='return_value')[0][0] }}"
                ),
                view_count=(
                    "{{ ti.xcom_pull(task_ids='bq_read_most_popular', "
                    "key='return_value')[0][1] }}"
                ),
                export_location=output_file,
            ),
        )

## Notifications on operator failure

Set `email_on_failure` to `True` to send an email notification when an operator in the DAG fails. To send email notifications from a Managed Airflow environment, you must [configure your environment to use SendGrid](https://docs.cloud.google.com/composer/docs/composer-3/configure-email).
    
    
    from airflow import models
    
    default_dag_args = {
        "start_date": yesterday,
        # Email whenever an Operator in the DAG fails.
        "email": "{{var.value.email}}",
        "email_on_failure": True,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": datetime.timedelta(minutes=5),
        "project_id": project_id,
    }
    
    with models.DAG(
        "composer_sample_bq_notify",
        schedule_interval=datetime.timedelta(weeks=4),
        default_args=default_dag_args,
    ) as dag:

## DAG workflow guidelines

  * Place any custom Python libraries in a DAG's ZIP archive in a nested directory. Do not place libraries at the top level of the DAGs directory.

When Airflow scans the `dags/` folder, Airflow only checks for DAGs in Python modules that are in the top-level of the DAGs folder and in the top level of a ZIP archive also located in the top-level `dags/` folder. If Airflow encounters a Python module in a ZIP archive that does not contain both `airflow` and `DAG` substrings, Airflow stops processing the ZIP archive. Airflow returns only the DAGs found up to that point.

  * For fault tolerance, do not define multiple DAG objects in the same Python module.

  * Do not use SubDAGs. Instead, [group tasks inside DAGs](https://docs.cloud.google.com/composer/docs/composer-3/group-tasks-inside-dags).

  * Place files that are required at DAG parse time into `dags/` folder, not in the `data/` folder.

  * [Implement unit tests for your DAGs](https://docs.cloud.google.com/composer/docs/samples/composer-dag-unit-testing).

  * Test developed or modified DAGs as recommended in [instructions for testing DAGs](https://docs.cloud.google.com/composer/docs/composer-3/test-dags).

  * Verify that developed DAGs do not increase [DAG parse times](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling#inspecting_dag_parse_times) too much.

  * Airflow tasks can fail for multiple reasons. To avoid failures of whole DAG runs, we recommend to enable task retries. Setting maximum retries to `0` means that no retries are performed.

We recommend to [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the [`default_task_retries`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#default-task-retries) option with a value for the task retries other than `0`. In addition, you can set the [`retries` parameter](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#timeouts) at the task level.

  * If you want to use GPU in your Airflow tasks then create a separate GKE cluster based on nodes using machines with GPUs. Use [GKEStartPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-gke-operator) to run your tasks.

  * Avoid running CPU- and memory-heavy tasks in the cluster's node pool where other Airflow components (schedulers, workers, web servers) are running. Instead, use [KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator) or [GKEStartPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-gke-operator) instead.

  * When deploying DAGs into an environment, upload only the files that are absolutely necessary for interpreting and executing DAGs into the `/dags` folder.

  * Limit the number of DAG files in `/dags` folder.

Airflow is continuously parsing DAGs in `/dags` folder. The parsing is a process that loops through the DAGs folder and the number of files that need to be loaded (with their dependencies) makes impacts the performance of DAG parsing and task scheduling. It is much more efficient to use 100 files with 100 DAGs each than 10000 files with 1 DAG each and so such optimization is recommended. This optimization is a balance between parsing time and efficiency of DAG authoring and management.

You can also consider, for example, to deploy 10000 DAG files you could create 100 zip files each containing 100 DAG files.

In addition to hints above, if you have more than 10000 DAG files then generating DAGs in a programamtic way might be a good option. For example, you can implement a single Python DAG file that generates some number of DAG objects (for example, 20, 100 DAG objects).

  * Avoid using deprecated Airflow operators. Instead, use their up-to-date alternatives.

  * Avoid using [CloudLoggingHandler](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.handlers.handlers.CloudLoggingHandler) to handle logging. This logging handler causes the environment's database overload and subsequent DAG failures with the "server closed the connection unexpectedly" errors.




## FAQs for writing DAGs

### How do I minimize code repetition if I want to run the same or similar tasks in multiple DAGs?

We suggest [defining libraries](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-local) and wrappers to minimize the code repetition.

### How do I reuse code between DAG files?

Put your utility functions in a [local Python library](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-local) and import the functions. You can reference the functions in any DAG located in the `dags/` folder in your environment's bucket.

### How do I minimize the risk of different definitions arising?

For example, you have two teams that want to aggregate raw data into revenue metrics. The teams write two slightly different tasks that accomplish the same thing. [Define libraries](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-local) to work with the revenue data so that the DAG implementers must clarify the definition of revenue that's being aggregated.

### How do I set dependencies between DAGs?

This depends on how you want to define the dependency.

If you have two DAGs (DAG A and DAG B) and you want DAG B to trigger after DAG A, you can put a [`TriggerDagRunOperator`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/trigger_dagrun/index.html) at the end of DAG A.

If DAG B depends only on an artifact that DAG A generates, such as a Pub/Sub message, then a sensor might work better.

If DAG B is integrated closely with DAG A, you might be able to merge the two DAGs into one DAG.

### How do I pass unique run IDs to a DAG and its tasks?

For example, you want to pass Dataproc cluster names and file paths.

You can generate a random unique ID by returning `str(uuid.uuid4())` in a `PythonOperator`. This places the ID into [`XComs`](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html) so that you can refer to the ID in other operators via templated fields.

Before generating a `uuid`, consider whether a DagRun-specific ID would be more valuable. You can also reference these IDs in Jinja substitutions by using [macros](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html).

### How do I separate tasks in a DAG?

Each task should be an idempotent unit of work. Consequently, you should avoid encapsulating a multi-step workflow within a single task, such as a complex program running in a `PythonOperator`.

### Should I define multiple tasks in a single DAG to aggregate data from multiple sources?

For example, you have multiple tables with raw data and want to create daily aggregates for each table. The tasks are not dependent on each other. Should you create one task and DAG for each table or create one general DAG?

If you are okay with each task sharing the same DAG-level properties, such as `schedule`, then it makes sense to define multiple tasks in a single DAG. Otherwise, to minimize code repetition, multiple DAGs can be generated from a single Python module by placing them into the module's `globals()`.

### How do I limit the number of concurrent tasks running in a DAG?

For example, you want to avoid exceeding API usage limits/quotas or avoid running too many simultaneous processes.

You can define [Airflow pools](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/pools.html) in the Airflow web UI and associate tasks with existing pools in your DAGs.

## FAQs for using operators

### Should I use the `DockerOperator`?

We do not recommend using the [`DockerOperator`](https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html), unless it's used to launch containers on a remote Docker installation (not within an environment's cluster). In a Managed Airflow environment the operator does not have access to Docker daemons.

Instead, use [`KubernetesPodOperator`](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator) or [`GKEStartPodOperator`](https://docs.cloud.google.com/composer/docs/composer-3/use-gke-operator). These operators launch Kubernetes pods into Kubernetes or GKE clusters respectively. Note that we don't recommend launching pods into an environment's cluster, because this can lead to resource competition.

### Should I use the `SubDagOperator`?

We do not recommend using the `SubDagOperator`.

Use alternatives as suggested in [Grouping tasks](https://docs.cloud.google.com/composer/docs/composer-3/group-tasks-inside-dags).

### Should I run Python code only in `PythonOperators` to fully separate Python operators?

Depending on your goal, you have a few options.

If your only concern is maintaining separate Python dependencies, you can use the `PythonVirtualenvOperator`.

Consider [using the `KubernetesPodOperator`](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator). This operator allows you to define Kubernetes pods and run the pods in other clusters.

### How do I add custom binary or non-PyPI packages?

You can [install packages hosted in private package repositories](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-private-repo).

### How do I uniformly pass arguments to a DAG and its tasks?

You can use Airflow's built-in support for [Jinja templating](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html#concepts-jinja-templating) to pass arguments that can be used in templated fields.

### When does template substitution happen?

Template substitution occurs on Airflow workers just before the `pre_execute` function of an operator is called. In practice, this means that templates are not substituted until just before a task runs.

### How do I know which operator arguments support template substitution?

Operator arguments that support Jinja2 template substitution are explicitly marked as such.

Look for the `template_fields` field in the Operator definition, which contains a list of argument names that undergo template substitution.

For example, see the [`BashOperator`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/bash/index.html), which supports templating for the `bash_command` and `env` arguments.

## Deprecated and removed Airflow operators

Airflow Operators listed in the following table are deprecated:

  * **Avoid using these operators** in your DAGs. Instead, use provided up-to-date replacement operators.

  * If an operator is listed as **removed** , then it already became unavailable in one of the released Airflow builds in Managed Airflow (Gen 3). 

  * If an operator is listed as **deprecated** , then it is deprecated and will be removed in a future Airflow build. 


**Note:** Make sure to update your DAGs to use replacement operators.Deprecated operator | Replacement operator  
---|---  
AutoMLBatchPredictOperator Removed in 13.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  vertex_ai.batch_prediction_job Available in 10.24.0. Versions: composer-3-airflow-2.9.3-build.4, composer-2.9.8-airflow-2.9.3.  
AutoMLCreateDatasetOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.dataset.CreateDatasetOperator, translate.TranslateCreateDatasetOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLDatasetLink Removed in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  TranslationLegacyDatasetLink Available in 10.19.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
AutoMLDatasetListLink Removed in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  TranslationDatasetListLink Available in 10.19.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
AutoMLDeleteDatasetOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.dataset.ListDatasetsOperator, translate.TranslateDatasetsListOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLDeleteModelOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.model_service.DeleteModelOperator, translate.TranslateDeleteModelOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLDeployModelOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.endpoint_service.DeployModelOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLGetModelOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.model_service.GetModelOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLImportDataOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.dataset.ImportDataOperator, translate.TranslateImportDataOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLListDatasetOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.dataset.ListDatasetsOperator, translate.TranslateDatasetsListOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLModelLink Removed in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  TranslationLegacyModelLink Available in 10.19.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
AutoMLModelPredictLink Removed in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  TranslationLegacyModelPredictLink Available in 10.19.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
AutoMLModelTrainLink Removed in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  TranslationLegacyModelTrainLink Available in 10.19.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
AutoMLPredictOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  TextGenerationModelPredictOperator, TranslateTextOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLTablesListColumnSpecsOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  No replacement (legacy version of AutoML Tables shut down)  
AutoMLTablesListTableSpecsOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  No replacement (legacy version of AutoML Tables shut down)  
AutoMLTablesUpdateDatasetOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.dataset.UpdateDatasetOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
AutoMLTrainModelOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.auto_ml.CreateAutoMLTabularTrainingJobOperator, CreateAutoMLVideoTrainingJobOperator, CreateAutoMLImageTrainingJobOperator, SupervisedFineTuningTrainOperator, TranslateCreateModelOperator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
BigQueryCreateEmptyTableOperator Removed in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  BigQueryCreateTableOperator Available in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
BigQueryCreateExternalTableOperator Removed in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  BigQueryCreateTableOperator Available in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
BigQueryExecuteQueryOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  BigQueryInsertJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
BigQueryPatchDatasetOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  BigQueryUpdateDatasetOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
BigQueryTableExistenceAsyncSensor Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  BigQueryTableExistenceSensor Available in 8.12.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
BigQueryTableExistencePartitionAsyncSensor Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  BigQueryTablePartitionExistenceSensor Available in 8.12.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
CloudAutoMLHook Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  vertex_ai.auto_ml.AutoMLHook, translate.TranslateHook Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
CloudComposerEnvironmentSensor Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  CloudComposerCreateEnvironmentOperator, CloudComposerDeleteEnvironmentOperator, CloudComposerUpdateEnvironmentOperator Available in 8.13.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
CloudDataCatalogCreateEntryGroupOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogCreateEntryGroupOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogCreateEntryOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogCreateEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogCreateTagOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogCreateEntryOperator, DataplexCatalogUpdateEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogCreateTagTemplateFieldOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateAspectTypeOperator, DataplexCatalogCreateAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogCreateTagTemplateOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogCreateAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogDeleteEntryGroupOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogDeleteEntryGroupOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogDeleteTagOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogDeleteTagTemplateFieldOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogDeleteTagTemplateOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogDeleteAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogGetEntryGroupOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogGetEntryGroupOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogGetEntryOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogGetEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogGetTagTemplateOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogGetAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogHook Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexHook Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogListTagsOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogGetEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogLookupEntryOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogLookupEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogRenameTagTemplateFieldOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogSearchCatalogOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogSearchEntriesOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogUpdateEntryOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogUpdateTagOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateEntryOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogUpdateTagTemplateFieldOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CloudDataCatalogUpdateTagTemplateOperator Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogUpdateAspectTypeOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CountTokensOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  GenAICountTokensOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CreateAutoMLTextTrainingJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  SupervisedFineTuningTrainOperator Available in 10.23.0. Versions: composer-3-airflow-2.9.3-build.1, composer-3-airflow-2.9.1-build.8, composer-2.9.5-airflow-2.9.3, composer-2.9.5-airflow-2.9.1.  
CreateCachedContentOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  GenAICreateCachedContentOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
CreateDataPipelineOperator Removed in 12.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataflowCreatePipelineOperator Available in 10.20.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
DataCatalogEntryGroupLink Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogEntryGroupLink Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
DataCatalogEntryLink Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogEntryLink Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
DataCatalogTagTemplateLink Deprecated in 16.1.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  DataplexCatalogAspectTypeLink Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
DataflowCreateJavaJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  beam.BeamRunJavaPipelineOperator Available in apache-airflow-providers-apache-beam==1.0.0. Versions: composer-3-*, composer-2-*.  
DataflowCreatePythonJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  beam.BeamRunPythonPipelineOperator Available in apache-airflow-providers-apache-beam==1.0.0. Versions: composer-3-*, composer-2-*.  
DataflowStartSqlJobOperator Removed in 13.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataflowStartYamlJobOperator Available in 10.23.0. Versions: composer-3-airflow-2.9.3-build.1, composer-3-airflow-2.9.1-build.8, composer-2.9.5-airflow-2.9.3, composer-2.9.5-airflow-2.9.1.  
DataPipelineHook Removed in 12.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataflowHook Available in 10.20.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
DataprocScaleClusterOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  DataprocUpdateClusterOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
DataprocSubmitHadoopJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataprocSubmitJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
DataprocSubmitHiveJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataprocSubmitJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
DataprocSubmitPigJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataprocSubmitJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
DataprocSubmitPySparkJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataprocSubmitJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
DataprocSubmitSparkJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataprocSubmitJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
DataprocSubmitSparkSqlJobOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataprocSubmitJobOperator Available in 1.0.0. Versions: composer-3-*, composer-2-*.  
DeleteExperimentRunOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  DeleteExperimentRunOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
GCSObjectExistenceAsyncSensor Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GCSObjectExistenceSensor Available in 8.12.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GCSObjectsWtihPrefixExistenceSensor Removed in 7.0.0. Versions: composer-3-*, composer-2.0.28-airflow-2.3.3. |  GCSObjectsWithPrefixExistenceSensor Available in 2.0.0. Versions: composer-3-*, composer-2-*.  
GenerateFromCachedContentOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  GenAIGenerateContentOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
GenerateTextEmbeddingsOperator Removed in 13.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  TextEmbeddingModelGetEmbeddingsOperator Available in 10.21.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
GenerativeModelGenerateContentOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  GenAIGenerateContentOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
GKECustomResourceHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GKEKubernetesHook Available in 10.17.0. Versions: composer-3-*, composer-2.7.1-airflow-2.7.3.  
GKEDeploymentHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GKEKubernetesHook Available in 10.17.0. Versions: composer-3-*, composer-2.7.1-airflow-2.7.3.  
GKEJobHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GKEKubernetesHook Available in 10.17.0. Versions: composer-3-*, composer-2.7.1-airflow-2.7.3.  
GKEPodAsyncHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GKEKubernetesAsyncHook Available in 10.17.0. Versions: composer-3-*, composer-2.7.1-airflow-2.7.3.  
GKEPodHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GKEKubernetesHook Available in 10.17.0. Versions: composer-3-*, composer-2.7.1-airflow-2.7.3.  
GoogleAnalyticsDataImportUploadOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleAnalyticsAdminCreateDataStreamOperator Available in 8.14.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GoogleAnalyticsDeletePreviousDataUploadsOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleAnalyticsAdminDeleteDataStreamOperator Available in 8.14.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GoogleAnalyticsGetAdsLinkOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleAnalyticsAdminGetGoogleAdsLinkOperator Available in 8.14.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GoogleAnalyticsHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleAnalyticsAdminHook Available in 8.14.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GoogleAnalyticsListAccountsOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleAnalyticsAdminListAccountsOperator Available in 8.14.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GoogleAnalyticsRetrieveAdsLinksListOperator Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleAnalyticsAdminListGoogleAdsLinksOperator Available in 8.14.0. Versions: composer-3-*, composer-2.3.0-airflow-2.5.1, composer-2.3.0-airflow-2.4.3.  
GoogleDisplayVideo360CreateQueryOperator Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  display_video.GoogleDisplayVideo360CreateSDFDownloadTaskOperator Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
GoogleDisplayVideo360DeleteReportOperator Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  SDF export task in v4 of the API Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
GoogleDisplayVideo360DownloadLineItemsOperator Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  display_video.GoogleDisplayVideo360CreateSDFDownloadTaskOperator Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
GoogleDisplayVideo360DownloadReportV2Operator Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  display_video.GoogleDisplayVideo360SDFtoGCSOperator Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
GoogleDisplayVideo360RunQueryOperator Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  display_video.GoogleDisplayVideo360CreateSDFDownloadTaskOperator Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
GoogleDisplayVideo360RunQuerySensor Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  SDF export task in v4 of the API Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
GoogleDisplayVideo360UploadLineItemsOperator Removed in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5. |  display_video.GoogleDisplayVideo360SDFtoGCSOperator Available in 18.0.0. Versions: composer-3-airflow-3.1.0-build.2, composer-3-airflow-2.10.5-build.17, composer-2.15.0-airflow-2.10.5.  
LifeSciencesHook Removed in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  Google Cloud Batch Operators' hook Available in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
LifeSciencesLink Removed in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  No replacement (API discontinued)  
LifeSciencesRunPipelineOperator Removed in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  Google Cloud Batch Operators Available in 17.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
MLEngineAsyncHook Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  vertex_ai.ModelServiceHook Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineCreateModelOperator Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  corresponding VertexAI operator Available in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5.  
MLEngineCreateVersionOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  parent_model parameter for VertexAI operators Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineDeleteModelOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  DeleteModelOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineDeleteVersionOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  DeleteModelVersionOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineGetModelOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  GetModelOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineHook Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  vertex_ai.ModelServiceHook Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineJobDetailsLink Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  appropriate link from airflow.providers.google.cloud.links.vertex_ai Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineJobSListLink Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  appropriate link from airflow.providers.google.cloud.links.vertex_ai Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineListVersionsOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  ListModelVersionsOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineManageModelOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  MLEngineCreateModelOperator, MLEngineGetModelOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineManageVersionOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  MLEngineCreateVersion, MLEngineSetDefaultVersion, MLEngineListVersions, MLEngineDeleteVersion Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineModelLink Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  airflow.providers.google.cloud.links.vertex_ai.VertexAIModelLink Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineModelsListLink Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  airflow.providers.google.cloud.links.vertex_ai.VertexAIModelListLink Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineModelVersionDetailsLink Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  airflow.providers.google.cloud.links.vertex_ai.VertexAIModelLink Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineSetDefaultVersionOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  SetDefaultVersionOnModelOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineStartBatchPredictionJobOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  CreateBatchPredictionJobOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineStartTrainingJobOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  CreateCustomPythonPackageTrainingJobOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
MLEngineStartTrainingJobTrigger Removed in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1. |  appropriate trigger from airflow.providers.google.cloud.triggers.vertex_ai Available in 22.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
MLEngineTrainingCancelJobOperator Removed in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3. |  CancelCustomTrainingJobOperator Available in 15.0.0. Versions: composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.2, composer-2.13.0-airflow-2.10.5, composer-2.13.1-airflow-2.9.3.  
PromptLanguageModelOperator Removed in 13.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  TextGenerationModelPredictOperator Available in 10.21.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
PromptMultimodalModelOperator Removed in 13.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GenerativeModelGenerateContentOperator Available in 10.21.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
PromptMultimodalModelWithMediaOperator Removed in 13.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GenerativeModelGenerateContentOperator Available in 10.21.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
RunDataPipelineOperator Removed in 12.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  DataflowRunPipelineOperator Available in 10.20.0. Versions: composer-3-airflow-2.9.1-build.0, composer-3-airflow-2.7.3-build.9, composer-2.8.6-airflow-2.9.1, composer-2.8.6-airflow-2.7.3.  
SecretsManagerHook Removed in 11.0.0. Versions: composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.2-build.12, composer-3-airflow-2.9.3-build.19, composer-2.12.1-airflow-2.10.5, composer-2.12.0-airflow-2.10.2, composer-2.12.0-airflow-2.9.3. |  GoogleCloudSecretManagerHook Available in 10.18.0. Versions: composer-3-airflow-2.7.3-build.6, composer-2.8.3-airflow-2.7.3.  
SupervisedFineTuningTrainOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  GenAISupervisedFineTuningTrainOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
TextEmbeddingModelGetEmbeddingsOperator Deprecated in 18.1.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  GenAIGenerateEmbeddingsOperator Available in 21.0.0. Versions: composer-3-airflow-3.1.7-build.11, composer-3-airflow-2.11.1-build.7, composer-2.17.4-airflow-2.11.1.  
TextGenerationModelPredictOperator Removed in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5. |  GenerativeModelGenerateContentOperator Available in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
TranslationDatasetListLink Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  TranslationDatasetsListLink Available in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
TranslationLegacyDatasetLink Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  TranslationDatasetsListLink Available in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
TranslationLegacyModelLink Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  TranslationModelLink Available in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
TranslationLegacyModelTrainLink Removed in 19.0.0. Versions: composer-3-airflow-2.10.5-build.22, composer-2.16.0-airflow-2.10.5. |  TranslationModelsListLink Available in 16.0.0. Versions: composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5.  
  
## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)
  * [Troubleshooting Scheduler](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling)
  * [Google Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/index.html)
  * [Google Cloud Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html)
  * [Apache Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
