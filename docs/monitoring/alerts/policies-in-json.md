---
url: https://docs.cloud.google.com/monitoring/alerts/policies-in-json/
title: Sample policies in JSON \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:43.737470+00:00
---

# Sample policies in JSON  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/policies-in-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Sample policies in JSON Stay organized with collections  Save and categorize content based on your preferences. 

This document provides samples of alerting policies. The samples are written in JSON, and they use [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters). You can create policies in either JSON or YAML, regardless of whether you define the policy by using Monitoring filters or Prometheus Query Language (PromQL). Google Cloud CLI can read and write both JSON and YAML, while the REST API can read JSON.

To learn about alerting policies that use PromQL, see the following documents:

  * [PromQL-based alerting policies](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting)
  * [Use PromQL to create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-promql)



For information about how to configure alerting policy fields, see the following:

  * [Create metric-based alerting policies by using the Google Cloud console](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui)
  * [Create metric-based alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api)



## Generate YAML for existing policies

To generate YAML representations of your existing alerting policies, use the [`gcloud monitoring policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/list) command to list your policies and the [`gcloud monitoring policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/describe) command to print the policy.

To generate YAML representations of your existing notification channels, use the [`gcloud monitoring channels list`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/channels/list) command to list your channels and the [`gcloud monitoring channels describe`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/channels/describe) command to print the channel configuration.

If you don't include the `--format` flag in the Google Cloud CLI commands, then, the format defaults to YAML for both `gcloud ... describe` commands.

For example, the following `gcloud monitoring policies describe` command retrieves a single policy named `projects/a-gcp-project/alertPolicies/12669073143329903307` and the redirect (`>`) copies the output to the `test-policy.yaml` file:
    
    
    gcloud monitoring policies describe projects/a-gcp-project/alertPolicies/12669073143329903307 > test-policy.yaml
    

## Generate JSON for existing policies

