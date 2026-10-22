---
url: https://docs.cloud.google.com/composer/docs/composer-3/debug-task-scheduling-issues/
title: Debug task scheduling issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:37.968500+00:00
---

# Debug task scheduling issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/debug-task-scheduling-issues/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Debug task scheduling issues Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/debug-task-scheduling-issues "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

**Note:** This page is **not yet revised for Managed Airflow (Gen 3)** and displays content for Managed Airflow (Gen 2).

This tutorial guides you through diagnosing and troubleshooting task scheduling and parsing issues that lead to scheduler malfunctioning, parsing errors and latency, and task failure.

## Introduction

The Airflow scheduler is primarily impacted by two factors: task scheduling and DAG parsing. Issues in one of those factors can have a negative impact on the environment health and performance.

Sometimes too many tasks are scheduled simultaneously. In this situation, the queue is filled up, and tasks remain in the "scheduled" state or become rescheduled after being queued, which might cause task failure and performance latency.

Another common issue is parsing latency and errors caused by the complexity of a DAG code. For example, a DAG code that contains Airflow variables at the top level of the code can lead to parsing delays, database overload, scheduling failures, and DAG timeouts.

In this tutorial, you will diagnose the example DAGs and learn how to troubleshoot scheduling and parsing problems, improve DAG scheduling, and optimize your DAG code and environment configurations to improve performance.

## Objectives

This section lists objectives for examples in this tutorial.

### Example: Scheduler malfunctioning and latency caused by high task concurrency

  * Upload the sample DAG that runs multiple times simultaneously and diagnose the scheduler malfunctioning and latency issues with Cloud Monitoring.

  * Optimize your DAG code by consolidating the tasks and evaluate the performance impact.

  * Distribute the tasks more evenly over time and evaluate the performance impact.

  * Optimize your Airflow configurations and environment configurations and evaluate the impact.




### Example: DAG parsing errors and latency caused by complex code

  * Upload the sample DAG with Airflow variables and diagnose parsing issues with Cloud Monitoring.

  * Optimize the DAG code by avoiding Airflow variables at the top level of the code and evaluate the impact on parsing time.

  * Optimize Airflow configurations and environment configurations and evaluate the impact on parsing time.




## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Managed Airflow](https://docs.cloud.google.com/composer/pricing) (see [additional costs](https://docs.cloud.google.com/composer/pricing#additional-costs))
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring#pricing)



When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more details, see Clean up.

## Before you begin

This section describes actions that are required before you start the tutorial.

### Create and configure a project

For this tutorial, you need a Google Cloud [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). Configure the project in the following way:

  1. In the Google Cloud console, [select or create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):

