---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/logs-based-metrics/
title: Using logs-based metrics \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:23.268606+00:00
---

# Using logs-based metrics  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/logs-based-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Using logs-based metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the basics of emitting logs to create availability and latency SLIs. It also provides implementation examples of how to define SLOs using logs-based metrics.

Using data elements in log entries to create service-level indicators is one way to take advantage of existing log payloads. Otherwise, it may be possible to add logging to an existing service, which may be easier than creating metric instrumentation.

## Logs and metrics

Logs collect records called _log entries_ that describe specific events that take place in computer systems. Logs are written by code, by the platform services the code is running on (for example, Dataflow), and the infrastructure the platform depends on (for example, Compute Engine instances).

Because logs in modern systems descend from—and sometimes still are—text files written to disk, a log entry is analogous to a line in a log file and can be considered the quantum unit of logging.

A log entry minimally consists of two things:

  * A timestamp that indicates either when the event took place or when it was ingested into the logging system
  * The text payload, either as unstructured text data or structured data, most commonly in JSON.



Logs can also carry associated metadata, especially when they're ingested into Cloud Logging. Such metadata might include the resource that's writing the log, the log name, and a severity for each entry.

### Logs

Logs are used for two main purposes:

  * _Event_ logs describe specific events that take place within the system. You can use event logs to output messages that assure users that things are working well ("task succeeded") or to provide information when things fail ("received exception from server").
  * _Transaction_ logs describe the details of every transaction processed by a system or component. For example, a load balancer logs every request that it receives, whether the request is successfully completed or not, and records additional information like the requested URL, HTTP response code, and possibly information like which backend was used to serve the request.



### Metrics

Unlike logs, metrics usually don't describe specific events. More commonly, metrics are used to represent the state or health of a system over time. A metric is made up of a series of data points that measure something about your system; each data point includes a timestamp and a numeric value.

Metrics can also have metadata associated with them; the series of data points, referred to as a _time series_ , might include information like the metric name, a description, and often labels that specify which resource is writing the data. For information on the Monitoring metric model, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

### Logs-based metrics

Logs-based metrics are metrics created from log entries by extracting information from log entries and transforming it into time-series data. Cloud Logging provides mechanisms for creating two kinds of metrics from log entries:

  * _Counter metrics_ , which count the number of log entries that match a particular filter. You can use a counter metric to determine, for example, the number of requests or errors recorded in the log.

  * _Distribution metrics_ , which use regular expressions to parse the payload in each log entry to extract numeric values as a distribution.




