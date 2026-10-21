---
url: https://docs.cloud.google.com/monitoring/mql/qn-from-api/
title: Using MQL from the Monitoring API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:36.926604+00:00
---

# Using MQL from the Monitoring API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/qn-from-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Using MQL from the Monitoring API Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

This page describes how to provide Monitoring Query Language (MQL) queries to the Cloud Monitoring API.

This page doesn't cover creating the MQL queries. For a set of example queries, see [Examples](https://docs.cloud.google.com/monitoring/mql/examples). [MQL Refererence](https://docs.cloud.google.com/monitoring/mql/reference) provides a comprehensive reference for the language.

For general information about MQL-based alerting policies, see [Alerting policies with MQL](https://docs.cloud.google.com/monitoring/mql/alerts).

**Note:** The code editor allows time ranges to be specified explicitly in queries, and implicitly by the chart options in the editor. If you copy MQL queries from the editor, and you are using the implicit, chart-based time selection, your queries may not be valid if you attempt to supply them directly to the API. For more information, see [Time ranges, charts, and the code editor](https://docs.cloud.google.com/monitoring/mql/query-editor#ql-time-in-editor).

## Using MQL from the API

You can provide MQL queries at the following places in the Monitoring API:

  * To select and manipulate time-series data by using MQL, call the [`timeSeries.query`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query) method. For examples, see Using `timeSeries.query`.

  * To select and manipulate time-series data for charts, you provide the query to a [`TimeSeriesQuery`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery) specification when you call the [`dashboards.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create) method. For an example, see Building charts.

  * To create MQL-based conditions in alerting policies, describe the condition for the alerting policy with the [`MonitoringQueryLanguageCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MonitoringQueryLanguageCondition) condition type when you call [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create). For examples, see Creating conditions for alerting policies.




## Retrieving data with `timeSeries.query`

To retrieve time-series data from the API with a MQL query, use the [`timeSeries.query`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query) method.

The `timeSeries.query` method takes a minimal structure that looks like this in JSON:
    
    
    {
      "query": string
    }
    

For the value of the `query` field, specify a string in MQL, as shown in the following simple queries:
    
    
    {
      "query": "fetch gce_instance::compute.googleapis.com/instance/disk/read_bytes_count | within 5m"
    }
    
    
    
    {
      "query": "fetch gce_instance::compute.googleapis.com/instance/disk/read_bytes_count | for 1h"
    }
    
    
    
    {
      "query": "fetch gce_instance::compute.googleapis.com/instance/cpu/usage_time | sum | next_older 10m | every 10m"
    }
    

If your query creates an unaligned output table, then you must supply a duration by using the [`within`](https://docs.cloud.google.com/monitoring/mql/reference#within-tabop) table operation when calling the API directly. Charting tools like Metrics Explorer provide a default query duration. The query in the following JSON snippet works in the MQL code editor in Metrics Explorer but fails when supplied directly to the API:
    
    
    {
       "query": "fetch gce_instance::compute.googleapis.com/instance/disk/read_bytes_count | mul(10)"
    }
    

With the addition of a `within` table operation to the prior query, the prior example can be supplied directly to the API:
    
    
    {
       "query": "fetch gce_instance::compute.googleapis.com/instance/disk/read_bytes_count | mul(10) | **within 1h** "
    }
    

To experiment with the API, you can use the APIs Explorer tool on the [`timeSeries.query`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query) reference page. For an introduction to APIs Explorer tool, see [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer).

Another way to try the API is to put the query into a text file and then execute the query using `curl`. The following example passes the query in the file `query.json` to the `timeSeries.query` method:
    
    
    curl -d @query.json -H "Authorization: Bearer $TOKEN" \
    --header "Content-Type: application/json" -X POST \
    https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/timeSeries:query
    

For more information about using `curl`, see Invoking `curl`.

If successful, the query returns a table containing the time series requested. The table is divided into two components:

  * The `timeSeriesDescriptor` describes the label keys, label values, and data points in the table. It doesn't contain any data; it simply describes the data.

  * The `timeSeriesData` contains the data described in the time-series descriptor. This data is presented as an array of pairs.

    * The first item in the pair, `labelValues`, records a set of values for the labels listed in the time-series descriptor.
    * The second, `pointData`, is an embedded array of value/timestamp pairs, which represent the data collected with the specified set of label values.



The response, slightly reformatted, looks like this:
    
    
    [{
      "timeSeriesTable": {
        "timeSeriesDescriptor": {
          "labelDescriptors": [
            { "key": "resource.project_id" },
            { "key": "resource.zone" },
            { "key": "resource.instance_id" },
            { "key": "metric.instance_name" }
          ],
          "valueDescriptors": [
            {
              "key": "value.utilization",
              "valueType": "DOUBLE",
              "metricKind": "GAUGE"
            }
          ],
          "pointDescriptors": [
            {
              "key": "value.utilization",
              "valueType": "DOUBLE",
              "metricKind": "GAUGE"
            }
          ]
        },
        "timeSeriesData": [
          {
            "labelValues": [
              { "stringValue": "632526624816" },
              { "stringValue": "us-central1-a" },
              { "stringValue": "5106847938297466291" },
              { "stringValue": "gke-kuber-cluster-default-pool-6fe301a0-n8r9" }
            ],
            "pointData": [
              {
                "values": [
                  {
                    "doubleValue": 0.063896992710942874
                  }
                ],
                "timeInterval": {
                  "startTime": "1969-12-31T23:59:59.999999Z",
                  "endTime": "2020-03-02T20:17:00Z"
                }
              },
              { ... additional value/timestamp pairs ...}
            ]
          },
          { ... additional labelValue/pointData pairs ...},
        ]
      }
    

## Building charts

You can use the [`dashboards.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create) method to programmatically create dashboards and the charts they contain.

The only difference between creating MQL-based charts and other charts is the type of [`TimeSeriesQuery`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query) query you use to populate the chart's data set.

### Constructing an MQL-based chart

For MQL queries, use the query as the value of the `timeSeriesQueryLanguage` string field in the chart's [`DataSet`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DataSet) array.

The following is a simple dashboard definition that includes MQL:
    
    
    {
      "displayName": "Dashboard for MQL chart (API)",
      "gridLayout": {
        "widgets": [
          {
            "title": "Min/Max Compute Engine CPU utilization",
            "xyChart": {
              "dataSets": [
                {
                  **"timeSeriesQuery": {
                    "timeSeriesQueryLanguage": "fetch gce_instance::compute.googleapis.com/instance/cpu/utilization | within(1h) | { top 1, max(val()) ; bottom 1, min(val()) } | union"
                  }** ,
                  "plotType": "LINE",
                }
              ],
              "timeshiftDuration": "0s",
              "yAxis": {
                "label": "y1Axis",
                "scale": "LINEAR"
              },
              "chartOptions": {
                "mode": "COLOR"
              }
            }
          }
        ]
      }
    }
    

This creates a dashboard titled "Dashboard for MQL chart (API)" in your project. The dashboard contains a chart called "Min/Max Compute Engine CPU Utilization", which shows two lines, one for the highest values and one for the lowest.

![Chart shows the time series with the highest and lowest
values.](https://docs.cloud.google.com/static/monitoring/images/qn-examples-top-and-bottom-union.png)

For more information about this example query, see [Combining selections with `union`](https://docs.cloud.google.com/monitoring/mql/examples#qlx-union).

### Creating a chart

You can put the dashboard JSON into a file and then pass the file to `gcloud beta monitoring dashboards create` or use `curl` to post it to `https://monitoring.googleapis.com/v1/projects/${PROJECT_ID}/dashboards`. For more examples, see [Creating a dashboard](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#create). For more information about using `curl`, see Invoking `curl`.

For general information about creating charts and dashboards, see [Managing dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard). For reference material, see [`Dashboards`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards).

## Creating conditions for alerting policies

You use the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) method to programmatically create alerting policies.

The only difference between creating MQL-based alerting policies and other alerting policies is the type of [`Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition) you use. Otherwise, you create these policies like any other alerting policy.

The following shows a simple MQL query for an alert-policy condition that tests for Compute Engine CPU utilization exceeding 15 percent:
    
    
    fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
    | group_by sliding(5m), mean(val())
    | condition val() > 0.15 '10^2.%'
    

For more information about the MQL `condition` alert operation, see [Alerting policies with MQL](https://docs.cloud.google.com/monitoring/mql/alerts).

### Constructing the alerting policy

To build an alerting policy based on an MQL query, use the `AlertPolicy` condition type [`MonitoringQueryLanguageCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MonitoringQueryLanguageCondition). The `MonitoringQueryLanguageCondition` has the following structure:
    
    
    {
      "query":    string,
      "duration": string,
      "trigger":  {
        object (Trigger)
      }
    }
    

The value of the `query` field is a MQL alerting-query string in either concise or strict form. The examples in this document are in concise form. For more information about strict form, see [Strict-form queries](https://docs.cloud.google.com/monitoring/mql/query-language#strict-form).

The `duration` field specifies the length of time during which each evaluation of the query must generate a `true` value before the alerting policy is triggered. For more information, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth). The value must be a number of minutes, expressed in seconds; for example, `600s` for a 10-minute duration.

The `trigger` field specifies how many time series must satisfy the condition during the `duration` period, expressed as a count or a percentage. The default value is a count of 1. For more in information, see [`Trigger`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger).

For the example alerting query, with a 10-minute duration and a trigger count of 1, the structure looks like the following:
    
    
    {
      "query": "fetch gce_instance::compute.googleapis.com/instance/cpu/utilization | group_by sliding(5m), mean(val()) | condition val() > 0.15 '10^2.%'",
      "duration": "600s",
      "trigger" : {
         "count": 1
      }
    }
    

Use this structure as the value of a `conditionMonitoringQueryLanguage` field in a condition, which is in turn embedded in an alerting-policy structure. For more information about these structures, see [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy).

**Note:** An alerting policy that uses MQL can have only the single MQL-based condition. Policies with multiple conditions are not supported if a condition uses MQL.

The following shows a complete minimal policy with a `MonitoringQueryLanguageCondition` condition in JSON:
    
    
    {
      "displayName":"Alert if CPU utilization exceeds 15% for 10 mins (MQL, API)",
      "combiner":"OR",
      "conditions":[
        {
          "displayName":"MQL-based utilization condition, API",
    
          **"conditionMonitoringQueryLanguage":
          {
            "query": "fetch gce_instance::compute.googleapis.com/instance/cpu/utilization | group_by sliding(5m), mean(val()) | condition val() > 0.15 '10^2.%'",
            "duration": "600s",
            "trigger" : {
               "count": 1
            },
         }**,
       }
      ],
    }
    

### Creating an alerting policy

To create the policy, you can put the alerting-policy JSON into a file and then pass the file to `gcloud monitoring policies create` or use `curl` to post it to `https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/alertPolicies`.

For more information about the Monitoring API for alerting policies, see [Managing alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).

For more information about using `curl`, see Invoking `curl`.

## Invoking `curl`

Each `curl` invocation includes a set of arguments, followed by the URL of an API resource. The common arguments include a Google Cloud project ID and an authentication token. These values are represented here by the `PROJECT_ID` and `TOKEN` environment variables.

You might also have to specify other arguments, for example, to specify the type of the HTTP request (for example, `-X DELETE`). The default request is `GET`, so the examples don't specify it.

Each `curl` invocation has this general structure:

`curl --http1.1 --header "Authorization: Bearer ${TOKEN}" <other_args> https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/<request>`

To use `curl`, you must specify your project ID and an access token. To reduce typing and errors, you can put these into environment variables as pass them to `curl` that way.

To set these variables, do the following:

  1. Create an environment variable to hold the ID of your scoping project of a metrics scope. These steps call the variable `PROJECT_ID`:
         
         PROJECT_ID=a-sample-project
         

  2. Authenticate to the Google Cloud CLI:
         
         gcloud auth login
         

  3. Optional. To avoid having to specify your project ID with each `gcloud` command, set your project ID as the default by using gcloud CLI:
         
         gcloud config set project ${PROJECT_ID}
         

  4. Create an authorization token and capture it in an environment variable. These steps call the variable `TOKEN`:
         
         TOKEN=`gcloud auth print-access-token`
         

You have to periodically refresh the access token. If commands that worked suddenly report that you are unauthenticated, reissue this command.

  5. To verify that you got an access token, echo the `TOKEN` variable:
         
         echo ${TOKEN}
         ya29.GluiBj8o....
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
