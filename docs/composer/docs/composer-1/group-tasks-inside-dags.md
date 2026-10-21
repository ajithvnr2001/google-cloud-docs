---
url: https://docs.cloud.google.com/composer/docs/composer-1/group-tasks-inside-dags/
title: Group tasks inside DAGs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:00.229328+00:00
---

# Group tasks inside DAGs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/group-tasks-inside-dags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Group tasks inside DAGs Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/group-tasks-inside-dags "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/group-tasks-inside-dags "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how you can group tasks in your Airflow pipelines using the following design patterns:

  * Grouping tasks in the DAG graph.
  * Triggering children DAGs from a parent DAG.
  * Grouping tasks with the `TaskGroup` operator.

**Important:** Airflow provides [SubDAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#subdags) to address repeating tasks. Despite being a common design pattern for grouping tasks together, SubDAGs often cause performance and functional issues, and is deprecated in Airflow. We recommend to **avoid using SubDAGs to group tasks together** in your workflow and prefer one of the alternative approaches described in this page.

## Group tasks in the DAG graph

To group tasks in certain phases of your pipeline, you can use relationships between the tasks in your DAG file.

Consider the following example:

[ ![The graph of Airflow tasks showing branching tasks](https://docs.cloud.google.com/static/composer/docs/images/workflow-group-dags.png)](https://docs.cloud.google.com/static/composer/docs/images/workflow-group-dags.png) **Figure 1.** Tasks can be grouped together in an Airflow DAG (click to enlarge) 

In this workflow, tasks `op-1` and `op-2` run together after the initial task `start`. You can achieve this by grouping tasks together with the statement `start >> [task_1, task_2]`.

The following example provides a complete implementation of this DAG:

###  Airflow 2 
    
    
    from airflow import DAG
    from airflow.operators.bash import BashOperator
    from airflow.operators.dummy import DummyOperator
    from airflow.utils.dates import days_ago
    
    DAG_NAME = "all_tasks_in_one_dag"
    
    args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}
    
    with DAG(dag_id=DAG_NAME, default_args=args) as dag:
        start = DummyOperator(task_id="start")
    
        task_1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)
    
        task_2 = BashOperator(task_id="op-2", bash_command=":", dag=dag)
    
        some_other_task = DummyOperator(task_id="some-other-task")
    
        task_3 = BashOperator(task_id="op-3", bash_command=":", dag=dag)
    
        task_4 = BashOperator(task_id="op-4", bash_command=":", dag=dag)
    
        end = DummyOperator(task_id="end")
    
        start >> [task_1, task_2] >> some_other_task >> [task_3, task_4] >> end

###  Airflow 1 
    
    
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    from airflow.operators.dummy_operator import DummyOperator
    from airflow.utils.dates import days_ago
    
    DAG_NAME = "all_tasks_in_one_dag"
    
    args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}
    
    with DAG(dag_id=DAG_NAME, default_args=args) as dag:
        start = DummyOperator(task_id="start")
    
        task_1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)
    
        task_2 = BashOperator(task_id="op-2", bash_command=":", dag=dag)
    
        some_other_task = DummyOperator(task_id="some-other-task")
    
        task_3 = BashOperator(task_id="op-3", bash_command=":", dag=dag)
    
        task_4 = BashOperator(task_id="op-4", bash_command=":", dag=dag)
    
        end = DummyOperator(task_id="end")
    
        start >> [task_1, task_2] >> some_other_task >> [task_3, task_4] >> end
    

## Trigger children DAGs from a parent DAG

You can trigger one DAG from another DAG with the [`TriggerDagRunOperator` operator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/trigger_dagrun/).

Consider the following example:

