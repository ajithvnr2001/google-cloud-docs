---
url: https://docs.cloud.google.com/composer/docs/composer-1/monitor-environments/
title: Monitor environments with Cloud Monitoring \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:30.427227+00:00
---

# Monitor environments with Cloud Monitoring  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/monitor-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Monitor environments with Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/monitor-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

You can use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) and [Cloud Logging](https://docs.cloud.google.com/logging/docs) with Managed Service for Apache Airflow.

Cloud Monitoring provides visibility into the performance, uptime, and overall health of cloud-powered applications. Cloud Monitoring collects and ingests metrics, events, and metadata from Managed Airflow to generate insights in dashboards and charts. You can use Cloud Monitoring to understand the performance and health of your Managed Airflow environments and Airflow metrics.

Logging captures logs produced by the scheduler and worker containers in your environment's cluster. These logs contain system-level and Airflow dependency information to help with debugging. For information about viewing logs, see [View Airflow logs](https://docs.cloud.google.com/composer/docs/composer-1/view-logs).

**Note:** Monitoring metrics for Managed Airflow are enabled automatically. See [Cloud Monitoring pricing](https://docs.cloud.google.com/stackdriver/pricing#monitoring-costs) for more information about costs associated with Cloud Monitoring.

## Before you begin

  * The following permissions are required to access logs and metrics for your Managed Airflow environment:

    * **Read-only access to logs and metrics:** `logging.viewer` and `monitoring.viewer`
    * **Read-only access to logs, including private logs:** `logging.privateLogViewer`
    * **Read/write access to metrics:** `monitoring.editor`

For more information about other permissions and roles for Managed Airflow, see [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control).

  * To avoid duplicate logging, Cloud Logging for Google Kubernetes Engine is disabled.

  * Cloud Logging produces an entry for each status and event that occurs in your Google Cloud project. You can use [exclusion filters](https://docs.cloud.google.com/logging/docs/exclusions#exclusion-filters) to reduce the volume of logs, including the logs that Cloud Logging produces for Managed Airflow.




## Environment metrics

You can use environment metrics to check the resource usage and health of your Managed Airflow environments.

**Note:** For a full reference of Managed Airflow metrics, see [Google Cloud metrics: API prefix is C](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-composer) in the Cloud Monitoring API documentation.

### Environment health

To check the health of your environment, you can use the following health status metric:

Metric | API  
---|---  
Healthiness of an environment  |  `composer.googleapis.com/environment/healthy`  
  
Managed Airflow runs a liveness DAG named `airflow_monitoring`, which runs on a schedule and reports environment health as follows:

  * If the liveness DAG run finishes successfully, the health status is `True`.
  * If the liveness DAG run fails, the health status is `False`.



The liveness DAG is stored in the `dags/` folder and visible in the Airflow UI. The frequency and contents of the liveness DAG are immutable and must not be modified. Changes to the liveness DAG do not persist.

### Environment's dependencies checks

Managed Airflow periodically checks that the environment can reach the services required for its operation and that it has enough permissions to interact with them. Examples of services required for the environment's operation are Artifact Registry, Cloud Logging, and Cloud Monitoring.

The following metrics are available for the environment's dependencies checks:

Metric | API | Description  
---|---|---  
Number of dependency checks  |  `composer.googleapis.com/environment/health/dependency_check_count` |  This metric tracks the number of times reachability checks are performed on services required for the environment's operation.  
Number of dependency permissions checks  |  `composer.googleapis.com/environment/health/dependency_permissions_check_count` |  This metric tracks the number of times permission checks are performed on services required for the environment's operation.  
  
### Database health

To check the health of your database, you can use the following health status metric: `composer.googleapis.com/environment/database_health`.

The Airflow monitoring pod pings the database every minute and reports health status as `True` if a SQL connection can be established or `False` if not.

### Database metrics

The following environment metrics are available for the Airflow metadata database used by Managed Airflow environments. You can use these metrics to monitor the performance and resource usage of your environment's database instance.

For example, you might want to [upgrade the Cloud SQL machine type of your environment](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments#db-machine-type) if your environment approaches resource limits. Or you might want to optimize costs related to Airflow metadata database usage by doing a [database cleanup](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database), in order to keep storage [under a certain threshold](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen).

Database metric | API | Description  
---|---|---  
Database CPU usage  |  `composer.googleapis.com/environment/database/cpu/usage_time` |   
Database CPU cores  |  `composer.googleapis.com/environment/database/cpu/reserved_cores` |   
Database CPU utilization  |  `composer.googleapis.com/environment/database/cpu/utilization` |   
Database Memory usage  |  `composer.googleapis.com/environment/database/memory/bytes_used` |   
Database Memory quota  |  `composer.googleapis.com/environment/database/memory/quota` |   
Database Memory utilization  |  `composer.googleapis.com/environment/database/memory/utilization` |   
Database Disk usage  |  `composer.googleapis.com/environment/database/disk/bytes_used` |   
Database Disk quota  |  `composer.googleapis.com/environment/database/disk/quota` |   
Database Disk utilization  |  `composer.googleapis.com/environment/database/disk/utilization` |   
Database Connections limit  |  `composer.googleapis.com/environment/database/network/max_connections` |   
Database Connections  |  `composer.googleapis.com/environment/database/network/connections` |   
Database available for failover  |  `composer.googleapis.com/environment/database/available_for_failover` |  Is `True` if the environment's Cloud SQL instance is in the high availability mode and is ready for failover.  
Database automatic failover requests count  |  `composer.googleapis.com/environment/database/auto_failover_request_count` |  Total number of auto-failover requests of the environment's Cloud SQL instance.  
  
### Worker metrics

The following environment metrics are available for Airflow workers in Managed Airflow (Gen 3) and Managed Airflow (Gen 2) environments.

This metric is used to [automatically scale](https://docs.cloud.google.com/composer/docs/composer-1/environment-scaling) the number of workers in your environment. The [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) sets this metric, then the [Airflow Worker Set Controller](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture) environment component uses this metric to scale the number of Airflow workers up or down, depending on the value of this metric.

Worker metric | API  
---|---  
Scale Factor Target  |  `composer.googleapis.com/environment/worker/scale_factor_target`  
  
### Scheduler metrics

**Note:** Other metrics related to schedulers are provided through Airflow metrics.Name | API | Description  
---|---|---  
Active schedulers  |  `composer.googleapis.com/environment/active_schedulers` |  Number of active scheduler instances.  
  
### Triggerer metrics

**Note:** Other metrics related to triggerers are provided through Airflow metrics.Name | API | Description  
---|---|---  
Active triggerers  |  `composer.googleapis.com/environment/active_triggerers` |  The number of active triggerer instances.  
  
### Web server metrics

The following environment metrics are available for the Airflow web server used by Managed Airflow environments. You can use these metrics to check the performance and resource usage of your environment's Airflow web server instance.

For example, you might want to [upgrade the web server machine type](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments#ws-machine-type) if it constantly approaches resource limits.

Name | API | Description  
---|---|---  
Active web servers | `composer.googleapis.com/environment/active_webservers` | Number of active web server instances.  
Web server CPU usage | `composer.googleapis.com/environment/web_server/cpu/usage_time` |   
Web server CPU quota | `composer.googleapis.com/environment/web_server/cpu/reserved_cores` |   
Web server memory usage | `composer.googleapis.com/environment/web_server/memory/bytes_used` |   
Web server memory quota | `composer.googleapis.com/environment/web_server/memory/quota` |   
  
### Quotas for services used by the environment

Managed Airflow uses other Google Cloud services. These services have project-level quotas, which apply when you use Managed Airflow.

In Managed Airflow (Gen 3), the environment's cluster is located [in the tenant project](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture#about-customer-tenant). Managed Airflow (Gen 3) provides the following metrics that report the utilization of quotas and corresponding quota limits for [services used by your environment](https://docs.cloud.google.com/composer/quotas#quotas-other-services) in the tenant project.

**Note:** In Managed Airflow (Gen 2) and Managed Airflow (Legacy Gen 1), you can check the same quotas in the project where your environment is located.Metric | API | Description  
---|---|---  
CPU quota limit for Managed Airflow workloads  |  `composer.googleapis.com/environment/workloads_cpu_quota` |  _(Managed Airflow (Gen 3) only)_ The Compute Engine [CPU allocation quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) for the total number of virtual CPUs used by an environment. The limit applies per environment. If your project has several Managed Airflow (Gen 3) environments, each environment has its own quota limit.  
CPU quota usage for Managed Airflow workloads  |  `composer.googleapis.com/environment/workloads_cpu_quota_usage` |  _(Managed Airflow (Gen 3) only)_ The usage of the Compute Engine CPU allocation quota by an environment.  
  
### DAG metrics

To help you monitor the efficiency of your DAG runs and identify tasks that cause high latency, the following DAG metrics are available.

**Note:** Other metrics related to DAGs are provided through Airflow metrics.DAG metric | API  
---|---  
Number of DAG runs  |  `composer.googleapis.com/workflow/run_count`  
Duration of each DAG run  |  `composer.googleapis.com/workflow/run_duration`  
Number of task runs  |  `composer.googleapis.com/workflow/task/run_count`  
Duration of each task run  |  `composer.googleapis.com/workflow/task/run_duration`  
  
Cloud Monitoring shows only the metrics for completed workflow and task runs (success or failure). **No Data** displays when there is no workflow activity and for in-progress workflow and task runs.

### Celery Executor metrics

The following Celery Executor metrics are available. These metrics can help you determine if there are sufficient worker resources in your environment.

Celery Executor metric | API  
---|---  
Number of tasks in the queue  |  `composer.googleapis.com/environment/task_queue_length`  
Number of online Celery workers  |  `composer.googleapis.com/environment/num_celery_workers`  
  
### Airflow metrics

The following Airflow metrics are available. These metrics correspond to [metrics provided by Airflow](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html).

Name | API | Name in Airflow | Description  
---|---|---|---  
Celery task non-zero exit codes  |  `composer.googleapis.com/environment/celery/execute_command_failure_count` |  `celery.execute_command.failure` |  Number of non-zero exit code from Celery tasks.  
Celery task publish timeouts  |  `composer.googleapis.com/environment/celery/task_timeout_error_count` |  `celery.task_timeout_error` |  Number of `AirflowTaskTimeout` errors raised when publishing Task to Celery Broker.  
Serialized DAG fetch duration  |  `composer.googleapis.com/environment/collect_db_dag_duration` |  `collect_db_dags` |  Time taken for fetching all Serialized DAGs from the database.  
DAG refresh errors  |  `composer.googleapis.com/environment/dag_callback/exception_count` |  `dag.callback_exceptions` |  Number of exceptions raised from DAG callbacks. When this happens, it means that a DAG callback is not working.  
DAG refresh errors  |  `composer.googleapis.com/environment/dag_file/refresh_error_count` |  `dag_file_refresh_error` |  Number of failures when loading any DAG files.  
DAG file load time  |  `composer.googleapis.com/environment/dag_processing/last_duration` |  `dag_processing.last_duration.<dag_file>` |  Time taken to load a specific DAG file.  
Time since DAG file processing  |  `composer.googleapis.com/environment/dag_processing/last_run_elapsed_time` |  `dag_processing.last_run.seconds_ago.<dag_file>` |  Seconds since a DAG file was last processed.  
DagFileProcessorManager stall count  |  `composer.googleapis.com/environment/dag_processing/manager_stall_count` |  `dag_processing.manager_stalls` |  Number of stalled `DagFileProcessorManager` processes.  
DAG parsing errors  |  `composer.googleapis.com/environment/dag_processing/parse_error_count` |  `dag_processing.import_errors` |  Number of errors generated when parsing DAG files.  
Running DAG parsing processes  |  `composer.googleapis.com/environment/dag_processing/processes` |  `dag_processing.processes` |  Number of currently running DAG parsing processes.  
Processor timeouts  |  `composer.googleapis.com/environment/dag_processing/processor_timeout_count` |  `dag_processing.processor_timeouts` |  Number of file processors that were killed because of taking too long.  
Time taken to scan and import all DAG files  |  `composer.googleapis.com/environment/dag_processing/total_parse_time` |  `dag_processing.total_parse_time` |  Total time taken to scan and import all DAG files once.  
Current DAG bag size  |  `composer.googleapis.com/environment/dagbag_size` |  `dagbag_size` |  Number of DAGs found when the scheduler ran a scan based on its configuration.  
Failed SLA miss email notifications  |  `composer.googleapis.com/environment/email/sla_notification_failure_count` |  `sla_email_notification_failure` |  Number of failed SLA miss email notification attempts.  
Open slots on executor  |  `composer.googleapis.com/environment/executor/open_slots` |  `executor.open_slots` |  Number of open slots on the executor.  
Queued tasks on executor  |  `composer.googleapis.com/environment/executor/queued_tasks` |  `executor.queued_tasks` |  Number of queued tasks on the executor.  
Running tasks on executor  |  `composer.googleapis.com/environment/executor/running_tasks` |  `executor.running_tasks` |  Number of running tasks on the executor.  
Task instance successes/failures  |  `composer.googleapis.com/environment/finished_task_instance_count` |  `ti_failures`, `ti_successes` |  Overall task instance successes/failures.  
Started/finished jobs  |  `composer.googleapis.com/environment/job/count` |  `<job_name>_start`, `<job_name>_end` |  Number of started/finished jobs, such as SchedulerJob, LocalTaskJob.  
Job heartbeat failures  |  `composer.googleapis.com/environment/job/heartbeat_failure_count` |  `<job_name>_heartbeat_failure` |  Number of failed heartbeats for a job.  
Tasks created per operator  |  `composer.googleapis.com/environment/operator/created_task_instance_count` |  `task_instance_created-<operator_name>` |  Number of tasks instances created for a given operator.  
Operator executions  |  `composer.googleapis.com/environment/operator/finished_task_instance_count` |  `operator_failures_<operator_name>`, `operator_successes_<operator_name>` |  Number of finished task instances per operator  
Open slots in the pool  |  `composer.googleapis.com/environment/pool/open_slots` |  `pool.open_slots.<pool_name>` |  Number of open slots in the pool.  
Queued slots in the pool  |  `composer.googleapis.com/environment/pool/queued_slots` |  `pool.queued_slots.<pool_name>` |  Number of queued slots in the pool.  
Running slots in the pool  |  `composer.googleapis.com/environment/pool/running_slots` |  `pool.running_slots.<pool_name>` |  Number of running slots in the pool.  
Starving tasks in the pool  |  `composer.googleapis.com/environment/pool/starving_tasks` |  `pool.starving_tasks.<pool_name>` |  Number of starving tasks in the pool.  
Time spent in scheduler's critical section  |  `composer.googleapis.com/environment/scheduler/critical_section_duration` |  `scheduler.critical_section_duration` |  Time spent in the critical section of scheduler loop. Only a single scheduler can enter this loop at a time.  
Critical section lock failures  |  `composer.googleapis.com/environment/scheduler/critical_section_lock_failure_count` |  `scheduler.critical_section_busy` |  Count of times a scheduler process tried to get a lock on the critical section (needed to send tasks to the executor) and found it locked by another process.  
Externally killed tasks  |  `composer.googleapis.com/environment/scheduler/task/externally_killed_count` |  `scheduler.tasks.killed_externally` |  Number of tasks killed externally.  
Orphaned tasks  |  `composer.googleapis.com/environment/scheduler/task/orphan_count` |  `scheduler.orphaned_tasks.cleared`, `scheduler.orphaned_tasks.adopted` |  Number of orphaned tasks cleared/adopted by the scheduler.  
Running/starving/executable tasks  |  `composer.googleapis.com/environment/scheduler/tasks` |  `scheduler.tasks.running`, `scheduler.tasks.starving`, `scheduler.tasks.executable` |  Number of running/starving/executable tasks.  
Scheduler heartbeats  |  `composer.googleapis.com/environment/scheduler_heartbeat_count` |  `scheduler_heartbeat` |  Scheduler heartbeats.  
Scheduler loop duration  |  `composer.googleapis.com/workload/scheduler/loop_duration` |  `scheduler.scheduler_loop_duration.<hostname>` |  Time spent running one scheduler loop.  
Failed SLA callback notifications  |  `composer.googleapis.com/environment/sla_callback_notification_failure_count` |  `sla_callback_notification_failure` |  Number of failed SLA miss callback notification attempts.  
Smart sensor poking exception failures  |  `composer.googleapis.com/environment/smart_sensor/exception_failures` |  `smart_sensor_operator.exception_failures` |  Number of failures caused by exception in the previous smart sensor poking loop.  
Smart sensor poking infrastructure failures  |  `composer.googleapis.com/environment/smart_sensor/infra_failures` |  `smart_sensor_operator.infra_failures` |  Number of infrastructure failures in the previous smart sensor poking loop.  
Smart sensor poking exceptions  |  `composer.googleapis.com/environment/smart_sensor/poked_exception` |  `smart_sensor_operator.poked_exception` |  Number of exceptions in the previous smart sensor poking loop.  
Smart sensor successfully poked tasks  |  `composer.googleapis.com/environment/smart_sensor/poked_success` |  `smart_sensor_operator.poked_success` |  Number of newly succeeded tasks poked by the smart sensor in the previous poking loop.  
Smart sensor poked tasks  |  `composer.googleapis.com/environment/smart_sensor/poked_tasks` |  `smart_sensor_operator.poked_tasks` |  Number of tasks poked by the smart sensor in the previous poking loop.  
Previously succeeded task instances  |  `composer.googleapis.com/environment/task_instance/previously_succeeded_count` |  `previously_succeeded` |  Number of previously succeeded task instances.  
Killed zombie tasks  |  `composer.googleapis.com/environment/zombie_task_killed_count` |  `zombies_killed` |  Number of killed zombie tasks.  
DAG run duration  |  `composer.googleapis.com/workflow/dag/run_duration` |  `dagrun.duration.success.<dag_id>`, `dagrun.duration.failed.<dag_id>` |  Time taken for a DagRun to reach success/failed state.  
DAG dependency check duration  |  `composer.googleapis.com/workflow/dependency_check_duration` |  `dagrun.dependency-check.<dag_id>` |  Time taken to check DAG dependencies. This metric is different from the environment's dependency and permission checks metrics and applies to DAGs  
DAG run schedule delay  |  `composer.googleapis.com/workflow/schedule_delay` |  `dagrun.schedule_delay.<dag_id>` |  Time of delay between the scheduled DagRun start date and the actual DagRun start date.  
Finished tasks  |  `composer.googleapis.com/workflow/task_instance/finished_count` |  `ti.finish.<dag_id>.<task_id>.<state>` |  Number of completed tasks in a given DAG.  
Task instance run duration  |  `composer.googleapis.com/workflow/task_instance/run_duration` |  `dag.<dag_id>.<task_id>.duration` |  Time taken to finish a task.  
Started tasks  |  `composer.googleapis.com/workflow/task_instance/started_count` |  `ti.start.<dag_id>.<task_id>` |  Number of started tasks in a given DAG.  
Task instance queued duration  |  `composer.googleapis.com/workflow/task_instance/queued_duration` |  `dag.<dag_id>.<task_id>.queued_duration` |  Time that a task spends in the Queued state before it switches into the Running state.  
Task CPU usage  |  `composer.googleapis.com/workflow/task/cpu_usage` |  `task.cpu_usage.<dag_id>.<task_id>` |  Percentage of CPU used by a task.  
Task memory usage  |  `composer.googleapis.com/workflow/task/mem_usage` |  `task.mem_usage.<dag_id>.<task_id>` |  Percentage of memory used by a task.  
Tasks removed from DAG  |  `composer.googleapis.com/workflow/task/removed_from_dag_count` |  `task_removed_from_dag.<dag_id>` |  Number of tasks removed for a given DAG (that is, task no longer exists in DAG).  
Tasks restored to DAG  |  `composer.googleapis.com/workflow/task/restored_to_dag_count` |  `task_restored_to_dag.<dag_id>` |  Number of tasks restored for a given DAG (that is, task instance which was previously in REMOVED state in the DB is added to DAG file).  
Task schedule delay  |  `composer.googleapis.com/workflow/task/schedule_delay` |  `dagrun.schedule_delay.<dag_id>` |  Time elapsed between first task start_date and dagrun expected start.  
Total number of running triggers  |  `composer.googleapis.com/workload/triggerer/num_running_triggers` |  `triggers.running` |  The number of running triggers per triggerer instance.  
Blocking triggers  |  `composer.googleapis.com/environment/trigger/blocking_count` |  `triggers.blocked_main_thread` |  Number of triggers that blocked the main thread (likely because of not being fully asynchronous).  
Failed triggers  |  `composer.googleapis.com/environment/trigger/failed_count` |  `triggers.failed` |  Number of triggers that failed with an error before they could fire an event.  
Succeeded triggers  |  `composer.googleapis.com/environment/trigger/succeeded_count` |  `triggers.succeeded` |  Number of triggers that have fired at least one event.  
  
## Using Monitoring for Managed Airflow environments

###  Console 

You can use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector) to display metrics related to your environments and DAGs:

  * **Cloud Composer Environment** resource contains metrics for environments.

To show metrics for a specific environment, [filter metrics](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option) by the `environment_name` label. You can also filter by other labels, such as environment's location or image version.

  * **Cloud Composer Workflow** resource contains metrics for DAGs.

To show metrics for a specific DAG or task, [filter metrics](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option) by the `workflow_name` and `task_name` labels. You can also filter by other labels, such as task status or Airflow operator name.




###  API and gcloud 

You can create and manage custom dashboards and the widgets through the Cloud Monitoring API and [`gcloud monitoring dashboards`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/dashboards) command. For more information, see [Manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

For more information about resources, metrics, and filters, see the reference for Cloud Monitoring API:

  * [Managed Airflow metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-composer)
  * [`cloud_composer_environment` resource](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)
  * [Using the APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer)



## Using Cloud Monitoring alerts

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Cloud Composer` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **Cloud Composer Environment** or **Cloud Composer Workflow**.
     3. Select a **Metric category** and a **Metric** , and then select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

## What's next

  * [Use the monitoring dashboard](https://docs.cloud.google.com/composer/docs/composer-1/use-monitoring-dashboard)
  * [Add Cloud Monitoring dashboard widgets](https://docs.cloud.google.com/monitoring/charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
