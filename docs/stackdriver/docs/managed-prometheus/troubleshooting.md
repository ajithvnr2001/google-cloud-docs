---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting/
title: Troubleshooting Managed Service for Prometheus \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:45.845799+00:00
---

# Troubleshooting Managed Service for Prometheus  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Troubleshooting Managed Service for Prometheus Stay organized with collections  Save and categorize content based on your preferences. 

This document describes some problems you might encounter when using Google Cloud Managed Service for Prometheus and provides information on diagnosing and resolving the problems.

You configured Managed Service for Prometheus but are not seeing any metric data in Grafana or the Prometheus UI. At a high level, the cause might be either of the following:

  * A problem on the query side, so that data can't be read. Query-side problems are often caused by incorrect permissions on the service account reading the data or by misconfiguration of Grafana.

  * A problem on the ingestion side, so that no data is sent. Ingestion-side problems can be caused by configuration problems with service accounts, collectors, or rule evaluation.




To determine whether the problem is on the ingestion side or the query side, try querying data by using the Metrics Explorer **PromQL** tab in the Google Cloud console. This page is guaranteed not to have any issues with read permissions or Grafana settings.

To view this page, do the following:

  1. Use the Google Cloud console project picker to select the project for which you are not seeing data.

  2. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

  4. Enter the following query into the editor, and then click **Run query** :
         
         up
         




If you query the `up` metric and see results, then the problem is on the query side. For information on resolving these problems, see Query-side problems.

If you query the `up` metric and do not see any results, then the problem is on the ingestion side. For information on resolving these problems, see Ingestion-side problems.

A firewall can also cause ingestion and query problems; for more information, see Firewalls.

The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

  * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
  * Data about labels and cardinality of metrics.
  * Number of reads for each metric.
  * Use of metrics in alerting policies and custom dashboards.
  * Rate of metric-write errors.



You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. 

To view the **Metrics Management** page, do the following: 

  1. In the Google Cloud console, go to the  query_stats **Metrics management** page: 