To generate JSON representations of your existing alerting policies and notification channels, do any of the following:

  * Add the `--format=json` flag to the `gcloud` CLI commands described in [Generate YAML for existing policies](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#generate_yaml_for_existing_policies). For example, to list policies, run the following command:
        
        gcloud monitoring policies list --format=json
        

  * Use the APIs Explorer widget on the reference page for each API method:

    * For alerting policies, see the [`alertPolicies.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list) and [`alertPolicies.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/get) methods.

    * For notification channels, see the [`notificationChannels.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list) and [`notificationChannels.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get) methods.

For more information, see [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer).




## Policy samples

As shown in the [backup/restore example](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api#api-example), you can use saved policies to create new copies of those policies.

You can use a policy saved in one project to create a new, or similar, policy in another project. However, you must first make the following changes in a copy of the saved policy:

  * Remove the following fields from any notification channels: 
    * `name`
    * `verificationStatus`
  * Create notification channels before referring to the channels in alerting policies (you need the new channel identifiers).
  * Remove the following fields from any alerting policies you are recreating: 
    * `name`
    * `condition.name`
    * `creationRecord`
    * `mutationRecord`



The policies in this document are organized using the same terminology that Monitoring in the Google Cloud console uses, for example, “rate-of-change policy”, and there are two types of conditions:

  * A threshold condition; almost all of the policy types mentioned in the UI are variants of a threshold condition
  * An absence condition



In the samples that follow, these conditions correspond to `conditionThreshold` and `conditionAbsent`. For more information, see the reference page for [`Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition).

You can create many of these policies manually, by using the Google Cloud console, but some can be created only by using the Monitoring API. For more information, see [Creating an alerting policy (UI)][alert-ui] or [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api).

### Metric-threshold policy

A metric-threshold policy detects when some value crosses a predetermined boundary. Threshold policies let you know that something is approaching an important point, so you can take some action. For example, the condition for a metric-threshold policy is met when available disk space becomes less than 10 percent of total disk space.

The following alerting policy uses the average CPU usage as an indicator of the health of a group of VMs. The policy's condition is met when the average CPU utilization of the VMs in a project, measured over 60-second intervals, exceeds a threshold of 90-percent utilization for 15 minutes (900 seconds):
    
    
    {
        "displayName": "Very high CPU usage",
        "combiner": "OR",
        "conditions": [
            {
                "displayName": "CPU usage is extremely high",
                "conditionThreshold": {
                    "aggregations": [
                        {
                            "alignmentPeriod": "60s",
                            "crossSeriesReducer": "REDUCE_MEAN",
                            "groupByFields": [
                                "project"
                            ],
                            "perSeriesAligner": "ALIGN_MAX"
                        }
                    ],
                    "comparison": "COMPARISON_GT",
                    "duration": "900s",
                    "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\"
                              AND resource.type=\"gce_instance\"",
                    "thresholdValue": 0.9,
                    "trigger": {
                        "count": 1
                    }
                }
            }
        ],
    }
    

### Metric-absence policy

A [metric-absence](https://docs.cloud.google.com/monitoring/alerts/metric-absence) condition is met when no data is written to a metric within the time range defined by the [`duration`](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration) field.

**Note:** Cloud Monitoring doesn't generate an alert and send a notification for a metric-absence condition if the monitored resource is deleted or shut down.

One way to demonstrate this is to create a custom metric.

Here's a sample descriptor for a custom metric. You could create the metric using the APIs Explorer.
    
    
    {
      "description": "Number of times the pipeline has run",
      "displayName": "Pipeline runs",
      "metricKind": "GAUGE",
      "type": "custom.googleapis.com/pipeline_runs",
      "labels": [
        {
          "description": "The name of the pipeline",
          "key": "pipeline_name",
          "valueType": "STRING"
        },
      ],
      "unit": "1",
      "valueType": "INT64"
    }
    

See [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics) for more information.

The condition in the following alerting policy is met when data stops being written to the metric for a period of approximately an hour: in other words, your hourly pipeline has failed to run. Note that the condition used here is `conditionAbsent`.
    
    
    {
        "displayName": "Data ingestion functioning",
        "combiner": "OR",
        "conditions": [
            {
                "displayName": "Hourly pipeline is up",
                "conditionAbsent": {
                    "duration": "3900s",
                    "filter": "resource.type=\"global\"
                              AND metric.type=\"custom.googleapis.com/pipeline_runs\"
                              AND metric.label.pipeline_name=\"hourly\"",
                }
            }
        ],
    }
    

### Forecast policy

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A [forecast condition](https://docs.cloud.google.com/monitoring/alerts/metric-forecast) is met when the following occur:

  * All forecasts for a time series are the same within the time range defined by the `duration` field.
  * Cloud Monitoring forecasts that the time series will violate the threshold within the forecast horizon.



A forecast condition is a metric-threshold condition that is configured to use forecasting. As illustrated in the following sample, these conditions include a `forecastOptions` field that enable forecasting and specify the forecast horizon. In the following sample, the forecast horizon is set to one hour, which is the minimum value:
    
    
    {
        "displayName": "NFS free bytes alert",
        "combiner": "OR",
        "conditions": [
          {
            "displayName": "Filestore Instance - Free disk space percent",
            "conditionThreshold": {
              "aggregations": [
                {
                  "alignmentPeriod": "300s",
                  "perSeriesAligner": "ALIGN_MEAN"
                }
              ],
              "comparison": "COMPARISON_LT",
              "duration": "900s",
              "filter": "resource.type = \"filestore_instance\" AND metric.type = \"file.googleapis.com/nfs/server/free_bytes_percent\"",
              "forecastOptions": {
                "forecastHorizon": "3600s"
              },
              "thresholdValue": 20,
              "trigger": {
                "count": 1
              }
            }
          }
        ],
    }
    

### Rate-of-change policy

Rate-of-change conditions are met when the values in a time series increase, or decrease, by at least the percentage specified by the threshold. When you create this type of condition, a percent-of-change computation is applied to the time series before comparison to the threshold.

The condition averages the values of the metric from the past 10 minutes, then compares the result with the 10-minute average that was measured just before the alignment period began. You can't change the 10-minute window used for comparisons in a rate-of-change alerting policy. However, you do specify the alignment period when you create the condition.

This alerting policy monitors whether CPU utilization is increasing rapidly:
    
    
    {
      "displayName": "High CPU rate of change",
      "combiner": "OR",
      "conditions": [
        {
          "displayName": "CPU usage is increasing at a high rate",
          "conditionThreshold": {
             "aggregations": [
               {
                 "alignmentPeriod": "900s",
                 "perSeriesAligner": "ALIGN_PERCENT_CHANGE",
               }],
            "comparison": "COMPARISON_GT",
            "duration": "180s",
            "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\" AND resource.type=\"gce_instance\"",
            "thresholdValue": 0.5,
            "trigger": {
              "count": 1
             }
          }
        }
      ],
    }
    

### Group-aggregate policy

This alerting policy monitors whether the average CPU utilization across a Google Kubernetes Engine cluster exceeds a threshold:
    
    
    {
        "displayName": "CPU utilization across GKE cluster exceeds 10 percent",
        "combiner": "OR",
        "conditions": [
             {
                "displayName": "Group Aggregate Threshold across All Instances in Group GKE cluster",
                "conditionThreshold": {
                    "filter": "group.id=\"3691870619975147604\" AND metric.type=\"compute.googleapis.com/instance/cpu/utilization\" AND resource.type=\"gce_instance\"",
                    "comparison": "COMPARISON_GT",
                    "thresholdValue": 0.1,
                    "duration": "300s",
                    "trigger": {
                        "count": 1
                    },
                    "aggregations": [
                        {
                            "alignmentPeriod": "60s",
                            "perSeriesAligner": "ALIGN_MEAN",
                            "crossSeriesReducer": "REDUCE_MEAN",
                            "groupByFields": [
                                  "project"
                            ]
                        },
                        {
                            "alignmentPeriod": "60s",
                            "perSeriesAligner": "ALIGN_SUM",
                            "crossSeriesReducer": "REDUCE_MEAN"
                        }
                    ]
                },
            }
        ],
    }
    

This policy assumes the existence of the following group:
    
    
        {
            "name": "projects/a-gcp-project/groups/3691870619975147604",
            "displayName": "GKE cluster",
            "filter": "resource.metadata.name=starts_with(\"gke-kuber-cluster-default-pool-6fe301a0-\")"
        }
    

To identify the equivalent fields for your groups, list your group details using the APIs Explorer on the [project.groups.list reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/list).

### Uptime-check policy

The status of uptime checks appears on the **Uptime checks** page, but you can configure an alerting policy so that Cloud Monitoring sends you a notification if the uptime check fails.

For example, the following JSON describes an HTTPS uptime check on the Google Cloud site. The alerting policy checks the availability every 5 minutes.

The uptime check was created with the Google Cloud console. The JSON representation here was created by listing the uptime checks in the project using the Monitoring API; see [`uptimeCheckConfigs.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list). You can also create uptime checks with the Monitoring API.
    
    
    {
        "name": "projects/a-gcp-project/uptimeCheckConfigs/uptime-check-for-google-cloud-site",
        "displayName": "Uptime check for Google Cloud site",
        "monitoredResource": {
            "type": "uptime_url",
            "labels": {
                "host": "cloud.google.com"
          }
        },
        "httpCheck": {
            "path": "/index.html",
            "useSsl": true,
            "port": 443,
            "authInfo": {}
        },
        "period": "300s",
        "timeout": "10s",
        "contentMatchers": [
            {}
        ]
    }
    

To create an alerting policy for an uptime check, refer to the uptime check by its `UPTIME_CHECK_ID`. This ID is set when the check is created; it appears as the last component of the `name` field and is visible in the UI as the `Check ID` in the configuration summary. If you are using the Monitoring API, the [`uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method returns the ID.

The ID is derived from the `displayName`, which was set in the UI in this case. The can be verified by listing the uptime checks and looking at the `name` value.

The ID for the uptime check previously described is `uptime-check-for-google-cloud-site`.

The following alerting policy's condition is met if the uptime check fails or if the SSL certificate on the Google Cloud site will expire in under 15 days. If either condition is met, then Monitoring sends a notification to the specified notification channel:
    
    
    {
        "displayName": "Google Cloud site uptime failure",
        "combiner": "OR",
        "conditions": [
            {
                "displayName": "Failure of uptime check_id uptime-check-for-google-cloud-site",
                "conditionThreshold": {
                    "aggregations": [
                        {
                            "alignmentPeriod": "1200s",
                            "perSeriesAligner": "ALIGN_NEXT_OLDER",
                            "crossSeriesReducer": "REDUCE_COUNT_FALSE",
                            "groupByFields": [ "resource.label.*" ]
                        }
                    ],
                    "comparison": "COMPARISON_GT",
                    "duration": "600s",
                    "filter": "metric.type=\"monitoring.googleapis.com/uptime_check/check_passed\"
                              AND metric.label.check_id=\"uptime-check-for-google-cloud-site\"
                              AND resource.type=\"uptime_url\"",
                    "thresholdValue": 1,
                    "trigger": {
                        "count": 1
                    }
                }
            },
            {
                "displayName": "SSL Certificate for google-cloud-site expiring soon",
                "conditionThreshold": {
                    "aggregations": [
                        {
                            "alignmentPeriod": "1200s",
                            "perSeriesAligner": "ALIGN_NEXT_OLDER",
                            "crossSeriesReducer": "REDUCE_MEAN",
                            "groupByFields": [ "resource.label.*" ]
                        }
                    ],
                    "comparison": "COMPARISON_LT",
                    "duration": "600s",
                    "filter": "metric.type=\"monitoring.googleapis.com/uptime_check/time_until_ssl_cert_expires\"
                              AND metric.label.check_id=\"uptime-check-for-google-cloud-site\"
                              AND resource.type=\"uptime_url\"",
                    "thresholdValue": 15,
                    "trigger": {
                        "count": 1
                    }
                }
            }
        ],
    }
    

The filter in the condition specifies the metric that is being monitored by its type and label. The metric types are `monitoring.googleapis.com/uptime_check/check_passed` and `monitoring.googleapis.com/uptime_check/time_until_ssl_cert_expires`. The metric label identifies the specific uptime check that is being monitored. In this example, the label field `check_id` contains the uptime check ID.
    
    
    AND metric.label.check_id=\"uptime-check-for-google-cloud-site\"
    

See [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters) for more information.

### Process-health policy

A process-health policy can notify you if the number of processes that match a pattern crosses a threshold. This can be used to tell you, for example, that a process has stopped running.

This alerting policy causes Monitoring to send a notification to the specified notification channel when no process matching the string `nginx`, running as user `www`, has been available for more than 5 minutes:
    
    
    {
        "displayName": "Server health",
        "combiner": "OR",
        "conditions": [
            {
                "displayName": "Process 'nginx' is not running",
                "conditionThreshold": {
                    "filter": "select_process_count(\"has_substring(\\\"nginx\\\")\", \"www\") AND resource.type=\"gce_instance\"",
                    "comparison": "COMPARISON_LT",
                    "thresholdValue": 1,
                    "duration": "300s"
                }
            }
        ],
    }
    

**Note:** Policies that filter on the command line used to start a process can use only the first 1024 characters of the command line. Command lines longer than 1024 characters are truncated.

For more information, see [Process health](https://docs.cloud.google.com/monitoring/alerts/monitor-process-count).

### Metric ratio

We recommend that you use PromQL to create ratio-based alerting policies. Although the Cloud Monitoring API supports the construction of some filter-based ratios, PromQL provides a more flexible and robust solution:

  * For information about creating alerting policies with PromQL, see [Use PromQL to create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-promql).

  * For information about charting or monitoring ratios of metrics, see [Ratios of metrics](https://docs.cloud.google.com/monitoring/charts/metric-ratios).




This section describes a filter-based ratio. With the API, you can create and view a policy that computes the ratio of two related metrics and fires when that ratio crosses a threshold. The related metrics must have the same [`MetricKind`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind). For example, you can create a ratio-based alerting policy if both metrics are gauge metrics. To determine the `MetricKind` of a metric type, see the [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics).

**Note:** To create, view, or modify a filter-based ratio-based alerting policy, you must use the Monitoring API. You can't manage these policies by using the Google Cloud console. For more information, see [Managing alerting policies by the API][alert-api]. The **Policies** table on the **Alerting** page in the Google Cloud console displays a list of all alerting policies, including those policies created by using the API.

A ratio condition is a variant on a metric-threshold condition, where the condition in a ratio policy uses two filters: the usual `filter`, which acts as the numerator of the ratio, and a `denominatorFilter`, which acts as the denominator of the ratio.

The time series from both filters must be aggregated in the same way, so that the computation of the ratio of the values is meaningful. The condition of the alerting policy is met when the ratio of the filters violates a threshold value for the time range defined by `duration` field.

The next section describes how to configure an alerting policy that monitors the ratio of HTTP error responses to all HTTP responses.

#### Ratio of HTTP errors

The following alerting policy has a threshold condition built on the ratio of the count of HTTP error responses to the count of all HTTP responses.
    
    
    {
        "displayName": "HTTP error count exceeds 50 percent for App Engine apps",
        "combiner": "OR",
        "conditions": [
            {
                "displayName": "Ratio: HTTP 500s error-response counts / All HTTP response counts",
                "conditionThreshold": {
                     "filter": "metric.label.response_code>=\"500\" AND
                                metric.label.response_code<\"600\" AND
                                metric.type=\"appengine.googleapis.com/http/server/response_count\" AND
                                project=\"a-gcp-project\" AND
                                resource.type=\"gae_app\"",
                     "aggregations": [
                        {
                            "alignmentPeriod": "300s",
                            "crossSeriesReducer": "REDUCE_SUM",
                            "groupByFields": [
                              "project",
                              "resource.label.module_id",
                              "resource.label.version_id"
                            ],
                            "perSeriesAligner": "ALIGN_DELTA"
                        }
                    ],
                    "denominatorFilter": "metric.type=\"appengine.googleapis.com/http/server/response_count\" AND
                                          project=\"a-gcp-project\" AND
                                          resource.type=\"gae_app\"",
                    "denominatorAggregations": [
                       {
                          "alignmentPeriod": "300s",
                          "crossSeriesReducer": "REDUCE_SUM",
                          "groupByFields": [
                            "project",
                            "resource.label.module_id",
                            "resource.label.version_id"
                           ],
                          "perSeriesAligner": "ALIGN_DELTA",
                        }
                    ],
                    "comparison": "COMPARISON_GT",
                    "thresholdValue": 0.5,
                    "duration": "0s",
                    "trigger": {
                        "count": 1
                    }
                }
            }
        ]
    }
    

#### The metric and resource types

The metric type for this policy is `appengine.googleapis.com/http/server/response_count`, which has two labels:

  * `response_code`, an 64-bit integer representing the HTTP status code for the request. This policy filters time-series data on this label, so it can determine the following: 
    * The number of responses received.
    * The number of error responses received.
    * The ratio of error responses to all responses.
  * `loading`, a boolean value that indicates whether the request was loading. The `loading` label is irrelevant in this alerting policy.



The alerting policy evaluates response data from App Engine apps, that is, data originating from the monitored-resource type `gae_app`. This monitored resource has three labels:

  * `project_id`, the ID for the Google Cloud project.
  * `module_id`, the name of the service or module in the app.
  * `version_id`, the version of the app.



For reference information on these metric and monitored-resource types, see [App Engine metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-appengine) in the list of metrics and the [`gae_app` entry](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app) in the list of monitored resources.

#### What this policy does

This condition computes the ratio of error responses to total responses. The condition is met if the ratio is greater than 50% (that is, the ratio is greater than 0.5) over the 5-minute alignment period.

This policy captures the module and version of the app that violates the condition by grouping the time series in each filter by the values of those labels.

  * The filter in the condition looks at HTTP responses from an App Engine app and selects those responses in the error range, 5xx. This is the numerator in the ratio.
  * The denominator filter in the condition looks at all HTTP responses from an App Engine app.



The condition is met and Monitoring sends a notification for the new alert immediately; the permitted time range of the `duration` field in the condition is zero seconds. This condition uses a `trigger` count of one, which is the number of time series that needs to violate the condition to cause the alert. For an App Engine app with a single service, a `trigger` count of one is fine. If you have an app with 20 services and you want to cause an alert if 3 or more services violate the condition, then use a `trigger` count of 3.

#### Setting up a ratio

The numerator and denominator filters are exactly the same except that the condition filter in the numerator matches response codes in the error range, and the condition filter in the denominator matches all response codes. The following clauses appear only in the numerator condition:
    
    
          metric.label.response_code>=\"500\" AND
          metric.label.response_code<\"600\"
    

Otherwise, the numerator and denominator filters are the same.

The time series selected by each filter must be aggregated in the same way to make the computation of the ratio valid. Each filter might collect multiple time series, since there will be a different time series for each combination of values for labels. This policy groups the set of time series by specified resource labels, which partitions the set of time series into a set of groups. Some of the time series in each group match the numerator filter; the rest match the denominator filter.

To compute a ratio, the set of time series that matches each filter must be aggregated down to a single time series each. This leaves each group with two time series, one for the numerator and one for the denominator. Next, the ratio of points in the numerator and denominator time series in each group can be computed.

In this policy, the time series for both filters are aggregated as follows:

  * Each filter creates a number of time series aligned at 5-minute intervals, with values represented computing `ALIGN_DELTA` on the values in that 5-minute alignment period. This aligner returns the number of matching responses in that alignment period as a 64-bit integer.

  * The time series within each filter are also grouped by the values of the resource labels for module and version, so each group with contain two sets of aligned time series, those matching the numerator filter and those matching the denominator filter.

  * The time series within each group matching the numerator or denominator filter are aggregated down to a single time by summing the values in the individual time series by using the `REDUCER_SUM` cross-series reducer. This results in one time series for the numerator and one for the denominator, each reporting the number of responses across all matching time series in the alignment period.




The policy then computes, for the numerator and denominator time series representing each group, the ratio of the values. The condition for the alerting policy is met when the ratio is greater than 50 percent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
