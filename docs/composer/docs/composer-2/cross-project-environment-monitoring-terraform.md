---
url: https://docs.cloud.google.com/composer/docs/composer-2/cross-project-environment-monitoring-terraform/
title: Cross-project environment monitoring with Terraform \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:53.026855+00:00
---

# Cross-project environment monitoring with Terraform  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/cross-project-environment-monitoring-terraform/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Cross-project environment monitoring with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/cross-project-environment-monitoring-terraform "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/cross-project-environment-monitoring-terraform "View this page for Managed Airflow \(Legacy Gen 1\)")

This page shows how to implement an integrated monitoring dashboard for multiple Managed Airflow environments across selected projects in the same organization.

## Overview

The described solution can help central enterprise platform teams support Managed Airflow environments used by other teams. This implementation can be used to monitor all Managed Airflow environments, even those that are not created using Terraform.

This guide implements the Cloud Monitoring dashboard in Managed Airflow along with alerting policies that continuously report key metrics of Managed Airflow environments and raise incidents in case of issues. The dashboard automatically scans all Managed Airflow environments in projects selected for this monitoring. The implementation relies on Terraform.

The model uses a Google Cloud project acting as a Monitoring Project, which is used to monitor (read-only) Managed Airflow environments deployed in multiple Monitored Projects. The central dashboard uses Cloud Monitoring metrics from the Monitored Projects to render its contents.

