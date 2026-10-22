---
url: https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring/
title: Use Cloud Monitoring for Dataflow pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:38.066915+00:00
---

# Use Cloud Monitoring for Dataflow pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Cloud Monitoring for Dataflow pipelines Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring provides powerful logging and diagnostics. Dataflow integration with Monitoring lets you access Dataflow job metrics such as job status, element counts, system lag (for streaming jobs), and user counters from the Monitoring dashboards. You can also use Monitoring alerts to notify you of various conditions, such as long streaming system lag or failed jobs.

## Before you begin

Follow the [Java tutorial](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-java), [Python tutorial](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-python), or [Go tutorial](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-go) to set up your Dataflow project. Then, [construct and run your pipeline](https://docs.cloud.google.com/dataflow/pipelines/constructing-your-pipeline).

**Note:** If your [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) is configured with a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) Service Perimeter for the Monitoring API, some metrics aren't available for pipeline Compute Engine workers outside the perimeter. To learn more about Service Perimeters, see the [VPC Service Controls Service Perimeter configuration documentation](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

To see logs in Metrics Explorer, the [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have the `roles/monitoring.metricWriter` role.

## Custom metrics

Any metric that you define in your Apache Beam pipeline is reported by Dataflow to Monitoring as a custom metric. Apache Beam has [three types of pipeline metrics](https://beam.apache.org/documentation/programming-guide/#metrics): `Counter`, `Distribution`, and `Gauge`.

  * Dataflow reports `Counter` and `Distribution` metrics to Monitoring.
  * `Distribution` is reported as four submetrics suffixed with `_MAX`, `_MIN`, `_MEAN`, and `_COUNT`.
  * Dataflow doesn't support creating a histogram from `Distribution` metrics.
  * Dataflow reports incremental updates to Monitoring approximately every 30 seconds.
  * To avoid conflicts, all Dataflow custom metrics are exported as a `double` data type.
  * For simplicity, all Dataflow custom metrics are exported as a `GAUGE` [metric kind](https://cloud.google.com/monitoring/api/v3/kinds-and-types#metric-kinds). You can monitor the delta over a time window for a `GAUGE` metric, as shown in the following [Prometheus Query Language](https://docs.cloud.google.com/monitoring/promql) (PromQL) example:
        
        sum by (ptransform, metric_name) (
           delta({
              "__name__"="dataflow.googleapis.com/job/user_counter",
              "monitored_resource"="dataflow_job",
              "job_id"="[JobID]"
           }[${__interval}])
        )
        

  * The Dataflow custom metrics appear in Monitoring as `dataflow.googleapis.com/job/user_counter` with the labels `metric_name: metric-name` and `ptransform: ptransform-name`.

  * For backward compatibility, Dataflow also reports custom metrics to Monitoring as `custom.googleapis.com/dataflow/metric-name`.

  * The Dataflow custom metrics are subject to the limitation of [cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality) in Monitoring.

  * Each project has a limit of 100 Dataflow custom metrics. These metrics are published as `custom.googleapis.com/dataflow/metric-name`.




Custom metrics that are reported to Monitoring incur charges based on the [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).

## Use Metrics Explorer

Use Monitoring to explore Dataflow metrics. Follow the steps in this section to observe the standard metrics that are provided for each of your Apache Beam pipelines. For more information about using Metrics Explorer, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

  1. In the Google Cloud console, select **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Metrics explorer**.

  3. In the **Select a metric** pane, enter `Dataflow Job` in the filter.

  4. From the list that appears, select a metric to observe for one of your jobs. Read about the available Dataflow-related metrics.
     * **Job status:** Provide job status (Failed, Successful) as an enum every 30 seconds and on update. Note: `enum` values might not be charted or used for alerts, but you can retrieve this value by using the Cloud Monitoring web interface. For alerting, use the "Failed" metric that sets to 1 if a job fails.
     * **Failed:** Failed sets 1 if a job exits with a failure. Use this metric to alert on and chart the number of failed pipelines.
     * **Elapsed time:** Job elapsed time (measured in seconds), reported every 30 seconds.
     * **System lag:** Max lag across the entire pipeline, reported in seconds.
     * **Current vCPU count:** Current # of virtual CPUs used by job and updated on value change.
     * **Total vCPU usage:** Total # of virtual CPUs used by a job and updated on value change.
     * **Total Persistent Disk usage:** Cumulative total of Persistent Disk used by job, measured in GB-seconds and updated on value change. Note: there are two different types of persistent disk (SSD and HDD). They are both reported using the same metric name and use a metric label to differentiate.
     * **Total memory usage:** Cumulative total memory allocated to job, measured in GB-seconds and updated on value change.
     * **Element count:** Number of elements per PCollection. Note: This metric is per-PCollection, not job level, so it's not yet available for alerting.
     * **Estimated byte count:** Number of bytes processed per PCollection. Note: This metric is per-PCollection, not job level, so it's not yet available for alerting.




When running Dataflow jobs, you might also want to monitor metrics for your sources and sinks. For example, you might want to monitor BigQuery Storage API metrics. For more information, see [Create dashboards, charts, and alerts](https://docs.cloud.google.com/bigquery/docs/monitoring-dashboard) and the complete list of [metrics from the BigQuery Data Transfer Service](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquerystorage).

## Create alerting policies and dashboards

Monitoring provides access to Dataflow-related metrics. Create dashboards to chart the time series of metrics, and create alerting policies that notify you when metrics reach specified values.

For streaming jobs, you can also use [turnkey alerts](https://docs.cloud.google.com/dataflow/docs/guides/turnkey-alerts) to automatically enable pre-configured alert policies at job startup.

### Create groups of resources

To make it easier to set alerts and build dashboards, create resource groups that include multiple Apache Beam pipelines.

  1. In the Google Cloud console, select **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Groups**.

  3. Click **Create group**.

  4. Enter a name for your group.

  5. Add filter criteria that define the Dataflow resources included in the group. For example, one of your filter criteria can be the name prefix of your pipelines. ![Create group.](https://docs.cloud.google.com/static/dataflow/images/stackdriver-create-groups.png)

  6. After the group is created, you can see the basic metrics related to resources in that group.




### Create alerting policies for Dataflow metrics

Monitoring lets you create alerts and receive notifications when a metric crosses a specified threshold. For example, you can receive a notification when system lag of a streaming pipeline increases above a predefined value.

  1. In the Google Cloud console, select **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Alerting**.

  3. Click **Create policy**.

  4. On the **Create new alerting policy** page, define the alerting conditions and notification channels.  
For example, to set an alert on the system lag for the `WindowedWordCount` Apache Beam pipeline group, complete the following steps:

     1. Click **Select a metric**.
     2. In the **Select a metric** field, enter `Dataflow Job`.
     3. For **Metric Categories** , select **Job**.
     4. For **Metrics** , select **System lag**.

Every time an alert is triggered, an incident and a corresponding event are created. If you specified a notification mechanism in the alert, such as email or SMS, you also receive a notification.




### Build custom monitoring dashboards

You can build Monitoring dashboards with the most relevant Dataflow-related charts. To add a chart to a dashboard, follow these steps:

  1. In the Google Cloud console, select **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Dashboards**.

  3. Click **Create dashboard**.

  4. Click **Add widget**.

  5. In the **Add widget** window, for **Data** , select **Metric**.

  6. In the **Select a metric** pane, for **Metric** , enter `Dataflow Job`.

  7. Select a metric category and a metric.




You can add as many charts to the dashboard as you like.

### Receive worker VM metrics from the Monitoring agent

**Caution:** The legacy Monitoring agent reached [end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents) on September 28, 2026. The `--experiments=enable_stackdriver_agent_metrics` option uses a deprecated container image that isn't maintained and might contain unpatched vulnerabilities. We recommend that you don't use this option.

You can use Monitoring to monitor persistent disk, CPU, network, and process metrics. When you run your pipeline, enable the [Monitoring agent](https://docs.cloud.google.com/monitoring/agent) from your Dataflow worker VM instances. See the list of [available Monitoring agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent).

To enable the Monitoring agent, use the `--experiments=enable_stackdriver_agent_metrics` option when running your pipeline. The [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have the `roles/monitoring.metricWriter` role.

To disable the Monitoring agent without stopping your pipeline, update your pipeline by [launching a replacement job](https://docs.cloud.google.com/dataflow/pipelines/updating-a-pipeline#launching-your-replacement-job) without the `--experiments=enable_stackdriver_agent_metrics` parameter.

## Storage and retention

Information about completed or cancelled Dataflow jobs is stored for 30 days.

Operational logs are stored in the [`_Default` log bucket](https://docs.cloud.google.com/logging/docs/routing/overview#default-bucket). The logging API service name is `dataflow.googleapis.com`. For more information about the Google Cloud monitored resource types and services used in Cloud Logging, see [Monitored resources and services](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

For details about how long log entries are retained by Logging, see the retention information in [Quotas and limits: Logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

For information about viewing operational logs, see [Monitor and view pipeline logs](https://docs.cloud.google.com/dataflow/docs/guides/logging#MonitoringLogs).

## What's next

To learn more, consider exploring these other resources:

  * [Monitoring documentation](https://docs.cloud.google.com/monitoring/docs)
  * [Use the Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