[Go to **Metrics management**](https://console.cloud.google.com/monitoring/metrics-management)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, select your time window. By default, the **Metrics Management** page displays information about the metrics collected in the previous one day.



For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

## Query-side problems

The cause of most query-side problems is one of the following:

  * Incorrect permissions or credentials for service accounts.
  * Misconfiguration of Workload Identity Federation for GKE, if your cluster has this feature enabled. For more information, see [Configure a service account for Workload Identity Federation for GKE](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#gmp-wli-svcacct).



Start by doing the following:

  * Check your configuration carefully against the [setup instructions for querying](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#begin).

  * If you are using Workload Identity Federation for GKE, verify that your service account has the correct permissions by doing the following;

    1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

    2. Identify the service account name in the list of principals. Verify that the name of the service account is correctly spelled. Then click _edit_ **Edit**.

    3. Select the **Role** field, then click **Currently used** and search for the Monitoring Viewer role. If the service account doesn't have this role, add it now.




If the problem still persists, then consider the following possibilities:

### Misconfigured or mistyped secrets

If you see any of the following, then you might have a missing or mistyped secret:

  * One of these "forbidden" errors in Grafana or the Prometheus UI:

    * "Warning: Unexpected response status when fetching server time: Forbidden"
    * "Warning: Error fetching metrics list: Unexpected response status when fetching metric names: Forbidden"
  * A message like this in your logs:  
"cannot read credentials file: open /gmp/key.json: no such file or directory"




If you are using the [data source syncer](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#grafana-oauth) to authenticate and configure Grafana, try the following to resolve these errors:

  1. Verify that you have chosen the correct Grafana API endpoint, Grafana data source UID, and Grafana API token. You can inspect the variables in the CronJob by running the command `kubectl describe cronjob datasource-syncer`.

  2. Verify that you have set the data source syncer's project ID to the same [metrics scope](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#env-setup) or project that your service account has credentials for.

  3. Verify that your Grafana service account has the "Admin" role and that your API token has not expired.

  4. Verify that your service account has the Monitoring Viewer role for the chosen project ID.

  5. Verify that there are no errors in the logs for the data source syncer Job by running `kubectl logs job.batch/datasource-syncer-init`. This command has to be run immediately after applying the `datasource-syncer.yaml` file.

  6. If using Workload Identity Federation for GKE, verify that you have not mistyped the account key or credentials, and verify that you have bound it to the correct namespace.




If you are using the [legacy frontend UI proxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#ui-prometheus), try the following to resolve these errors:

  1. Verify that you have set the frontend UI's project ID to the same [metrics scope](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#env-setup) or project that your service account has credentials for.

  2. Verify the project ID you've specified for any [`--query.project-id` flags](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#query-project-id).

  3. Verify that your service account has the Monitoring Viewer role for the chosen project ID.

  4. Verify you have set the correct project ID when [deploying the frontend UI](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#promui-deploy) and did not leave it set to the literal string `PROJECT_ID`.

  5. If using Workload Identity, verify that you have not mistyped the account key or credentials, and verify that you have bound it to the correct namespace.

  6. If mounting your own secret, make sure the secret is present:
         
         kubectl get secret gmp-test-sa -o json | jq '.data | keys'
         

  7. Verify that the secret is correctly mounted:
         
         kubectl get deploy frontend -o json | jq .spec.template.spec.volumes
         
         kubectl get deploy frontend -o json | jq .spec.template.spec.containers[].volumeMounts
         

  8. Make sure the secret is passed correctly to the container: 
         
         kubectl get deploy frontend -o json | jq .spec.template.spec.containers[].args
         




### Incorrect HTTP method for Grafana

If you see the following API error from Grafana, then Grafana is configured to send a `POST` request instead of a `GET` request:

  * "{"status":"error","errorType":"bad_data","error":"no match[] parameter provided"}%"



To resolve this issue, configure Grafana to use a `GET` request by following the instructions in [Configure a data source](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#grafana-datasource).

### Timeouts on large or long-running queries

If you see the following error in Grafana, then your default query timeout is too low:

  * "Post "http://frontend.NAMESPACE_NAME.svc:9090/api/v1/query_range": net/http: timeout awaiting response headers"



Managed Service for Prometheus does not time out until a query exceeds 120 seconds, while Grafana times out after 30 seconds by default. To fix this, raise the timeouts in Grafana to 120 seconds by following the instructions in [Configure a data source](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#grafana-datasource).

### Label-validation errors

If you see one of the following errors in Grafana, then you might be using an unsupported endpoint:

  * "Validation: labels other than **name** are not supported yet"
  * "Templating [job]: Error updating options: labels other than **name** are not supported yet."



Managed Service for Prometheus supports the `/api/v1/$label/values` endpoint only for the `__name__` label. This limitation causes queries using the `label_values($label)` variable in Grafana to fail.

Instead, use the `label_values($metric, $label)` form. This query is recommended because it constrains the returned label values by metric, which prevents retrieval of values not related to the dashboard's contents. This query calls a supported endpoint for Prometheus.

For more information about supported endpoints, see [API compatibility](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#http-api-details).

### Quota exceeded

If you see the following error, then you have exceeded your read quota for the Cloud Monitoring API:

  * "429: RESOURCE_EXHAUSTED: Quota exceeded for quota metric 'Time series queries ' and limit 'Time series queries per minute' of service 'monitoring.googleapis.com' for consumer 'project_number:...'."



To resolve this issue, submit a request to increase your read quota for the Monitoring API. For assistance, contact [Google Cloud Support](https://docs.cloud.google.com/support). For more information about quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

### Metrics from multiple projects

If you want to view metrics from multiple Google Cloud projects, you don't have to configure multiple data source syncers or create multiple data sources in Grafana.

Instead, create a Cloud Monitoring metrics scope in one Google Cloud project — the scoping project — that contains the projects you want to monitor. When you configure the Grafana data source with a scoping project, you get access to the data from all projects in the metrics scope. For more information, see [Queries and metrics scopes](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#scoping-intro).

### No monitored resource type specified

If you see the following error, then you need to specify a [monitored resource type](https://docs.cloud.google.com/monitoring/api/resources) when using PromQL to query a [Google Cloud system metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp):

  * "metric is configured to be used with more than one monitored resource type; series selector must specify a label matcher on monitored resource name"



You can specify a monitored resource type by filtering using the `monitored_resource` label. For more information about identifying and choosing a valid monitored resource type, see [Specifying a monitored resource type](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql#specifying-monitored-resource-type).

### Counter, histogram, and summary raw values not matching between the collector UI and the Google Cloud console

You might notice a difference between the values in the local collector Prometheus UI and the Google Cloud Google Cloud console when querying the raw value of cumulative Prometheus metrics, including counters, histograms, and summaries. This behavior is expected.

Monarch requires start timestamps, but Prometheus doesn't have start timestamps. Managed Service for Prometheus generates start timestamps by skipping the first ingested point in any time series and converting it into a start timestamp. Subsequent points have the value of the initial skipped point subtracted from their value to ensure rates are correct. This causes a persistent deficit in the raw value of those points.

The difference between the number in the collector UI and the number in the Google Cloud console is equal to the first value recorded in the collector UI, which is expected because the system skips that initial value, and subtracts it from subsequent points.

This is acceptable because there's no production need for running a query for raw values for cumulative metrics; all useful queries require a `rate()` function or the like, in which case the difference over any time horizon is identical between the two UIs. Cumulative metrics only ever increase, so you can't set an alert on a raw query as a time series only ever hits a threshold one time. All useful alerts and charts look at the change or the rate of change in the value.

The collector only holds about 10 minutes of data locally. Discrepancies in raw cumulative values might also arise due to a reset happening before the 10 minute horizon. To rule out this possibility, try setting only a 10 minute query lookback period when comparing the collector UI to the Google Cloud console.

Discrepancies can also be caused by having multiple worker threads in your application, each with a `/metrics` endpoint. If your application spins up multiple threads, you have to put the Prometheus client library in multiprocess mode. For more information, see the documentation for [using multiprocess mode in Prometheus' Python client library](https://prometheus.github.io/client_python/multiprocess/).

### Missing counter data or broken histograms

The most common signal of this problem is seeing no data or seeing data gaps when querying a plain counter metric (for example, a PromQL query of `metric_name_foo`). You can confirm this if data appears after you add a `rate` function to your query (for example, `rate(metric_name_foo[5m])`).

You might also notice that your samples ingested has risen sharply without any major change in scrape volume or that new metrics are being created with "unknown" or "unknown:counter" suffixes in Cloud Monitoring.

You might also notice that histogram operations, such as the `quantile()` function, don't work as expected.

These issues occur when a metric is collected without a [Prometheus metric TYPE](https://prometheus.io/docs/concepts/metric_types). As Monarch is strongly typed, Managed Service for Prometheus accounts for untyped metrics suffixing them with "unknown" and ingesting them twice, once as a gauge and once as a counter. The query engine then chooses whether to query the underlying gauge or counter metric based on what query functions you use.

While this heuristic usually works quite well, it can lead to issues such as strange results when querying a raw "unknown:counter" metric. Also, as histograms are specifically typed objects in Monarch, ingesting the [three required histogram metrics](https://prometheus.io/docs/concepts/metric_types/#histogram) as individual counter metrics causes histogram functions to not work. As "unknown"-typed metrics are ingested twice, not setting a TYPE doubles your samples ingested.

Common reasons why TYPE might not be set include:

  * Accidentally configuring a Managed Service for Prometheus collector as a federation server. **Federation is not supported when using Managed Service for Prometheus**. As federation intentionally drops TYPE information, implementing federation causes "unknown"-typed metrics.
  * Using Prometheus Remote Write at any point in the ingestion pipeline. This protocol also intentionally drops TYPE information.
  * Using a relabeling rule that modifies the metric name. This causes the renamed metric to disassociate from the TYPE information associated with the original metric name.
  * The exporter not emitting a TYPE for each metric.
  * A transient issue where TYPE is dropped when the collector first starts up.



To resolve this issue, do the following:

  * Stop using federation with Managed Service for Prometheus. If you want to reduce cardinality and cost by "rolling up" data before sending it to Monarch, see [Configure local aggregation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation).
  * Stop using Prometheus Remote Write in your collection path.
  * Confirm that the `# TYPE` field exists for each metric by visiting the `/metrics` endpoint.
  * Delete any relabeling rules that modify the name of a metric.
  * Delete any conflicting metrics with the "unknown" or "unknown:counter" suffix by [calling DeleteMetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete).
  * Or always query counters using a `rate` or other counter-processing function.



You can also [create a metric-exclusion rule within Metrics Management](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics) to prevent any "unknown"-suffixed metrics from being ingested by using the regular expression `prometheus.googleapis.com/.+/unknown.*`. If you don't fix the underlying issue before installing this rule, you might prevent wanted metric data from being ingested.

### Grafana data not persisted after pod restart

If your data appears to vanish from Grafana after a pod restart but is visible in Cloud Monitoring, then you are using Grafana to query the local Prometheus instance instead of Managed Service for Prometheus.

For information about configuring Grafana to use the managed service as a data source, see [Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#ui-grafana).

### Inconsistent query or alert rule results that automatically fix themselves

You might notice a pattern where queries over recent windows, such as queries run by recording or alerting rules, return unexplainable spikes in data. When you investigate the spike by running the query in Grafana or Metrics Explorer, you might see that the spike has disappeared and the data looks normal again.

This behavior might happen more often if any of the following are true:

  * You are consistently running many very similar queries in parallel, perhaps by using rules. These queries might differ from each other only by a single attribute. For example, you might be running 50 recording rules that differ only by the VALUE for the filter `{foo="VALUE"}`, or that differ only by having different `[duration]` values for the `rate` function.
  * You are running queries at time=now with no buffer.
  * You are running instant queries such as alerts or recording rules. If you are using a recording rule, you might notice that the saved output has the spike, but the spike can't be found when running a query over the raw data.
  * You are querying two metrics to create a ratio. The spikes are more pronounced when the count of time series is low in either the numerator or the denominator query.
  * Your metric data lives in larger Google Cloud regions such as `us-central1` or `us-east4`.



There are a few possible causes for temporary spikes in these kinds of queries:

  * (Most common cause) Your similar, parallel queries are all requesting data from the same set of Monarch nodes, consuming a large amount of memory on each node in aggregate. When Monarch has sufficient available resources in a cloud region, your queries work. When Monarch is under resource pressure in a cloud region, each node throttles queries, preferentially throttling users that are consuming the most memory on each node. When Monarch once again has sufficient resources, your queries work again. These queries might be SLIs that are automatically generated from tools such as [Sloth](https://sloth.dev/).
  * You have late-arriving data, and your queries are not tolerant to this. It takes approximately 3-7 seconds for newly-written data to be queryable, excluding networking latency and any delay caused by resource pressure within your environment. If your query does not build in a delay or offset to account for late data, then you might unknowingly query over a period where you only have partial data. Once the data arrives, your query results look normal.
  * Monarch might have a slight inconsistency when saving your data in different replicas. The query engine attempts to pick the "best quality" replica, but if different queries pick different replicas with slightly different sets of data, it's possible that your results slightly vary between queries. This is an expected behavior of the system, and your alerts should be tolerant to these slight discrepancies.
  * An entire Monarch region might be temporarily unavailable. If a region is not reachable, the query engine treats the region like it never existed. After the region becomes available, query results continue returning that region's data.



To account for these possible root causes, you should ensure your queries, rules, and alerts follow these best practices:

  * Consolidate similar rules and alerts into a single rule that aggregates by labels instead of having separate rules for each permutation of label values. If these are alerting rules, you can use label-based notifications to route alerts from the aggregate rule instead of configuring individual routing rules for each alert.

For example, if you have a label `foo` with values `bar`, `baz`, and `qux`, instead of having a separate rule for each label value (one with the query `sum(metric{foo="bar"})`, one with the query `sum(metric{foo="baz"})`, one with the query `sum(metric{foo="qux"})`), have a single rule that aggregates across that label and optionally filters to the label values you care about (such as `sum by (foo) metric{foo=~"bar|baz|qux"}`).

If your metric has 2 labels, and each label has 50 values, and you have a separate rule for each combination of label values, and your rule queries are a ratio, then each period you are launching 50 x 50 x 2 = **5,000 parallel Monarch queries** that each hit the same set of Monarch nodes. In aggregate, these 5,000 parallel queries consume a large amount of memory on each Monarch node, which increases your risk of being throttled when a Monarch region is under resource pressure.

If you instead use aggregations to consolidate these rules into a single rule that's a ratio, then each period you only launch 2 parallel Monarch queries. These 2 parallel queries consume much less memory in aggregate than the 5,000 parallel queries, and your risk of being throttled is much lower.

  * If your rule looks back more than 1 day, then run it less frequently than every minute. Queries that access data older than 25 hours go to the Monarch on-disk data repository. These repository queries are slower and consume more memory than queries over more recent data, which exacerbates any problems with memory consumption from parallel recording rules.

Consider running these kinds of queries once an hour instead of once a minute. Running a day-long query every minute only gives you a 1/1440 = 0.07% change in the result each period, which is a negligible change. Running a day-long query every hour gives you a 60/1440 = 4% change in the result each period, which is a more relevant signal size. If you need to get alerted if recent data changes, then you can run a different rule with a shorter lookback (such as 5 minutes) once a minute.

  * Use the [`for:` field](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule) in your rules to tolerate transient aberrant results. The `for:` field stops your alert from firing unless the alert condition has been met for at least the configured duration. Set this field to be twice the length of your rule evaluation interval or longer.

Using the `for:` field helps because transient issues often resolve themselves, meaning they don't occur on consecutive alert cycles. If you see a spike, and that spike persists across multiple timestamps and multiple alert cycles, you can be more confident that it's a real spike and not a transient issue.

  * Use the [`offset` modifier in PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier) to delay your query evaluation so it doesn't operate over the most recent period of data. Look at your sampling interval and your rule-evaluation interval and identify the longer of the two. Ideally, your query offset is at least twice the length of the longer interval. For example, if you send data every 15s and run rules every 30s, then offset your queries by at least 1m. A 1m offset causes your rules to use an end timestamp that's at least 60 seconds old, which builds in a buffer for late data to arrive before running your rule.

This is both a Cloud Monitoring best practice (all [managed PromQL alerts](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting) have at least a 1m offset) and a [Prometheus best practice](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule-query-offset).

  * Group your results by the `location` label to isolate potential unavailable region issues. The label that has the Google Cloud region might be called `zone` or `region` in some system metrics.

If you don't group by region and a region becomes unavailable, then it looks like your results drop suddenly and you might see historical results drop as well. If you group by region and a region becomes unavailable, then you don't receive any results from that region but results from other regions are unaffected.

  * If your ratio is a success ratio (such as 2xx responses over total responses), consider making it an error ratio (such as 4xx+5xx responses over total responses) instead. Error ratios are more tolerant to inconsistent data, as a temporary dip in the data makes the query result lower than your threshold and therefore doesn't cause your alert to fire.

  * Break apart a ratio query or recording rule into separate numerator and denominator queries, if possible. This is a [Prometheus best practice](https://prometheus.io/docs/practices/rules/#examples). Using ratios is valid, but because the query in the numerator executes independently from the query in the denominator, using ratios can magnify the impact of transient issues:

    * If Monarch throttles the numerator query but not the denominator query, then you might see unexpectedly low results. If Monarch throttles the denominator query but not the numerator query, then you might see unexpectedly high results.
    * If you are querying recent time periods and you have late-arriving data, it's possible that one query in the ratio executes before the data arrives and the other query in the ratio executes after the data arrives.
    * If either side of your ratio is comprised of relatively few time series, then any errors get magnified. If your numerator and denominator each have 100 time series, and Monarch doesn't return 1 time series in the numerator query, then you are likely to notice the 1% difference. If your numerator and denominator each have 1,000,000 time series, and Monarch doesn't return 1 time series in the numerator query, you are unlikely to notice the 0.0001% difference.
  * If your data is sparse, then use a longer rate duration in your query. If your data arrives every 10 minutes and your query uses `rate(metric[1m])`, then your query only looks back 1 minute for data and you sometimes get empty results. As a rule of thumb, set your `[duration]` to be at least 4 times your scrape interval.

Gauge queries by default look back 5 minutes for data. To make them look back further, use any valid `x_over_time` function such as `last_over_time`.




These recommendations are mostly relevant if you are seeing inconsistent query results when querying recent data. If you see this issue happening when querying data that's over 25 hours old, then there might be a technical issue with Monarch. If this happens, contact Cloud Customer Care so we can investigate.

### Importing Grafana dashboards

For information about using and troubleshooting the dashboard importer, see [Import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/import-grafana-dashboards).

For information about problems with the conversion of the dashboard contents, see the importer's [`README`](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/scripts/dashboard-importer/README.md#troubleshooting) file.

## Ingestion-side problems

Ingestion-side problems can be related to either collection or rule evaluation. Start by looking at the error logs for managed collection. You can run the following commands:
    
    
    kubectl logs -f -n gmp-system -lapp.kubernetes.io/part-of=gmp
    
    kubectl logs -f -n gmp-system -lapp.kubernetes.io/name=collector -c prometheus
    

On GKE Autopilot clusters, you can run the following commands:
    
    
    kubectl logs -f -n gke-gmp-system -lapp.kubernetes.io/part-of=gmp
    
    kubectl logs -f -n gke-gmp-system -lapp.kubernetes.io/name=collector -c prometheus
    

The target status feature can help you debug your scrape target. For more information, see [target status information](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#target-status).

### Endpoint status is missing or too old

If you have enabled the [target status feature](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#target-status) but one or more of your PodMonitoring or ClusterPodMonitoring resources are missing the `Status.Endpoint Statuses` field or value, then you might have one of the following problems:

  * Managed Service for Prometheus was unable to reach a collector on the same node as one of your endpoints.
  * One or more of your PodMonitoring or ClusterPodMonitoring configs resulted in no valid targets.



Similar problems can also cause the `Status.Endpoint Statuses.Last Update Time` field to have value older than a few minutes plus your scrape interval.

To resolve this issue, start by checking that the Kubernetes pods associated with your scrape endpoint are running. If your Kubernetes pods are running, the label selectors match, and you can manually access the scrape endpoints (typically by visiting the `/metrics` endpoint), then check whether the Managed Service for Prometheus collectors are running.

### Collectors fraction is less than 1

If you have enabled the [target status feature](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#target-status), then you get status information about your resources. The `Status.Endpoint Statuses.Collectors Fraction` value of your PodMonitoring or ClusterPodMonitoring resources represents the fraction of collectors, expressed from `0` to `1`, that are reachable. For example, a value of `0.5` indicates that 50% of your collectors are reachable, while a value of `1` indicates that 100% of your collectors are reachable.

If the `Collectors Fraction` field has a value other than `1`, then one or more collectors are unreachable, and metrics in any of those nodes are possibly not being scraped. Ensure that all collectors are running and reachable over the cluster network. You can view the status of collector pods with the following command:
    
    
    kubectl -n gmp-system get pods --selector="app.kubernetes.io/name=collector"
    

On GKE Autopilot clusters, this command looks slightly different:
    
    
    kubectl -n gke-gmp-system get pods --selector="app.kubernetes.io/name=collector"
    

You can investigate individual collector pods (for example, a collector pod named `collector-12345`) with the following command:
    
    
    kubectl -n gmp-system describe pods/collector-12345
    

On GKE Autopilot clusters, run the following command:
    
    
    kubectl -n gke-gmp-system describe pods/collector-12345
    

If collectors are not healthy, see [GKE workload troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#workload_issues).

If the collectors are healthy, then check the operator logs. To check the operator logs, first run the following command to find the operator pod name:
    
    
    kubectl -n gmp-system get pods --selector="app.kubernetes.io/name=gmp-collector"
    

On GKE Autopilot clusters, run the following command:
    
    
    kubectl -n gke-gmp-system get pods --selector="app.kubernetes.io/name=gmp-collector"
    

Then, check the operator logs (for example, an operator pod named `gmp-operator-12345`) with the following command:
    
    
    kubectl -n gmp-system logs pods/gmp-operator-12345
    

On GKE Autopilot clusters, run the following command:
    
    
    kubectl -n gke-gmp-system logs pods/gmp-operator-12345
    

### Unhealthy targets

If you have enabled the [target status feature](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#target-status), but one or more of your PodMonitoring or ClusterPodMonitoring resources has the `Status.Endpoint Statuses.Unhealthy Targets` field with the value other than 0, then the collector cannot scrape one or more of your targets.

View the `Sample Groups` field, which groups targets by error message, and find the `Last Error` field. The `Last Error` field comes from Prometheus and tells you why the target was unable to be scraped. To resolve this issue, using the sample targets as a reference, check whether your scrape endpoints are running.

### Unauthorized scrape endpoint

If you see one of the following errors and your scrape target requires authorization, then your collector is either not set up to use the correct authorization type or is using the incorrect authorization payload:

  * `server returned HTTP status 401 Unauthorized`
  * `x509: certificate signed by unknown authority`



To resolve this issue, see [Configuring an authorized scrape endpoint](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#endpoint-authorization).

### Quota exceeded

If you see the following error, then you have exceeded your ingestion quota for the Cloud Monitoring API:

  * "429: Quota exceeded for quota metric 'Time series ingestion requests' and limit 'Time series ingestion requests per minute' of service 'monitoring.googleapis.com' for consumer 'project_number:PROJECT_NUMBER'., rateLimitExceeded"



This error is most commonly seen when first bringing up the managed service. The default quota exhausts at 100,000 samples per second ingested.

To resolve this issue, submit a request to increase your ingestion quota for the Monitoring API. For assistance, contact [Google Cloud Support](https://docs.cloud.google.com/support). For more information about quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

### Missing permission on the node's default service account

If you see one of the following errors, then the default service account on the node might be missing permissions:

  * "execute query: Error querying Prometheus: client_error: client error: 403"
  * "Readiness probe failed: HTTP probe failed with statuscode: 503"
  * "Error querying Prometheus instance"



Managed collection and the managed rule evaluator in Managed Service for Prometheus both use the default service account on the node. This account is created with all the necessary permissions, but customers sometimes manually remove the Monitoring permissions. This removal causes collection and rule evaluation to fail.

To verify the permissions of the service account, do one of the following:

  * Identify the underlying Compute Engine node name, and then run the following command:
        
        gcloud compute instances describe NODE_NAME --format="json" | jq .serviceAccounts
        

Look for the string `https://www.googleapis.com/auth/monitoring`. If necessary, add Monitoring as described in Misconfigured service account.

  * Navigate to the underlying VM in the cluster and check the configuration of the node's service account:

    1. In the Google Cloud console, go to the **Kubernetes clusters** page: 

[Go to **Kubernetes clusters**](https://console.cloud.google.com/kubernetes/list)

If you use the search bar to find this page, then select the result whose subheading is **Kubernetes Engine**.

    2. Select **Nodes** , then click on the name of the node in the **Nodes** table.

    3. Click **Details**.

    4. Click the **VM Instance** link.

    5. Locate the **API and identity management** pane, and click **Show details**.

    6. Look for **Stackdriver Monitoring API** with full access.




It's also possible that the data source syncer or the Prometheus UI has been configured to look at the wrong project. For information about verifying that you are querying the intended metrics scope, see [Change the queried project](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#query-project-id).

### Misconfigured service account

If you see one of the following error messages, then the service account used by the collector does not have the correct permissions:

  * "code = PermissionDenied desc = Permission monitoring.timeSeries.create denied (or the resource may not exist)"
  * "google: could not find default credentials. See https://developers.google.com/accounts/docs/application-default-credentials for more information."



To verify that your service account has the correct permissions, do the following:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Identify the service account name in the list of principals. Verify that the name of the service account is correctly spelled. Then click _edit_ **Edit**.

  3. Select the **Role** field, then click **Currently used** and search for the Monitoring Metric Writer or the Monitoring Editor role. If the service account doesn't have one of these roles, then grant the service account the role [Monitoring Metric Writer (`roles/monitoring.metricWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter).




If you are running on non-GKE Kubernetes, then you must explicitly pass credentials to both the collector and the rule evaluator. You must repeat the credentials in both the `rules` and `collection` sections. For more information, see [Provide credentials explicitly](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#explicit-credentials) (for collection) or [Provide credentials explicitly](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged#explicit-credentials) (for rules).

Service accounts are often scoped to a single Google Cloud project. Using one service account to write metric data for multiple projects — for example, when one managed rule evaluator is querying a multi-project metrics scope — can cause this permission error. If you are using the default service account, consider configuring a dedicated service account so that you can safely add the `monitoring.timeSeries.create` permission for several projects. If you can't grant this permission, then you can use metric relabeling to rewrite the `project_id` label to another name. The project ID then defaults to the Google Cloud project in which your Prometheus server or rule evaluator is running.

### Invalid scrape configuration

If you see the following error, then your PodMonitoring or ClusterPodMonitoring is improperly formed:

  * "Internal error occurred: failed calling webhook "validate.podmonitorings.gmp-operator.gmp-system.monitoring.googleapis.com": Post "https://gmp-operator.gmp-system.svc:443/validate/monitoring.googleapis.com/v1/podmonitorings?timeout=10s": EOF""



To solve this, make sure your custom resource is properly formed [according to the specification](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#podmonitoring).

### Metric paths with HTTP query parameters aren't scraped

You are trying to send a metric by using a `path` field that includes query parameters to Managed Service for Prometheus, but the metric isn't scraped. For example, your scrape configuration might include the following:
    
    
        path: /metrics/detailed?family=queue_metrics&family=queue_consumer_count
    

The reason the metric isn't scraped is that [Prometheus URL-encodes the question-mark (`?`) character as `%3F`](https://stackoverflow.com/questions/40172415/question-mark-in-prometheus-metrics-path-gets-encoded), so the data is sent to `/metrics/detailed%3Ffamily=queue_metrics&family=queue_consumer_count` instead.

To fix this problem, use the `params` field. For example, if the metric is `/metrics/detailed?family=queue_metrics&family=queue_consumer_count`, then set up the scrape configuration as follows:
    
    
        path: /metrics/detailed
        params:
          family: ['queue_metrics', 'queue_consumer_count']
    

### Admission webhook unable to parse or invalid HTTP client config

On versions of Managed Service for Prometheus earlier than 0.12, you might see an error similar to the following, which is related to secret injection in the non-default namespace:

  * "admission webhook "validate.podmonitorings.gmp-operator.gmp-system.monitoring.googleapis.com" denied the request: invalid definition for endpoint with index 0: unable to parse or invalid Prometheus HTTP client config: must use namespace "my-custom-namespace", got: "default""



To solve this issue, upgrade to version 0.12 or later.

### Problems with scrape intervals and timeouts

When using Managed Service for Prometheus, the scrape timeout can't be greater than the scrape interval. To check your logs for this problem, run the following command:
    
    
    kubectl -n gmp-system logs ds/collector prometheus
    

On GKE Autopilot clusters, run the following command:
    
    
    kubectl -n gke-gmp-system logs ds/collector prometheus
    

Look for this message:

  * "scrape timeout greater than scrape interval for scrape config with job name "PodMonitoring/gmp-system/example-app/go-metrics""



To resolve this issue, set the value of the scrape interval equal to or greater than the value of the scrape timeout.

### Missing TYPE on metric

If you see the following error, then the metric is missing type information:

  * "no metadata found for metric name "{metric_name}""



To verify that missing type information is the problem, check the `/metrics` output of the exporting application. If there is no line like the following, then the type information is missing:

`# TYPE {metric_name} <type>`

Certain libraries, such as [those from VictoriaMetrics older than version 1.28.0](https://github.com/VictoriaMetrics/metrics), intentionally drop the type information. These libraries are not supported by Managed Service for Prometheus.

### Time-series collisions

If you see one of the following errors, you might have more than one collector attempting to write to the same time series:

  * "One or more TimeSeries could not be written: One or more points were written more frequently than the maximum sampling period configured for the metric."
  * "One or more TimeSeries could not be written: Points must be written in order. One or more of the points specified had an older end time than the most recent point."



The most common causes and solutions follow:

  * Using high-availability pairs. Managed Service for Prometheus does not support traditional high-availability collection. Using this configuration can create multiple collectors that try to write data to the same time series, causing this error.

To resolve the problem, disable the duplicate collectors by reducing the replica count to 1, or use the [supported high-availability method](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#ha-collection).

  * Using relabeling rules, particularly those that operate on jobs or instances. Managed Service for Prometheus partially identifies a unique time series by the combination of {`project_id`, `location`, `cluster`, `namespace`, `job`, `instance`} labels. Using a relabeling rule to drop these labels, especially the `job` and `instance` labels, can frequently cause collisions. Rewriting these labels is not recommended.

To resolve the problem, delete the rule that is causing it; this can be often done by [`metricRelabeling` rule](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#filter-metrics) that uses the `labeldrop` action. You can identify the problematic rule by commenting out all the relabeling rules and then reinstating them, one at a time, until the error recurs.




A less common cause of time-series collisions is using a scrape interval shorter than 5 seconds. The minimum scrape interval supported by Managed Service for Prometheus is 5 seconds.

### Exceeding the limit on the number of labels

If you see the following error, then you might have too many labels defined for one of your metrics:

  * "One or more TimeSeries could not be written: The new labels would cause the metric `prometheus.googleapis.com/METRIC_NAME` to have over PER_PROJECT_LIMIT labels".



This error usually occurs when you rapidly change the definition of the metric so that one metric name effectively has multiple independent sets of label keys over the whole lifetime of your metric. The Cloud Monitoring imposes a limit on number of labels for each metric; for more information see the limits for [user-defined metrics](https://docs.cloud.google.com/monitoring/quotas#custom_metrics_quotas).

**Note:** The number of labels (also called _label names_ , _label keys_ , or _dimensions_) is different than cardinality. [Cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality) refers to the number of combinations of unique label values across all labels.

There are three steps to resolve this problem:

  1. Identify why a given metric has too many or frequently changing labels.

     * You can use the APIs Explorer widget on the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) page to call the method. For more information, see APIs Explorer. For examples, see [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics).
  2. Address the source of the problem, which might involve adjusting your PodMonitoring's relabeling rules, changing the exporter, or fixing your instrumentation.

  3. Delete the metric descriptor for this metric (which incurs data loss), so it can be recreated with a smaller, more stable set of labels. You can use the [`metricDescriptors.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete) method to do so.




The most common sources of the problem are:

  * Collecting metrics from exporters or applications that attach dynamic labels on metrics. For example, self-deployed cAdvisor with additional [container labels and environment variables](https://github.com/google/cadvisor/blob/master/docs/runtime_options.md) or the DataDog agent, which injects dynamic annotations.

To resolve this, you can use a [`metricRelabeling` section](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#filter-metrics) on the PodMonitoring to either keep or drop labels. Some applications and exporters also allow configuration that changes exported metrics. For example, cAdvisor has a number of advanced runtime settings that can dynamically add labels. When using managed collection, we recommend using the built-in [automatic kubelet](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor) collection.

  * Using relabeling rules, particularly those that attach label names dynamically, which can cause an unexpected number of labels.

To resolve the problem, delete the rule entry that is causing it.




### Rate limits on creating and updating metrics and labels

If you see the following error, then you have hit the per-minute rate limit on creating new metrics and adding new metric labels to existing metrics:

  * "Request throttled. You have hit the per-project limit on metric definition or label definition changes per minute."



This rate limit is usually only hit when first integrating with Managed Service for Prometheus, for example when you migrate an existing, mature Prometheus deployment to use self-deployed collection. **This is not a rate limit on ingesting data points**. This rate limit only applies when creating never-before-seen metrics or when adding new labels to existing metrics.

This quota is fixed, but any issues should automatically resolve as new metrics and metric labels get created up to the per-minute limit.

### Limits on the number of metric descriptors

If you see the following error, then you have hit the quota limit for the [number of metric descriptors within a single Google Cloud project](https://docs.cloud.google.com/monitoring/quotas#custom_metrics_quotas):

  * "Your metric descriptor quota has been exhausted."



By default, this limit is set to 25,000. Although this quota can be lifted by request if your metrics are well-formed, it is far more likely that you hit this limit because you are ingesting malformed metric names into the system.

Prometheus has a [dimensional data model](https://prometheus.io/docs/concepts/data_model/) where information such as cluster or namespace name should get encoded as a [label value](https://prometheus.io/docs/practices/naming/). When dimensional information is instead embedded in the metric name itself, then the number of metric descriptors increases indefinitely. In addition, because in this scenario labels are not properly used, it becomes much more difficult to query and aggregate data across clusters, namespaces, or services.

Neither Cloud Monitoring nor Managed Service for Prometheus supports non-dimensional metrics, such as those formatted for StatsD or Graphite. While most Prometheus exporters are configured correctly out-of-the-box, certain exporters, such as the StatsD exporter, the Vault exporter, or the Envoy Proxy that comes with Istio, must be explicitly configured to use labels instead of embedding information in the metric name. Examples of malformed metric names include:

  * `request_path_____path_to_a_resource____istio_request_duration_milliseconds`
  * `envoy_cluster_grpc_method_name_failure`
  * `envoy_cluster_clustername_upstream_cx_connect_ms_bucket`
  * `vault_rollback_attempt_path_name_1700683024`
  * `service__________________________________________latency_bucket`



To confirm this issue, do the following:

  1. Within Google Cloud console, select the Google Cloud project that is linked to the error.
  2. In the Google Cloud console, go to the  query_stats **Metrics management** page: 

[Go to **Metrics management**](https://console.cloud.google.com/monitoring/metrics-management)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. Confirm that the sum of Active plus Inactive metrics is over 25,000. In most situations, you should see a large number of Inactive metrics.
  4. Select "Inactive" in the Quick Filters panel, page through the list, and look for patterns.
  5. Select "Active" in the Quick Filters panel, sort by **Samples billable volume** descending, page through the list, and look for patterns.
  6. Sort by **Samples billable volume** ascending, page through the list, and look for patterns.



Alternatively, you can confirm this issue by using Metrics Explorer:

  1. Within Google Cloud console, select the Google Cloud project that is linked to the error.
  2. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the query builder, click select a metric, then clear the "Active" checkbox.
  4. Type "prometheus" into the search bar.
  5. Look for any patterns in the names of metrics.



Once you have identified the patterns that indicate malformed metrics, you can mitigate the issue by fixing the exporter at the source and then deleting the offending metric descriptors.

To prevent this issue from happening again, you must first configure the relevant exporter to no longer emit malformed metrics. We recommend consulting the documentation for your exporter for help. You can confirm you have fixed the problem by manually visiting the `/metrics` endpoint and inspecting the exported metric names.

You can then free up your quota by deleting the malformed metrics using the [`projects.metricDescriptors.delete` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete). To more easily iterate through the list of malformed metrics, we provide [a Golang script](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/examples/scripts/delete_metric_descriptors/delete_metric_descriptors.go) you can use. This script accepts a regular expression that can identify your malformed metrics and deletes any metric descriptors that match the pattern. **As metric deletion is irreversible, we strongly recommend first running the script using dry run mode.**

### Some metrics are missing for short-running targets

Google Cloud Managed Service for Prometheus is deployed and there are no configuration errors; however, some metrics are missing.

Determine the deployment that generates the partially missing metrics. If the deployment is a Google Kubernetes Engine' CronJob, then determine how long the job typically runs:

  1. Find the cron job deployment yaml file and find the status, which is list at the end of the file. The status in this example shows that the job ran for one minute:
         
         status:
             lastScheduleTime: "2024-04-03T16:20:00Z"
             lastSuccessfulTime: "2024-04-03T16:21:07Z"
         

  2. If the run time is less than five minutes, then the job isn't running long enough for the metric data to be consistently scraped.

To resolve this situation, try the following:

     * Configure the job to ensure that it doesn't exit until at least five minutes have elapsed since the job started.

     * Configure the job to detect whether metrics have been scraped before exiting. This capability requires library support.

     * Consider creating a log based distribution-valued metric instead of collecting metric data. This approach is suggested when data is published at a low rate. For more information, see [Log-based metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/logs-based-metrics#lbm-defn).

  3. If the run time is longer than five minutes or if it is inconsistent, then see the Unhealthy targets section of this document.




### Problems with collection from exporters

If your metrics from an exporter are not being ingested, check the following:

  * Verify that the exporter is working and exporting metrics by using the [`kubectl port-forward` command](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward).

For example, to check that pods with the selector `app.kubernetes.io/name=redis` in the namespace `test` are emitting metrics at the `/metrics` endpoint on port 9121, you can port-forward as follows:
        
        kubectl port-forward "$(kubectl get pods -l app.kubernetes.io/name=redis -n test -o jsonpath='{.items[0].metadata.name}')" -n test 9121
        

Access the endpoint `localhost:9121/metrics` by using the browser or `curl` in another terminal session to verify that the metrics are being exposed by the exporter for scraping.

  * Check if you can query the metrics in the Google Cloud console but not Grafana. If so, then the problem is with Grafana, not the collection of your metrics.

  * Verify that the managed collector is able to scrape the exporter by inspecting the Prometheus web interface the collector exposes.

    1. Identify the managed collector running on the same node on which your exporter is running. For example, if your exporter is running on pods in the namespace `test` and the pods are labeled with `app.kubernetes.io/name=redis`, the following command identifies the managed collector running on the same node:
           
           kubectl get pods -l app=managed-prometheus-collector --field-selector="spec.nodeName=$(kubectl get pods -l app.kubernetes.io/name=redis -n test -o jsonpath='{.items[0].spec.nodeName}')" -n gmp-system -o jsonpath='{.items[0].metadata.name}'
           

    2. Set up port-forwarding from port 19090 of the managed collector:
           
           kubectl port-forward POD_NAME -n gmp-system 19090
           

    3. Navigate to the URL `localhost:19090/targets` to access the web interface. If the exporter is listed as one of the targets, then your managed collector is successfully scraping the exporter.




### Collector Out Of Memory (OOM) errors

If you are using managed collection and encountering Out Of Memory (OOM) errors on your collectors, then consider [enabling vertical pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#vpa).

### Operator Out Of Memory (OOM) errors

If you are using managed collection and encountering Out Of Memory (OOM) errors on your operator, then consider [disabling target status feature](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#target-status). The target status feature can cause operator performance issues in larger clusters.

### Too many time series or increased 503 responses and context deadline exceeded errors, especially during peak load

You might be encountering this issue if you see the following error message:

  * "Monitored resource (abcdefg) has too many time series (prometheus metrics)"



"Context deadline exceeded" is a generic 503 error returned from Monarch for any ingestion-side problem that doesn't have a specific cause. A very small number of "context deadline exceeded" errors is expected with normal use of the system.

However, you might notice a pattern where "context deadline exceeded" errors increase and materially impact your data ingestion. One potential root cause is that you might be incorrectly setting target labels. This is more likely if the following are true:

  * Your "Context deadline exceeded" errors have a cyclical pattern, where they increase during either times of high load for you or times of high load for the Google Cloud region specified by your `location` label.
  * You see more errors as you onboard more metric volume to the service.
  * You are using the [`statsd_exporter` for Prometheus](https://github.com/prometheus/statsd_exporter), Envoy for Istio, the SNMP exporter, the Prometheus Pushgateway, kube-state-metrics, or you otherwise have a similar exporter that intermediates and reports metrics on behalf of other resources running in your environment. The problem only happens for metrics emitted by this type of exporter.
  * You notice that your affected metrics tend to have the string `localhost` in the value for the `instance` label, or there are very few values for the `instance` label.
  * If you have access to the in-cluster Prometheus collector query UI, you can see that the metrics are being collected successfully.



If these points are true, it's likely that your exporter has misconfigured the [resource labels](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#reserved-labels) in a way that conflicts with Monarch's requirements.

Monarch scales by storing related data together in a target. A target for Managed Service for Prometheus is defined by the [`prometheus_target`](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target) resource type and the `project_id`, `location`, `cluster`, `namespace`, `job`, and `instance` labels. For more information about these labels and defaulting behavior, see [Reserved labels in Managed Collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#reserved-labels) or [Reserved labels in Self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#reserved-labels).

Of these labels, `instance` is the lowest-level target field and is therefore most important to get right. Efficiently storing and querying metrics in Monarch requires relatively small, diverse targets, ideally around the size of a typical VM or a container. When running Managed Service for Prometheus in typical scenarios, the [open-source default behavior built into the collector](https://prometheus.io/docs/concepts/jobs_instances/) usually picks good values for the `job` and `instance` labels, which is why this topic is not covered elsewhere in the documentation.

However, the default logic might fail when you are running an exporter that reports metrics on behalf of other resources in your cluster, such as the statsd_exporter. Instead of setting the value of `instance` to the IP:port of the resource that emits the metric, the value of `instance` gets set to **the IP:port of the statsd_exporter itself**. The issue can be compounded by the `job` label, as instead of relating to the metric package or service, it also lacks diversity by being set to `statsd-exporter`.

When this happens, all metrics that come from this exporter within a given cluster and namespace get written into the same Monarch target. As this target gets larger, writes begin failing, and you see increased "Context deadline exceeded" 503 errors.

You can get verification that this is happening to you by contacting Cloud Customer Care and asking them to check the "Monarch Quarantiner hospitalization logs". Include any known values for the six reserved labels in your ticket. Make sure to report the Google Cloud project that is sending the data, not the Google Cloud project of your metrics scope.

To fix this issue, you have to change your collection pipeline to use more diverse target labels. Some potential strategies, listed in order of effectiveness, include:

  * Instead of running a central exporter that reports metrics on behalf of all VMs or nodes, run a separate exporter for each VM as a node agent or by deploying the exporter as a Kubernetes Daemonset. To avoid setting the `instance` label to `localhost`, don't run the exporter on the same node as your collector. 
    * If, after sharding the exporter, you still need more target diversity, run multiple exporters on each VM and logically assign different sets of metrics to each exporter. Then, instead of discovering the job using the static name `statsd-exporter`, use a different job name for each logical set of metrics. Instances with different values for `job` get assigned to different targets in Monarch.
    * If you're using kube-state-metrics, use the [built-in horizontal sharding](https://github.com/kubernetes/kube-state-metrics?tab=readme-ov-file#horizontal-sharding) to create more target diversity. Other exporters might have similar capabilities.
  * If you're using OpenTelemetry or self-deployed collection, use a relabeling rule to change the value of `instance` from the IP:Port or name of the exporter to the IP:Port or unique name of the resource that is generating the metrics. It's very likely that you are already capturing the IP:Port or name of the originating resource as a metrics label. You also have to set the `honor_labels` field to `true` in your Prometheus or OpenTelemetry configuration.
  * If you're using OpenTelemetry or self-deployed collection, use a relabeling rule with a hashmod function to run multiple scrape jobs against the same exporter and ensure that a different instance label is chosen for each scrape configuration.



### Duplicate buckets within a histogram point

You might be encountering this issue if you see the following error message:

  * "Field points[0].distributionValue had an invalid value: Distribution |explicit_buckets.bounds| entry 1 has a value of 1 which is less than the value of entry 0 which is 1"



This is caused by having two histogram points within your exporter that have the exact same set of labels. This could happen for the following reasons:

  * You drop labels in your exporter before scraping.
  * You have an exporter that fills in a label with a default value if it can't be detected, such as "unknown" for a source IP that can't be sniffed.



Prometheus spec allows out-of-order time series within a /metrics endpoint. The collector scrapes out-of-order time series, re-orders them, merges them into a single metric based on the labels, and sends the point.

When there are histograms with duplicative labels in a single /metrics endpoint, the resulting merged histogram ends up with two buckets that have the same `le` value. This error is retuned by the API because bucket `le` values must be unique and in increasing order.

To fix this, make sure that all histogram points have a unique set of labels in your exporter.

### No errors and no metrics

If you are using managed collection, you don't see any errors, but data is not appearing in Cloud Monitoring, then the most likely cause is that your metric exporters or scrape configurations are not configured correctly. Managed Service for Prometheus does not send any time series data unless you first apply a valid scrape configuration.

To identify whether this is the cause, try [deploying the example application and example PodMonitoring resource](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#deploy-app). If you now see the `up` metric (it may take a few minutes), then the problem is with your scrape configuration or exporter.

The root cause could be any number of things. We recommend checking the following:

  * Your PodMonitoring references a valid port.

  * Your exporter's Deployment spec has properly named ports.

  * Your selectors (most commonly `app`) match on your Deployment and PodMonitoring resources.

  * You can see data at your expected endpoint and port by manually visiting it.

  * You have installed your PodMonitoring resource in the same namespace as the application you wish to scrape. Do not install any custom resources or applications in the `gmp-system` or `gke-gmp-system` namespace.

  * Your metric and label names match Prometheus' [validating regular expression](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). Managed Service for Prometheus does not support label names that start with the `_` character.

  * You are not using a set of filters that causes all data to be filtered out. Take extra care that you don't have conflicting filters when using a [`collection` filter in the `OperatorConfig` resource](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor).

  * If running outside of Google Cloud, `project` or `project-id` is set to a valid Google Cloud project and `location` is set to a valid Google Cloud region. You can't use `global` as a value for `location`.

  * Your metric is one of [the four Prometheus metric types](https://prometheus.io/docs/concepts/metric_types). Some libraries like [Kube State Metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics) expose [OpenMetrics metric types](https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md#metric-types) like Info, Stateset and GaugeHistogram, but these metric types are not supported by Managed Service for Prometheus and are silently dropped.




## Firewalls

A firewall can cause both ingestion and query problems. Your firewall must be configured to permit both `POST` and `GET` requests to the Monitoring API service, `monitoring.googleapis.com`, to allow ingestion and queries.

## Error about concurrent edits

The error message "Too many concurrent edits to the project configuration" is usually transient, resolving after a few minutes. It is usually caused by removing a relabeling rule that affects many different metrics. The removal causes the formation of a queue of updates to the metric descriptors in your project. The error goes away when the queue is processed.

For more information, see [Limits on creating and updating metrics and labels](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#descriptor_limits).

## Queries blocked and cancelled by Monarch

If you see the following error, then you have hit the internal limit for the number of concurrent queries that can be run for any given project:

  * "internal: expanding series: generic::aborted: invalid status monarch::220: Cancelled due to the number of queries whose evaluation is blocked waiting for memory is 501, which is equal to or greater than the limit of 500."



To protect against abuse, the system enforces a hard limit on the number of queries from one project that can run concurrently within Monarch. With typical Prometheus usage, queries should be quick and this limit should never be reached.

You might hit this limit if you are issuing a lot of concurrent queries that run for a longer-than-expected time. Queries requesting more than 25 hours of data are usually slower to execute than queries requesting less than 25 hours of data, and the longer the query lookback, the slower the query is expected to be.

Typically this issue is triggered by running lots of long-lookback rules in an inefficient way. For example, you might have many rules that run once every minute and request a 4-week rate. If each of these rules takes a long time to run, it might eventually cause a backup of queries waiting to run for your project, which then causes Monarch to throttle queries.

To resolve this issue, you need to increase the evaluation interval of your long-lookback rules so that they're not running every 1 minute. Running a query for a 4-week rate every 1 minute is unnecessary; there are 40,320 minutes in 4 weeks, so each minute gives you almost no additional signal (your data changes at most by 1/40,320th). Using a 1 hour evaluation interval should be sufficient for a query that requests a 4-week rate.

Once you resolve the bottleneck caused by inefficient long-running queries executing too frequently, this issue should resolve itself.

## Incompatible value types

If you see the following error upon ingestion or query, then you have a value type incompatibility in your metrics:

  * "Value type for metric prometheus.googleapis.com/metric_name/gauge must be INT64, but is DOUBLE"
  * "Value type for metric prometheus.googleapis.com/metric_name/gauge must be DOUBLE, but is INT64"
  * "One or more TimeSeries could not be written: Value type for metric prometheus.googleapis.com/target_info/gauge conflicts with the existing value type (INT64)"



You might see this error upon ingestion, as Monarch does not support writing DOUBLE-typed data to INT64-typed metrics nor does it support writing INT64-typed data to DOUBLE-typed metrics. You also might see this error when querying using a multi-project metrics scope, as Monarch cannot union DOUBLE-typed metrics in one project with INT64-typed metrics in another project.

This error only happens when you have OpenTelemetry collectors reporting data, and it is more likely to happen if you have both OpenTelemetry (using the `googlemanagedprometheus` exporter) and Prometheus reporting data for the same metric as commonly happens for the `target_info` metric.

The cause is likely one of the following:

  * You are collecting OTLP metrics, and the OTLP metric library changed its value type from DOUBLE to INT64, as happened with OpenTelemetry's Java metrics. The new version of the metric library is now incompatible with the metric value type created by the old version of the metric library.
  * You are collecting the `target_info` metric using both Prometheus and OpenTelemetry. Prometheus collects this metric as a DOUBLE, while OpenTelemetry collects this metric as an INT64. Your collectors are now writing two value types to the same metric in the same project, and only the collector that first created the metric descriptor is succeeding.
  * You are collecting `target_info` using OpenTelemetry as an INT64 in one project, and you are collecting `target_info` using Prometheus as a DOUBLE in another project. Adding both metrics to the same metrics scope, then querying that metric through the metrics scope, causes an invalid union between incompatible metric value types.



This problem can be solved by forcing all metric value types to DOUBLE by doing the following:

  1. Reconfigure your OpenTelemetry collectors to force all metrics to be a DOUBLE by enabling the [feature-gate `exporter.googlemanagedprometheus.intToDouble` flag](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/googlemanagedprometheusexporter/README.md#feature-gates).
  2. [Delete all INT64 metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete) and let them get recreated as a DOUBLE. You can use the [`delete_metric_descriptors.go` script](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/examples/scripts/delete_metric_descriptors/delete_metric_descriptors.go) to automate this.



**Following these steps deletes all data that is stored as an INT64 metric.** There is no alternative to deleting the INT64 metrics that fully solves this problem.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