[ ![The graph of Airflow tasks showing children DAGs triggered as a part of a DAG graph](https://docs.cloud.google.com/static/composer/docs/images/workflow-trigger-dags.png)](https://docs.cloud.google.com/static/composer/docs/images/workflow-trigger-dags.png) **Figure 2.** DAGs can be triggered from within a DAG with the TriggerDagRunOperator (click to enlarge) 

In this workflow, the blocks `dag_1` and `dag_2` represent a series of tasks that are grouped together in a separate DAG in the Managed Airflow environment.

The implementation of this workflow requires two separate DAG files. The controlling DAG file looks like the following:

###  Airflow 2 
    
    
    from airflow import DAG
    from airflow.operators.dummy import DummyOperator
    from airflow.operators.trigger_dagrun import TriggerDagRunOperator
    from airflow.utils.dates import days_ago
    
    
    with DAG(
        dag_id="controller_dag_to_trigger_other_dags",
        default_args={"owner": "airflow"},
        start_date=days_ago(1),
        schedule_interval="@once",
    ) as dag:
        start = DummyOperator(task_id="start")
    
        trigger_1 = TriggerDagRunOperator(
            task_id="dag_1",
            trigger_dag_id="dag-to-trigger",  # Ensure this equals the dag_id of the DAG to trigger
            conf={"message": "Hello World"},
        )
        trigger_2 = TriggerDagRunOperator(
            task_id="dag_2",
            trigger_dag_id="dag-to-trigger",  # Ensure this equals the dag_id of the DAG to trigger
            conf={"message": "Hello World"},
        )
    
        some_other_task = DummyOperator(task_id="some-other-task")
    
        end = DummyOperator(task_id="end")
    
        start >> trigger_1 >> some_other_task >> trigger_2 >> end

###  Airflow 1 
    
    
    from airflow import DAG
    from airflow.operators.dagrun_operator import TriggerDagRunOperator
    from airflow.operators.dummy_operator import DummyOperator
    from airflow.utils.dates import days_ago
    
    
    with DAG(
        dag_id="controller_dag_to_trigger_other_dags",
        default_args={"owner": "airflow"},
        start_date=days_ago(1),
        schedule_interval="@once",
    ) as dag:
        start = DummyOperator(task_id="start")
    
        trigger_1 = TriggerDagRunOperator(
            task_id="dag_1",
            trigger_dag_id="dag-to-trigger",  # Ensure this equals the dag_id of the DAG to trigger
            conf={"message": "Hello World"},
        )
        trigger_2 = TriggerDagRunOperator(
            task_id="dag_2",
            trigger_dag_id="dag-to-trigger",  # Ensure this equals the dag_id of the DAG to trigger
            conf={"message": "Hello World"},
        )
    
        some_other_task = DummyOperator(task_id="some-other-task")
    
        end = DummyOperator(task_id="end")
    
        start >> trigger_1 >> some_other_task >> trigger_2 >> end

**Note:** The value for `trigger_dag_id` inside `TriggerDagRunOperator` must match the `dag_id` value of the DAG you want to trigger.

The implementation of the child DAG, which is triggered by the controlling DAG, looks like the following:

###  Airflow 2 
    
    
    from airflow import DAG
    from airflow.operators.dummy import DummyOperator
    from airflow.utils.dates import days_ago
    
    DAG_NAME = "dag-to-trigger"
    
    args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "None"}
    
    with DAG(dag_id=DAG_NAME, default_args=args) as dag:
        dag_task = DummyOperator(task_id="dag-task")

###  Airflow 1 
    
    
    from airflow import DAG
    from airflow.operators.dummy_operator import DummyOperator
    from airflow.utils.dates import days_ago
    
    
    DAG_NAME = "dag-to-trigger"
    
    args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "None"}
    
    with DAG(dag_id=DAG_NAME, default_args=args) as dag:
        dag_task = DummyOperator(task_id="dag-task")

You must [upload both DAG files](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags#add) in your Managed Airflow environment for the DAG to work.

## Grouping tasks with the TaskGroup operator

This approach works only in Airflow 2. 

You can use the [`TaskGroup` operator](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#taskgroups) to group tasks together in your DAG. Tasks defined within a `TaskGroup` block are still part of the main DAG.

Consider the following example:

[ ![The graph of Airflow tasks showing two task groups](https://docs.cloud.google.com/static/composer/docs/images/workflow-taskgroup-dag.png)](https://docs.cloud.google.com/static/composer/docs/images/workflow-taskgroup-dag.png) **Figure 3.** Tasks can be visually grouped together in the UI with the TaskGroup operator (click to enlarge) 

The tasks `op-1` and `op-2` are grouped together in a block with ID `taskgroup_1`. An implementation of this workflow looks like the following code:
    
    
    from airflow.models.dag import DAG
    from airflow.operators.bash import BashOperator
    from airflow.operators.dummy import DummyOperator
    from airflow.utils.dates import days_ago
    from airflow.utils.task_group import TaskGroup
    
    with DAG(dag_id="taskgroup_example", start_date=days_ago(1)) as dag:
        start = DummyOperator(task_id="start")
    
        with TaskGroup("taskgroup_1", tooltip="task group #1") as section_1:
            task_1 = BashOperator(task_id="op-1", bash_command=":")
            task_2 = BashOperator(task_id="op-2", bash_command=":")
    
        with TaskGroup("taskgroup_2", tooltip="task group #2") as section_2:
            task_3 = BashOperator(task_id="op-3", bash_command=":")
            task_4 = BashOperator(task_id="op-4", bash_command=":")
    
        some_other_task = DummyOperator(task_id="some-other-task")
    
        end = DummyOperator(task_id="end")
    
        start >> section_1 >> some_other_task >> section_2 >> end

## What's next

  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-1/write-dags)
  * [Test DAGs](https://docs.cloud.google.com/composer/docs/composer-1/test-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