For more information on logs-based metrics in Cloud Logging, see [Using logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

### Using log-based metrics as SLIs

Logs-based metrics let you extract data from logs in a form you can use for building SLIs in Monitoring:

  * You can use logs-based counter metrics to express a request-based availability SLI.

  * You can use a logs-based distribution metric to express a request-based latency SLI.




### Sample log entries

The Stack Doctor application is an example of a service instrumented to emit log messages that contain information about all requests, errors, and latency made to the service. The code for the service is available in the [`stack-doctor` GitHub repository](https://github.com/yuriatgoogle/stack-doctor/blob/master/log-based-metrics/slis/slis.js).

The service generates Cloud Logging log entries in the `projects/stack-doctor/logs/bunyan_log` log. The log entry for each type of event includes a different `message` value. The log entries for different types of events look like the following:

  * On every request:
        
        {
          "insertId": "..........iTRVT5MOK2VOsVe31bzrTD",
          "jsonPayload": {
            "pid": 81846,
            "time": "Mon Aug 31 2020 20:30:49 GMT-0700 (Pacific Daylight Time)",
            "hostname": "<hostname>",
            "level": 30,
            "message": "request made",
            "v": 0,
            "name": "sli-log"
          },
            "resource": {
            "type": "global",
            "labels": {
              "project_id": "stack-doctor"
            }
          },
          "timestamp": "2020-09-01T03:30:49.263999938Z",
          "severity": "INFO",
          "logName": "projects/stack-doctor/logs/bunyan_log",
          "receiveTimestamp": "2020-09-01T03:30:50.003471183Z"
        }
        

  * On successful requests:
        
        {
          "insertId": "..........qTRVT5MOK2VOsVe31bzrTD",
          "jsonPayload": {
            "name": "sli-log",
            "v": 0,
            "pid": 81846,
            "level": 30,
            "hostname": "<hostname>",
            "time": "Mon Aug 31 2020 20:30:49 GMT-0700 (Pacific Daylight Time)",
            "message": "success!"
          },
          "resource": {
            "type": "global",
            "labels": {
              "project_id": "stack-doctor"
            }
          },
          "timestamp": "2020-09-01T03:30:49.874000072Z",
          "severity": "INFO",
          "logName": "projects/stack-doctor/logs/bunyan_log",
          "receiveTimestamp": "2020-09-01T03:30:50.201547371Z"
        }
        

  * On completed requests:
        
        {
          "insertId": "..........mTRVT5MOK2VOsVe31bzrTD",
          "jsonPayload": {
            "time": "Mon Aug 31 2020 20:30:49 GMT-0700 (Pacific Daylight Time)",
            "level": 30,
            "name": "sli-log",
            "message": "slept for 606 ms",
            "hostname": "<hostname>",
            "pid": 81846,
            "v": 0
          },
          "resource": {
            "type": "global",
            "labels": {
              "project_id": "stack-doctor"
            }
          },
          "timestamp": "2020-09-01T03:30:49.874000072Z",
          "severity": "INFO",
          "logName": "projects/stack-doctor/logs/bunyan_log",
          "receiveTimestamp": "2020-09-01T03:30:50.201547371Z"
        }
        

  * On error:
        
        {
          "insertId": "..........DTRVT5MOK2VOsVe31bzrTD",
          "jsonPayload": {
            "hostname": "<hostname>",
            "level": 50,
            "pid": 81846,
            "message": "failure!",
            "name": "sli-log",
            "time": "Mon Aug 31 2020 20:30:44 GMT-0700 (Pacific Daylight Time)",
            "v": 0
          },
          "resource": {
            "type": "global",
            "labels": {
              "project_id": "stack-doctor"
            }
          },
          "timestamp": "2020-09-01T03:30:44.414999961Z",
          "severity": "ERROR",
          "logName": "projects/stack-doctor/logs/bunyan_log",
          "receiveTimestamp": "2020-09-01T03:30:46.182157077Z"
        }
        




Based on these entries, you can create logs-based metrics that count all requests, count errors, and track request latency. You can then use the logs-based metrics to create availability and latency SLIs.

## Creating logs-based metrics for SLIs.

Before you can create SLIs on logs-based metrics, you must create the logs-based metrics.

  * For availability SLIs on request and error counts, use logs-based counter metrics.
  * For latency SLIs, use logs-based distribution metrics.



After you create the your logs-based metrics, you can find them in Monitoring by searching for them in Metrics Explorer. In Monitoring, logs-based metrics have the prefix `logging.googleapis.com/user`.

**Caution:** The following examples create logs-based metrics against the `global` monitored resource, which is generally inadvisable. For a real deployment, take care to emit logs against an existing monitored resource.

### Metrics for availability SLIs

You express a request-based availability SLI in the Cloud Monitoring API by using the [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure to set up a ratio of "good" or "bad" requests to total requests. This ratio is used in the `goodTotalRatio` field of a [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli) structure.

You must create logs-based counter metrics that can be used to construct this ratio. You must create at least two of the following:

  1. A metric that counts total events; use this metric in the ratio's `totalServiceFilter`.

For the "stack-doctor" example, you can create a logs-based metric that counts log entries in which the message string "request made" appears.

  2. A metric that counts "bad" events, use this metric in the ratio's `badServiceFilter`.

For the "stack-doctor" example, you can create a logs-based metric that counts log entries in which the message string "failure!" appears.

  3. A metric that counts "good" events, use this metric in the ratio's `goodServiceFilter`.

For the "stack-doctor" example, you can create a logs-based metric that counts log entries in which the message string "success!" appears.




The SLI described for this example is based on a metric for total requests named `log_based_total_requests`, and a metric for errors named `log_based_errors`.

You can create logs-based metrics by using the Google Cloud console, the Cloud Logging API or the Google Cloud CLI. To create logs-based counter metrics by using the Google Cloud console, you can use the following procedure:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

The logs-based metrics page shows a table of user-defined metrics and a table of system-defined metrics.

  2. Click **Create Metric** , located above the table of user-defined metrics.

  3. In the **Metric type** pane, select **Counter**.

  4. In the **Details** pane, give your new metric a name. For the "stack-doctor" example, enter `log_based_total_requests` or `log_based_errors`.

You can ignore the other fields for this example.

  5. In the **Filter selection** panel, create a query that retrieves only the log entries that you want to count in your metric.

For the "stack-doctor" example, the query for `log_based_total_requests` might include the following:
         
         resource.type="global"
         logName="projects/stack-doctor/logs/bunyan_log"
         jsonPayload.message="request made"
         

The query for `logs_based_errors` changes the message string:
         
         resource.type="global"
         logName="projects/stack-doctor/logs/bunyan_log"
         jsonPayload.message="failure!"
         

  6. Click **Preview logs** to check your filter, and adjust it if necessary.

  7. Ignore the **Labels** pane for this example.

  8. Click **Create Metric** to finish the procedure.




For more information on creating logs-based counter metrics, see [Creating a counter metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics#creating_a_counter_metric).

### Metrics for latency SLIs

You express a request-based latency SLI in the Cloud Monitoring API by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure, which is used in the `distributionCut` field of a [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli) structure. You must create a logs-based distribution metric to create a latency SLI. This example create a logs-based distribution metric named `log_based_latency.`

You can create logs-based metrics by using the Google Cloud console, the Cloud Logging API or the Google Cloud CLI. To create logs-based distribution metrics by using the Google Cloud console, you can use the following procedure:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

The logs-based metrics page shows a table of user-defined metrics and a table of system-defined metrics.

  2. Click **Create Metric** , located above the table of user-defined metrics.

  3. In the **Metric type** pane, select **Distribution**.

  4. In the **Details** pane, give your new metric a name. For the "stack-doctor" example, enter `log_based_latency`.

You can ignore the other fields for this example.

  5. In the **Filter selection** panel, create a query that retrieves only the log entries that you want to count in your metric. 

For the "stack-doctor" example, the query for `log_based_latency` might include the following:
         
         resource.type="global"
         logName="projects/stack-doctor/logs/bunyan_log"
         jsonPayload.message="slept for"
         

Specify the following fields for the filter query:

     * **Field name** : `json.message`
     * **Regular expression** : `\s(\d*)\s`

The message string for completed requests has the form "slept for _n_ ms". The regular expression extracts the latency value _n_ from the string.

  6. Ignore the **Labels** pane for this example.

  7. Click **Create Metric** to finish the procedure.




For more information on creating logs-based distribution metrics, see [Creating Distribution metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics).

## Availability SLIs

In Cloud Monitoring, you express a request-based availability SLI by using a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure. The following example shows an SLO that uses the `log_based_total_requests` and `log_based_errors` metrics in the ratio. This SLO expects that the ratio of "good"-to-total requests is at least 98% over a rolling 24-hour period:
    
    
    {
     "serviceLevelIndicator": {
       "requestBased": {
         "goodTotalRatio": {
           "totalServiceFilter":
             "metric.type=\"logging.googleapis.com/user/log_based_total_requests\"
              resource.type=\"global\"",
           "badServiceFilter":
             "metric.type=\"logging.googleapis.com/user/log_based_errors\"
              resource.type=\"global\""
         }
       }
     },
     "goal": 0.98,
     "rollingPeriod": "86400s",
     "displayName": "Log-Based Availability"
    }
    

## Latency SLIs

In Cloud Monitoring, you express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. The following example shows an SLO that uses the `log_based_latency` metric and expects that 98% of requests are under 500 ms over a rolling 24-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"logging.googleapis.com/user/log_based_latency\"
              resource.type=\"global\"",
            "range": {
              "min": 0,
              "max": 500
            }
          }
        }
      },
      "goal": 0.98,
      "rollingPeriod": "86400s",
      "displayName": "98% requests under 500 ms"
    }
    

## Additional resources

  * [Can you alert on logs in Stackdriver? | by Yuri Grinshteyn](https://medium.com/google-cloud/can-you-alert-on-logs-in-stackdriver-7dfb07f495c0)
  * [Configure notifications for log-based metrics | Cloud Logging](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts)
  * [Extracting value from your logs with logs-based-metrics](https://cloud.google.com/blog/products/gcp/extracting-value-from-your-logs-with-stackdriver-logs-based-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
