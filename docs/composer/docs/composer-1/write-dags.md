---
url: https://docs.cloud.google.com/composer/docs/composer-1/write-dags/
title: Write Airflow DAGs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:10.210686+00:00
---

# Write Airflow DAGs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/write-dags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Write Airflow DAGs Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/write-dags "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/write-dags "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This guide shows you how to write an Apache Airflow directed acyclic graph (DAG) that runs in a Managed Service for Apache Airflow environment.

Because Apache Airflow does not provide strong DAG and task isolation, we recommend that you use separate production and test environments to prevent DAG interference. For more information, see [Testing DAGs](https://docs.cloud.google.com/composer/docs/composer-1/test-dags).

**Note:** The way you implement your DAGs influences performance of DAG scheduling and execution. The [Scheduler troubleshooting](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-scheduling) and [DAG Troubleshooting](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags) sections provide information about how to implement and deploy your DAGs optimally and avoid common mistakes.

## Structuring an Airflow DAG

An Airflow DAG is defined in a Python file and is composed of the following components:

  * DAG definition
  * Airflow operators
  * Operator relationships



The following code snippets show examples of each component out of context.

### A DAG definition

The following example demonstrates an [Airflow DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) definition:

###  Airflow 2 
    
    
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

###  Airflow 1 
    
    
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

###  Airflow 2 
    
    
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

###  Airflow 1 
    
    
    from airflow.operators import bash_operator
    from airflow.operators import python_operator
    
        def greeting():
            import logging
    
            logging.info("Hello World!")
    
        # An instance of an operator is called a task. In this case, the
        # hello_python task calls the "greeting" Python function.
        hello_python = python_operator.PythonOperator(
            task_id="hello", python_callable=greeting
        )
    
        # Likewise, the goodbye_bash task calls a Bash script.
        goodbye_bash = bash_operator.BashOperator(
            task_id="bye", bash_command="echo Goodbye."
        )

### Task relationships

[Task relationships](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#relationships) describe the order in which the work must be completed.

###  Airflow 2 
    
    
    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hello_python >> goodbye_bash

###  Airflow 1 
    
    
    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hello_python >> goodbye_bash

### Full DAG workflow example in Python

The following workflow is a complete working DAG template that is composed of two tasks: a `hello_python` task and a `goodbye_bash` task:

###  Airflow 2 
    
    
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

###  Airflow 1 
    
    
    import datetime
    
    from airflow import models
    
    from airflow.operators import bash_operator
    from airflow.operators import python_operator
    
    
    
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
        hello_python = python_operator.PythonOperator(
            task_id="hello", python_callable=greeting
        )
    
        # Likewise, the goodbye_bash task calls a Bash script.
        goodbye_bash = bash_operator.BashOperator(
            task_id="bye", bash_command="echo Goodbye."
        )
    
        # Define the order in which the tasks complete by using the >> and <<
        # operators. In this example, hello_python executes before goodbye_bash.
        hello_python >> goodbye_bash

For more information about defining Airflow DAGs, see the [Airflow tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) and [Airflow concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html).

## Airflow operators

The following examples show a few popular Airflow operators. For an authoritative reference of Airflow operators, see the [Operators and Hooks Reference](https://airflow.apache.org/docs/apache-airflow-providers/operators-and-hooks-ref/index.html) and [Providers index](https://airflow.apache.org/docs/#providers-packages-docs-apache-airflow-providers-index-html).

### BashOperator

Use the [BashOperator](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html) to run command-line programs.

###  Airflow 2 
    
    
    from airflow.operators import bash
    
        # Create BigQuery output dataset.
        make_bq_dataset = bash.BashOperator(
            task_id="make_bq_dataset",
            # Executing 'bq' command requires Google Cloud SDK which comes
            # preinstalled in Cloud Composer.
            bash_command=f"bq ls {bq_dataset_name} || bq mk {bq_dataset_name}",
        )

###  Airflow 1 
    
    
    from airflow.operators import bash_operator
    
        # Create BigQuery output dataset.
        make_bq_dataset = bash_operator.BashOperator(
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

To install additional Python packages, see [Installing Python Dependencies](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies).

### Google Cloud Operators

To run tasks that use Google Cloud products, use the Google Cloud Airflow operators. For example, [BigQuery operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html) query and process data in [BigQuery](https://docs.cloud.google.com/bigquery/docs).

There are many more Airflow operators for Google Cloud and individual services provided by Google Cloud. See [Google Cloud Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html) for the full list.

**Note:** Managed Airflow automatically configures [Airflow connections](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html) for many Google Cloud services. For more information, see [Manage Airflow connections](https://docs.cloud.google.com/composer/docs/composer-1/manage-airflow-connections).

###  Airflow 2 
    
    
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

###  Airflow 1 
    
    
    from airflow.contrib.operators import bigquery_operator
    
        # Query recent StackOverflow questions.
        bq_recent_questions_query = bigquery_operator.BigQueryOperator(
            task_id="bq_recent_questions_query",
            sql="""
            SELECT owner_display_name, title, view_count
            FROM `bigquery-public-data.stackoverflow.posts_questions`
            WHERE creation_date < CAST('{max_date}' AS TIMESTAMP)
                AND creation_date >= CAST('{min_date}' AS TIMESTAMP)
            ORDER BY view_count DESC
            LIMIT 100
            """.format(
                max_date=max_query_date, min_date=min_query_date
            ),
            use_legacy_sql=False,
            destination_dataset_table=bq_recent_questions_table_id,
        )

### EmailOperator

Use the [EmailOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/email/index.html) to send email from a DAG. To send email from a Managed Airflow environment, [configure your environment to use SendGrid](https://docs.cloud.google.com/composer/docs/composer-1/configure-email).

###  Airflow 2 
    
    
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

###  Airflow 1 
    
    
    from airflow.operators import email_operator
    
        # Send email confirmation
        email_summary = email_operator.EmailOperator(
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

Set `email_on_failure` to `True` to send an email notification when an operator in the DAG fails. To send email notifications from a Managed Airflow environment, you must [configure your environment to use SendGrid](https://docs.cloud.google.com/composer/docs/composer-1/configure-email).

###  Airflow 2 
    
    
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

###  Airflow 1 
    
    
    from airflow import models
    
    default_dag_args = {
        "start_date": yesterday,
        # Email whenever an Operator in the DAG fails.
        "email": "{{var.value.email}}",
        "email_on_failure": True,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": datetime.timedelta(minutes=5),
        "project_id": "{{var.value.gcp_project}}",
    }
    
    with models.DAG(
        "composer_sample_bq_notify",
        schedule_interval=datetime.timedelta(weeks=4),
        default_args=default_dag_args,
    ) as dag:

## DAG workflow guidelines

  * Place any custom Python libraries in a DAG's ZIP archive in a nested directory. Do not place libraries at the top level of the DAGs directory.

When Airflow scans the `dags/` folder, Airflow only checks for DAGs in Python modules that are in the top-level of the DAGs folder and in the top level of a ZIP archive also located in the top-level `dags/` folder. If Airflow encounters a Python module in a ZIP archive that does not contain both `airflow` and `DAG` substrings, Airflow stops processing the ZIP archive. Airflow returns only the DAGs found up to that point.

  * Use Airflow 2 instead of Airflow 1.

The Airflow community does not publish new minor or patch releases for Airflow 1 anymore.

  * For fault tolerance, do not define multiple DAG objects in the same Python module.

  * Do not use SubDAGs. Instead, [group tasks inside DAGs](https://docs.cloud.google.com/composer/docs/composer-1/group-tasks-inside-dags).

  * Place files that are required at DAG parse time into `dags/` folder, not in the `data/` folder.

  * [Implement unit tests for your DAGs](https://docs.cloud.google.com/composer/docs/samples/composer-dag-unit-testing).

  * Test developed or modified DAGs as recommended in [instructions for testing DAGs](https://docs.cloud.google.com/composer/docs/composer-1/test-dags).

  * Verify that developed DAGs do not increase [DAG parse times](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-scheduling#inspecting_dag_parse_times) too much.

  * Airflow tasks can fail for multiple reasons. To avoid failures of whole DAG runs, we recommend to enable task retries. Setting maximum retries to `0` means that no retries are performed.

We recommend to [override](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the [`default_task_retries`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#default-task-retries) option with a value for the task retries other than `0`. In addition, you can set the [`retries` parameter](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#timeouts) at the task level.

  * If you want to use GPU in your Airflow tasks then create a separate GKE cluster based on nodes using machines with GPUs. Use [GKEStartPodOperator](https://docs.cloud.google.com/composer/docs/composer-1/use-gke-operator) to run your tasks.

  * Avoid running CPU- and memory-heavy tasks in the cluster's node pool where other Airflow components (schedulers, workers, web servers) are running. Instead, use [KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-1/use-kubernetes-pod-operator) or [GKEStartPodOperator](https://docs.cloud.google.com/composer/docs/composer-1/use-gke-operator) instead.

  * When deploying DAGs into an environment, upload only the files that are absolutely necessary for interpreting and executing DAGs into the `/dags` folder.

  * Limit the number of DAG files in `/dags` folder.

Airflow is continuously parsing DAGs in `/dags` folder. The parsing is a process that loops through the DAGs folder and the number of files that need to be loaded (with their dependencies) makes impacts the performance of DAG parsing and task scheduling. It is much more efficient to use 100 files with 100 DAGs each than 10000 files with 1 DAG each and so such optimization is recommended. This optimization is a balance between parsing time and efficiency of DAG authoring and management.

You can also consider, for example, to deploy 10000 DAG files you could create 100 zip files each containing 100 DAG files.

In addition to hints above, if you have more than 10000 DAG files then generating DAGs in a programamtic way might be a good option. For example, you can implement a single Python DAG file that generates some number of DAG objects (for example, 20, 100 DAG objects).

  * Avoid using deprecated Airflow operators. Instead, use their up-to-date alternatives.

  * Avoid using [CloudLoggingHandler](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.handlers.handlers.CloudLoggingHandler) to handle logging. This logging handler causes the environment's database overload and subsequent DAG failures with the "server closed the connection unexpectedly" errors.




## FAQs for writing DAGs

### How do I minimize code repetition if I want to run the same or similar tasks in multiple DAGs?

We suggest [defining libraries](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-local) and wrappers to minimize the code repetition.

### How do I reuse code between DAG files?

Put your utility functions in a [local Python library](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-local) and import the functions. You can reference the functions in any DAG located in the `dags/` folder in your environment's bucket.

### How do I minimize the risk of different definitions arising?

For example, you have two teams that want to aggregate raw data into revenue metrics. The teams write two slightly different tasks that accomplish the same thing. [Define libraries](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-local) to work with the revenue data so that the DAG implementers must clarify the definition of revenue that's being aggregated.

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

Instead, use [`KubernetesPodOperator`](https://docs.cloud.google.com/composer/docs/composer-1/use-kubernetes-pod-operator) or [`GKEStartPodOperator`](https://docs.cloud.google.com/composer/docs/composer-1/use-gke-operator). These operators launch Kubernetes pods into Kubernetes or GKE clusters respectively. Note that we don't recommend launching pods into an environment's cluster, because this can lead to resource competition.

### Should I use the `SubDagOperator`?

We do not recommend using the `SubDagOperator`.

Use alternatives as suggested in [Grouping tasks](https://docs.cloud.google.com/composer/docs/composer-1/group-tasks-inside-dags).

### Should I run Python code only in `PythonOperators` to fully separate Python operators?

Depending on your goal, you have a few options.

If your only concern is maintaining separate Python dependencies, you can use the `PythonVirtualenvOperator`.

Consider [using the `KubernetesPodOperator`](https://docs.cloud.google.com/composer/docs/composer-1/use-kubernetes-pod-operator). This operator allows you to define Kubernetes pods and run the pods in other clusters.

### How do I add custom binary or non-PyPI packages?

You can [install packages hosted in private package repositories](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-private-repo).

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

  * The latest maintenance release of Managed Airflow (Legacy Gen 1) (1.20.12) uses a version of the `apache-airflow-providers-google` package which is based on public version 8.9.0. See the following table to determine if a specific operator is supported or a replacement is available based on the listed version of the package.

  * Some of the replacement operators are not supported in any version of Managed Airflow (Legacy Gen 1). To use them, consider upgrading to Managed Airflow (Gen 3) or Managed Airflow (Gen 2).


Deprecated operator | Replacement operator  
---|---  
AutoMLBatchPredictOperator |  vertex_ai.batch_prediction_job  
AutoMLCreateDatasetOperator |  vertex_ai.dataset.CreateDatasetOperator, translate.TranslateCreateDatasetOperator  
AutoMLDatasetLink |  TranslationLegacyDatasetLink  
AutoMLDatasetListLink |  TranslationDatasetListLink  
AutoMLDeleteDatasetOperator |  vertex_ai.dataset.ListDatasetsOperator, translate.TranslateDatasetsListOperator  
AutoMLDeleteModelOperator |  vertex_ai.model_service.DeleteModelOperator, translate.TranslateDeleteModelOperator  
AutoMLDeployModelOperator |  vertex_ai.endpoint_service.DeployModelOperator  
AutoMLGetModelOperator |  vertex_ai.model_service.GetModelOperator  
AutoMLImportDataOperator |  vertex_ai.dataset.ImportDataOperator, translate.TranslateImportDataOperator  
AutoMLListDatasetOperator |  vertex_ai.dataset.ListDatasetsOperator, translate.TranslateDatasetsListOperator  
AutoMLModelLink |  TranslationLegacyModelLink  
AutoMLModelPredictLink |  TranslationLegacyModelPredictLink  
AutoMLModelTrainLink |  TranslationLegacyModelTrainLink  
AutoMLPredictOperator |  TextGenerationModelPredictOperator, TranslateTextOperator  
AutoMLTablesListColumnSpecsOperator |  No replacement (legacy version of AutoML Tables shut down)  
AutoMLTablesListTableSpecsOperator |  No replacement (legacy version of AutoML Tables shut down)  
AutoMLTablesUpdateDatasetOperator |  vertex_ai.dataset.UpdateDatasetOperator  
AutoMLTrainModelOperator |  vertex_ai.auto_ml.CreateAutoMLTabularTrainingJobOperator, CreateAutoMLVideoTrainingJobOperator, CreateAutoMLImageTrainingJobOperator, SupervisedFineTuningTrainOperator, TranslateCreateModelOperator  
BigQueryCreateEmptyTableOperator |  BigQueryCreateTableOperator  
BigQueryCreateExternalTableOperator |  BigQueryCreateTableOperator  
BigQueryExecuteQueryOperator |  BigQueryInsertJobOperator  
BigQueryPatchDatasetOperator |  BigQueryUpdateDatasetOperator  
BigQueryTableExistenceAsyncSensor |  BigQueryTableExistenceSensor  
BigQueryTableExistencePartitionAsyncSensor |  BigQueryTablePartitionExistenceSensor  
CloudAutoMLHook |  vertex_ai.auto_ml.AutoMLHook, translate.TranslateHook  
CloudComposerEnvironmentSensor |  CloudComposerCreateEnvironmentOperator, CloudComposerDeleteEnvironmentOperator, CloudComposerUpdateEnvironmentOperator  
CloudDataCatalogCreateEntryGroupOperator |  DataplexCatalogCreateEntryGroupOperator  
CloudDataCatalogCreateEntryOperator |  DataplexCatalogCreateEntryOperator  
CloudDataCatalogCreateTagOperator |  DataplexCatalogCreateEntryOperator, DataplexCatalogUpdateEntryOperator  
CloudDataCatalogCreateTagTemplateFieldOperator |  DataplexCatalogUpdateAspectTypeOperator, DataplexCatalogCreateAspectTypeOperator  
CloudDataCatalogCreateTagTemplateOperator |  DataplexCatalogCreateAspectTypeOperator  
CloudDataCatalogDeleteEntryGroupOperator |  DataplexCatalogDeleteEntryGroupOperator  
CloudDataCatalogDeleteTagOperator |  DataplexCatalogUpdateEntryOperator  
CloudDataCatalogDeleteTagTemplateFieldOperator |  DataplexCatalogUpdateAspectTypeOperator  
CloudDataCatalogDeleteTagTemplateOperator |  DataplexCatalogDeleteAspectTypeOperator  
CloudDataCatalogGetEntryGroupOperator |  DataplexCatalogGetEntryGroupOperator  
CloudDataCatalogGetEntryOperator |  DataplexCatalogGetEntryOperator  
CloudDataCatalogGetTagTemplateOperator |  DataplexCatalogGetAspectTypeOperator  
CloudDataCatalogHook |  DataplexHook  
CloudDataCatalogListTagsOperator |  DataplexCatalogGetEntryOperator  
CloudDataCatalogLookupEntryOperator |  DataplexCatalogLookupEntryOperator  
CloudDataCatalogRenameTagTemplateFieldOperator |  DataplexCatalogUpdateAspectTypeOperator  
CloudDataCatalogSearchCatalogOperator |  DataplexCatalogSearchEntriesOperator  
CloudDataCatalogUpdateEntryOperator |  DataplexCatalogUpdateEntryOperator  
CloudDataCatalogUpdateTagOperator |  DataplexCatalogUpdateEntryOperator  
CloudDataCatalogUpdateTagTemplateFieldOperator |  DataplexCatalogUpdateAspectTypeOperator  
CloudDataCatalogUpdateTagTemplateOperator |  DataplexCatalogUpdateAspectTypeOperator  
CountTokensOperator |  GenAICountTokensOperator  
CreateAutoMLTextTrainingJobOperator |  SupervisedFineTuningTrainOperator  
CreateCachedContentOperator |  GenAICreateCachedContentOperator  
CreateDataPipelineOperator |  DataflowCreatePipelineOperator  
DataCatalogEntryGroupLink |  DataplexCatalogEntryGroupLink  
DataCatalogEntryLink |  DataplexCatalogEntryLink  
DataCatalogTagTemplateLink |  DataplexCatalogAspectTypeLink  
DataflowCreateJavaJobOperator |  beam.BeamRunJavaPipelineOperator  
DataflowCreatePythonJobOperator |  beam.BeamRunPythonPipelineOperator  
DataflowStartSqlJobOperator |  DataflowStartYamlJobOperator  
DataPipelineHook |  DataflowHook  
DataprocScaleClusterOperator |  DataprocUpdateClusterOperator  
DataprocSubmitHadoopJobOperator |  DataprocSubmitJobOperator  
DataprocSubmitHiveJobOperator |  DataprocSubmitJobOperator  
DataprocSubmitPigJobOperator |  DataprocSubmitJobOperator  
DataprocSubmitPySparkJobOperator |  DataprocSubmitJobOperator  
DataprocSubmitSparkJobOperator |  DataprocSubmitJobOperator  
DataprocSubmitSparkSqlJobOperator |  DataprocSubmitJobOperator  
DeleteExperimentRunOperator |  DeleteExperimentRunOperator  
GCSObjectExistenceAsyncSensor |  GCSObjectExistenceSensor  
GCSObjectsWtihPrefixExistenceSensor |  GCSObjectsWithPrefixExistenceSensor  
GenerateFromCachedContentOperator |  GenAIGenerateContentOperator  
GenerateTextEmbeddingsOperator |  TextEmbeddingModelGetEmbeddingsOperator  
GenerativeModelGenerateContentOperator |  GenAIGenerateContentOperator  
GKECustomResourceHook |  GKEKubernetesHook  
GKEDeploymentHook |  GKEKubernetesHook  
GKEJobHook |  GKEKubernetesHook  
GKEPodAsyncHook |  GKEKubernetesAsyncHook  
GKEPodHook |  GKEKubernetesHook  
GoogleAnalyticsDataImportUploadOperator |  GoogleAnalyticsAdminCreateDataStreamOperator  
GoogleAnalyticsDeletePreviousDataUploadsOperator |  GoogleAnalyticsAdminDeleteDataStreamOperator  
GoogleAnalyticsGetAdsLinkOperator |  GoogleAnalyticsAdminGetGoogleAdsLinkOperator  
GoogleAnalyticsHook |  GoogleAnalyticsAdminHook  
GoogleAnalyticsListAccountsOperator |  GoogleAnalyticsAdminListAccountsOperator  
GoogleAnalyticsRetrieveAdsLinksListOperator |  GoogleAnalyticsAdminListGoogleAdsLinksOperator  
GoogleDisplayVideo360CreateQueryOperator |  display_video.GoogleDisplayVideo360CreateSDFDownloadTaskOperator  
GoogleDisplayVideo360DeleteReportOperator |  SDF export task in v4 of the API  
GoogleDisplayVideo360DownloadLineItemsOperator |  display_video.GoogleDisplayVideo360CreateSDFDownloadTaskOperator  
GoogleDisplayVideo360DownloadReportV2Operator |  display_video.GoogleDisplayVideo360SDFtoGCSOperator  
GoogleDisplayVideo360RunQueryOperator |  display_video.GoogleDisplayVideo360CreateSDFDownloadTaskOperator  
GoogleDisplayVideo360RunQuerySensor |  SDF export task in v4 of the API  
GoogleDisplayVideo360UploadLineItemsOperator |  display_video.GoogleDisplayVideo360SDFtoGCSOperator  
LifeSciencesHook |  Google Cloud Batch Operators' hook  
LifeSciencesLink |  No replacement (API discontinued)  
LifeSciencesRunPipelineOperator |  Google Cloud Batch Operators  
MLEngineAsyncHook |  vertex_ai.ModelServiceHook  
MLEngineCreateModelOperator |  corresponding VertexAI operator  
MLEngineCreateVersionOperator |  parent_model parameter for VertexAI operators  
MLEngineDeleteModelOperator |  DeleteModelOperator  
MLEngineDeleteVersionOperator |  DeleteModelVersionOperator  
MLEngineGetModelOperator |  GetModelOperator  
MLEngineHook |  vertex_ai.ModelServiceHook  
MLEngineJobDetailsLink |  appropriate link from airflow.providers.google.cloud.links.vertex_ai  
MLEngineJobSListLink |  appropriate link from airflow.providers.google.cloud.links.vertex_ai  
MLEngineListVersionsOperator |  ListModelVersionsOperator  
MLEngineManageModelOperator |  MLEngineCreateModelOperator, MLEngineGetModelOperator  
MLEngineManageVersionOperator |  MLEngineCreateVersion, MLEngineSetDefaultVersion, MLEngineListVersions, MLEngineDeleteVersion  
MLEngineModelLink |  airflow.providers.google.cloud.links.vertex_ai.VertexAIModelLink  
MLEngineModelsListLink |  airflow.providers.google.cloud.links.vertex_ai.VertexAIModelListLink  
MLEngineModelVersionDetailsLink |  airflow.providers.google.cloud.links.vertex_ai.VertexAIModelLink  
MLEngineSetDefaultVersionOperator |  SetDefaultVersionOnModelOperator  
MLEngineStartBatchPredictionJobOperator |  CreateBatchPredictionJobOperator  
MLEngineStartTrainingJobOperator |  CreateCustomPythonPackageTrainingJobOperator  
MLEngineStartTrainingJobTrigger |  appropriate trigger from airflow.providers.google.cloud.triggers.vertex_ai  
MLEngineTrainingCancelJobOperator |  CancelCustomTrainingJobOperator  
PromptLanguageModelOperator |  TextGenerationModelPredictOperator  
PromptMultimodalModelOperator |  GenerativeModelGenerateContentOperator  
PromptMultimodalModelWithMediaOperator |  GenerativeModelGenerateContentOperator  
RunDataPipelineOperator |  DataflowRunPipelineOperator  
SecretsManagerHook |  GoogleCloudSecretManagerHook  
SupervisedFineTuningTrainOperator |  GenAISupervisedFineTuningTrainOperator  
TextEmbeddingModelGetEmbeddingsOperator |  GenAIGenerateEmbeddingsOperator  
TextGenerationModelPredictOperator |  GenerativeModelGenerateContentOperator  
TranslationDatasetListLink |  TranslationDatasetsListLink  
TranslationLegacyDatasetLink |  TranslationDatasetsListLink  
TranslationLegacyModelLink |  TranslationModelLink  
TranslationLegacyModelTrainLink |  TranslationModelsListLink  
  
## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags)
  * [Troubleshooting Scheduler](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-scheduling)
  * [Google Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/index.html)
  * [Google Cloud Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html)
  * [Apache Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