[Go to Project Selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. [Learn how to check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Make sure that your Google Cloud project user has the following [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to create the necessary resources:

     * **Environment and Storage Object Administrator** (`roles/composer.environmentAndStorageObjectAdmin`)
     * **Compute Admin** (`roles/compute.admin`)



### Enable APIs for your project

Enable the Managed Airflow API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=composer.googleapis.com)

### Create your Managed Airflow environment

[Create a Managed Airflow (Gen 2) environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#basic-setup).

**Important:** Make sure that you use the **Small environment preset** in order to reproduce the errors when using the examples provided further in this tutorial. This is the default preset when creating an environment through Google Cloud console.

[As a part of creating the environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#grant-permissions), you grant the **Cloud Composer v2 API Service Agent Extension** (`roles/composer.ServiceAgentV2Ext`) role to the Composer Service Agent account. Managed Airflow uses this account to perform operations in your Google Cloud project.

## Example: Scheduler malfunctioning and task failure because of task scheduling issues

This example demonstrates debugging scheduler malfunctioning and latency caused by high task concurrency.

### Upload the sample DAG to your environment

[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the following sample DAG to the environment that you created in the previous steps. In this tutorial, this DAG is named `dag_10_tasks_200_seconds_1`.

This DAG has 200 tasks. Each task waits for 1 second and prints "Complete!". The DAG is triggered automatically once uploaded. Managed Airflow runs this DAG 10 times, and all DAG runs happen in parallel.

**Warning:** This DAG **simulates issues with DAG scheduling** , which can potentially disrupt operations in your environment.
    
    
    import time
    from datetime import datetime, timedelta
    
    from airflow import DAG
    from airflow.decorators import task
    
    
    tasks_amount = 200
    seconds = 1
    minutes = 5
    
    with DAG(
        dag_id=f"dag_10_tasks_{tasks_amount}_sec_{seconds}",
        start_date=datetime(2023, 11, 22, 20, 0),
        end_date=datetime(2023, 11, 22, 20, 49),
        schedule=timedelta(minutes=minutes),
        catchup=True,
    ) as dag:
    
        @task
        def create_subtasks(seconds: int) -> None:
            time.sleep(seconds)
    
        for i in range(tasks_amount):
            create_subtasks(seconds)
    

### Diagnose the scheduler malfunctioning and task failure issues

After the DAG runs complete, open Airflow UI, and click the `dag_10_tasks_200_seconds_1` DAG. You will see that 10 total DAG runs were successful, and each has 200 tasks that succeeded.

Review the Airflow task logs:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Logs** tab, then go to **All logs** > **Airflow logs** > **Workers** > **View in Logs Explorer**.




On the logs histogram, you can see the errors and warnings indicated with red and orange colors:

[ ![The histogram of Airflow worker logs with errors and warnings
    indicated with red and orange colors](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram.png) **Figure 1.** Airflow worker logs histogram (click to enlarge) 

The example DAG resulted in about 130 warnings and 60 errors. Click any column that contains yellow and red bars. You will see some of the following warnings and errors in the logs:
    
    
    State of this instance has been externally set to success. Terminating
    instance.
    
    Received SIGTERM. Terminating subprocesses.
    
    worker: Warm shutdown (MainProcess).
    

These logs might indicate that the resource usage exceeded the limits and the worker restarted itself.

If an Airflow task is kept in the queue for too long then the scheduler marks it as failed and up_for_retry and is going to reschedule it once again for execution. One way to observe the symptoms of this situation is to look at the chart with the number of queued tasks and if the spikes in this chart don't drop in about 10 minutes, then there will likely be failures of tasks (with no logs).

Review the monitoring information:

  1. Go to the **Monitoring** tab and select **Overview**.

  2. Review the **Airflow tasks** graph.

[ ![The graph of Airflow tasks over time, showing a spike in the
    number of queued tasks](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-airflow-tasks-graph.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-airflow-tasks-graph.png) **Figure 2.** Airflow tasks graph (click to enlarge) 

In the Airflow tasks graph, there is a spike in queued tasks that lasts for more than 10 minutes, which might mean that there are not enough resources in your environment to process all scheduled tasks.

  3. Review the **Active workers** graph:

[ ![The graph of active Airflow workers over time shows that the
    numebr of active workers was increased up to the maximum limit](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-active-workers-graph.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-active-workers-graph.png) **Figure 3.** Active workers graph (click to enlarge) 

The **Active workers** graph indicates that the DAG triggered autoscaling to the maximum allowed limit of three workers during the DAG run.

  4. Resource usage graphs can indicate the lack of capacity in Airflow workers to run queued tasks. On the **Monitoring** tab, select **Workers** and review **Total worker CPU usage** and **Total worker memory usage** graphs.

[ ![The graph of CPU usage by Airflow workers shows CPU usage
    increasing up to the maximum limit](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-cpu-usage-graph.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-cpu-usage-graph.png) **Figure 4.** Total workers CPU usage graph (click to enlarge) [ ![The graph of memory usage by Airflow workers shows memory usage
    increasing, but not reaching the maximum limit](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-memory-usage-graph.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-memory-usage-graph.png) **Figure 5.** Total workers memory usage graph (click to enlarge) 

The graphs indicate that the execution of too many tasks simultaneously resulted in hitting the CPU limit. The resources had been used for over 30 minutes, which is even longer than the total duration of 200 tasks in 10 DAG runs running one by one.




These are the indicators of the queue being filled up and a lack of resources to process all scheduled tasks.

### Consolidate your tasks

The current code creates many DAGs and tasks with no sufficient resources to process all tasks in parallel, which results in the queue being filled up. Keeping tasks in the queue for too long may cause tasks to reschedule or fail. In such situations, you should opt for a smaller number of more consolidated tasks.

The following sample DAG changes the number of tasks in the initial example from 200 to 20 and increase the wait time from 1 to 10 seconds to imitate more consolidated tasks that do the same amount of work.

[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the following sample DAG to the environment that you created. In this tutorial, this DAG is named `dag_10_tasks_20_seconds_10`.

**Warning:** This DAG **simulates issues with DAG scheduling** , which can potentially disrupt operations in your environment.
    
    
    import time
    from datetime import datetime, timedelta
    
    from airflow import DAG
    from airflow.decorators import task
    
    
    tasks_amount = 20
    seconds = 10
    minutes = 5
    
    with DAG(
        dag_id=f"dag_10_tasks_{tasks_amount}_sec_{seconds}",
        start_date=datetime(2021, 12, 22, 20, 0),
        end_date=datetime(2021, 12, 22, 20, 49),
        schedule=timedelta(minutes=minutes),
        catchup=True,
    ) as dag:
    
        @task
        def create_subtasks(seconds: int) -> None:
            time.sleep(seconds)
    
        for i in range(tasks_amount):
            create_subtasks(seconds)
    

Evaluate the impact of more consolidated tasks on scheduling processes:

  1. Wait until the DAG runs are completed.

  2. In the Airflow UI, on the **DAGs** page, click the `dag_10_tasks_20_seconds_10` DAG. You will see 10 DAG runs, each has 20 tasks that succeeded.

  3. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  4. In the list of environments, click the name of your environment. The **Environment details** page opens.

  5. Go to the **Logs** tab, then go to **All logs** > **Airflow logs** > **Workers** > **View in Logs Explorer**.

The second example with more consolidated tasks resulted in approximately 10 warnings and 7 errors. On the histogram, you can compare the number of errors and warnings in the initial example (earlier values) and the second example (later values).

[ ![The histogram of Airflow worker logs with errors and warnings
    shows the decreased amount of errors and warning after tasks were
    consolidated](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram-consolidated.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram-consolidated.png) **Figure 6.** Airflow worker logs histogram after the tasks were consolidated (click to enlarge) 

When comparing the first example with the more consolidated one, you can see that there are significantly fewer errors and warnings in the second example. However, the same errors related to warm shutdown still appear in the logs because of resource overload.

  6. On the **Monitoring** tab, select **Workers** and review the graphs.

When you compare the **Airflow tasks** graph for the first example (earlier values) with the graph for the second example with more consolidated tasks, you can see that the spike in queued tasks lasted for a shorter period of time when the tasks were more consolidated. However, it lasted close to 10 minutes, which is still sub-optimal.

[ ![The graph of Airflow tasks over time shows that the spike in
    Airflow tasks lasted for a shorter period of time than before.](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-airflow-tasks-graph-consolidated.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-airflow-tasks-graph-consolidated.png) **Figure 7.** Airflow tasks graph after the tasks were consolidated (click to enlarge) 

On the Active workers graph, you can see the first example (on the left side of the graph) used resources for a much more extended period of time than the second one, even though both examples imitate the same amount of work.

[ ![The graph of active Airflow workers over time shows that the
    number of active workers was increased for a shorter period of time
    than before.](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-active-workers-graph-consolidated.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-active-workers-graph-consolidated.png) **Figure 8.** Active workers graph after the tasks were consolidated (click to enlarge) 

Review the worker resource consumption graphs. Even though the difference between the resources used in the example with more consolidated tasks and the initial example is quite significant, the CPU usage is still spiking to 70% of the limit.

[ ![The graph of CPU usage by Airflow workers shows CPU usage
    increasing up to 70% of the maximum limit](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-cpu-usage-graph-consolidated.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-cpu-usage-graph-consolidated.png) **Figure 9.** Total workers CPU usage graph after the tasks were consolidated (click to enlarge) [ ![The graph of memory usage by Airflow workers shows memory usage increasing, but not reaching the maximum limit](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-memory-usage-graph-consolidated.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-total-worker-memory-usage-graph-consolidated.png) **Figure 10.** Total workers memory usage graph after the tasks were consolidated (click to enlarge) 



### Distribute tasks more evenly over time

Too many concurrent tasks result in the queue being filled up, which leads to tasks being stuck in the queue or rescheduled. In the previous steps, you decreased the number of tasks by consolidating those tasks, however, the output logs and monitoring indicated that the number of concurrent tasks is still sub-optimal.

You can control the number of concurrent task runs by implementing a schedule or setting limits for how many tasks can be run simultaneously.

In this tutorial, you distribute tasks more evenly over time by adding DAG-level parameters into the `dag_10_tasks_20_seconds_10` DAG:

  1. Add `max_active_runs=1` argument to the DAG context manager. This argument sets a limit of only a single instance of a DAG run in a given moment.

  2. Add `max_active_tasks=5` argument to the DAG context manager. This argument controls the maximum number of task instances that can run concurrently in each DAG.




[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the following sample DAG to the environment that you created. In this tutorial, this DAG is named `dag_10_tasks_20_seconds_10_scheduled.py`.
    
    
    import time
    from datetime import datetime, timedelta
    
    from airflow import DAG
    from airflow.decorators import task
    
    
    tasks_amount = 20
    seconds = 10
    minutes = 5
    active_runs = 1
    active_tasks = 5
    
    
    with DAG(
        dag_id=f"dag_10_tasks_{tasks_amount}_sec_{seconds}_runs_{active_runs}_tasks_{active_tasks}",
        start_date=datetime(2021, 12, 22, 20, 0),
        end_date=datetime(2021, 12, 22, 20, 49),
        schedule=timedelta(minutes=minutes),
        max_active_runs=active_runs,
        max_active_tasks=active_tasks,
        catchup=True,
    ) as dag:
    
        @task
        def create_subtasks(seconds: int) -> None:
            time.sleep(seconds)
    
        for i in range(tasks_amount):
            create_subtasks(seconds)
    

Evaluate the impact of distributing tasks over time on scheduling processes:

  1. Wait until the DAG runs are completed.

  2. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  3. In the list of environments, click the name of your environment. The **Environment details** page opens.

  4. Go to the **Logs** tab, then go to **All logs** > **Airflow logs** > **Workers** > **View in Logs Explorer**.

  5. On the histogram, you can see that the third DAG with a limited number of active tasks and runs did not generate any warnings or errors and the distribution of logs looks more even compared to the previous values.

[ ![The histogram of Airflow worker logs with errors and warnings
    shows no errors or warnings after tasks were consolidated and
    distributed over time.](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram-consolidated-distributed.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram-consolidated-distributed.png) **Figure 11.** Airflow worker logs histogram after the tasks were consolidated and distributed over time (click to enlarge) 



The tasks in the `dag_10_tasks_20_seconds_10_scheduled` example that has a limited number of active tasks and runs did not cause resource pressure because the tasks were queued evenly.

After you performed the described steps, you optimized the resource usage by consolidating small tasks and distributing them more evenly over time.

### Optimize environment configurations

You can adjust your environment configurations to make sure there is always capacity in Airflow workers to run queued tasks.

#### Number of workers and worker concurrency

You can [adjust the maximum number of workers](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments#autoscaling-workers) to make Managed Airflow automatically scale your environment within the set limits.

The `[celery]worker_concurrency` parameter defines the maximum number of tasks a single worker can pick up from the task queue. Changing this parameter adjusts the number of tasks that a single worker can execute at the same time. You can change this Airflow configuration option by [overriding it](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations). By default, the worker concurrency is set based on the number of lightweight concurrent task instances that a worker can accommodate. This means that its value is dependent on worker resource limits. The worker concurrency value doesn't depend on the number of workers in your environment.

The number of workers and worker concurrency work in combination with each other, and your environment performance is highly dependent on both parameters. You can use the following considerations to pick the correct combination:

  * **Multiple quick tasks running in parallel**. You can increase worker concurrency when there are tasks waiting in the queue, and your workers use a low percentage of their CPUs and memory at the same time. However, under certain circumstances the queue might never fill up, causing autoscaling to never trigger. If small tasks finish execution by the time the new workers are ready, an existing worker can pick up the remaining tasks, and there will be no tasks for newly created workers.

In these situations, it is recommended to **increase the minimum number of workers and increase worker concurrency** to avoid overeager scaling.

  * **Multiple long tasks running in parallel**. The high worker concurrency prevents the system from scaling the number of workers. If multiple tasks are resource-intensive and take a long time to complete, a high worker concurrency can lead to the queue never being filled up and all tasks being picked up by just one worker, which results in performance issues. In these situations, it is recommended to **increase the maximum number of workers and decrease worker concurrency**.


**Important:** There are scenarios where setting the `[celery]worker_concurrency` parameter to a higher value might not be optimal for your environment. Before modifying worker concurrency settings, check [performance considerations](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments#worker_concurrency_performance_considerations).

#### The importance of parallelism

Airflow schedulers control the scheduling of DAG runs and individual tasks from DAGs. The `[core]parallelism` Airflow configuration option controls how many tasks the Airflow scheduler can queue in the executor's queue after all dependencies for these tasks are met.

Parallelism is a protective mechanism of Airflow that determines how many tasks can be run at the same time per each scheduler, regardless of the worker count. The parallelism value, multiplied by the number of schedulers in your cluster, is the maximum number of task instances that your environment can queue.

Usually, `[core]parallelism` is set as a product of a maximum number of workers and `[celery]worker_concurrency`. It is also affected by the [pool](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#pool). You can change this Airflow configuration option by [overriding it](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations). For more information about adjusting Airflow configurations related to scaling, see [Scaling Airflow configuration](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-scheduling#scaling_airflow_configuration).

#### Find optimal environment configurations

The recommended way to fix scheduling issues is consolidating small tasks into larger tasks and distributing tasks more evenly over time. In addition to optimizing DAG code, you can also optimize environment configurations to have a sufficient capacity for running multiple tasks concurrently.

For example, assume you consolidate tasks in your DAG as much as possible but limiting active tasks to spread them more evenly over time is not a preferred solution for your specific use case.

You can adjust parallelism, number of workers, and worker concurrency parameters to run the `dag_10_tasks_20_seconds_10` DAG without limiting active tasks. In this example, DAG runs 10 times and each run contains 20 small tasks. If you want to run them all simultaneously:

  * You will need a larger environment size, because it controls performance parameters of the managed Managed Airflow infrastructure of your environment.

  * Airflow workers must to be able to run 20 tasks simultaneously, which means you need to set worker concurrency to 20.

  * The workers need sufficient CPU and memory to handle all tasks. Worker concurrency is affected by worker CPU and memory, thus, you will need at least `worker_concurrency / 12` in CPU and at `least worker_concurrency / 8` in memory.

  * You will need to increase parallelism to match the higher worker concurrency. In order for workers to pick up 20 tasks from the queue, the scheduler will need to schedule those 20 tasks first.




Adjust your environment configurations in the following way:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Find the **Resources** > **Workloads** configuration and click **Edit**.

  5. In the **Worker** section, in the **Memory** field, specify the new memory limit for Airflow workers. In this tutorial, use 4 GB.

  6. In the **CPU** field, specify the new CPU limit for Airflow workers. In this tutorial, use 2 vCPU.

  7. Save the changes and allow several minutes for your Airflow workers to restart.




Next, override parallelism and worker concurrency Airflow configuration options:

  1. Go to the **Airflow Configuration Overrides** tab.

  2. Click **Edit** , then click **Add Airflow Configuration Override**.

  3. Override the parralelism configuration:

Section | Key | Value  
---|---|---  
`core` | `parallelism` | `20`  
  4. Click **Add Airflow Configuration Override** and override the worker concurrency configuration:

Section | Key | Value  
---|---|---  
`celery` | `worker_concurrency` | `20`  
  5. Click **Save** and wait until the environment updates its configuration.




Trigger the same example DAG again with the adjusted configurations:

  1. In the Airflow UI, go to the **DAGs** page.

  2. Find the `dag_10_tasks_20_seconds_10` DAG and delete it.

After the DAG is deleted, Airflow checks the DAGs folder in your environment's bucket and automatically runs the DAG again.




After the DAG runs are completed, review the Logs histogram again. On diagram, you can see that the `dag_10_tasks_20_seconds_10` example with more consolidated tasks did not generate any errors and warnings when running with the adjusted environment configuration. Compare the results to the earlier data on the diagram, where the same example generated errors and warnings when running with tge default environment configuration.

[ ![The histogram of Airflow worker logs with errors and warnings
        shows no errors and warning after the environment configuration was
        adjusted](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram-configurations.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-logs-histogram-configurations.png) **Figure 12.** Airflow worker logs histogram after the environment configuration was adjusted (click to enlarge) 

Environment configurations and Airflow configurations play a crucial role in task scheduling, however, it is not possible to increase the configurations beyond certain limits.

We recommend to optimize the DAG code, consolidate tasks, and use scheduling for optimized performance and efficiency.

## Example: DAG parsing errors and latency because of complex DAG code

In this example, you investigate the parsing latency of a sample DAG that imitates an excess of Airflow variables.

### Create a new Airflow variable

Before you upload the sample code, create a new Airflow variable.

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. Go to **Admin** > **Variables** > **Add a new record**.

  4. Set the following values:

     * key: `example_var`
     * val: `test_airflow_variable`



### Upload the sample DAG to your environment

[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the following sample DAG to the environment that you created in the previous steps. In this tutorial, this DAG is named `dag_for_loop_airflow_variable`.

This DAG contains a for loop that runs 1,000 times and imitates an excess of Airflow variables. Each iteration reads the `example_var` variable and generates a task. Each task contains one command that prints the variable's value.

**Warning:** This DAG **simulates issues with DAG scheduling** , which can potentially disrupt operations in your environment.
    
    
    from datetime import datetime
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    from airflow.models import Variable
    
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2023, 2, 17),
        'retries': 0
    }
    
    dag = DAG(
        'dag_for_loop_airflow_variable',
        default_args=default_args,
        catchup=False,
        schedule="@daily"
    )
    
    for i in range(1000):
        a = Variable.get('example_var', 'N/A')
        task = BashOperator(
            task_id=f'task_{i}',
            bash_command='echo variable foo=${foo_env}',
            dag=dag,
            env={'foo_env': a}
        )
    

### Diagnose the parsing issues

DAG parse time is the amount of time it takes for the Airflow scheduler to read a DAG file and parse it. Before the Airflow scheduler can schedule any task from a DAG, the scheduler must parse the DAG file to discover the structure of the DAG and defined tasks.

If a DAG takes a long time to parse, this consumes the scheduler's capacity and might reduce the performance of DAG runs.

To monitor the DAG parse time:

  1. Run the `dags report` [Airflow CLI command](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli) in gcloud CLI to see the parse time for all your DAGs:
         
         gcloud composer environments run ENVIRONMENT_NAME \
             --location LOCATION \
             dags report
         

Replace the following:

     * `ENVIRONMENT_NAME`: the name of your environment.
     * `LOCATION`: the region where the environment is located.
  2. In the command's output, look for the duration value for the `dag_for_loop_airflow_variables` DAG. A large value might indicate that this DAG is not implemented in an optimal way. If you have multiple DAGs, from the output table, you can identify which DAGs have a long parsing time.

Example:
         
         file                | duration       | dag_num | task_num | dags
         ====================+================+=========+==========+=====================
         /dag_for_loop_airfl | 0:00:14.773594 | 1       | 1000     | dag_for_loop_airflow
         ow_variable.py      |                |         |          | _variable
         /airflow_monitoring | 0:00:00.003035 | 1       | 1        | airflow_monitoring
         .py
         
         

  3. Inspect DAG parse times in Google Cloud console:

     1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  4. In the list of environments, click the name of your environment. The **Environment details** page opens.

  5. Go to the **Logs** tab, then go to **All logs** > **DAG processor manager**.

  6. Review `dag-processor-manager` logs and identify possible issues.

[ ![A log entry for the sample DAG shows that DAG parsing time is 46.3 seconds](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-parsing-logs.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-parsing-logs.png) **Figure 13.** DAG processor manager logs show DAG parse times (click to enlarge) 



If the total DAG parse time exceeds about 10 seconds, your schedulers might be overloaded with DAG parsing and cannot run DAGs effectively.

### Optimize the DAG code

It is [recommended](https://cloud.google.com/blog/products/data-analytics/optimize-cloud-composer-via-better-airflow-dags) to avoid unnecessary "top-level" Python code in your DAGs. DAGs with many imports, variables, and functions outside of the DAG introduce greater parse times for the Airflow scheduler. This reduces performance and scalability of Managed Airflow and Airflow. Excess of Airflow variables reading leads to long parsing time and high database load. If this code is in a DAG file, these functions execute on every scheduler heartbeat, which may be slow.

Airflow's template fields allow you to incorporate values from Airflow variables and Jinja templates into your DAGs. This prevents unnecessary function execution during scheduler heartbeats.

To implement the DAG example in a better way, avoid using Airflow variables at the top-level Python code of DAGs. Instead, pass Airflow variables to existing operators throguh a Jinja template, which will delay reading the value until the task execution.

[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the new version of the sample DAG to your environment. In this tutorial, this DAG is named `dag_for_loop_airflow_variable_optimized`.

**Warning:** This DAG **simulates issues with DAG scheduling** , which can potentially disrupt operations in your environment.
    
    
    from datetime import datetime
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2023, 2, 17),
        'retries': 0
    }
    
    dag = DAG(
        'dag_for_loop_airflow_variable_optimized',
        default_args=default_args,
        catchup=False,
        schedule='@daily'
    )
    
    for i in range(1000):
        task = BashOperator(
            task_id=f'bash_use_variable_good_{i}',
            bash_command='echo variable foo=${foo_env}',
            dag=dag,
            env={'foo_env': '{{ var.value.get("example_var") }}'},
        )
    

Inspect the new DAG parse time:

  1. Wait until the DAG run is completed.

  2. Run the `dags report` command again to see the parse time for all your DAGs:
         
         file                | duration       | dag_num | task_num | dags
         ====================+================+=========+==========+=====================
         /dag_for_loop_airfl | 0:00:37.000369 | 1       | 1000     | dag_for_loop_airflow
         ow_variable.py      |                |         |          | _variable
         /dag_for_loop_airfl | 0:00:01.109457 | 1       | 1000     | dag_for_loop_airflow
         ow_variable_optimiz |                |         |          | _variable_optimized
         ed.py               |                |         |          |
         /airflow_monitoring | 0:00:00.040510 | 1       | 1        | airflow_monitoring
         .py                 |                |         |          |
         

  3. Review `dag-processor-manager` logs again and analyze the parse duration.

[ ![A log entry for the sample DAG shows that DAG parsing time is 4.21
    seconds](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-parsing-logs-optimized.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-parsing-logs-optimized.png) **Figure 14.** DAG processor manager logs show DAG parse times after the DAG code was optimized (click to enlarge) 



By replacing the environment variables with Airflow templates, you simplified the DAG code and reduced the parsing latency by about ten times.

### Optimize Airflow environment configurations

The Airflow scheduler constantly tries to trigger new tasks and parses all DAGs in your environment bucket. If your DAGs have a long parsing time and the scheduler consumes a lot of resources, you can optimize Airflow scheduler configurations in order for the scheduler to use resources more efficiently.

In this tutorial, the DAG files take a lot of time to parse, and parsing cycles start to overlap, which then exhausts the scheduler's capacity. In our example, the first example DAG takes more than 5 seconds to parse, so you will configure the scheduler to run less frequently to use resources more efficiently. You will override the [`scheduler_heartbeat_sec`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#scheduler-heartbeat-sec) Airflow configuration option. This configuration defines how often the scheduler should run (in seconds). By default, the value is set to 5 seconds. You can change this Airflow configuration option by [overriding it](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations).

Override the `scheduler_heartbeat_sec` Airflow configuration option:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Airflow Configuration Overrides** tab.

  4. Click **Edit** , then click **Add Airflow Configuration Override**.

  5. Override the Airflow configuration option:

Section | Key | Value  
---|---|---  
`scheduler` | `scheduler_heartbeat_sec` | `10`  
  6. Click **Save** and wait until the environment updates its configuration.




Check the scheduler metrics:

  1. Go to the **Monitoring** tab and select **Schedulers**.

  2. In the **Scheduler heartbeat** graph, click the **More options** button (three dots) and then click **View in the Metrics Explorer**.


[ ![The scheduler heartbeat graph shows that heartbeat occurs less frequently](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-heartbeat.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-heartbeat.png) **Figure 15.** Scheduler heartbeat graph (click to enlarge) 

On the graph, you will see the scheduler runs twice less frequently after you changed the default configuration from 5 seconds to 10 seconds. By reducing the frequency of heartbeats, you make sure that the scheduler does not start running while the previous parsing cycle is ongoing and the scheduler's resource capacity is not exhausted.

### Assign more resources to the scheduler

In Managed Airflow (Gen 2), you can allocate more CPU and memory resources to the scheduler. In this way, you can increase the performance of your scheduler and accelerate parsing time for your DAG.

Allocate additional CPU and memory to the scheduler:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Find the **Resources** > **Workloads** configuration and click **Edit**.

  5. In the **Scheduler** section, in the **Memory** field, specify the new memory limit. In this tutorial, use 4 GB.

  6. In the **CPU** field, specify the new CPU limit. In this tutorial, use 2 vCPU.

  7. Save the changes and allow several minutes for your Airflow schedulers to restart.

  8. Go to the **Logs** tab, then go to **All logs** > **DAG processor manager**.

  9. Review `dag-processor-manager` logs and compare the parse duration for the example DAGs:

[ ![A log entry for the sample DAG shows that DAG parsing time for the optimized DAG is 1.5 seconds. For the unoptimized DAG, the parse time is 28.71 seconds](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-parsing-logs-resources.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-scheduling-parsing-logs-resources.png) **Figure 16.** DAG processor manager logs show DAG parse times after more resources were assigned to the scheduler (click to enlarge) 



By assigning more resources to the scheduler, you increased the scheduler's capacity and reduced the parsing latency significantly compared to the default environment configurations. With more resources, the scheduler can parse the DAGs faster, however, the costs associated with Managed Airflow resources will also increase. Additionally, it is not possible to increase the resources beyond a certain limit.

We recommend to allocate resources only after the possible DAG code and Airflow configuration optimizations were implemented.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

[Delete the Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments). You also delete the environment's bucket during this procedure.

## What's next

  * [Optimize your environment performance and costs](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments)
  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
