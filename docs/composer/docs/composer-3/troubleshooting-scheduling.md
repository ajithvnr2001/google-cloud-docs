---
url: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling/
title: Troubleshooting Airflow scheduler issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:44.482653+00:00
---

# Troubleshooting Airflow scheduler issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Troubleshooting Airflow scheduler issues Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-scheduling "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-scheduling "View this page for Managed Airflow \(Legacy Gen 1\)")

This page provides troubleshooting steps and information for common issues with Airflow schedulers and DAG processors.

## Identify the source of the issue

To begin troubleshooting, identify if the issue happens:

  * At DAG parse time, while the DAG is parsed by an Airflow DAG processor
  * At execution time, while the DAG is processed by an Airflow scheduler

**Note:** In Managed Airflow (Gen 3), **DAG processors and Airflow schedulers run as separate environment's components** and utilize their own CPU, memory, and storage resources. In Managed Airflow (Gen 2), these two components share resources and the Airflow scheduler could be overloaded because of DAG parsing issues.

For more information about parse time and execution time, read [Difference between DAG parse time and DAG execution time](https://docs.cloud.google.com/composer/docs/composer-3/use-monitoring-dashboard#dag-parsing-and-execution-time).

### Inspect DAG processing issues

  1. [Inspect the DAG processor logs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dag-processor#inspect-dag-processor-logs).
  2. [Check DAG parse times](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dag-processor#inspect-dag-parse-times).



### Monitoring running and queued tasks

To check if you have tasks stuck in a queue, follow these steps.

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Monitoring** tab.

  4. In the **Monitoring** tab, review the **Airflow tasks** chart in the **DAG runs** section and identify possible issues. Airflow tasks are tasks that are in a queued state in Airflow, they can go either to Celery or Kubernetes Executor broker queue. Celery queued tasks are task instances that are put into the Celery broker queue.




## Troubleshooting issues at DAG parse time

The following sections describe symptoms and potential fixes for some common issues at DAG parse time.

### Number and time distribution of tasks

Airflow can have issues when scheduling a large number of DAGs or tasks at the same time. To avoid issues with scheduling, you can:

  * Adjust your DAGs to use a smaller number of more consolidated tasks.
  * Adjust schedule intervals of your DAGs to distribute DAG runs more evenly over time.



## Scaling Airflow configuration

Airflow provides Airflow configuration options, that control how many tasks and DAGs Airflow can execute at the same time. To set these configuration options, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) their values for your environment. You can also set some of these values at the DAG or task level.

  * [Worker concurrency](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency)

The `[celery]worker_concurrency` parameter controls the maximum number of tasks that an Airflow worker can execute at the same time. If you multiply the value of this parameter by the number of Airflow workers in your Managed Airflow environment, then you get the maximum number of tasks that can be executed in a given moment in your environment. This number is limited by the `[core]parallelism` Airflow configuration option, which is described further.

In Managed Airflow (Gen 3) environments, the default value of `[celery]worker_concurrency` is calculated automatically based on the number of lightweight concurrent task instances that a worker can accommodate. This means that its value is dependent on worker resource limits. The worker concurrency value doesn't depend on the number of workers in your environment.

  * [Max active DAG runs](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-max-active-runs-per-dag)

The `[core]max_active_runs_per_dag` Airflow configuration option controls the maximum number of active DAG runs per DAG. The scheduler does not create more DAG runs if it reaches this limit.

If this parameter is set incorrectly, you might encounter a problem where the scheduler throttles DAG execution because it cannot create more DAG run instances in a given moment.

You can also set this value at the DAG level with the `max_active_runs` parameter.

  * [Max active tasks per DAG](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-max-active-tasks-per-dag)

The `[core]max_active_tasks_per_dag` Airflow configuration option controls the maximum number of task instances that can run concurrently in each DAG.

If this parameter is set incorrectly then you might encounter a problem where the execution of a single DAG instance is slow because there is only a limited number of DAG tasks that can be executed at a given moment. In this case, you can increase the value of this configuration option.

You can also set this value at the DAG level with the `max_active_tasks` parameter.

You can use `max_active_tis_per_dag` and `max_active_tis_per_dagrun` parameters at the task level to control how many instances with a specific task ID are allowed to run per DAG and per a DAG run.

  * [Parallelism](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parallelism) and pool size

The `[core]parallelism` Airflow configuration option controls how many tasks the Airflow scheduler can queue in the Executor's queue after all dependencies for these tasks are met.

This is a global parameter for the whole Airflow setup.

Tasks are queued and executed within a pool. Managed Airflow environments use only one pool. The size of this pool controls how many tasks can be queued by the scheduler for execution in a given moment. If the pool size is too small, then the scheduler cannot queue tasks for execution even though the thresholds, which are defined by the `[core]parallelism` configuration option and by the `[celery]worker_concurrency` configuration option multiplied by the number of Airflow workers, are not met yet.

You can configure the pool size in the Airflow UI (**Admin** > **Pools**). Adjust the pool size to the level of parallelism you expect in your environment.

Usually, `[core]parallelism` is set a product of maximum number of workers and [`[celery]worker_concurrency`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency).




## Troubleshooting issues with running and queued tasks

The following sections describe symptoms and potential fixes for some common issues with running and queued tasks.

### DAG runs are not executed

Symptom:

When a schedule date for a DAG is set dynamically, this can lead to various unexpected side effects. For example:

  * A DAG execution is always in the future, and the DAG is never executed.

  * Past DAG runs are marked as executed and successful despite not being executed.




More information is available in the [Apache Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/faq.html#what-s-the-deal-with-start-date).

Possible solutions:

  * Follow the recommendations in the [Apache Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/faq.html#what-s-the-deal-with-start-date).

  * Set static `start_date` for DAGs. As an option, you can use `catchup=False` to disable running the DAG for past dates.

  * Avoid using `datetime.now()` or `days_ago(<number of days>)` unless you are aware of the side effects of this approach.




### Using TimeTable feature of Airflow scheduler

Managed Airflow (Gen 3) doesn't support custom plugins for the Airflow scheduler, including time tables implemented in DAGs. Plugins aren't synchronized to the schedulers in your environment.

You can still use [Built-In Timetables](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html#built-in-timetables) in Managed Airflow (Gen 3).

### Avoid task scheduling during maintenance windows

You can define maintenance windows for your environment so that environment's maintenance happens outside of times when you run your DAGs. You can still run your DAGs during maintenance windows, as long as it is acceptable that some tasks can be interrupted and retried. For more information about how maintenance windows affect your environment, see [Specify maintenance windows](https://docs.cloud.google.com/composer/docs/composer-3/specify-maintenance-windows).

### Usage of 'wait_for_downstream' in your DAGs

If you set the `wait_for_downstream` parameter to `True` in your DAGs, then for a task to succeed, all tasks that are immediately **downstream** of this task must also succeed. It means that the execution of tasks belonging to a certain DAG run might be slowed down by the execution of tasks from the previous DAG run. Read more about it in the [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/faq.html#why-is-task-not-getting-scheduled).

### Tasks queued for too long will be cancelled and rescheduled

If an Airflow task is kept in the queue for too long, then the scheduler will reschedule it again for execution after the amount of time set in the `[scheduler]task_queued_timeout` Airflow configuration option have passed. The default value is `2400`. 

One way to observe the symptoms of this situation is to look at the chart with the number of queued tasks ("Monitoring" tab in Managed Airflow UI) and if the spikes in this chart don't drop within about two hours then the tasks will most-likely be rescheduled (with no logs) followed by "Adopted tasks were still pending ..." log entries in the scheduler logs. In such cases, you might see "Log file is not found..." message in Airflow tasks logs because the task was not executed.

In general, this behavior is expected and the next instance of the scheduled task is meant to be executed according to the schedule. If you observe a lot of such cases in your Managed Airflow environments then it might mean that there is not enough Airflow workers in your environment to process all of the scheduled tasks.

Resolution: To solve this issue, you need to make sure there is always capacity in Airflow workers to run queued tasks. For example, you may increase number of workers or worker_concurrency. You may also tune parallelism or pools to prevent queuing tasks more than capacity you have.

### Managed Airflow approach to the min_file_process_interval parameter

Managed Airflow changes the way [`[scheduler]min_file_process_interval`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#min-file-process-interval) is used by the Airflow scheduler.

Airflow scheduler is restarted after a certain number of times all DAGs are scheduled and the [`[scheduler]num_runs`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#num-runs) parameter controls how many times it's done by scheduler. When the scheduler reaches `[scheduler]num_runs` scheduling loops, it is restarted. The scheduler is a stateless component and such an restart is an auto-healing mechanism for any problems that the scheduler might experience. The default value of `[scheduler]num_runs` is 5000.

`[scheduler]min_file_process_interval` can be used to configure how frequently DAG parsing happens but this parameter can't be longer than the time required for a scheduler to perform `[scheduler]num_runs` loops when scheduling your DAGs.

### Marking tasks as failed after reaching dagrun_timeout

The scheduler marks tasks that are not finished (running, scheduled and queued) as failed if a DAG run doesn't finish within [`dagrun_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/dag/index.html) (a DAG parameter).

Solution:

  * Extend [`dagrun_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/dag/index.html) to meet the timeout.

  * [Increase the number of workers](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#autoscaling-workers) or [increase worker performance parameters](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#workloads-configuration), so that the DAG is executed faster.




### Symptoms of the Airflow database being under heavy load

Sometimes in the Airflow worker logs you might see the following warning log entry:
    
    
    psycopg2.OperationalError: connection to server at ... failed
    

Such errors or warnings might be a symptom of the Airflow database being overloaded by the number of open connections or the number of queries executed in the same time, either by schedulers or by other Airflow components like workers, triggerers, and web servers.

Possible solutions:

  * [Remove unnecessary data from the Airflow database](https://docs.cloud.google.com/composer/docs/composer-3/cleanup-airflow-database).

  * Scale up the Airflow database by [Adjusting the size of your environment](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#environment-size). 

  * Reduce the number of schedulers and DAG processors. Start with one scheduler and one DAG processor, then increase the number of schedulers or DAG processors if you observe that these components approach their resource limits.

  * Avoid using global variables in Airflow DAGs. Instead, use [environment variables](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables) and [Airflow variables](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html#variables).

  * Set [`[scheduler]scheduler_heartbeat_sec`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#scheduler-heartbeat-sec) to a higher value, for example, to 15 seconds or more.

  * Set [`[scheduler]job_heartbeat_sec`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#job-heartbeat-sec) to a higher value, for example 30 seconds or more.

  * Set [`[scheduler]scheduler_health_check_threshold`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#scheduler-health-check-threshold) to a value equal to `[scheduler]job_heartbeat_sec` multiplied by `4`.




### Web server shows 'The scheduler does not appear to be running' warning

The scheduler reports its heartbeat on a regular basis to the Airflow database. Based on this information, the Airflow web server determines if the scheduler is active.

Sometimes, if the scheduler is under heavy load then it might not be able to report its heartbeat every [`[scheduler]scheduler_heartbeat_sec`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#scheduler-heartbeat-sec).

In such a situation, the Airflow web server might show the following warning:
    
    
    The scheduler does not appear to be running. Last heartbeat was received <X>
    seconds ago.
    

Possible solutions:

  * Increase CPU and memory the resources for the scheduler.

  * Optimize your DAGs so that their parsing and scheduling is faster and doesn't consume too much of the scheduler resources.

  * Avoid using global variables in Airflow DAGs. Instead, use [environment variables](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables) and [Airflow variables](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html#variables).

  * Increase the value of the [`[scheduler]scheduler_health_check_threshold`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#scheduler-health-check-threshold) Airflow configuration option, so that the web server waits longer before reporting the unavailability of the scheduler.




### Workarounds for issues encountered during backfilling DAGs

Sometimes, you might want to re-run DAGs that were already executed. You can do it with an Airflow CLI command in the following way:
    
    
    gcloud composer environments run \
      ENVIRONMENT_NAME \
      --location LOCATION \
       dags backfill -- -B \
       -s START_DATE \
       -e END_DATE \
       DAG_NAME
    

To re-run only failed tasks for a specific DAG, also use the `--rerun-failed-tasks` argument.

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `START_DATE` with a value for the `start_date` DAG parameter, in the `YYYY-MM-DD` format.
  * `END_DATE` with a value for the `end_date` DAG parameter, in the `YYYY-MM-DD` format.
  * `DAG_NAME` with the name of the DAG.



Backfill operation might sometimes generate a deadlock situation where a backfill is not possible because there is a lock on a task. For example:
    
    
    2022-11-08 21:24:18.198 CET DAG ID Task ID Run ID Try number
    2022-11-08 21:24:18.201 CET -------- --------- -------- ------------
    2022-11-08 21:24:18.202 CET 2022-11-08 21:24:18.203 CET These tasks are deadlocked:
    2022-11-08 21:24:18.203 CET DAG ID Task ID Run ID Try number
    2022-11-08 21:24:18.204 CET ----------------------- ----------- ----------------------------------- ------------
    2022-11-08 21:24:18.204 CET <DAG name> <Task name> backfill__2022-10-27T00:00:00+00:00 1
    2022-11-08 21:24:19.249 CET Command exited with return code 1
    ...
    2022-11-08 21:24:19.348 CET Failed to execute job 627927 for task backfill
    

In some cases, you can use the following workarounds to overcome deadlocks:

  * Disable mini-scheduler by [overriding](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the [`[core]schedule_after_task_execution`](https://airflow.apache.org/docs/apache-airflow/2.10.5/configurations-ref.html#schedule-after-task-execution) to `False`.

  * Run backfills for narrower date ranges. For example, set `START_DATE` and `END_DATE` to specify a period of only 1 day.




## What's next

  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