![Diagram that shows the monitoring project, which contains the monitoring dashboard, and three monitored projects that each contain composer environments. Each monitored project has an arrow pointing to the monitored project labeled 'metrics'](https://docs.cloud.google.com/static/composer/docs/images/terraform-monitoring-overview.png)

The dashboard monitors and creates alerts for multiple metrics, including environment health:

![Screenshot of the monitoring dashboard showing Environment Health, Database Health, Webserver Health, and Scheduler Heartbeat](https://docs.cloud.google.com/static/composer/docs/images/terraform-monitoring-health.png)

or CPU metrics:

![Screenshot of the monitoring dashboard showing Database CPU, Scheduler CPU, Worker CPU, and Webserver CPU](https://docs.cloud.google.com/static/composer/docs/images/terraform-monitoring-cpu.png)

Hold the pointer over a particular line to see which environment it represents. The dashboard then displays a project name and resource:

![Screenshot of the monitoring dashboard showing the pop up when you hover over a line. The pop up shows four resources, one of which corresponds to the line.](https://docs.cloud.google.com/static/composer/docs/images/terraform-monitoring-hover.png)

In case a metric exceeds a predefined threshold, an incident is raised and a respective alert is shown in a chart corresponding to this metric:

![Screenshot of the open incidents view showing two open incidents. Each listed incident has a link to view the details.](https://docs.cloud.google.com/static/composer/docs/images/terraform-monitoring-incidents.png)

## List of monitored metrics

A complete list of monitored metrics:

  * Managed Airflow environment health (based on Monitoring DAG)
  * Database health
  * Web Server Health
  * Scheduler Heartbeats
  * CPU and Memory utilization for all Workers
  * CPU and Memory utilization for the Airflow database
  * CPU and Memory utilization for the Web Server 
  * CPU and Memory utilization for Airflow Schedulers
  * Proportion of Queued, Scheduled, Queued or Scheduled tasks in an environment (useful to spot Airflow concurrency configuration issues)
  * DAG Parsing time
  * Current versus minimal number of Workers - useful to understand Worker stability issues or scaling problems
  * Worker Pod evictions
  * Number of errors thrown in Logs by Workers, Schedulers, Web Server or other components (individual charts)

**Note:** You don't need to modify the dashboard when Managed Airflow environments are added or removed as long as the list of monitored projects stays the same.

## Before you begin

To use Managed Airflow and Cloud Monitoring, you need to create a Google Cloud project and enable billing. The project must contain a Managed Airflow environment. This project is referred to as the **Monitoring Project** in this guide.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli) if it is not already installed.
  7. Configure the metrics scope of your project. By default, a project can only display or monitor time-series data that it stores. If you want to display data or to monitor data stored in multiple projects, then configure the metrics scope of the project. For more information, see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).



## Implementation steps

  1. On your local computer where you run Terraform, set the `GOOGLE_CLOUD_PROJECT` environment variable [to the ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your **Monitoring Project** :
         
         export GOOGLE_CLOUD_PROJECT=MONITORING_PROJECT_ID
         

  2. Make sure that your Terraform Google provider is authenticated and has access to the following permissions:

     * `roles/monitoring.editor` permission in **Monitoring Project**
     * `roles/monitoring.viewer`, `roles/logging.viewer` in all **Monitored Projects**
  3. Copy the following `main.tf` file to the local computer where you run Terraform.

**Click to expand**
         
         #   Monitoring for multiple Cloud Composer environments
         #
         #   Usage:
         #       1. Create a new project that you will use for monitoring of Cloud Composer environments in other projects
         #       2. Replace YOUR_MONITORING_PROJECT with the name of this project in the "metrics_scope" parameter that is part of the "Add Monitored Projects to the Monitoring project" section
         #       3. Replace the list of projects to monitor with your list of projects with Cloud Composer environments to be monitored in the "for_each" parameter of the "Add Monitored Projects to the Monitoring project" section
         #       4. Set up your environment and apply the configuration following these steps: https://cloud.google.com/docs/terraform/basic-commands. Your GOOGLE_CLOUD_PROJECT environment variable should be the new monitoring project you just created.
         #
         #   The script creates the following resources in the monitoring project:
         #           1. Adds monitored projects to Cloud Monitoring
         #           2. Creates Alert Policies
         #           3. Creates Monitoring Dashboard
         #
         
         
         
         #######################################################
         #
         # Add Monitored Projects to the Monitoring project
         #
         ########################################################
         
         resource "google_monitoring_monitored_project" "projects_monitored" {
           for_each      = toset(["YOUR_PROJECT_TO_MONITOR_1", "YOUR_PROJECT_TO_MONITOR_2", "YOUR_PROJECT_TO_MONITOR_3"])
           metrics_scope = join("", ["locations/global/metricsScopes/", "YOUR_MONITORING_PROJECT"])
           name          = each.value
         }
         
         
         #######################################################
         #
         # Create alert policies in Monitoring project
         #
         ########################################################
         
         resource "google_monitoring_alert_policy" "environment_health" {
           display_name = "Environment Health"
           combiner     = "OR"
           conditions {
             display_name = "Environment Health"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| {metric 'composer.googleapis.com/environment/dagbag_size'",
                 "| group_by 5m, [value_dagbag_size_mean: if(mean(value.dagbag_size) > 0, 1, 0)]",
                 "| align mean_aligner(5m)",
                 "| group_by [resource.project_id, resource.environment_name],    [value_dagbag_size_mean_aggregate: aggregate(value_dagbag_size_mean)];  ",
                 "metric 'composer.googleapis.com/environment/healthy'",
                 "| group_by 5m,    [value_sum_signals: aggregate(if(value.healthy,1,0))]",
                 "| align mean_aligner(5m)| absent_for 5m }",
                 "| outer_join 0",
                 "| group_by [resource.project_id, resource.environment_name]",
                 "| value val(2)",
                 "| align mean_aligner(5m)",
                 "| window(5m)",
                 "| condition val(0) < 0.9"
               ])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "database_health" {
           display_name = "Database Health"
           combiner     = "OR"
           conditions {
             display_name = "Database Health"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/database_health'",
                 "| group_by 5m,",
                 "    [value_database_health_fraction_true: fraction_true(value.database_health)]",
                 "| every 5m",
                 "| group_by 5m,",
                 "    [value_database_health_fraction_true_aggregate:",
                 "       aggregate(value_database_health_fraction_true)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_database_health_fraction_true_aggregate_aggregate:",
                 "       aggregate(value_database_health_fraction_true_aggregate)]",
               "| condition val() < 0.95"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "webserver_health" {
           display_name = "Web Server Health"
           combiner     = "OR"
           conditions {
             display_name = "Web Server Health"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/web_server/health'",
                 "| group_by 5m, [value_health_fraction_true: fraction_true(value.health)]",
                 "| every 5m",
                 "| group_by 5m,",
                 "    [value_health_fraction_true_aggregate:",
                 "       aggregate(value_health_fraction_true)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_health_fraction_true_aggregate_aggregate:",
                 "       aggregate(value_health_fraction_true_aggregate)]",
               "| condition val() < 0.95"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "scheduler_heartbeat" {
           display_name = "Scheduler Heartbeat"
           combiner     = "OR"
           conditions {
             display_name = "Scheduler Heartbeat"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/scheduler_heartbeat_count'",
                 "| group_by 10m,",
                 "    [value_scheduler_heartbeat_count_aggregate:",
                 "      aggregate(value.scheduler_heartbeat_count)]",
                 "| every 10m",
                 "| group_by 10m,",
                 "    [value_scheduler_heartbeat_count_aggregate_mean:",
                 "       mean(value_scheduler_heartbeat_count_aggregate)]",
                 "| every 10m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_scheduler_heartbeat_count_aggregate_mean_aggregate:",
                 "       aggregate(value_scheduler_heartbeat_count_aggregate_mean)]",
               "| condition val() < 80"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "database_cpu" {
           display_name = "Database CPU"
           combiner     = "OR"
           conditions {
             display_name = "Database CPU"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/database/cpu/utilization'",
                 "| group_by 10m, [value_utilization_mean: mean(value.utilization)]",
                 "| every 10m",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val() > 0.8"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "scheduler_cpu" {
           display_name = "Scheduler CPU"
           combiner     = "OR"
           conditions {
             display_name = "Scheduler CPU"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch k8s_container",
                 "| metric 'kubernetes.io/container/cpu/limit_utilization'",
                 "| filter (resource.pod_name =~ 'airflow-scheduler-.*')",
                 "| group_by 10m, [value_limit_utilization_mean: mean(value.limit_utilization)]",
                 "| every 10m",
                 "| group_by [resource.cluster_name],",
                 "    [value_limit_utilization_mean_mean: mean(value_limit_utilization_mean)]",
               "| condition val() > 0.8"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "worker_cpu" {
           display_name = "Worker CPU"
           combiner     = "OR"
           conditions {
             display_name = "Worker CPU"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch k8s_container",
                 "| metric 'kubernetes.io/container/cpu/limit_utilization'",
                 "| filter (resource.pod_name =~ 'airflow-worker.*')",
                 "| group_by 10m, [value_limit_utilization_mean: mean(value.limit_utilization)]",
                 "| every 10m",
                 "| group_by [resource.cluster_name],",
                 "    [value_limit_utilization_mean_mean: mean(value_limit_utilization_mean)]",
               "| condition val() > 0.8"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "webserver_cpu" {
           display_name = "Web Server CPU"
           combiner     = "OR"
           conditions {
             display_name = "Web Server CPU"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch k8s_container",
                 "| metric 'kubernetes.io/container/cpu/limit_utilization'",
                 "| filter (resource.pod_name =~ 'airflow-webserver.*')",
                 "| group_by 10m, [value_limit_utilization_mean: mean(value.limit_utilization)]",
                 "| every 10m",
                 "| group_by [resource.cluster_name],",
                 "    [value_limit_utilization_mean_mean: mean(value_limit_utilization_mean)]",
               "| condition val() > 0.8"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
         
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "parsing_time" {
           display_name = "DAG Parsing Time"
           combiner     = "OR"
           conditions {
             display_name = "DAG Parsing Time"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/dag_processing/total_parse_time'",
                 "| group_by 5m, [value_total_parse_time_mean: mean(value.total_parse_time)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val(0) > cast_units(30,\"s\")"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "database_memory" {
           display_name = "Database Memory"
           combiner     = "OR"
           conditions {
             display_name = "Database Memory"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/database/memory/utilization'",
                 "| group_by 10m, [value_utilization_mean: mean(value.utilization)]",
                 "| every 10m",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val() > 0.8"])
               duration = "0s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "scheduler_memory" {
           display_name = "Scheduler Memory"
           combiner     = "OR"
           conditions {
             display_name = "Scheduler Memory"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch k8s_container",
                 "| metric 'kubernetes.io/container/memory/limit_utilization'",
                 "| filter (resource.pod_name =~ 'airflow-scheduler-.*')",
                 "| group_by 10m, [value_limit_utilization_mean: mean(value.limit_utilization)]",
                 "| every 10m",
                 "| group_by [resource.cluster_name],",
                 "    [value_limit_utilization_mean_mean: mean(value_limit_utilization_mean)]",
               "| condition val() > 0.8"])
               duration = "0s"
               trigger {
                 count = "1"
               }
             }
           }
           documentation {
             content = join("", [
               "Scheduler Memory exceeds a threshold, summed across all schedulers in the environment. ",
             "Add more schedulers OR increase scheduler's memory OR reduce scheduling load (e.g. through lower parsing frequency or lower number of DAGs/tasks running"])
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "worker_memory" {
           display_name = "Worker Memory"
           combiner     = "OR"
           conditions {
             display_name = "Worker Memory"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch k8s_container",
                 "| metric 'kubernetes.io/container/memory/limit_utilization'",
                 "| filter (resource.pod_name =~ 'airflow-worker.*')",
                 "| group_by 10m, [value_limit_utilization_mean: mean(value.limit_utilization)]",
                 "| every 10m",
                 "| group_by [resource.cluster_name],",
                 "    [value_limit_utilization_mean_mean: mean(value_limit_utilization_mean)]",
               "| condition val() > 0.8"])
               duration = "0s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "webserver_memory" {
           display_name = "Web Server Memory"
           combiner     = "OR"
           conditions {
             display_name = "Web Server Memory"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch k8s_container",
                 "| metric 'kubernetes.io/container/memory/limit_utilization'",
                 "| filter (resource.pod_name =~ 'airflow-webserver.*')",
                 "| group_by 10m, [value_limit_utilization_mean: mean(value.limit_utilization)]",
                 "| every 10m",
                 "| group_by [resource.cluster_name],",
                 "    [value_limit_utilization_mean_mean: mean(value_limit_utilization_mean)]",
               "| condition val() > 0.8"])
               duration = "0s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "scheduled_tasks_percentage" {
           display_name = "Scheduled Tasks Percentage"
           combiner     = "OR"
           conditions {
             display_name = "Scheduled Tasks Percentage"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/unfinished_task_instances'",
                 "| align mean_aligner(10m)",
                 "| every(10m)",
                 "| window(10m)",
                 "| filter_ratio_by [resource.project_id, resource.environment_name], metric.state = 'scheduled'",
               "| condition val() > 0.80"])
               duration = "300s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "queued_tasks_percentage" {
           display_name = "Queued Tasks Percentage"
           combiner     = "OR"
           conditions {
             display_name = "Queued Tasks Percentage"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/unfinished_task_instances'",
                 "| align mean_aligner(10m)",
                 "| every(10m)",
                 "| window(10m)",
                 "| filter_ratio_by [resource.project_id, resource.environment_name], metric.state = 'queued'",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val() > 0.95"])
               duration = "300s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "queued_or_scheduled_tasks_percentage" {
           display_name = "Queued or Scheduled Tasks Percentage"
           combiner     = "OR"
           conditions {
             display_name = "Queued or Scheduled Tasks Percentage"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/unfinished_task_instances'",
                 "| align mean_aligner(10m)",
                 "| every(10m)",
                 "| window(10m)",
                 "| filter_ratio_by [resource.project_id, resource.environment_name], or(metric.state = 'queued', metric.state = 'scheduled' )",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val() > 0.80"])
               duration = "120s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         
         resource "google_monitoring_alert_policy" "workers_above_minimum" {
           display_name = "Workers above minimum (negative = missing workers)"
           combiner     = "OR"
           conditions {
             display_name = "Workers above minimum"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| { metric 'composer.googleapis.com/environment/num_celery_workers'",
                 "| group_by 5m, [value_num_celery_workers_mean: mean(value.num_celery_workers)]",
                 "| every 5m",
                 "; metric 'composer.googleapis.com/environment/worker/min_workers'",
                 "| group_by 5m, [value_min_workers_mean: mean(value.min_workers)]",
                 "| every 5m }",
                 "| outer_join 0",
                 "| sub",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val() < 0"])
               duration = "0s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "pod_evictions" {
           display_name = "Worker pod evictions"
           combiner     = "OR"
           conditions {
             display_name = "Worker pod evictions"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'composer.googleapis.com/environment/worker/pod_eviction_count'",
                 "| align delta(1m)",
                 "| every 1m",
                 "| group_by [resource.project_id, resource.environment_name]",
               "| condition val() > 0"])
               duration = "60s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "scheduler_errors" {
           display_name = "Scheduler Errors"
           combiner     = "OR"
           conditions {
             display_name = "Scheduler Errors"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'logging.googleapis.com/log_entry_count'",
                 "| filter (metric.log == 'airflow-scheduler' && metric.severity == 'ERROR')",
                 "| group_by 5m,",
                 "    [value_log_entry_count_aggregate: aggregate(value.log_entry_count)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_log_entry_count_aggregate_max: max(value_log_entry_count_aggregate)]",
               "| condition val() > 50"])
               duration = "300s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "worker_errors" {
           display_name = "Worker Errors"
           combiner     = "OR"
           conditions {
             display_name = "Worker Errors"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'logging.googleapis.com/log_entry_count'",
                 "| filter (metric.log == 'airflow-worker' && metric.severity == 'ERROR')",
                 "| group_by 5m,",
                 "    [value_log_entry_count_aggregate: aggregate(value.log_entry_count)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_log_entry_count_aggregate_max: max(value_log_entry_count_aggregate)]",
               "| condition val() > 50"])
               duration = "300s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "webserver_errors" {
           display_name = "Web Server Errors"
           combiner     = "OR"
           conditions {
             display_name = "Web Server Errors"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'logging.googleapis.com/log_entry_count'",
                 "| filter (metric.log == 'airflow-webserver' && metric.severity == 'ERROR')",
                 "| group_by 5m,",
                 "    [value_log_entry_count_aggregate: aggregate(value.log_entry_count)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_log_entry_count_aggregate_max: max(value_log_entry_count_aggregate)]",
               "| condition val() > 50"])
               duration = "300s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         resource "google_monitoring_alert_policy" "other_errors" {
           display_name = "Other Errors"
           combiner     = "OR"
           conditions {
             display_name = "Other Errors"
             condition_monitoring_query_language {
               query = join("", [
                 "fetch cloud_composer_environment",
                 "| metric 'logging.googleapis.com/log_entry_count'",
                 "| filter",
                 "    (metric.log !~ 'airflow-scheduler|airflow-worker|airflow-webserver'",
                 "     && metric.severity == 'ERROR')",
                 "| group_by 5m, [value_log_entry_count_max: max(value.log_entry_count)]",
                 "| every 5m",
                 "| group_by [resource.project_id, resource.environment_name],",
                 "    [value_log_entry_count_max_aggregate: aggregate(value_log_entry_count_max)]",
               "| condition val() > 10"])
               duration = "300s"
               trigger {
                 count = "1"
               }
             }
           }
           # uncomment to set an auto close strategy for the alert
           #alert_strategy {
           #    auto_close = "30m"
           #}
         }
         
         
         #######################################################
         #
         # Create Monitoring Dashboard
         #
         ########################################################
         
         
         resource "google_monitoring_dashboard" "Composer_Dashboard" {
           dashboard_json = <<EOF
         {
           "category": "CUSTOM",
           "displayName": "Cloud Composer - Monitoring Platform",
           "mosaicLayout": {
             "columns": 12,
             "tiles": [
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "MARKDOWN"
                   },
                   "title": "Health"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 0
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.environment_health.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 1
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.database_health.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 1
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.webserver_health.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 5
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.scheduler_heartbeat.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 5
               },
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "RAW"
                   },
                   "title": "Airflow Task Execution and DAG Parsing"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 9
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.scheduled_tasks_percentage.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 10
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.queued_tasks_percentage.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 10
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.queued_or_scheduled_tasks_percentage.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 14
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.parsing_time.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 14
               },
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "RAW"
                   },
                   "title": "Workers presence"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 18
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.workers_above_minimum.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 19
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.pod_evictions.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 19
               },
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "RAW"
                   },
                   "title": "CPU Utilization"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 23
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.database_cpu.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 24
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.scheduler_cpu.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 24
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.worker_cpu.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 28
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.webserver_cpu.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 28
               },
         
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "RAW"
                   },
                   "title": "Memory Utilization"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 32
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.database_memory.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 33
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.scheduler_memory.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 33
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.worker_memory.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 37
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.webserver_memory.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 37
               },
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "RAW"
                   },
                   "title": "Airflow component errors"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 41
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.scheduler_errors.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 42
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.worker_errors.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 42
               },
                     {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.webserver_errors.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 0,
                 "yPos": 48
               },
               {
                 "height": 4,
                 "widget": {
                   "alertChart": {
                     "name": "${google_monitoring_alert_policy.other_errors.name}"
                   }
                 },
                 "width": 6,
                 "xPos": 6,
                 "yPos": 48
               },
               {
                 "height": 1,
                 "widget": {
                   "text": {
                     "content": "",
                     "format": "RAW"
                   },
                   "title": "Task errors"
                 },
                 "width": 12,
                 "xPos": 0,
                 "yPos": 52
               }
             ]
           }
         }
         EOF
         }

  4. Edit the `"google_monitoring_monitored_project"` `resource` block:

     1. Replace the list of projects in the `for_each` block with your **Monitored Projects**.
     2. Replace `"YOUR_MONITORING_PROJECT"` in the `metrics_scope` with the name of your **Monitoring Project**.
  5. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations. Make corrections if necessary.
         
         terraform plan
         

  6. Apply the Terraform configuration by running the following command and entering yes at the prompt:
         
         terraform apply
         

  7. In Google Cloud console of your **Monitoring Project** , go to the **Monitoring Dashboard** page:

Go to [Monitoring Dashboard](https://console.cloud.google.com/monitoring/dashboards)

  8. Find your custom dashboard named **Cloud Composer - Monitoring Platform** in the **Custom** tab.




## What's next

  * [Monitoring environments](https://docs.cloud.google.com/composer/docs/composer-2/monitor-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
